# OpenPool

OpenPool ist eine eigene Poolsteuerungs-App ähnlich EVCC.

## Start

Aktueller Stand:

- `index.html` enthält den bereinigten HTML-Prototyp.
- `openpool/` enthält die Home-Assistant-Add-on-Hülle für die Einbindung über ein GitHub Repository.
- `repository.yaml` und `repository.json` liegen im Root, damit Home Assistant das Repository als Add-on Repository erkennen kann.

## Wichtige Regeln

- Hauptfreigabe AUS sperrt alles.
- Heizung darf nur mit Pumpenflow laufen.
- Pumpe AUS bedeutet: zuerst Heizung AUS; 5 Minuten Nachlauf nur, wenn die Heizung noch läuft oder erst kürzlich ausging.
- Neue Steuerung während Nachlauf bricht Nachlauf ab.
- Intex 26680 braucht regelmäßige Restart-Pulse.
- Nachtbaden ist eigener Modus mit Pumpe + Heizung EIN, max. 10h.
