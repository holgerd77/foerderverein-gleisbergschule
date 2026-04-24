#!/usr/bin/env python3
"""
Poster-Generator für den Förderverein Gleisbergschule
DIN A1 Querformat (841mm x 594mm)

Verwendung:
    source ../poster-venv/bin/activate
    python generate_poster.py
"""

import base64
from io import BytesIO
from pathlib import Path

import qrcode
from weasyprint import HTML

# ---------------------------------------------------------------------------
# Konfiguration
# ---------------------------------------------------------------------------
WEBSITE_URL = "https://foerderverein-gleisbergschule.de"

BASE_DIR = Path(__file__).resolve().parent.parent
ASSETS_DIR = BASE_DIR / "website" / "assets"
OUTPUT_PDF = Path(__file__).resolve().parent / "poster_foerderverein_a1.pdf"
OUTPUT_HTML = Path(__file__).resolve().parent / "poster_foerderverein_a1.html"


def img_to_uri(path: Path) -> str:
    suffix = path.suffix.lower()
    mime = {".jpg": "image/jpeg", ".jpeg": "image/jpeg", ".png": "image/png"}.get(
        suffix, "image/png"
    )
    data = base64.b64encode(path.read_bytes()).decode()
    return f"data:{mime};base64,{data}"


def make_qr(url: str) -> str:
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=2,
    )
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="#2C4A7C", back_color="#FFFFFF")
    buf = BytesIO()
    img.save(buf, format="PNG")
    data = base64.b64encode(buf.getvalue()).decode()
    return f"data:image/png;base64,{data}"


# ---------------------------------------------------------------------------
# Bild-Assets laden
# ---------------------------------------------------------------------------
logo = img_to_uri(ASSETS_DIR / "Logo.jpg")
img_klassenzimmer = img_to_uri(ASSETS_DIR / "projekte" / "Gruenes_Klassenzimmer.png")
img_spielekiste = img_to_uri(ASSETS_DIR / "projekte" / "Spielekiste.png")
img_erdbeerfest = img_to_uri(ASSETS_DIR / "events" / "Erdbeerfest.png")
img_umzug = img_to_uri(
    ASSETS_DIR / "events" / "2026-02_Umzug_Gonsenheim_Umzug.jpeg"
)
qr_code = make_qr(WEBSITE_URL)

