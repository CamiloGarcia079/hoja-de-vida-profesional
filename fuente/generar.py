"""Genera las hojas de vida en PDF: formato Campus y formato ATS, en español e inglés.

Uso (desde la carpeta fuente/):
    python3 generar.py

Escribe un HTML por versión en salida/ y luego usa Chromium (Playwright, con node) para
imprimir cada HTML como PDF tamaño A4 en la carpeta raíz del repositorio.
"""
import os
import subprocess
from html import escape as e
from datos import DATOS, CONTACTO

AQUI = os.path.dirname(os.path.abspath(__file__))
SALIDA = os.path.join(AQUI, 'salida')
RAIZ = os.path.dirname(AQUI)
os.makedirs(SALIDA, exist_ok=True)

NAVY = '#14234f'


def contacto_items(d):
    etq = d['etq']
    return [(etq['telefono'], CONTACTO['telefono']), (etq['correo'], CONTACTO['correo']),
            (etq['linkedin'], CONTACTO['linkedin']), (etq['github'], CONTACTO['github']),
            (etq['portafolio'], CONTACTO['portafolio']), (etq['ciudad'], d['ciudad'])]


# ------------------------------------------------------------------ formato Campus
def campus(lang):
    d = DATOS[lang]
    s = d['secciones']
    exp = ''.join(f'''
      <div class="item">
        <div class="fila"><h4>{e(t)}</h4><span class="fecha">{e(f)}</span></div>
        <p class="sub">{e(sub)}</p>
        {''.join(f'<p class="txt">{e(x)}</p>' for x in pts)}
      </div>''' for t, sub, f, pts in d['experiencia'])
    form = ''.join(f'''
      <div class="item"><div class="fila"><h4>{e(t)}</h4><span class="fecha">{e(f)}</span></div><p class="sub">{e(sub)}</p></div>'''
                   for t, sub, f in d['formacion'])
    logros = ''.join(f'''
      <div class="item"><div class="fila"><h4>{e(t)}</h4><span class="fecha">{e(f)}</span></div>
        <p class="sub">{e(sub)}</p><p class="txt">{e(x)}</p></div>''' for t, sub, f, x in d['logros'][:1])
    return f'''<!doctype html><html lang="{lang}"><head><meta charset="utf-8"><style>
@page {{ size: A4; margin: 0; }}
* {{ box-sizing: border-box; margin: 0; padding: 0; }}
body {{ width: 210mm; height: 297mm; font-family: 'Inter', 'Liberation Sans', sans-serif; color: #1d2433; font-size: 8.4pt; line-height: 1.38; position: relative; }}
header {{ display: grid; grid-template-columns: 52mm 1fr; height: 46mm; background: {NAVY}; color: #fff; }}
.foto {{ background: url(foto.jpg) center 30% / cover; clip-path: polygon(0 0, 100% 0, 82% 100%, 0 100%); }}
.cab {{ display: grid; grid-template-rows: 1fr auto; }}
.cab h1 {{ align-self: center; text-align: center; font: 700 25pt/1.1 'Liberation Serif', serif; }}
.cab p {{ border-top: 1px solid rgba(255,255,255,.35); text-align: center; padding: 2.6mm 0 3mm; font: 400 10.5pt 'Liberation Serif', serif; letter-spacing: .04em; }}
main {{ display: grid; grid-template-columns: 1fr 62mm; gap: 0 9mm; padding: 6mm 11mm 0; }}
.der {{ border-left: 1px solid #d5d9e2; padding-left: 7mm; }}
h3 {{ font: 700 11pt 'Liberation Serif', serif; letter-spacing: .28em; text-transform: uppercase; color: #121a2c; margin: 0 0 2.6mm; }}
section {{ padding-bottom: 3mm; margin-bottom: 3mm; border-bottom: 1px solid #d5d9e2; }}
section:last-child {{ border-bottom: 0; }}
.item {{ margin-bottom: 2.6mm; }}
.fila {{ display: flex; justify-content: space-between; gap: 3mm; align-items: baseline; }}
h4 {{ font-size: 9.2pt; font-weight: 700; color: #121a2c; }}
.fecha {{ font-size: 7.6pt; color: #8a91a0; white-space: nowrap; }}
.sub {{ font-size: 7.4pt; color: #8a91a0; margin-bottom: .6mm; }}
.txt {{ text-align: justify; }}
.perfil {{ text-align: justify; }}
ul {{ list-style: none; }}
.lista li {{ position: relative; padding-left: 4.5mm; margin-bottom: 1.2mm; }}
.lista li::before {{ content: ''; position: absolute; left: 0; top: 1.5mm; width: 2mm; height: 2mm; border-radius: 50%; background: {NAVY}; }}
.dos {{ display: grid; grid-template-columns: 1fr 1fr; gap: 0 3mm; font-size: 8pt; }}
.contacto li {{ margin-bottom: 1.6mm; }}
.contacto b {{ display: block; font-size: 7pt; letter-spacing: .08em; text-transform: uppercase; color: #8a91a0; font-weight: 600; }}
.contacto span {{ font-size: 7.6pt; white-space: nowrap; }}
footer {{ position: absolute; left: 0; right: 0; bottom: 0; height: 17mm; background: {NAVY}; display: flex; justify-content: flex-end; align-items: center; padding-right: 9mm; }}
footer img {{ height: 13mm; }}
</style></head><body>
<header>
  <div class="foto"></div>
  <div class="cab"><h1>{e(d['nombre'][0])}<br>{e(d['nombre'][1])}</h1><p>{e(d['titulo_corto'])}</p></div>
</header>
<main>
  <div>
    <section><h3>{e(s['perfil'])}</h3><p class="perfil">{e(d['perfil'])}</p></section>
    <section><h3>{e(s['formacion'])}</h3>{form}</section>
    <section><h3>{e(s['experiencia'])}</h3>{exp}</section>
    <section><h3>{e(s['logros'])}</h3>{logros}</section>
  </div>
  <div class="der">
    <section><h3>{e(s['habilidades'])}</h3><ul class="lista">{''.join(f'<li>{e(h)}</li>' for h in d['habilidades'])}</ul></section>
    <section><h3>{e(s['competencias'])}</h3><ul class="lista">{''.join(f'<li>{e(c)}</li>' for c in d['competencias'])}</ul></section>
    <section><h3>{e(s['contacto'])}</h3><ul class="contacto">{''.join(f'<li><b>{e(k)}</b><span>{e(v)}</span></li>' for k, v in contacto_items(d))}</ul></section>
    <section><h3>{e(s['idiomas'])}</h3><ul class="lista">{''.join(f'<li>{e(a)} – {e(b)}</li>' for a, b in d['idiomas'])}</ul></section>
  </div>
</main>
<footer><img src="campuslands.png" alt="CampusLands"></footer>
</body></html>'''


