# Room 3 basement expansion

The existing Laundry Room now has one secret washer (the rightmost of the four). With the existing interaction control, open its hinged door, then interact with the opening again to enter a 3.5-second first-person metal chute. There are no floating hints. Movement resumes at a safe basement landing.

The basement is 6 × 6 metres with a 2.2-metre ceiling, one warm flickering bulb, indirect ambient fill, worn concrete/brick, damp patches, pipes, shelves, cartons, crates, chairs, a damaged table, draped furniture, suitcases, mirrors, an off CRT partly hidden on a low shelf, and a closed damaged wardrobe. Props are decoration only. Spatial drips, pipe noises, occasional creaks and muffled footsteps above leave quiet intervals; dry, wet and metal stair footsteps use the existing audio mixer.

Eighteen real stair treads and railings connect to an open Laundry doorway. Walking works in both directions without teleportation or a scripted return. Perimeter, stair and furniture collisions keep players inside the traversable area. Existing coffee cups can be carried between the areas. No puzzle, clue, collectible, narrator line, monster or ending was added.

## Files

Changed existing game files: `src/main.js` (integration, route, movement, preload and sound), `src/laundry-room.js` (one washer and stair opening), `src/coffee-play.js` (shared walking space and carry visibility during the chute).

New modules: `src/basement-layout.js`, `src/basement-journey.js`, `src/secret-washer.js`, `src/basement-room.js`, `src/basement-audio.js`. New route/state tests: `tests/basement.test.js`, `tests/basement-browser.mjs`. Existing Laundry/portrait browser assertions now allow the one additional washer target. `package.json` adds the basement test command; `README.md` documents the expansion. Standalone/web builds and download packages were regenerated.

The prior complete game and source were backed up in `/workspace/AKUMU-Before-Basement/`. A hash audit against that backup finds 88 existing source/assets files unchanged; only the three integration files above changed. The preservation check also confirms 78 earlier source/assets files and 28 unrelated main.js function bodies are byte-identical, including the original ending, mode selection and room-transition functions. Storage puzzles, wrench requirements, portrait images and DEMO modules were not edited.

## Verification

- Production web build and standalone HTML build passed.
- Existing `npm test` suite passed (60 tests).
- Three new basement tests passed: dimensions and bidirectional collision traversal, perimeter/doorway guards, and one-at-a-time/pause-safe 3.5-second slide with a valid landing.
- Three existing coffee state tests and two Laundry journey/collision tests passed.
- Desktop Chromium: hidden washer has no prompt; first interaction opens it; second slides and lands; actual keyboard movement traverses the stairs both ways and restores the correct floor height. One primary bulb and no page errors verified.
- Emulated-touch Chromium: the same washer/slide route passed; actual joystick movement traversed both directions on the stairs, with correct standing heights and no page errors.
- Existing coffee desktop and emulated-touch browser regressions passed: timed spill cleanup, pickup/place/brew/drink, 3× boost and reversion, safe drop and second cup.
- Full existing Room 2 desktop browser route passed: original letter and voice, all computer stages, box opening/carrying/restacking, wrench guards and separate collection, physical climb, vent opening, manual shaft traversal, exit grille and Laundry landing/models.
- After cutting the physical chute aperture, the final desktop build replay passed. A triangle-level check of the actual batched meshes verifies that no solid geometry crosses the chute exit. This geometry-only correction was checked on desktop; touch controls had already passed the same route.
- Full Room 1 desktop browser puzzle passed: notes, mechanical drawer code, hammer pickup/drop, barricade break, key reveal/collection, door opening and physical entry into Room 2; no console/page errors.
- Desktop and emulated-touch DEMO invitation regressions passed: live-camera silence, post-black delay, once-only invitation, button gating, fresh NORMAL name entry/start and preserved NORMAL ending. Desktop used the existing caption fallback; touch used a short test audio buffer to verify completion gating. No new narrator recording was added.
- Player-view screenshots inspected for the open washer, basement shelves/lighting and stair arrival.

## Limits

Browser testing uses software-rendered Chromium. Physical iPad/Safari and real-device frame rates have not been measured. The basement has no puzzle or further progression by design. The staircase is intentionally open and freely walkable in either direction. Static hosting and browser restrictions are unchanged; see the Atlas README for iframe/pointer-lock and mobile preview requirements.
