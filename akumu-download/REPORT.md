# Latest update: secret reception corridor

Clicking the visible corridor entrance or a visible corridor door from the reception title opens the requested secret joke. Entry fades to black in 0.55 seconds (0.1 seconds for reduced motion), then shows exactly “WOW! You did it.” and “(...probably the laziest way possible.)”, with a single ivory BACK TO MAIN MENU button and selection arrow. It stays until dismissed. Back restores the existing reception/PLAY screen without reloading or starting a mode; the event is repeatable. There is no narrator line, bell, stinger, image, new puzzle or gameplay change. Existing quiet button feedback is reused.

Picking uses the existing camera and Three.js raycaster against the actual visible reception meshes, plus a small world-space box aligned with the corridor opening. A nearer wall or desk occludes that target. Actual door-leaf hits are restricted to the corrected corridor door positions. There is no screen-wide invisible click region, added rendered geometry, dependency, animation loop or per-frame raycast. Listeners use the existing AbortController and are removed when the reception is disposed. Duplicate activation is blocked during the fade and while the secret is visible.

Changed files: `index.html`, `src/menu.js`, `src/reception.css`, new `src/reception-corridor-pick.js`, targeted `tests/reception-corridor-pick.test.js` and `tests/reception-corridor-secret.mjs`, `package.json` test command, this report and generated distributions. `src/main.js`, reception geometry, reception audio and gameplay assets were not changed.

Verification: standalone HTML and production web builds passed. Three targeted picking tests passed (opening versus wall/desk, visible/hidden occlusion, and actual corridor door). Chromium mouse and emulated touch checks passed for exact black-screen text and one button, persistent display, repeated activation, duplicate guarding, Back restoration without URL change or game start, wall/desk rejection, and visible-door activation. The door check used a held inspection camera because the normal reception view hides the right-hand door leaves. Desktop NORMAL and emulated-touch DEMO both reached the original introduction after PLAY → mode choice → guestbook → loading, retained the accepted name and produced no page errors. Both debug shortcuts still entered the guestbook and returned on desktop and touch. Desktop and touch secret-screen screenshots were visually inspected.

A source-preservation audit passed: 94 previous source/assets files and 39 gameplay functions remain byte-identical. Full puzzle/room playthroughs were not repeated for this isolated menu feature. Physical iPad, Safari and hardware FPS were not tested. Older sections describe earlier updates and their own verification.

---

# Latest correction: signature stays in place during book closing

The confirmation ink now uses the native name input's measured font, text baseline, colour, visible clipping area and horizontal scroll position rather than a separate hard-coded font/position. The HTML input is projected onto the exact 3D page surface. During confirmation, its text is replaced on the same render frame so there is no displaced or doubled signature.

Changed for this correction: `src/menu.js`, `src/reception-scene.js`, `tests/reception-signature.mjs` and its npm command. Name validation, personalization, menu flow and gameplay were not changed.

Verification: standalone HTML and production web builds passed. Targeted Chromium screenshot comparisons passed for desktop, phone-sized emulated touch and a long horizontally scrolled name. All four visible text bounds matched exactly before and after the handoff in every case. Real confirmation retained the accepted name and entered loading without page errors. The wider regression results below belong to the earlier updates and were not repeated for this local visual fix; physical iPad/Safari limitations remain unchanged.

---

# Latest correction: reception doors and wall joins

The three decorative corridor doors now occupy real openings in the wallpaper and lower wood panelling. Their leaves are recessed, the knobs meet the leaves, and jambs meet the head pieces edge-to-edge instead of overlapping. Corridor wall/ceiling ends meet the reception cleanly. The room and hall carpet now meet at one boundary with continuous texture coordinates instead of two coincident floor surfaces.

Changed for this correction: `src/reception-scene.js`, the targeted `tests/reception-doorway.mjs`, the npm test command and this report. No gameplay environment, route, controls, dialogue or menu flow was changed. The previous guestbook-cover fix is retained.

Verification: standalone HTML and production web builds passed. Browser probes of the actual batched geometry passed for all three recessed door leaves, uncovered lower doorway sections, single frame-joint surfaces, aligned wall headers, a single carpet surface and a clear corridor entry. Before/after close-ups and the menu-wide view were inspected. The earlier complete regression results below were not repeated for this menu-geometry-only change; physical-device/FPS limitations are unchanged.

---

# Latest correction: guestbook back cover

The stationary back board previously spanned both halves of the open register, leaving its left half on the table when the front cover shut. It now sits only under the right page block, matching the closed book. The closing animation, bell timing, name input and start flow are unchanged.

Changed for this fix: `src/reception-scene.js` (one board dimension/position), `tests/reception-book-cover.mjs` (targeted browser regression), and the corresponding npm test command/documentation.

Verification: standalone HTML and production web builds passed. A browser check of the real closed model measured an open width of 1.09 and a closed width of 0.56 in book-local units, with no remaining left-side board. The fully closed screenshot was inspected. Real name confirmation retained Alex and reached loading without page errors. The earlier complete regression results below were not repeated for this geometry-only fix.

---

# AKUMU — 1986 Reception

## Implemented presentation

The illustrated menu is replaced by a separate real-time Three.js reception scene rendered through the existing renderer and single animation loop. It contains a bevelled walnut counter, aged beige patterned wallpaper and dark panelling, faded burgundy carpet, a receding corridor with static doors, a numbered twelve-key rack, a curved rotary telephone and cord, a lathed tarnished-brass service bell, a fountain pen, a banker's lamp and a physical two-page guest register. There is no reception clock, wall logo, figure, moving key/door, secret event or new gameplay target.