# ---------------------------------------------------------------------------
# HTML + CSS
# ---------------------------------------------------------------------------
html_content = f"""<!DOCTYPE html>
<html lang="de">
<head>
<meta charset="UTF-8">
<style>
@page {{
  size: 841mm 594mm;
  margin: 0;
}}

* {{ box-sizing: border-box; margin: 0; padding: 0; }}

body {{
  font-family: 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
  width: 841mm;
  height: 594mm;
  color: #333;
  background: #fff;
  overflow: hidden;
}}

/* ═══════════════════════════════════════════════════════════════
   HEADER  –  ~90mm
   ═══════════════════════════════════════════════════════════════ */
.header {{
  background: linear-gradient(135deg, #2C4A7C 0%, #3D5A8A 60%, #4A6A9A 100%);
  color: #fff;
  height: 90mm;
  padding: 10mm 35mm;
  display: flex;
  align-items: center;
  gap: 20mm;
  position: relative;
}}

.header::after {{
  content: '';
  position: absolute;
  bottom: 0; left: 0; right: 0;
  height: 4mm;
  background: linear-gradient(90deg, #E6A42C 0%, #F5C45A 50%, #E6A42C 100%);
}}

.logo-img {{
  height: 72mm;
  width: auto;
  background: #fff;
  padding: 3mm;
  border-radius: 5mm;
  flex-shrink: 0;
}}

.title-block h1 {{
  font-size: 62pt;
  font-weight: 700;
  letter-spacing: 0.5pt;
  margin-bottom: 4mm;
}}

.title-block .tagline {{
  font-size: 28pt;
  opacity: 0.92;
  font-weight: 300;
}}

/* ═══════════════════════════════════════════════════════════════
   MAIN  –  ~389mm   (zwei Spalten)
   ═══════════════════════════════════════════════════════════════ */
.main {{
  height: 389mm;
  padding: 16mm 35mm 12mm;
  display: flex;
  gap: 25mm;
}}

/* ── Über uns (links, ~300mm breit) ───────────────────────── */
.about {{
  width: 300mm;
  flex-shrink: 0;
  display: flex;
  flex-direction: column;
}}

.section-heading {{
  color: #2C4A7C;
  font-size: 44pt;
  font-weight: 700;
  margin-bottom: 10mm;
  padding-bottom: 4mm;
  border-bottom: 3mm solid #E6A42C;
  display: inline-block;
}}

.about-text {{
  font-size: 26pt;
  line-height: 1.45;
  margin-bottom: 14mm;
}}

.about-text p {{
  margin-bottom: 9mm;
}}

.about-text .highlight {{
  color: #E6A42C;
  font-weight: 700;
}}

.about-text strong {{
  color: #2C4A7C;
}}

.about-image-wrapper {{
  margin-top: auto;
  border-radius: 5mm;
  overflow: hidden;
  box-shadow: 0 2mm 8mm rgba(0,0,0,0.12);
}}

.about-image-wrapper img {{
  width: 100%;
  height: 145mm;
  object-fit: cover;
  display: block;
}}

.about-image-caption {{
  background: #4A5621;
  color: #fff;
  text-align: center;
  padding: 4mm;
  font-size: 18pt;
  font-weight: 600;
}}

/* ── Projekte (rechts, rest) ──────────────────────────────── */
.projects {{
  flex: 1;
  display: flex;
  flex-direction: column;
}}

.project-grid {{
  flex: 1;
  display: flex;
  flex-wrap: wrap;
  gap: 11mm;
}}

.project-card {{
  width: 140mm;
  height: 158mm;
  background: #F8F9FA;
  border-radius: 5mm;
  border-left: 3mm solid #4A5621;
  overflow: hidden;
  display: flex;
  flex-direction: column;
  word-wrap: break-word;
}}

.project-card img {{
  width: 100%;
  height: 90mm;
  object-fit: cover;
  display: block;
  flex-shrink: 0;
}}

.card-body {{
  padding: 8mm 10mm;
  flex: 1;
  display: flex;
  flex-direction: column;
  justify-content: center;
}}

.card-body h3 {{
  color: #2C4A7C;
  font-size: 26pt;
  margin-bottom: 5mm;
  line-height: 1.15;
}}

.card-body p {{
  font-size: 19pt;
  color: #444;
  line-height: 1.35;
}}

/* Karten ohne Bild: farbiger Akzent oben statt Icon */
.card-accent-bar {{
  height: 6mm;
  background: linear-gradient(90deg, #4A5621, #6B8A30);
  flex-shrink: 0;
}}

.project-card.text-only .card-body {{
  justify-content: center;
  padding: 10mm 11mm;
}}

.project-card.text-only h3 {{
  font-size: 30pt;
  margin-bottom: 6mm;
}}

.project-card.text-only p {{
  font-size: 21pt;
  line-height: 1.4;
}}

/* ═══════════════════════════════════════════════════════════════
   FOOTER  –  ~115mm
   ═══════════════════════════════════════════════════════════════ */
.footer {{
  height: 115mm;
  background: linear-gradient(135deg, #2C4A7C 0%, #3D5A8A 100%);
  color: #fff;
  padding: 14mm 35mm;
  display: flex;
  align-items: center;
  gap: 14mm;
  position: relative;
}}

.footer::before {{
  content: '';
  position: absolute;
  top: 0; left: 0; right: 0;
  height: 4mm;
  background: linear-gradient(90deg, #E6A42C 0%, #F5C45A 50%, #E6A42C 100%);
}}

.footer-col {{
  flex: 1;
  padding: 0 8mm;
}}

.footer-col h3 {{
  color: #E6A42C;
  font-size: 26pt;
  font-weight: 700;
  margin-bottom: 5mm;
}}

.footer-col p {{
  font-size: 17pt;
  line-height: 1.5;
}}

.footer-col .big-price {{
  font-size: 54pt;
  font-weight: 700;
  color: #E6A42C;
  line-height: 1.1;
}}

.footer-col .sub-note {{
  font-size: 16pt;
  opacity: 0.88;
  margin-top: 3mm;
  line-height: 1.4;
}}

.bank {{
  font-family: 'Courier New', Courier, monospace;
  font-size: 15pt;
  line-height: 1.6;
}}

.email-highlight {{
  color: #F5C45A;
  font-size: 20pt;
  font-weight: 600;
}}

.qr-col {{
  flex: 0 0 105mm;
  text-align: center;
}}

.qr-col img {{
  width: 85mm;
  height: 85mm;
  border-radius: 3mm;
  background: #fff;
  padding: 2mm;
}}

.qr-col .url {{
  font-size: 14pt;
  font-weight: 700;
  color: #F5C45A;
  margin-top: 4mm;
}}
</style>
</head>
<body>

<!-- ═══════ HEADER ═══════ -->
<div class="header">
  <img src="{logo}" alt="Logo" class="logo-img">
  <div class="title-block">
    <h1>Förderverein Gleisbergschule</h1>
    <div class="tagline">Gemeinsam für unsere Kinder an der Grundschule am Gleisberg</div>
  </div>
</div>

<!-- ═══════ MAIN ═══════ -->
<div class="main">

  <!-- Über uns -->
  <div class="about">
    <div class="section-heading">Über uns</div>
    <div class="about-text">
      <p>
        Der <strong>Verein der Freunde und Förderer
        der Gleisbergschule Gonsenheim e.V.</strong> besteht aus
        rund <span class="highlight">150 Mitgliedern</span>: Eltern,
        Lehrkräfte, Ehemalige sowie Freunde und Förderer
        unserer Schule.
      </p>
      <p>
        Mit Mitgliedsbeiträgen, Spenden und Erlösen aus
        Veranstaltungen ergänzen wir – gemeinsam mit dem
        Schulelternbeirat (SEB) – die Ausstattung der Schule dort,
        wo der Schulträger keine Mittel bereitstellen kann.
      </p>
      <p>
        Zuletzt konnten wir dank Ihrer Unterstützung das
        <strong>Grüne Klassenzimmer</strong> auf dem Schulhof
        errichten. <span class="highlight">Machen Sie mit!</span>
      </p>
    </div>
    <div class="about-image-wrapper">
      <img src="{img_umzug}" alt="Gleisbergschüler:innen beim Fastnachtsumzug">
      <div class="about-image-caption">Fastnachtsumzug Gonsenheim 2026</div>
    </div>
  </div>

  <!-- Projekte -->
  <div class="projects">
    <div class="section-heading">Unsere Projekte</div>
    <div class="project-grid">

      <article class="project-card">
        <img src="{img_klassenzimmer}" alt="Grünes Klassenzimmer">
        <div class="card-body">
          <h3>Grünes Klassenzimmer</h3>
          <p>Unterricht im Freien – mit Sitzgelegenheiten und Tafel auf dem Schulhof. Errichtet 2024.</p>
        </div>
      </article>

      <article class="project-card">
        <img src="{img_spielekiste}" alt="Spielekiste">
        <div class="card-body">
          <h3>Spielekisten</h3>
          <p>Jede erste Klasse erhält eine Kiste mit Bällen, Seilen &amp; mehr für bewegte Pausen.</p>
        </div>
      </article>

      <article class="project-card">
        <img src="{img_erdbeerfest}" alt="Erdbeerfest">
        <div class="card-body">
          <h3>Feste &amp; Events</h3>
          <p>Adventsbasar, Erdbeerfest &amp; Sommerfest – gemeinsam mit dem SEB.</p>
        </div>
      </article>

      <article class="project-card text-only">
        <div class="card-accent-bar"></div>
        <div class="card-body">
          <h3>Selbst&shy;behauptung</h3>
          <p>Kurse für alle Klassenstufen – für mehr Selbstbewusstsein und innere Stärke der Kinder.</p>
        </div>
      </article>

      <article class="project-card text-only">
        <div class="card-accent-bar"></div>
        <div class="card-body">
          <h3>Sichere Schulwege</h3>
          <p>Warnwesten für Erstklässler und Preise bei der Laufpunkteaktion.</p>
        </div>
      </article>

      <article class="project-card text-only">
        <div class="card-accent-bar"></div>
        <div class="card-body">
          <h3>Sozialfonds</h3>
          <p>Unterstützung für Klassenfahrten &amp; Co. – damit alle Kinder mitmachen.</p>
        </div>
      </article>

    </div>
  </div>

</div>

<!-- ═══════ FOOTER ═══════ -->
<div class="footer">

  <div class="footer-col">
    <h3>Mitglied werden!</h3>
    <div class="big-price">12 &euro;</div>
    <div class="sub-note">Mindestbeitrag / Jahr<br>Steuerlich absetzbar!</div>
  </div>

  <div class="footer-col">
    <h3>Spendenkonto</h3>
    <p class="bank">
      VR-Bank Mainz<br>
      IBAN:<br>
      DE74 5509 1200 0083 7002 03
    </p>
  </div>

  <div class="footer-col">
    <h3>Kontakt</h3>
    <p class="email-highlight">fv-gleisbergschule@web.de</p>
    <p class="sub-note" style="margin-top: 4mm;">
      Gleisbergweg 50, 55122 Mainz
    </p>
  </div>

  <div class="qr-col">
    <img src="{qr_code}" alt="QR-Code">
    <div class="url">foerderverein-gleisbergschule.de</div>
  </div>

</div>

</body>
</html>"""

# ---------------------------------------------------------------------------
# HTML speichern (zum Debuggen) + PDF rendern
# ---------------------------------------------------------------------------
OUTPUT_HTML.write_text(html_content, encoding="utf-8")
print(f"HTML gespeichert: {OUTPUT_HTML}")

html_doc = HTML(string=html_content, base_url=str(BASE_DIR))
html_doc.write_pdf(str(OUTPUT_PDF))
print(f"PDF erstellt:     {OUTPUT_PDF}")
