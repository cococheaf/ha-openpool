# OpenPool

[English version](README.en.md)

OpenPool ist ein OpenSource Pool System Controller für Home Assistant. Das
Add-on steuert Pumpe, Chlorsystem, Wärmepumpe und PV-Überschussheizung über
eine kompakte Oberfläche, die besonders für Tablet-Dashboards wie ein iPad in
Home Assistant gedacht ist.

Aktuell ist OpenPool gezielt für ein Setup rund um das Intex 26680
Sandfilter-/Salzwasserelektrolyse-System ausgelegt. Andere Systeme können
funktionieren, sind derzeit aber nicht der primäre Entwicklungsfokus.

![OpenPool Dashboard Demo](../OpenPool_DemoImage.png)

## Warum dieses Add-on entstanden ist

OpenPool kommt aus einem ganz praktischen Familienproblem: Ein sauberer Pool im
Garten sollte den Sommer entspannter machen, ohne jedes Mal mit Kindern,
Badetaschen und allem Drumherum ins Freibad fahren zu müssen. Aus einem Intex
XTR Frame Pool wurde nach der ersten Saison schnell ein Setup mit stärkerer
Sandfilter- und Salzwasserelektrolyse-Anlage. Die Wasserqualität wurde besser,
aber die Steuerung blieb unflexibel.

Ein Tasmota Smartplug half zunächst, die Intex 26680 bequem aus Home Assistant
zu schalten. Dabei zeigte sich, dass der Chlorgenerator nach einem Stromverlust
wieder anlief, was sich als einfacher Restart-Pulse nutzen ließ. Mit einer
zusätzlichen Wärmepumpe wurde das Zusammenspiel aber schwieriger: Die
Wärmepumpe braucht sicheren Volumenstrom, während die Pumpe weiterhin gezielt
für die Chlorproduktion geschaltet werden muss.

OpenPool verbindet diese Teile deshalb in einer gemeinsamen Logik. Home
Assistant liefert die Schalter und Sensoren, OpenPool übernimmt die
Entscheidungen.

## Was OpenPool macht

- Pumpenprofile für Badebetrieb, Schlechtwetter, Dauerbetrieb, Nachtbaden und
  Aus.
- Automatische Restart-Pulse für das Chlorsystem.
- Chlorinator-Anzeige aus der Pumpenleistung mit konfigurierbaren
  Leistungsschwellen.
- Sicherer Pumpennachlauf nach Heizbetrieb.
- Wärmepumpensteuerung mit Zieltemperatur.
- Wärmepumpenfreigabe mit Start-/Stoppgrenzen und Stabilzeiten.
- Wetterempfehlung aus der täglichen Home-Assistant-Vorhersage.
- Live-Synchronisation zwischen mehreren geöffneten UI-Sitzungen.
- Persistenter Controller-State in `/data/openpool_state.json`, damit Laufzeit,
  Jobs und Aufgabenverlauf nach einem Neustart erhalten bleiben.
- Wettersteuerung und Wärmepumpensteuerung optional per Add-on-Konfiguration.

## Wichtig vor dem ersten Start

Bitte passe vor dem ersten echten Test die Entitäten in der Add-on-Konfiguration
an deine Home-Assistant-Installation an. Die mitgelieferten Entity-IDs sind
Beispiele aus der ursprünglichen Anlage.

Besonders wichtig sind:

- `pump_switch`
- `heater_climate`
- `weather`
- `pv_generation`
- `pv_export`
- `grid_import`
- Pumpen- und Heizungssensoren für Leistung, Strom, Spannung, Signal und
  Temperaturen

Wenn diese Entitäten nicht korrekt sind, kann OpenPool keine zuverlässigen
Entscheidungen treffen oder Befehle an die falschen beziehungsweise an keine
Geräte senden.

Die Wetter-Entität ist nicht an einen festen Anbieter gebunden. Trage in
`entities.weather` einfach die Weather-Entität deiner bevorzugten
Home-Assistant-Integration ein.

## Home-Assistant-Verlauf

Standardmäßig nutzt das Add-on den Home-Assistant-`SUPERVISOR_TOKEN`. Damit ist
keine zusätzliche Anmeldung nötig, der Home-Assistant-Verlauf zeigt
Service-Calls aber als vom Supervisor ausgelöst.

Soll der Verlauf `wurde ausgelöst durch OpenPool` anzeigen, lege in Home
Assistant einen Benutzer namens `OpenPool` an, erstelle in dessen Profil einen
Long-Lived Access Token und setze in der Add-on-Konfiguration:

```yaml
connection:
  auth_mode: openpool_user_token
  access_token: "TOKEN_DES_OPENPOOL_BENUTZERS"
```

OpenPool nutzt dann diesen Benutzer-Token für Home-Assistant-Service-Calls.

## Installation

1. In Home Assistant **Einstellungen -> Add-ons -> Add-on Store** öffnen.
2. Unter **Repositories** `https://github.com/cococheaf/ha-openpool` hinzufügen
   und den Store neu laden.
3. **OpenPool** installieren.
4. Add-on-Konfiguration anpassen, insbesondere alle Entitäten.
5. Add-on starten und **In Seitenleiste anzeigen** aktivieren.

## Status

Das Add-on stellt die OpenPool-Weboberfläche über Home Assistant Ingress bereit.
Die Automatik läuft im Add-on-Server, nicht im Browser. Dadurch bleiben mehrere
offene Oberflächen synchron, und Laufzeiten sowie geplante Jobs überstehen
Frontend-Reloads und Add-on-Neustarts.
