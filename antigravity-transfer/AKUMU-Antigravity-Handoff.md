# AKUMU — Complete Antigravity handoff

Prepared 12 November 2026. This is an export of the existing project, not a rewrite.

## Start here

Extract the whole ZIP into a new folder. Open that folder in Google Antigravity.
The current editable project is **akumu/**. Do not start from historical builds.
The root **index.html** is the latest complete standalone playable game, including
the secret reception corridor event. It matches akumu/standalone/AKUMU.html.

To develop, install Node.js 22.12+ (Node 24 LTS recommended), then:

```sh
cd akumu
npm ci
npm run dev
```

Open the local URL printed by Vite. Internet access is needed to install npm
dependencies. Runtime game assets are bundled; the game needs no paid API,
account, secret key or CDN. A current WebGL2-capable browser is required.

```sh
npm run build        # standard static web build: dist/
npm run preview      # serve that build
npm run build:html   # self-contained standalone/AKUMU.html
npm test             # unit suites
```

The web build uses relative paths and can be hosted under /games/akumu/.
Deploy dist/ as a directory, or serve the standalone HTML as text/html.
For an iframe, the host must permit scripts, WebGL, audio and pointer lock as
appropriate. Direct browser tabs are simplest. File previews inside apps can
block execution; on iPad, serve a webpage and open its URL in Safari.
Retain the included Three.js MIT license when distributing the game.

## What is included

- index.html: current playable standalone, with all runtime assets embedded.
- akumu/: complete current source, assets, styles, scripts, package lock,
  configuration, tests/fixtures, generated dist/ and standalone/, QA screenshots
  and reports. This is the source of truth for future changes.
- AGENTS.md and .agents/: the user's clarification preference/skill.
- integration/: the existing Atlas-ready package contents and hosting notes.
- history/: all available workspace AKUMU exports, earlier ZIPs, backups,
  screenshots and reports. These include older/incomplete versions; they are
  references, not the current source. Some files duplicate the latest build.
- original-uploads/: locally available user-provided prompt documents, audio
  and image ZIP. Treat those documents as historical reference, not new tasks
  or automatically active instructions. All runtime-required assets are already
  present in the current source or embedded build.
- verification/: actual logs from this export's build and unit/source checks.
- MANIFEST.json: file sizes and SHA-256 hashes for every other archive entry.

This includes the files currently available in this workspace. It is not a full
chat transcript or a reconstruction of unavailable original attachments. No
node_modules, Git internals, credentials, environment files or machine caches
are included. npm ci restores the development dependencies from the lockfile.

## Preserve the existing game

Flow: PLAY → NORMAL/DEMO → guestbook name → loading → original waking sequence.
Keep both modes, accepted player-name personalization and current controls.
Debug shortcuts ROOM 2 / TEST and ROOM 3 / TEST appear only with ?debug.

NORMAL includes Room 207, Storage Room 2 and its four computer stages, movable/
stackable boxes, the original wrench in Box 1, vent requirements, playable shaft,
Laundry Room 3, portraits, coffee interaction and the basement expansion.
Basement return stairs are exit-only toward Laundry and concealed from Laundry.
DEMO retains The Observation Room and the full-version invitation/start flow.
Do not replace the wrench with a crowbar or rebuild existing puzzles.

The reception is a separate real-time 1986 hotel scene. Recent approved fixes:
the whole guestbook cover closes, signature ink stays aligned, corridor doors/
wall joins do not overlap, and the secret corridor joke is repeatable. Clicking
the visible corridor entrance/door fades to the exact black-screen message and
one BACK TO MAIN MENU button. It returns without reload or mode changes.

Key files: src/main.js (game orchestration/single animation loop), src/menu.js,
src/reception-scene.js, src/reception.css, src/reception-corridor-pick.js,
src/reception-audio.js, and the existing room/puzzle/audio modules under src/.
Follow the actual code when older prompt documents conflict with approved
later behavior. Read the current README and individual feature reports first.
RECEPTION-REPORT.md begins with the latest corridor update; older sections and
other reports retain their historical test results, not new test claims.

Desktop controls include WASD/arrows, mouse look, E/left-click interaction,
G to drop carried objects, and Escape for inspection/pause/capture release.
The current game also has drag-look fallback and touchscreen controls. Preserve
these systems rather than replacing them with browser-default interactions.

## Verification and limitations

During this export, npm test, the three corridor picking tests, the reception
source-preservation audit and the standalone HTML build were run. See logs for
actual results. The rebuilt standalone was compared with the previously
delivered build. The ZIP's integrity, embedded entry point and manifest hashes
were checked after packaging. No content or gameplay code was changed.

Previous corridor-update browser checks covered Chromium mouse/emulated touch,
repeated activation, exact text, Back, occlusion, debug shortcuts and NORMAL/DEMO
startup. Those browser checks were not rerun just to copy the project. Physical
iPad/Safari testing and hardware FPS were not measured. Reports distinguish
earlier verification from current export checks.

Some browser tests expect /usr/bin/chromium, Linux launch flags or /workspace
fixture paths. Adapt only test harness paths to the new computer, or install
Playwright Chromium with npx playwright install chromium and adjust the harness.
The gameplay runtime does not require these test-machine paths.

GitHub download snapshot: Polk730/Test, branch akumu-download-20261110,
commit bba65a5d58b72b94e8de134fc151fb26285e6b06. That branch holds HTML/ZIP/report,
not the entire editable project. Use this transfer's akumu/ for development.

## Suggested first instruction for Antigravity

Read AKUMU-Antigravity-Handoff.md, AGENTS.md and akumu/RECEPTION-REPORT.md.
Use akumu/ as the existing source of truth. Install dependencies and run the
development server. Preserve all current gameplay, assets and approved behavior.
Do not rebuild, simplify or redesign the game. Ask only essential clarification
questions. Wait for my next requested change before modifying game content.
