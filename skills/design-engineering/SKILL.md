---
name: design-engineering
description: Build and review polished, accessible product interfaces and UI interactions.
---

# Design Engineering

Build interfaces that are clear before they are clever and polished before they
are decorative. Treat design engineering as the coordination of hierarchy,
layout, typography, color, behavior, accessibility, and performance—not as a
final CSS pass.

Preserve the product's existing visual language unless the user explicitly asks
for a redesign. Reuse the installed design system and feature-level components
before creating new primitives or dependencies.

## Working method

1. Understand the user's job, the primary action, and the consequence of failure.
2. Inspect existing tokens, components, nearby screens, and interaction patterns.
3. Define the visual hierarchy and all UI states before polishing the happy path.
4. Build the static layout and responsive behavior before adding motion.
5. Add interaction feedback, accessibility, and motion as one coherent system.
6. Verify with real content, keyboard navigation, zoom, reduced motion, dark mode,
   narrow screens, slow data, and a 6x CPU throttle.

When no design is supplied, create three or four intentionally different
directions behind a simple variant switcher. Vary information architecture,
density, or emphasis—not merely colors.

## Hierarchy and composition

- Make one action or content region dominant. Avoid several elements competing at
  the same visual weight.
- Use position, spacing, size, weight, and contrast in that order before adding
  decoration.
- Align related content to shared edges. Break the grid only for an intentional
  focal point.
- Group by proximity. A gap within a group must be smaller than the gap between
  groups.
- Keep controls visually distinct from content while preserving the product's
  existing conventions.
- Use progressive disclosure for secondary settings and advanced actions. Do not
  hide the primary path.
- Prefer fewer, stronger surfaces. Do not wrap every section in a card.

## Spacing and layout

Use a 4px base unit and an 8px primary rhythm. Start with this token scale and
reuse existing project tokens when they are equivalent:

| Token | Value | Typical use |
| --- | ---: | --- |
| `0.5` | 2px | Optical correction only |
| `1` | 4px | Icon/text micro-gap, compact inset |
| `2` | 8px | Tight control gap, small padding |
| `3` | 12px | Related-item gap, compact control inset |
| `4` | 16px | Default component padding and mobile gutter |
| `6` | 24px | Card padding, section sub-group gap |
| `8` | 32px | Page gutter or section gap |
| `12` | 48px | Major section separation |
| `16` | 64px | Large page rhythm |

- Prefer 8px increments for structural layout and 4px increments inside compact
  components. Use 2px only for optical alignment, never as a new spacing system.
- Use responsive gutters such as 16px on small screens, 24px on medium screens,
  and 32px or 48px on wide screens, adjusted to the existing product density.
- Let components respond to available space rather than device labels. Collapse
  only when the full layout no longer fits.
- Keep prose around 45–75 characters per line; target about 60–66ch for sustained
  reading. UI labels may be shorter.
- Reserve dimensions or matching skeletons for images, lists, charts, and fetched
  content. Avoid every preventable layout shift.
- Derive nested radii: `outer radius = inner radius + inset`. Match the spacing
  between nested surfaces on every side.
- Use logical properties where practical so spacing survives right-to-left
  layouts.
- Reject unexplained arbitrary values. Document the rare exception when geometry
  requires an optical correction.

## Typography

Use the existing typeface first. Add a font only when it materially improves the
brand or reading experience and its loading cost is justified.

Start from a small semantic scale instead of styling each screen independently:

| Role | Suggested size / line height | Weight | Use |
| --- | --- | ---: | --- |
| Caption | 12 / 16px | 400–500 | Metadata and secondary labels |
| UI label | 14 / 20px | 500 | Buttons, tabs, inputs, navigation |
| Body | 16 / 24px | 400 | Primary readable content |
| Subheading | 18 / 24px or 20 / 28px | 500–600 | Local hierarchy |
| Heading | 24 / 32px | 600 | Page or panel heading |
| Display | 32 / 40px and above | 600–700 | Rare high-emphasis moments |

