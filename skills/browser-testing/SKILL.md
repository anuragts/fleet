---
name: browser-testing
description: Reproduce bugs and verify web UI behavior in a real browser. Use for browser testing, frontend verification, and end-to-end manual checks, including selecting a browser, development login, and collecting evidence.
---

# Browser testing

## Choose the browser and controls

Default to Helium's sandbox profile. Honor a browser, profile, or tab explicitly
chosen by the user. Follow the host's required browser-tool routing when it
overrides these defaults.

1. Discover the browser tools actually available in this session. Prefer the
   connected Claude or Codex browser extension for the current agent. Confirm
   it can read and control the target tab; do not assume an extension exists.
2. If no working extension is available, use computer use on the same browser
   and profile. Read the tool's documentation before operating it.
3. If Helium is closed, try opening it and selecting the sandbox profile.
   Inspect the profile picker or known configuration instead of guessing a
   profile directory or silently using the personal profile.
4. If Helium cannot be opened or controlled, use another installed, controllable
   browser, preferably with a dedicated test profile. Report the fallback and
   reason. Do not install browsers, extensions, or change security settings
   merely to make testing possible.
5. If no browser can be controlled, report the blocker. Run useful available
   non-browser checks, but do not describe them as browser verification.

Prefer accessible names and stable locators when supported. With computer use,
inspect fresh screenshots after navigation or state changes before clicking.
Reacquire the tab after redirects, login, or reload if the handle is stale.
Retry a failed connection once after a concrete recovery action, then fall back
instead of looping through the same error.

## Confirm the environment and sign in

- Confirm the target URL, dev environment, and running app before testing.
  Check existing listeners and project run instructions before starting another
  server. Verify the running app corresponds to the checkout being tested.
- Reuse the current authenticated session when it has the intended account and
  workspace. Do not sign out or switch accounts unnecessarily.
- If signed out in a confirmed development environment, use the app's
  **Continue with GitHub** flow. Complete normal sign-in using the available
  GitHub session, then verify the callback returns to the intended dev app and
  the correct account and workspace are active. This is the default dev login
  method; no extra permission question is needed for ordinary sign-in.
- Confirm development status from the URL and project configuration, not from
  a page's appearance. This automatic login instruction does not apply to
  production or an uncertain environment.
- If credentials, MFA, CAPTCHA, account selection, or new OAuth permissions
  require user input, use the host's secure input or user handoff mechanism.
  Never request secrets in ordinary chat, bypass authentication, or copy
  cookies between profiles. Do not approve unrelated account or organization
  access as part of testing.

## Test the actual behavior

Keep checks proportional to the change. Choose the user journey and expected
result before clicking; do not turn a small fix into a full application audit.

- For bug fixes, reproduce the reported behavior before editing when feasible.
  Record the trigger, expected result, and observed result. If reproduction is
  unavailable, say so and verify the fix with the strongest available evidence.
- Run the whole affected journey, including its visible final result. A page
  load, successful click, screenshot, or HTTP 200 alone does not prove success.
- Exercise relevant initial, loading, success, empty, and error states. Include
  partial data, retry, or interrupted actions when the feature supports them.
  Use controlled dev fixtures or supported network controls for failures.
  Do not alter production data or invent mock behavior and call it a real test.
- Check repeated interactions, back/forward navigation, reload, and persistence
  when they affect the change. Confirm duplicate submissions do not occur.
- For changed UI, check keyboard navigation, focus visibility and restoration,
  labels, disabled states, and overflow at representative desktop and narrow
  widths. Check reduced motion when motion changes. Follow project-specific
  design and performance checks when applicable.
- Inspect console errors and failed network requests when tools expose them.
  Separate pre-existing failures from regressions. If these signals are not
  available through computer use, report that limitation rather than inventing
  a clean console.
- For permission-sensitive behavior, confirm the actual role and workspace.
  Test relevant allowed and denied paths with authorized test identities.
- Use disposable dev data where possible. Track records created by the test
  and clean up only those records when authorized. Do not send real messages,
  make purchases, or delete existing user data merely to exercise a UI.

## Evidence and handoff

Record the browser/profile, URL, tested account role without secrets, key steps,
and observed outcomes. Capture screenshots for visual differences or failures
when useful. Redact sensitive content and do not include tokens or cookies in
logs or reports.

Report passed, failed, and blocked or untested checks separately. Distinguish
browser observations from builds, type checks, automated tests, and assumptions.
Include enough detail to reproduce any remaining failure. Do not claim coverage
of browsers, states, or devices that were not exercised.

Preserve existing tabs, sessions, and processes. Clean up temporary test tabs
and servers you created when appropriate under the host's rules; do not close
the user's browser or stop a pre-existing dev server.
