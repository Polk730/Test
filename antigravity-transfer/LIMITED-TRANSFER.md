# AKUMU — transfer with both attachment limits respected

Upload ALL THREE AKUMU-Transfer-Part-1.zip, AKUMU-Transfer-Part-2.zip and AKUMU-Transfer-Part-3.zip to Antigravity. These are separate standard ZIP files, not binary split volumes. Each contains fewer than 100 entries and is below 8,000,000 bytes. Extract all three into the SAME folder, preserving paths. Do not run the project until all three have been extracted. They contain different files with no conflicting replacements.

Together they contain the complete current game source, runtime assets, tests/fixtures, reports, existing user skill and available original uploads. No gameplay source/assets were removed. Earlier START-HERE/manifest files were replaced with these corrected instructions and per-part manifests. Earlier handoff documents describe larger historical exports; generated standalone HTML, dist/, old backups and QA screenshots are not in this source edition.

Current source: akumu/. Install Node.js 22.12+ (Node 24 LTS recommended). In that directory run npm ci, then npm run dev and open the local URL printed by Vite. To build a playable single HTML file, run npm run build:html; output is standalone/AKUMU.html. npm run build creates the static dist/ website. npm test runs unit suites. Internet is needed for npm installation, but runtime needs no paid API, account, secret key or CDN.

Read AGENTS.md, akumu/README.md and akumu/RECEPTION-REPORT.md. Preserve all modes, rooms, puzzles, controls, sounds and approved reception behavior. Original uploads are references, not new tasks. Wait for the user's next requested change; do not rebuild or simplify the game.

All three ZIPs were checked for size, entry count, CRC and manifest hashes. Their combined preserved files were compared byte-for-byte with the previous two-part transfer. This is packaging only; gameplay was not changed and browser tests were not rerun.
