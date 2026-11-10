# Visible, exit-only basement stairs

The existing stairs now have lighter worn metal treads, pale painted nosings and more readable rails. The lower metre of the stairwell side walls is opened so the existing basement bulb can illuminate the first steps naturally. Subtle indirect fill on the treads and nosings helps retain their shape in shadow; existing Laundry fixtures stay lit so the room above is visible. No extra lamp was added.

A metal return gate at the top opens automatically while the player walks up from the basement and closes after the player clears it into Laundry. It requires no interaction, code, key or puzzle. The player can no longer enter the basement through these stairs from Laundry, even while the gate is closing. The secret washer remains the entrance. The upper opening is opaque from Laundry and see-through from the stair side, so the stairs stay concealed from above while the player can see the Laundry Room on the way up.

Changed game files: `src/basement-room.js` (visible stairs and automatic return gate), `src/basement-layout.js` (one-way swept movement guard), `src/main.js` (gate animation and the local movement integration). Updated the basement unit/browser tests. Room 1, Storage puzzles, wrench requirements, Laundry coffee, portraits and DEMO modules were not changed.

Checks completed:

- Production standalone HTML and web builds passed.
- 60 existing unit tests, four basement tests, three coffee tests and two Laundry tests passed (69 total).
- The new movement test covers upward exit without interaction, repeated blocked entry from Laundry, fast moves and diagonal/side approaches.
- Source-preservation audit passed: 78 earlier source/assets files and 28 unrelated main.js function bodies remain byte-identical, including original ending, mode selection and room transitions.

- Final desktop Chromium route passed: washer/slide, visible stairs, automatic upward exit using actual keyboard movement, correct Laundry standing height, gate closing and blocked return using actual input.
- One-way screen orientation checked in the browser; player-view screenshots inspected from below and from Laundry. The lower view shows the steps and upper room, while Laundry shows the opaque face.
- Final emulated-touch Chromium route passed: washer/slide, visible stairs, automatic upward exit with the joystick, correct standing height and blocked return from Laundry. Both browser runs reported no page errors and confirmed the basement still has exactly one primary bulb.

Limits: no physical iPad/Safari testing or hardware FPS benchmark. This update intentionally replaces the earlier two-way stair design with an exit-only return. There is no new puzzle.
