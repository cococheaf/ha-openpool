# OpenPool – Projektkontext

## Ziel

OpenPool soll eine eigene Web-App ähnlich EVCC werden, um ein Intex 26680 Poolsystem, eine Poolwärmepumpe und PV-Überschusslogik über Home Assistant zu steuern.

Home Assistant liefert Sensoren und führt Schaltbefehle aus. OpenPool enthält die eigentliche Logik, Konfiguration und Bedienoberfläche.

## Aktueller Stand

Es gibt einen Single-File-Prototypen in `index.html`.

Der Prototyp enthält:

- EVCC-ähnliches dunkles Dashboard
- Hauptfreigabe für das gesamte Poolsystem
- Pumpenmodi
- Heizungsmodi
- Wetterprognose auf Tagesbasis
- Konfigurationsseite
- Demo-State per JavaScript
- Home-Assistant-Add-on-Hülle unter `openpool/`
- noch keine vollständige persistente Backend-Steuerlogik

## Hardware / Pooldaten

Pool:
- ca. 19 m³
- Salzwasser
- Salzgehalt ca. 2800 ppm
- pH ca. 7,2
- CYA ca. 11 ppm

Pumpe / Chlorinator:
- Gerät: Intex 26680
- Pumpe und Chlorinator sind ein zusammenhängendes Gerät
- Home Assistant Entity: `switch.poolpumpe`
- Pumpenleistung ca. 8 m³/h
- ca. 450 W nur Pumpe
- ca. 550 W bei aktivem Chlorinator
- Chlorinator ca. 11 g/h
- Gerät geht nach 12 h in Ruhezustand, daher sind Restart-Pulse nötig

Poolheizung:
- Home Assistant Entity: `climate.poolheizung`
- Tuya Local
- benötigt Pumpenflow
- darf nie ohne Pumpe laufen
- beim Ausschalten der Pumpe muss zuerst die Heizung aus, dann ca. 5 Minuten Pumpennachlauf, danach Pumpe aus
- bei kurzer Pumpenunterbrechung für Chlorinator-Restart max. 5–6 Sekunden, damit die Wärmepumpe nicht in Safemode geht

PV / Energie:
- Gesamtes Poolsystem unter Vollast ca. 2000 W
- Haus-Eigenverbrauch ohne Poolsystem soll angezeigt werden
- PV-Automatik soll mit Antipendelzeit arbeiten
- Wärmepumpe braucht ca. 15 Minuten zum Wiederanfahren nach Abschaltung

Home Assistant Sensoren:
- `sensor.solaredge_modbuszahler_ac_power`
- `sensor.solaredge_wechselrichter_ac_power`
- `sensor.energy_grid_stromzahler_active_power_plus_stromzahler_active_power_minus_net_power`
- `sensor.stromzahler_active_power_minus` Export
- `sensor.stromzahler_active_power_plus` Import
- `weather.openweathermap`

## Hauptlogik

### Hauptfreigabe

Wenn Hauptfreigabe AUS:
- Pumpe aus
- Chlorinator aus
- Heizung aus
- Pumpenmodus ausgegraut
- Heizungsmodus ausgegraut
- alle laufenden Nachlauf-/Override-Timer abbrechen

Wenn Hauptfreigabe EIN:
- Pumpenmodus und je nach Pumpenstatus Heizungsmodus freigeben

## Pumpenmodi

### Aus

- Heizungsmodus wird ausgegraut
- Beim Umschalten auf Aus:
  1. Heizung ausschalten
  2. ca. 5 Minuten Pumpennachlauf
  3. Pumpe ausschalten
- Wenn während der Nachlaufzeit ein neuer Pumpenmodus gewählt wird, muss die Nachlaufsequenz sofort abgebrochen werden und der neue Modus aktiv werden

### Dauerbetrieb

- Pumpe läuft dauerhaft
- alle 12 Stunden kurzer Restart-Pulse, damit das Intex-System nicht in Ruhezustand geht

### Badebetrieb

Zeitplan:
- 07:30 EIN
- 11:59:55 kurzer Restart-Pulse
- 12:00 EIN
- 16:59:55 kurzer Restart-Pulse
- 17:00 EIN
- 22:00 Abschaltsequenz

Ziel:
- hoher Badebetrieb
- ausreichende Chlorproduktion

### Schlechtwetter

Zeitplan:
- 13:00 EIN
- 16:15 AUS

