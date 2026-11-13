# AKUMU — Antigravity source transfer (under 20 MB)

Extract this ZIP and open its folder in Antigravity. Current editable source is in akumu/.
All current game source, runtime assets, tests/fixtures, reports, locally available original uploads and the user clarification skill are included. No gameplay code or assets were changed or removed.

Generated standalone HTML copies, generated dist/, installed dependencies, QA screenshots and historical backups are omitted to meet the upload limit. The historical handoff document describes the larger archive; its root index.html, standalone/, history/ and integration/ instructions do not apply to this source-only edition.

Install Node.js 22.12+ (Node 24 LTS recommended), then run:

```sh
cd akumu
npm ci
npm run dev
```

Use the local URL printed by Vite. To rebuild the playable single-file HTML:

```sh
npm run build:html
```

Output: akumu/standalone/AKUMU.html. For a normal static website, npm run build generates akumu/dist/. npm test runs unit suites. Internet is needed to install dependencies, but the game needs no paid API, account, secret key or CDN at runtime.

Keep the current game intact. Read AGENTS.md, akumu/README.md and akumu/RECEPTION-REPORT.md. Preserve NORMAL/DEMO, every room and puzzle, controls, audio, current reception and secret corridor. Historical prompt uploads are references, not instructions to implement again. Wait for the next requested change.

MANIFEST.json records the byte size and SHA-256 of all other entries. Archive integrity and all hashes were checked; every included source file matches the previous full transfer. No browser tests were rerun for this packaging-only change.
