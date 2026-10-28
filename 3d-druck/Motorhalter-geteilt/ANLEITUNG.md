# Geteilter Motorhalter – Motor Ø 24 × 30,5 mm

Diese Alternative ersetzt **nur den bisherigen einteiligen Motorhalter**.
Propeller-B.stl und Schutzgitter-B.stl bleiben unverändert. Den alten einteiligen
Halter nicht zusätzlich verwenden. Das Gesamtmodell besteht jetzt aus fünf
Druckteilen statt drei; die ursprüngliche Drei-Teile-Vorgabe wird damit bewusst
auf Wunsch geändert.

## Die drei neuen STL-Dateien

| Datei | Funktion | Druckausrichtung |
|---|---|---|
| 01-Motorhuelse-24mm.stl | Motoraufnahme mit Montageflansch | Breiter Flansch auf Druckbett, Hülse nach oben |
| 02-Hinteres-Gitter.stl | Hinteres Gitter mit Motor- und Fußaufnahme | Ebene Gitterfront auf Druckbett, Fußaufnahmen nach oben |
| 03-Standfuss.stl | Breite Basis mit zwei Steckzapfen | Breite Bodenfläche auf Druckbett, Zapfen nach oben |

Gesamthöhe montiert ca. 99,6 mm, maximale Breite 96,2 mm.
Die STLs sind bereits so ausgerichtet, Unterkante Z=0. In Tinkercad und im
Slicer **Millimeter, 100 %** wählen. Nicht gemeinsam automatisch skalieren.
Alle Geometrien wachsen in dieser Ausrichtung vom Bett aus; es sind keine
absichtlich frei in der Luft beginnenden Flächen vorhanden. Kleine Überhänge
an Kabelöffnungen und Passrippen bleiben. Für die kleinen oberen Absätze
des Standfußes lokale Stützen vorsehen. Hülse und Gitter sind für den Druck
ohne flächige Stützen ausgelegt. Noch nicht durch Slicing oder Probedruck bestätigt.

Ausgangsprofil: PETG, 0,4-mm-Düse, 0,2-mm-Schichten, 3 Wände, 4 Boden- und
Deckschichten, 20–30 % Infill. Vor dem Drucken die Schichtvorschau kontrollieren.
Die Druckzeit hängt vom Druckerprofil ab; maximal 2 Stunden pro Teil sind nicht
verifiziert.

## Zusätzlich für die Montage

- 3 × M3×10-Senkschrauben, üblicher 90°-Kopf, Kopfdurchmesser maximal 6,4 mm.
- 3 × M3-Muttern; Schraubenlänge gegen tatsächliche Hardware kontrollieren.
- Materialgeeigneter Klebstoff für die beiden Fußzapfen, ohne Motor mitzunehmen.

Die Motorhülse wird **verschraubt**, nicht nur eingeklipst. Die Senkköpfe müssen
bündig sitzen, damit der Propeller sie nicht berührt. Nicht stark anziehen:
Die Flanschplatte ist 2 mm dick. Bei anderem Schraubenkopf nicht gewaltsam
versenken. Muttern liegen hinter dem hinteren Gitter und sind außen am Motor
zugänglich.

## Montage

1. Teile entgraten. 3,2-mm-Schraubenlöcher und 29,2-mm-Zentrieröffnung prüfen.
2. Die Motorhülse von der Vorderseite durch die zentrale Gitteröffnung schieben,
   bis der breite Flansch vorne plan aufliegt. Die drei Schraubenlöcher decken
   sich. Mit den drei M3-Senkschrauben und rückseitigen Muttern befestigen.
3. Die zwei Fußzapfen von unten in die rückseitigen Rechteckaufnahmen schieben.
   Zapfen 3,8 × 2 mm, Aufnahmen 4,0 × 2,2 mm. Vor dem Kleben trocken anpassen,
   dann mit geeignetem Klebstoff fixieren und vollständig aushärten lassen.
4. Motor von hinten einsetzen und Kabel durch die Aussparungen führen.
   Motoraufnahme: 24,2 mm Grundbohrung, Länge 30,5 mm; drei Anpassrippen
   verengen lokal auf etwa 23,8 mm. Bei Bedarf nur die Rippen vorsichtig
   nacharbeiten. Der reale Drucker und Motor bestimmen die Passform.
5. Den vorhandenen Propeller mit mindestens 1 mm Abstand zur 2-mm-Frontplatte
   einsetzen. Motorwelle beim Aufsetzen abstützen, nicht hämmern. Von Hand drehen.
6. Das unveränderte vordere Schutzgitter **4 mm weiter nach hinten** schieben
   als bei der einteiligen Version: Sein rückseitiger Rand sitzt bündig mit
   der Rückseite des 4-mm-Ringflanschs. Der Anschlussdurchmesser bleibt 92 mm.
   In der CAD-Einbaulage reicht der neue Ringflansch von Z=-4 bis Z=0;
   das vordere Gitter reicht von Z=-4 bis Z=14, sein Frontgitter von Z=12 bis 14.
   Der Propeller bleibt von Z=3 bis 11: nominal mindestens 1 mm axialer Abstand.
   Die STL-Druckausrichtungen sind nicht mit diesen Einbaukoordinaten identisch.
7. Nach vollständiger Montage erneut alle Freiräume von Hand prüfen. Frontgitter
   und Fuß müssen fest sitzen. Erst danach mit niedriger Drehzahl testen.

## Prüfstand und Grenzen

Alle drei STLs wurden mit OpenSCAD/CGAL gerendert. Der beigefügte Prüfbericht
kontrolliert je einen geschlossenen, zusammenhängenden Körper, konsistente
Dreiecksorientierung und Abmessungen unter 100 mm. Die zehn möglichen
Paarungen der fünf Druckteile wurden zusätzlich in Einbaulage auf
Volumenüberschneidungen geprüft: alle zehn ohne Volumenkollision bestanden. Berührende Montageflächen sind vorgesehen.
Das prüft keine Drucktoleranzen, Schrauben, Klebstoff, Motor oder Verformung.

Keine physische Passprobe, kein Probedruck, keine Festigkeits- oder
Drehzahlfreigabe. Bei Vibration, Rissen oder Schleifen stoppen. Ein gedrucktes
Gitter ist kein zertifizierter Berstschutz; keine Freigabe für 14.500 rpm.
Motoranschluss fachkundig prüfen lassen. Nicht im laufenden Zustand anfassen.

Motorhalter-geteilt.scad ist die bearbeitbare OpenSCAD-Quelle; zum Import
in Tinkercad sind nur die drei STL-Dateien nötig.