Bedeutung:
- reduzierte Chlorung, nicht primär reduzierte Filterung
- für Regen, wenig UV, wenig/kein Badebetrieb

### Nachtbaden

Eigener Pumpenmodus, nicht nur Aktionsbutton.

- Pumpe EIN
- Heizung EIN
- PV-Leistungszustand ignorieren
- maximal 10 Stunden
- danach Rückkehr in vorherigen/konfigurierten Modus oder sichere Abschaltung
- soll als große Modus-Karte wie Badebetrieb/Schlechtwetter dargestellt werden

## Heizungsmodi

Heizungsmodus muss gesperrt sein, wenn:
- Hauptfreigabe AUS
- Pumpenmodus AUS
- reale Pumpe aus und kein erlaubter Restart-Pulse läuft

### Aus
Heizung bleibt aus.

### Ein
Heizung manuell ein, aber nur wenn Pumpe läuft.

### PV-Automatik
Heizung nach PV-Überschuss mit Antipendelung.

Startidee:
- Start bei stabilem PV-Überschuss
- Stop bei stabilem Netzbezug oder zu wenig Überschuss
- Mindestlaufzeit ca. 30 Minuten
- Sperrzeit nach Abschaltung ca. 20 Minuten

### Wetterautomatik
Soll Wetter, Temperatur, Regenrisiko und PV berücksichtigen.

## Wetterprognose

Die UI soll Tagesbasis zeigen, nicht Stundenbasis.

Anzeige:
- Heute
- Morgen
- Übermorgen

Pro Tag:
- Icon
- Temperatur
- Regenwahrscheinlichkeit
- Empfehlung:
  - Badebetrieb
  - Schlechtwetter

Die Wetterprognose ist primär Entscheidungshilfe für den Nutzer, keine überladene Detailansicht.

## Aktueller UI-Stand

Dashboard enthält:
- Header mit OpenPool-Logo und Untertitel
- Verbindung zu Home Assistant
- Tabs: Dashboard / Info / Konfiguration
- Hauptstatuskarte
- kompakte Entscheidungsbox
- Wetterprognose auf Tagesbasis
- Pumpenmodus-Karten:
  - Aus
  - Dauerbetrieb
  - Badebetrieb
  - Schlechtwetter
  - Nachtbaden
  - Chlorsystem neu starten
- Heizungsmodus-Karten:
  - Aus
  - Ein
  - PV-Automatik
  - Wetterautomatik
- PV-Freigabe:
  - PV frei für WP
  - Bereit ab

Konfiguration enthält:
- Home Assistant URL
- Long-Lived Access Token
- Entity IDs
- Pumpenprofile
- PV-Heizungsautomatik
- Wetterparameter
- Prognosetage

## Aktuelle Designrichtung

- EVCC-ähnlich
- dunkles modernes UI
- Kartenlayout
- große Modusbuttons
- kompakte Info-/Entscheidungsbox
- Animationen für:
  - Energiefluss
  - Abschaltsequenz
  - Nachlauf
  - Statusänderungen

## Nächster sinnvoller Schritt

Den Single-File-Prototypen in eine echte Vite/React/TypeScript-App portieren.

Wichtig:
- Design möglichst exakt beibehalten
- Komponenten sauber trennen
- Demo-State zunächst lokal halten
- noch keine echte Home-Assistant-API anbinden
- danach Backend und Regel-Engine planen

## Gewünschte Zielstruktur

Vorschlag:

```text
poolcontrol/
├─ frontend/
│  ├─ src/
│  │  ├─ components/
│  │  │  ├─ Header.tsx
│  │  │  ├─ HeroStatus.tsx
│  │  │  ├─ DecisionCard.tsx
│  │  │  ├─ WeatherForecast.tsx
│  │  │  ├─ PumpModeCard.tsx
│  │  │  ├─ HeaterModeCard.tsx
│  │  │  ├─ EnergyFlow.tsx
│  │  │  └─ SettingsPanel.tsx
│  │  ├─ state/
│  │  │  └─ poolState.ts
│  │  ├─ App.tsx
│  │  └─ main.tsx
│  └─ package.json
├─ backend/
│  ├─ src/
│  │  ├─ haClient.ts
│  │  ├─ scheduler.ts
│  │  ├─ ruleEngine.ts
│  │  └─ config.ts
│  └─ package.json
├─ config/
│  └─ config.yaml
├─ docs/
│  └─ PROJECT_CONTEXT.md
├─ docker-compose.yml
└─ README.md