Warm desk lighting contrasts with a dim greenish corridor fixture. The corridor flickers briefly at long irregular intervals. Geometry is batched by material; only the bell and book remain articulated. One 512-pixel shadowed light is reused with cached shadows; the existing renderer's DPR limits remain. Pointer movement gives a small smoothed camera offset; reduced motion disables parallax/tracking and shortens UI transitions. Fine grain/scanlines affect the background, while controls remain sharp.

The main title is faded ivory, with one text-only PLAY action and small selection arrows. Existing author credit remains subdued. The old menu music and illustrated flame/bird presentation are replaced by quiet filtered ventilation/tape noise, electrical hum and rare creaks. Bell/click sounds use the existing AudioContext and mixer; audio failure leaves navigation usable. There are no new narrator lines or gameplay sound changes.

## Preserved flow and personalization

Normal entry remains PLAY → NORMAL/DEMO → name entry → loading → original game introduction. PLAY rings once and briefly extinguishes the lights/fades; it cannot start duplicate transitions. Mode choice remains intact, with the same mode variables and handlers.

The original accessible text input, validation, 24-character limit and name setters are retained. The input form is projected onto the physical register page. Valid confirmation writes the name as ink on the page, folds the book closed, rings a quieter bell and invokes the unchanged game startup/preloader. Blood-wall, letter and terminal personalization keep using the existing name. The existing DEMO → PLAY FULL VERSION handoff still starts fresh NORMAL name entry.

ROOM 2 / TEST and ROOM 3 / TEST are hidden by default and visible only with `?debug`. Their original destinations and startup flags are unchanged. Returning to title skips the full tracking intro using a presentation-only session flag; no gameplay save behavior was introduced.

## Loading and interface

The existing loading screen is an aged hotel arrival document with a thin ink progress bar. Progress still comes from the original resource/preload tasks, with no fake percentage or additional loading delay. No seamless room-transition loading screen was added.

Mode, guestbook, loading, pause, return/full-version and generic inspection/touch controls share restrained retro typography and spacing. The original `style.css`, including all Room 2 terminal styling, is byte-identical; the new stylesheet uses scoped overrides and leaves the in-world computer unchanged.

## Files

Changed: `src/main.js` (presentation hooks only), `src/menu.js` (new menu controller), `index.html` (semantic title/guestbook/document markup), `package.json` and `README.md` (current workflow/tests).

New: `src/reception-scene.js`, `src/reception-audio.js`, `src/reception.css`, this report, `tests/reception-flow.mjs`, `tests/reception-presentation.mjs`, `tests/reception-preservation.mjs`, `tests/reception-preview.mjs` and the reception baseline fixture. The existing basement browser script accepts `--touch-only` for targeted regression runs. Build/export artifacts were regenerated.

Backup: `/workspace/AKUMU-Before-Reception/`. The source audit confirms 94 existing source/assets files and 39 main.js functions are byte-identical, including the start/preload implementation, controls, puzzles, room transitions, basement movement and endings. No gameplay environment module or existing audio asset was modified.

## Checks actually performed

- Production standalone HTML and web builds passed.
- 60 existing unit tests, four basement tests, three coffee tests and two Laundry tests passed (69 total).
- Source-preservation audit passed.
- Desktop and emulated-touch regular menu flows passed at a nested `/games/akumu/` URL: exactly one visible PLAY, hidden debug controls, classic pointer, mode selection, one bell per activation, validation, duplicate-submit guard, two scheduled bell cues, book-close/loading sequence, original introduction, pause/return and no repeated full startup.
- The final phone flow also passed after the portrait camera correction and both keyboard-layout simulations: a resized layout viewport and a smaller visual viewport with unchanged layout height. Input and confirmation remained visible.
- Debug presentation checks passed: actual 3D scene/props, bounded parallax, reduced-motion behavior, both debug guestbook entries and portrait framing.
- With AudioContext deliberately made unavailable, PLAY, mode choice and guestbook input still worked without page errors.
- Desktop full Room 1 puzzle and physical entry into Storage passed, including hammer/barricade/key/door and name retention.
- Desktop full Room 2 route passed: original letter/voice, all computer stages, separate box opening, carrying/restacking, wrench guard/collection, physical climb, vent, manual shaft traversal, Laundry exit/landing and models.
- Touch basement regression passed: hidden washer, slide, upward exit, blocked Laundry re-entry, one-way surface, visible steps and one primary basement bulb.
- Touch DEMO invitation/NORMAL handoff regression passed: live-camera silence, post-black delay, once-only invitation, button gating, fresh NORMAL guestbook entry/start and unchanged NORMAL ending. A short test audio buffer verified finish gating; no new narrator recording was added.
- Screenshots inspected: wide reception, mode screen, guestbook, loading document, portrait menu and keyboard-adjusted page.

## Limitations

Tests used software-rendered Chromium and emulated touch. Physical iPad/Safari, actual on-screen keyboards and ordinary school-computer frame rates were not measured; no FPS guarantee is made. The automated keyboard checks simulate both common viewport behaviors. Initial shader/asset preparation depends on the device. If sessionStorage is unavailable, the brief presentation intro can repeat on reload; gameplay still works.

All runtime assets and Three.js remain embedded in the standalone HTML. No paid service, account, secret key, external font or runtime CDN is required. Existing static-hosting, CSP, WebGL2 and iframe pointer-lock requirements remain in the Atlas README. Legacy artwork/pixel-menu screenshot expectations are superseded by the reception checks.
