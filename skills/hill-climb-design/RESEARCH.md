# Research: references worth climbing toward

A reference is only useful if we can name what it does well. Each entry lists
the thing to steal, so the council can score against something specific
instead of "make it look like Linear."

Status: first pass. Entries marked _verify_ need a fresh look at the live
product before we use them as a scoring anchor.

## Apps

| App | Steal this | Best for |
| --- | --- | --- |
| [Linear](https://linear.app) | Keyboard-first flow, dense but calm lists, restrained color, fast optimistic updates, subtle motion | Productivity, lists, issue views, command menus |
| [Vercel dashboard](https://vercel.com) | Geist type scale, strict grid, monochrome with one accent, clear empty and loading states | Dashboards, deploy logs, settings |
| [Raycast](https://raycast.com) | Command palette design, instant feedback, tight keyboard model | Launchers, search, command menus |
| [Stripe dashboard and docs](https://stripe.com/docs) | Data tables, forms, error copy, docs layout with live code | Forms, payments, docs, tables |
| [Things 3](https://culturedcode.com/things) | Whitespace, typographic hierarchy, motion that explains state | Personal tools, task lists |
| [Superhuman](https://superhuman.com) | Speed as a design feature, shortcut teaching, focus states | Inbox and triage UIs |
| [Notion Calendar](https://www.notion.com/product/calendar) | Dense time grid that still reads cleanly | Calendars, scheduling |
| [Figma](https://figma.com) | Tool panels, property inspectors, multiplayer presence | Editors, canvases |
| [Arc / Dia](https://arc.net) _verify_ | Sidebar navigation, playful but controlled color | Navigation, browser-like shells |
| [Resend](https://resend.com) | Developer-product polish, dark theme done well | Dev tools, marketing for dev tools |
| [Cal.com](https://cal.com) | Open source booking flow, readable code to study | Booking, multistep flows |
| [Apple HIG apps](https://developer.apple.com/design/human-interface-guidelines) | Platform conventions, spacing and type defaults | Native and native-feeling UIs |

## Components and craft

| Source | Steal this |
| --- | --- |
| [shadcn/ui](https://ui.shadcn.com) | Our default kit. Baseline for structure and tokens |
| [Radix Primitives](https://www.radix-ui.com) | Accessible behavior for dialogs, menus, popovers |
| [Base UI](https://base-ui.com) _verify_ | Newer primitive layer. Reported as a shadcn default in 2026, unconfirmed |
| [React Aria](https://react-spectrum.adobe.com/react-aria) | The strictest accessibility and i18n reference |
| [Ark UI](https://ark-ui.com) | State machine driven components (Zag.js) |
| [cmdk](https://cmdk.paco.me) by Paco Coursey | Command menu behavior |
| [Sonner](https://sonner.emilkowal.ski) and [Vaul](https://vaul.emilkowal.ski) by Emil Kowalski | Toasts and drawers with motion that feels physical |
| [Rauno Freiberg's interfaces](https://rauno.me) | Interaction details, the "Invisible details of interaction design" essay |
| [Geist](https://vercel.com/geist) | A complete design system to compare token decisions against |

## Reference galleries

Use these to find more references for a given screen type. They show real
shipped screens, which beats Dribbble shots that never had to handle data.

- [Mobbin](https://mobbin.com): largest library of real app screens and flows.
- [Refero](https://refero.design): web and iOS screens, searchable by pattern.
- [Godly](https://godly.website): curated web design, mostly marketing sites.
- [Awwwards](https://www.awwwards.com): award sites. Good for ambition, risky
  as a product UI reference because many winners ignore usability.

## How a reference gets used

1. Pick one primary reference per screen type. A settings page climbs toward
   Vercel settings, not toward Linear's issue list.
2. Capture the reference in the same states we capture the target: idle,
   loading, empty, error, hover, focus, mobile, dark.
3. Write 3 to 6 named traits per reference ("list rows are 32px, single line,
   secondary text at 60% opacity"). The council scores the gap to those traits.

## Open questions

- Do we store reference screenshots in the repo, or fetch them per run?
- One reference per run, or a primary plus a secondary for tie breaks?
- Who curates traits: the user, or a model with the user approving?

## Sources

- [Softr: 12 web app design examples for 2026](https://www.softr.io/blog/web-app-design-examples)
- [Design Studio UIUX: web app design examples](https://www.designstudiouiux.com/blog/web-app-design-examples/)
- [GreatFrontEnd: top headless UI libraries for React in 2026](https://www.greatfrontend.com/blog/top-headless-ui-libraries-for-react-in-2026)
- [Builder.io: React component libraries 2026](https://builder.io/blog/react-component-libraries-2026)
- [UXMagic: best React UI component libraries](https://uxmagic.ai/hi/blog/best-react-ui-component-libraries)
- [AlternativeTo: design reference libraries](https://alternativeto.net/lists/44740/design-reference-libraries-for-real-world-inspiration/)
- [App Launchpad: Mobbin alternatives](https://theapplaunchpad.com/blog/best-mobbin-alternatives/)