- Adapt these values to existing tokens; do not introduce a parallel scale.
- Use regular weight for body text, medium for controls and labels, semibold for
  headings, and bold sparingly. If everything is semibold, nothing is emphasized.
- Prefer unitless line-height in CSS. Ensure final line boxes align with the 4px
  rhythm and remain safe when users increase text spacing.
- Use normal tracking for body copy. Tighten large display text gently; add modest
  tracking only to small uppercase labels.
- Use `text-wrap: balance` for short headings and `text-wrap: pretty` for prose
  when supported. Never balance long body content.
- Use `font-variant-numeric: tabular-nums` for counters, prices, timers, and tables
  whose values change.
- Allow text to zoom to 200% without clipping, overlap, or loss of functionality.
  Test long labels, localization, and multiline controls.
- Load only required weights. Prefer a variable font when it replaces several
  static files without increasing the payload. Choose `font-display` deliberately
  and metric-compatible fallbacks to prevent invisible text and layout shift.

## Color matching and surfaces

- Start from the product's existing palette, screenshots, or brand assets. Sample
  repeated colors and infer roles before inventing new ones.
- Define semantic roles such as canvas, surface, elevated surface, primary text,
  muted text, border, accent, success, warning, and danger. Components consume
  roles, not one-off color values.
- Use one hue family for a related interaction state and change lightness or
  brightness consistently. Do not hand-pick unrelated hover and active hex codes.
- In design tools, tune variants with HSB/HSV or OKLCH. In CSS, prefer existing
  tokens or a perceptual space such as `oklch()`; CSS has no native HSB syntax.
- Keep neutral surfaces genuinely neutral unless the brand intentionally uses a
  tinted neutral. Check the tint against imagery and surrounding surfaces.
- Use accent color for meaning and priority, not decoration everywhere. Keep
  status colors reserved for their status.
- Meet WCAG AA contrast: at least 4.5:1 for normal text, 3:1 for large text, and
  3:1 for meaningful non-text controls and focus indicators. Check every state in
  both light and dark themes.
- Never communicate status with color alone. Pair it with text, shape, iconography,
  or position.
- Prefer subtle shadows or tonal separation for depth. Use borders when they
  communicate structure, focus, or boundaries—not as default decoration.

## Controls and interaction states

Every interactive component must define:

| State | Required treatment |
| --- | --- |
| Default | Clear affordance and readable label |
| Hover | Small tonal/elevation change; no layout movement |
| Focus-visible | Obvious ring distinct from selected state |
| Active/pressed | Immediate tactile feedback |
| Disabled | Visually subdued and semantically disabled |
| Loading | Stable dimensions and progress communication |
| Success/error | Textual feedback, not color alone |

- Gate pointer-specific hover effects with
  `@media (hover: hover) and (pointer: fine)`. Hover must never be the only path to
  an action.
- Keep hover transitions around 120–180ms. Prefer a small brightness, background,
  border, or shadow change. Avoid moving controls under the pointer.
- Give pressable controls an immediate active state. A subtle `scale(0.96–0.98)`
  is appropriate when it does not disturb surrounding layout.
- Use a visible 2px focus ring with separation from the component and at least
  3:1 contrast against adjacent colors. Never remove focus without replacing it.
- Keep focus and selection visually distinct. Opening a dialog moves focus inside;
  closing it usually returns focus to the trigger.
- Prefer native semantic controls and established design-system primitives. If a
  custom control is unavoidable, reproduce its keyboard behavior, name, role,
  state, and focus management.
- Target at least 44×44px for touch controls and about 40×40px for comfortable
  desktop controls. Never fall below WCAG's 24×24 CSS-pixel minimum without a
  documented exception and sufficient spacing.
- Make hover/focus disclosures dismissible, hoverable, and persistent. Support
  Escape where the disclosure obscures other content.
