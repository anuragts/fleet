#!/usr/bin/env python3
"""Send an explicitly prepared code-evaluation request to TypeSafe."""

import argparse
import json
import math
import os
from pathlib import Path
import sys
import urllib.error
import urllib.request

ENDPOINT = "https://api.typesafe.ai/v1/systemone"
KEY_FILE = Path(__file__).resolve().parents[3] / ".env" / "typesafe.env"


def load_api_key():
    key = os.environ.get("TYPESAFE_API_KEY", "").strip()
    if key:
        return key
    try:
        lines = KEY_FILE.read_text().splitlines()
    except FileNotFoundError:
        return ""
    for line in lines:
        name, separator, value = line.strip().partition("=")
        if separator and name.strip() == "TYPESAFE_API_KEY":
            value = value.strip()
            if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
                value = value[1:-1]
            return value.strip()
    return ""


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


def validate_request(payload):
    if not isinstance(payload, dict):
        raise ValueError("Request must be a JSON object.")
    if not isinstance(payload.get("model"), str) or not payload["model"].strip():
        raise ValueError("Provide a nonempty model name.")
    if not isinstance(payload.get("state"), (str, dict, list)):
        raise ValueError("State must be text, an object, or an array.")
    questions = payload.get("questions")
    if not isinstance(questions, dict) or not questions:
        raise ValueError("Provide a nonempty questions object.")
    for question in questions.values():
        if not isinstance(question, dict):
            raise ValueError("Each question must be an object.")
        if not isinstance(question.get("instructions"), (str, dict, list)) or not question["instructions"]:
            raise ValueError("Each question needs nonempty instructions.")
        kind, criteria = question.get("type"), question.get("criteria")
        if kind == "choice":
            if not isinstance(criteria, dict) or not criteria or not all(
                value is None or isinstance(value, str) for value in criteria.values()
            ):
                raise ValueError("Choice criteria must map options to text or null.")
        elif kind == "score":
            if not isinstance(criteria, list) or len(criteria) < 2 or not all(
                isinstance(value, str) and value for value in criteria
            ):
                raise ValueError("Score needs at least two text criteria.")
        elif kind == "noul":
            if criteria is not None and (
                not isinstance(criteria, dict)
                or not set(criteria).issubset({"true", "false"})
                or not all(isinstance(value, str) for value in criteria.values())
            ):
                raise ValueError("Noul criteria must describe true and/or false.")
        else:
            raise ValueError("Supported question types: choice, score, noul.")


def number_between(value, low, high):
    return type(value) in (int, float) and math.isfinite(value) and low <= value <= high


def validate_response(result, questions):
    if not isinstance(result, dict) or not isinstance(result.get("model"), str):
        raise ValueError("Response is missing the model.")
    answers = result.get("answers")
    if not isinstance(answers, dict) or set(answers) != set(questions):
        raise ValueError("Response answer IDs do not match the request.")
    for key, question in questions.items():
        answer, kind = answers[key], question["type"]
        if not isinstance(answer, dict) or answer.get("type") != kind:
            raise ValueError("Response answer type does not match the request.")
        if kind == "noul":
            if not number_between(answer.get("noul"), 0, 1):
                raise ValueError("Invalid Noul probability.")
            continue
        options = set(question["criteria"]) if kind == "choice" else {
            str(index) for index in range(len(question["criteria"]))
        }
        probabilities = answer.get("probabilities")
        if not isinstance(probabilities, dict) or set(probabilities) != options:
            raise ValueError("Response probability options do not match criteria.")
        if not all(number_between(value, 0, 1) for value in probabilities.values()):
            raise ValueError("Invalid response probabilities.")
        if not math.isclose(sum(probabilities.values()), 1, abs_tol=0.001):
            raise ValueError("Response probabilities must sum to one.")
        if not number_between(answer.get("confidence"), 0, 1):
            raise ValueError("Invalid response confidence.")
        if kind == "choice" and answer.get("choice") not in options:
            raise ValueError("Response selected an unknown option.")
        if kind == "score" and not number_between(answer.get("score"), 0, len(options) - 1):
            raise ValueError("Response score is outside the rubric.")


def evaluate(payload):
    key = load_api_key()
    if not key:
        raise ValueError(f"Set TYPESAFE_API_KEY in the environment or {KEY_FILE}; do not paste it into chat.")
    request = urllib.request.Request(
        ENDPOINT,
        data=json.dumps(payload, allow_nan=False).encode("utf-8"),
        headers={"Authorization": "Bearer " + key, "Content-Type": "application/json"},
        method="POST",
    )
    opener = urllib.request.build_opener(NoRedirect())
    with opener.open(request, timeout=60) as response:
        result = json.load(response)
    validate_response(result, payload["questions"])
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("request", type=Path, help="Prepared request JSON file")
    parser.add_argument("--dry-run", action="store_true", help="Validate without network or credentials")
    args = parser.parse_args()
    try:
        payload = json.loads(args.request.read_text())
        validate_request(payload)
        encoded = json.dumps(payload, allow_nan=False).encode("utf-8")
        if args.dry_run:
            result = {"dry_run": True, "model": payload["model"],
                      "question_ids": list(payload["questions"]), "request_bytes": len(encoded)}
        else:
            result = evaluate(payload)
        print(json.dumps(result, indent=2, allow_nan=False))
        return 0
    except urllib.error.HTTPError as error:
        # Response bodies can echo submitted code; never print them on failures.
        print(f"TypeSafe HTTP {error.code}; no result. Check credentials, quota, or request schema. No automatic retry.", file=sys.stderr)
    except (urllib.error.URLError, OSError):
        print("Could not read the request or reach TypeSafe. No result; no automatic retry.", file=sys.stderr)
    except ValueError as error:
        message = "Invalid JSON; no usable result." if isinstance(error, json.JSONDecodeError) else str(error)
        print(message, file=sys.stderr)
    return 1


if __name__ == "__main__":
    sys.exit(main())
