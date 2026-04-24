# Förderverein Gleisbergschule

Dies ist das GitHub Repository des Fördervereins der Gleisbergschule Mainz-Gonsenheim.

## Website

Der Quellcode der Website befindet sich in dem Ordner `website`. Pull requests mit Verbesserungen oder Aktualisierungen der Webseite sind willkommen! ❤️

### Technische Basis

Die Webseite ist als statische Webseite implementiert und nutzt HTML, CSS und minimales JavaScript (für Header/Footer-Includes).

Zentrale KI-Prompts zur Erstellung der Webseite und für inhaltliche oder technische Updates finden sich im Ordner [ki-prompts](ki-prompts).

### Technische Details

#### CSS und JavaScript Versionierung

Die Dateien `style.css` und `includes.js` werden mit einem Datums-Suffix versioniert (z.B. `style_2026-02-24.css`, `includes_2026-02-24.js`). Bei Änderungen an diesen Dateien wird die Datei per `git mv` umbenannt und das aktuelle Datum angehängt. Die Referenzen in allen HTML-Dateien (inkl. `news/`) müssen dann ebenfalls angepasst werden.

## Poster (DIN A1, Querformat)

Im Ordner [`poster`](poster) liegt ein Python-Skript, das aus den Webinhalten ein druckfertiges A1-Poster (z.B. für Schulfeste oder Infostände) als PDF erzeugt. Inhalte, Bilder und Farben werden direkt aus dem `website`-Ordner übernommen, der QR-Code verweist auf die Webseite.

### Voraussetzungen

Das Skript nutzt [WeasyPrint](https://weasyprint.org/). Unter Debian/Ubuntu werden einmalig folgende System-Bibliotheken benötigt:

```bash
sudo apt-get install -y python3-venv \
    libpango-1.0-0 libpangocairo-1.0-0 libgdk-pixbuf2.0-0 \
    libffi-dev libcairo2
```

### Python-Umgebung einrichten

Virtuelles Environment im Projekt-Root anlegen und Abhängigkeiten installieren:

```bash
python3 -m venv poster-venv
source poster-venv/bin/activate
pip install -r poster/requirements.txt
```

### Poster erzeugen

```bash
source poster-venv/bin/activate
cd poster
python generate_poster.py
```

Ergebnis: `poster/poster_foerderverein_a1.pdf`.

Inhaltliche Anpassungen (Texte, Bilder, URL, Farben) werden direkt in `poster/generate_poster.py` vorgenommen.

## Lizenz

Der Quellcode der Webseite ist unter der [MIT-Lizenz](LICENSE) lizenziert.