- Disabled controls must not be the only explanation. If the reason is not
  obvious, show it near the control.

## Motion and transitions

Animate only to explain spatial relationships, preserve continuity, show state,
or confirm an action. Repeated expert actions and keyboard-driven commands should
usually be instant.

| Interaction | Typical duration |
| --- | ---: |
| Press feedback | 100–160ms |
| Hover or color change | 120–180ms |
| Tooltip or small popover | 125–200ms |
| Dropdown or select | 150–220ms |
| Modal, drawer, route transition | 200–300ms |
| Exits | About 15–25% faster than entry |

- Treat durations as a system, then adjust for distance, size, and frequency.
  Routine product motion should rarely exceed 300ms.
- Use ease-out for entry and direct feedback, ease-in-out for movement already on
  screen, and linear only for constant progress. Avoid slow ease-in entrances.
- Prefer CSS transitions for predetermined, interruptible state changes. Use an
  existing motion library only for gestures, shared layout, orchestration, or
  physics that CSS cannot express cleanly.
- Never use `transition: all`. Name the exact properties.
- Prefer `transform` and `opacity`; avoid animating layout properties such as
  margin, padding, width, and height in hot paths.
- Set transform origins to the source of the interaction for menus and popovers.
  Keep centered modals centered.
- Keep stagger delays short, around 30–80ms, cap the total sequence, and never
  block interaction until the stagger finishes.
- Honor `prefers-reduced-motion`. Replace large translation, scale, parallax, and
  depth changes with instant state changes or restrained fades.
- Test animation at normal speed, in slow motion, and under a 6x CPU throttle. If
  it drops frames, simplify it before shipping.

## Async and data states

Handle idle, loading, success, empty, error, partial, and stale-data states when
the feature can produce them.

- Use skeletons shaped like the final content, not generic spinners. Keep the
  skeleton and final layout dimensions aligned.
- Preserve usable stale content during background refresh when safe.
- Make empty states explain what is empty and provide the next useful action.
- Keep errors near the failed region, describe the problem in text, preserve user
  input, and provide a recovery path.
- Prevent duplicate submission while preserving visible progress and cancellation
  where cancellation is meaningful.
- Announce asynchronous status changes to assistive technology without stealing
  focus.

## Accessibility and resilience

- Verify complete keyboard operation and a logical focus order. Do not create
  keyboard traps.
- Use semantic landmarks and heading order. Give icon-only controls accessible
  names and decorative icons no accessible noise.
- Ensure content reflows without two-dimensional scrolling at 320 CSS pixels,
  except where the content inherently requires it, such as a data table.
- Do not clip content when line height, paragraph spacing, letter spacing, or word
  spacing is increased.
- Respect reduced motion, increased contrast, forced colors, color scheme, text
  size, locale, and right-to-left direction where the platform exposes them.
- Make validation errors identifiable in text and associate them with the relevant
  input. Move focus to an error summary only when that improves recovery.
- Do not use placeholder text as the only label. Do not hide critical information
  exclusively in a tooltip.

## Definition of done

- The primary action and hierarchy are obvious in five seconds.
- Spacing comes from the 4/8px system, with optical exceptions justified.
- Typography uses semantic roles, few weights, readable line lengths, and stable
  font loading.
- Color roles are consistent and every meaningful state meets contrast targets.
- Hover, focus, active, disabled, loading, success, empty, partial, and error
  behavior are covered where applicable.
- Keyboard, screen-reader semantics, 200% zoom, 320px reflow, reduced motion,
  light/dark themes, long content, and localization are checked.
- Dynamic content has reserved space or matching skeletons and introduces no
  avoidable layout shift.
- Motion communicates, stays responsive under 6x CPU throttle, and adds no unjustified
  dependency.
- The result uses the existing design system and is precise enough that a designer
  does not need to correct basic spacing, type, state, or accessibility issues.

For the standards and platform research behind the measurable rules, read
[references/research.md](references/research.md).
