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

## Lizenz

Der Quellcode der Webseite ist unter der [MIT-Lizenz](LICENSE) lizenziert.