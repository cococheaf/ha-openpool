# OpenPool

[English version](README.en.md)

OpenPool ist ein Home-Assistant-Add-on fuer eine kompakte Poolsteuerung rund um
Pumpe, Chlorsystem, Waermepumpe, Wetterprofil und PV-Ueberschuss. Das System ist
aktuell fuer Setups mit dem Intex 26680 Sandfilter-/Salzwasserelektrolyse-System
ausgelegt.

## Funktionen

- Pumpenprofile: Aus, Dauerbetrieb, Badebetrieb, Schlechtwetter und Nachtbaden.
- Restart-Pulse fuer das Chlorsystem mit einstellbarer Pulse-Dauer.
- Waermepumpensteuerung mit Zieltemperatur, Start-Betriebsmodus aus einem
  Home-Assistant-Auswahlfeld, Nachlauf und optionaler PV-Automatik.
- PV-Freigabe mit optionaler Batterie-Prioritaet.
- Abschaltbare Batterielogik fuer Anlagen ohne Batteriespeicher.
- Wettersteuerung als Empfehlung oder Automatik.
- Live-Sync zwischen mehreren Browsern und persistenter Zustand unter
  `/data/openpool_state.json`.

## Vor dem ersten Start

Passe in der Add-on-Konfiguration alle Entitaeten an deine Home-Assistant-Anlage
an. Besonders wichtig sind:

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
  `energy.prefer_battery_charging` schuetzt die Batterieladung vor der
  Waermepumpenfreigabe. Wenn die Batterie nicht laedt und trotzdem
  PV-Ueberschuss bleibt, behandelt OpenPool sie als voll. Bei aktiver
  Batterie-Prioritaet ist ein Batterieentlade- oder gemeinsamer Batteriesensor
  Pflicht; ohne dieses Signal blockiert OpenPool PV-Heizen fail-safe.
- Pumpen- und Heizungssensoren

`Heizung Ein` und `Nachtbaden` sind bewusste manuelle Overrides. Sie umgehen die
PV-/Batterieautomatik, brauchen aber weiterhin Pumpenflow und Hauptfreigabe.

Falsche Entitaeten koennen dazu fuehren, dass OpenPool keine sauberen
Entscheidungen trifft oder Befehle an das falsche Geraet sendet.

## Installation

1. Add-on installieren.
2. Add-on-Konfiguration pruefen und Entitaeten anpassen.
3. Add-on starten.
4. **In Seitenleiste anzeigen** aktivieren.

Technische Details stehen in [DOCS.md](DOCS.md).
