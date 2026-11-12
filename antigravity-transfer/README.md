# AKUMU — vollständiger Projekttransfer

## Vollständige ZIP mit einem Klick

[AKUMU-Antigravity-Complete.zip herunterladen (ca. 300 MB)](https://github.com/Polk730/Test/releases/download/akumu-antigravity-2026-11-12/AKUMU-Antigravity-Complete.zip)

GitHub hat die vier Teile erfolgreich zusammengesetzt, ihre Prüfsummen geprüft und die vollständige ZIP als Release veröffentlicht. Diesen Download kannst du direkt entpacken; kein Zusammensetzen nötig. Die Teile unten bleiben als zusätzlicher Downloadweg erhalten.

## Aktuelles Projekt als einzelne ZIP

[AKUMU-Antigravity-Current.zip herunterladen](https://raw.githubusercontent.com/Polk730/Test/akumu-download-20261110/antigravity-transfer/AKUMU-Antigravity-Current.zip)

Diese ZIP enthält den gesamten aktuellen bearbeitbaren Spielcode, alle benötigten Spielassets, Tests, Berichte, verfügbare Original-Uploads, den Skill und die neueste spielbare HTML. Für die Weiterentwicklung reicht diese Datei. Historische Backups und QA-Screenshots sind nur im vollständigen Archiv unten.

## Vollständiges Archiv inklusive aller verfügbaren alten Versionen und Backups

Die vollständige ZIP ist etwa 300 MB groß. GitHub hat ein Limit von 100 MB pro normaler Repository-Datei; Releases waren aus der Exportumgebung nicht zugänglich. Deshalb liegt die unveränderte vollständige ZIP in vier Teilen vor. Keiner davon ist allein die vollständige ZIP.

Alle vier Dateien herunterladen und im selben Ordner speichern:

- [Teil 1](https://raw.githubusercontent.com/Polk730/Test/akumu-download-20261110/antigravity-transfer/AKUMU-Antigravity-Complete.zip.001)
- [Teil 2](https://raw.githubusercontent.com/Polk730/Test/akumu-download-20261110/antigravity-transfer/AKUMU-Antigravity-Complete.zip.002)
- [Teil 3](https://raw.githubusercontent.com/Polk730/Test/akumu-download-20261110/antigravity-transfer/AKUMU-Antigravity-Complete.zip.003)
- [Teil 4](https://raw.githubusercontent.com/Polk730/Test/akumu-download-20261110/antigravity-transfer/AKUMU-Antigravity-Complete.zip.004)

### Windows

In diesem Ordner **cmd** öffnen und folgenden Befehl ausführen (in der Eingabeaufforderung, nicht PowerShell):

```bat
copy /b AKUMU-Antigravity-Complete.zip.001+AKUMU-Antigravity-Complete.zip.002+AKUMU-Antigravity-Complete.zip.003+AKUMU-Antigravity-Complete.zip.004 AKUMU-Antigravity-Complete.zip
```

Die entstandene `AKUMU-Antigravity-Complete.zip` normal entpacken. Der Befehl liest die vier Teile und erzeugt nur die neue ZIP; er verändert die Teile nicht.

### macOS / Linux

Terminal im Downloadordner öffnen:

```sh
cat AKUMU-Antigravity-Complete.zip.001 AKUMU-Antigravity-Complete.zip.002 AKUMU-Antigravity-Complete.zip.003 AKUMU-Antigravity-Complete.zip.004 > AKUMU-Antigravity-Complete.zip
```

Alternativ kann 7-Zip das vollständige Split-Archiv über `.001` öffnen, wenn alle vier Teile danebenliegen.

## Weiterarbeiten

Entpackten Ordner in Antigravity öffnen. Der aktuelle Quellcode liegt in `akumu/`, ältere Versionen in `history/`. `AKUMU-Antigravity-Handoff.md` zuerst lesen. Der Export ändert kein Gameplay. Die Wurzeldatei `index.html` ist die neueste spielbare Standalone-Version.

`SHA256.json` enthält Dateigrößen und Prüfsummen der vier Teile und der zusammengesetzten vollständigen ZIP. Das vollständige Archiv enthält zusätzlich ein geprüftes Dateimanifest. Es enthält die verfügbaren Projektdateien und Uploads, keinen vollständigen Chatverlauf.
