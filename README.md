# OpenPool

[English version](README.en.md)

OpenPool ist ein OpenSource Pool System Controller fuer Home Assistant. Das
Add-on steuert Pumpe, Chlorsystem, Waermepumpe, Wetterprofile und
PV-Ueberschussheizung aus einer kompakten Weboberflaeche. Die eigentliche
Automatik laeuft serverseitig im Home Assistant Add-on, damit Browser, iPad und
Smartphone immer denselben Zustand sehen.

OpenPool ist derzeit gezielt fuer Setups rund um das Intex 26680
Sandfilter-/Salzwasserelektrolyse-System ausgelegt. Andere Systeme koennen
funktionieren, sind aber noch nicht der primaere Entwicklungsfokus.

## Screenshots

| Desktop | Tablet | iPhone |
| --- | --- | --- |
| ![OpenPool Desktop](docs/screenshots/openpool-desktop.png) | ![OpenPool Tablet](docs/screenshots/openpool-tablet.png) | ![OpenPool iPhone](docs/screenshots/openpool-iphone.png) |

## Warum OpenPool entstanden ist

Ausgangspunkt war ein Intex Frame Pool, der im Sommer sauber und ohne staendige
Handarbeit laufen sollte. Die originale Filterpumpe war zu schwach, die spaeter
nachgeruestete Intex 26680 Kombination aus Sandfilter und Salzwasserelektrolyse
war besser, aber in der Zeitsteuerung unflexibel. Ein Tasmota Smartplug machte
das Schalten bequemer und zeigte nebenbei, dass der Chlorinator nach einem
kurzen Stromverlust wieder startet.

Mit einer Waermepumpe wurde daraus ein echtes Steuerungsproblem: Die
Waermepumpe braucht sicheren Volumenstrom, die Pumpe muss fuer Chlorung und
Profile aber weiterhin gezielt geschaltet werden. OpenPool verbindet diese
Logik mit den ohnehin vorhandenen Home-Assistant-Entitaeten.

## Funktionen

- Pumpenprofile: Aus, Dauerbetrieb, Badebetrieb, Schlechtwetter und
  Nachtbaden.
- Einstellbare Nachtbadedauer und Restart-Pulse fuer das Chlorsystem.
- Chlorinator-Erkennung ueber die Pumpenleistung.
- Waermepumpensteuerung mit Zieltemperatur, Start-Betriebsmodus aus
  Home-Assistant-Selector, Pumpennachlauf und optionaler PV-Automatik.
- PV-Freigabe mit Start-/Stoppgrenzen, Stabilzeiten und optionaler
  Batterie-Prioritaet.
- Abschaltbare Batterielogik fuer Anlagen ohne Batteriespeicher.
- Wettersteuerung als Empfehlung oder Automatik fuer Badebetrieb und
  Schlechtwetterprofil.
- Provider-neutrale Wetter-Entitaet, nur zwei Vorhersageabrufe pro Tag.
- Live-Sync zwischen mehreren offenen Oberflaechen.
- Persistenter Controller-State in `/data/openpool_state.json`.
- Konfiguration komplett ueber Home Assistant Add-on-Optionen.

## Wichtig vor dem ersten Start

Die Entity-IDs in der Add-on-Konfiguration muessen vor dem ersten Live-Test an
deine Home-Assistant-Installation angepasst werden. Die Standardwerte sind nur
Beispiele aus der urspruenglichen OpenPool-Anlage.

Besonders wichtig sind:

- `devices.pump_and_chlorinator_switch`
- `devices.heat_pump`
- `devices.heat_pump_operating_mode`
- `devices.weather_service`
- `features.battery_logic`, falls Batteriesensoren und Batterie-Prioritaet
  genutzt werden sollen
- `energy.pv_production_sensor`
- Energie/Netz/Batterie: entweder `energy.grid_export_sensor` und
  `energy.grid_import_sensor` oder `energy.shared_grid_power_sensor` mit
  `energy.one_grid_sensor_for_import_and_export` und passender Vorzeichen-Option
  `energy.positive_grid_value_is_import`. Fuer Batteriespeicher kann entweder
  `energy.shared_battery_power_sensor` mit
  `energy.one_battery_sensor_for_charge_and_discharge` und
  `energy.positive_battery_value_is_charge` verwendet werden oder getrennt
  `energy.battery_charge_sensor` und `energy.battery_discharge_sensor`.
  `energy.battery_soc_sensor` zeigt optional den Batterie-Ladezustand an.
  `energy.battery_discharge_threshold_w` legt fest, welche kurze
  Batterie-Entladespitze bei Batterie-Prioritaet noch toleriert wird.
  `energy.prefer_battery_charging` sorgt dafuer, dass OpenPool die Waermepumpe
  erst freigibt, wenn nach Hausverbrauch und Batterieladung noch genug
  PV-Ueberschuss bleibt. Wenn die Batterie nicht laedt und trotzdem
  PV-Ueberschuss bleibt, behandelt OpenPool sie als voll. Bei aktiver
  Batterie-Prioritaet ist ein Batterieentlade- oder gemeinsamer Batteriesensor
  Pflicht; ohne dieses Signal blockiert OpenPool PV-Heizen fail-safe.
- Pumpen- und Heizungssensoren fuer Leistung, Strom, Spannung, Signal und
  Temperaturen

`Heizung Ein` und `Nachtbaden` sind bewusste manuelle Overrides. Sie umgehen die
PV-/Batterieautomatik, brauchen aber weiterhin Pumpenflow und Hauptfreigabe.

Wenn diese Entitaeten nicht passen, kann OpenPool starten, aber keine sauberen
Entscheidungen treffen oder Befehle an die richtigen Geraete senden.

## Installation

1. In Home Assistant **Einstellungen -> Add-ons -> Add-on Store** oeffnen.
2. Unter **Repositories** dieses Repository hinzufuegen:
   `https://github.com/cococheaf/ha-openpool`
3. Store neu laden und **OpenPool** installieren.
4. Add-on-Konfiguration anpassen, insbesondere alle Entitaeten.
5. Add-on starten und **In Seitenleiste anzeigen** aktivieren.

## Dokumentation

- Add-on-Dokumentation: [openpool/DOCS.md](openpool/DOCS.md)
- Changelog: [openpool/CHANGELOG.md](openpool/CHANGELOG.md)
- Home Assistant Add-on: [openpool/](openpool/)

## Releases

Versionierte Releases entstehen ueber Git-Tags im Format `vX.Y.Z`. Beim Push
eines Tags erstellt GitHub Actions automatisch einen GitHub Release aus dem
passenden Abschnitt in `openpool/CHANGELOG.md`.
