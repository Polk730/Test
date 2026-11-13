# AKUMU — two-part transfer for the 8 MB attachment limit

Upload BOTH ZIPs to Antigravity. They are separate normal ZIP archives, not split binary volumes. Extract both into the same project folder, preserving paths.

1. AKUMU-Antigravity-1-Project.zip: complete current editable source, runtime assets, tests/fixtures, reports, user skill and existing handoff notes. This archive alone contains everything required to build and run the current game.
2. AKUMU-Antigravity-2-References.zip: available original user uploads and historical prompt documents. These are supplementary references, not new implementation instructions. Do not reimplement old requests from them.

Current source is akumu/. No gameplay or runtime assets were removed. These two archives together preserve every file from the previous 13.73 MB export, except that START-HERE.md and its manifest have been replaced by these corrected instructions and per-archive manifests. Earlier handoff notes describe a larger historical export; generated standalone HTML, dist/, old backups and screenshots are absent here.

Install Node.js 22.12+ (Node 24 LTS recommended), then:

```sh
cd akumu
npm ci
npm run dev
```

For a playable single HTML file, run npm run build:html; output is akumu/standalone/AKUMU.html. npm run build creates dist/. Internet is needed to install dependencies, but runtime needs no paid API, account, secret key or CDN.

Read AGENTS.md, akumu/README.md and akumu/RECEPTION-REPORT.md. Preserve all existing modes, rooms, puzzles, controls, sounds and approved reception behavior. Wait for the user's next requested change. Do not rebuild or simplify the game.

Verification for this repackaging: both ZIPs are below 8,000,000 bytes (also below the reported 8,388,608-byte limit), CRC and SHA-256 manifests passed, and all preserved entries match the prior export byte-for-byte. No gameplay files changed; browser tests were not rerun for packaging.