# ------------------------------------------------------------------ formato ATS
def ats(lang):
    """Una sola columna, texto plano, sin imágenes ni tablas: lo que leen bien los sistemas ATS."""
    d = DATOS[lang]
    s = d['secciones']
    contacto = ' | '.join(v for _, v in contacto_items(d))
    # Palabras clave sueltas y sin repetir: así las encuentran los filtros ATS
    claves = []
    for h in d['habilidades']:
        for k in h.split(' · '):
            if k not in claves and k not in ('automatización', 'automation'):
                claves.append(k)
    exp = ''.join(f'''
    <div class="item"><p><b>{e(t)}</b> — {e(f)}</p><p class="sub">{e(sub)}</p>
      <ul>{''.join(f'<li>{e(x)}</li>' for x in pts)}</ul></div>''' for t, sub, f, pts in d['experiencia'])
    form = ''.join(f'<div class="item"><p><b>{e(t)}</b> — {e(f)}</p><p class="sub">{e(sub)}</p></div>' for t, sub, f in d['formacion'])
    logros = ''.join(f'<div class="item"><p><b>{e(t)}</b> — {e(f)}</p><p class="sub">{e(sub)}</p><ul><li>{e(x)}</li></ul></div>'
                     for t, sub, f, x in d['logros'])
    return f'''<!doctype html><html lang="{lang}"><head><meta charset="utf-8"><style>
@page {{ size: A4; margin: 16mm 17mm; }}
* {{ margin: 0; padding: 0; }}
body {{ font-family: 'Liberation Sans', Arial, sans-serif; color: #000; font-size: 10.2pt; line-height: 1.4; }}
h1 {{ font-size: 19pt; }}
.cargo {{ font-size: 11pt; margin: 1mm 0; }}
.contacto {{ font-size: 9.4pt; margin-bottom: 4mm; }}
h2 {{ break-after: avoid; font-size: 11pt; text-transform: uppercase; border-bottom: 1px solid #000; margin: 4.5mm 0 2mm; padding-bottom: .8mm; }}
.item {{ margin-bottom: 2.4mm; break-inside: avoid; }}
.sub {{ font-style: italic; }}
ul {{ padding-left: 5mm; }}
</style></head><body>
<h1>{e(' '.join(d['nombre']))}</h1>
<p class="cargo">{e(d['titulo_corto'])} | {e(d['cargo'])}</p>
<p class="contacto">{e(contacto)}</p>
<h2>{e(s['perfil'])}</h2><p>{e(d['perfil'])}</p>
<h2>{e(s['habilidades'])}</h2><p>{e(', '.join(claves))}</p>
<h2>{e(s['experiencia'])}</h2>{exp}
<h2>{e(s['formacion'])}</h2>{form}
<h2>{e(s['logros'])}</h2>{logros}
<h2>{e(s['competencias'])}</h2><p>{e(', '.join(d['competencias']))}</p>
<h2>{e(s['idiomas'])}</h2><p>{e(', '.join(f'{a} ({b})' for a, b in d['idiomas']))}</p>
</body></html>'''


VERSIONES = {
    'HojaDeVida_Campus_ES_CamiloGarcia': campus('es'),
    'HojaDeVida_Campus_EN_CamiloGarcia': campus('en'),
    'HojaDeVida_ATS_ES_CamiloGarcia': ats('es'),
    'HojaDeVida_ATS_EN_CamiloGarcia': ats('en'),
}
for nombre, html in VERSIONES.items():
    with open(os.path.join(SALIDA, nombre + '.html'), 'w', encoding='utf-8') as f:
        f.write(html)

# Copia los recursos junto a los HTML para que las rutas relativas funcionen
for rec in ('foto.jpg', 'campuslands.png'):
    with open(os.path.join(AQUI, rec), 'rb') as src, open(os.path.join(SALIDA, rec), 'wb') as dst:
        dst.write(src.read())

subprocess.run(['node', os.path.join(AQUI, 'imprimir.js'), SALIDA, RAIZ, *VERSIONES.keys()], check=True)
