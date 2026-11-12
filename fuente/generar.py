"""Genera las hojas de vida en PDF a partir de datos.py:
  - Formato Campus en español e inglés (misma estructura de la hoja Campus original).
  - Formato ATS en español (una columna, solo texto, enlaces completos).

Uso (desde la carpeta fuente/):
    python3 generar.py
Los PDF quedan en la raíz del repositorio, con enlaces que se pueden hacer clic.
"""
import os
import subprocess
from html import escape as e
from datos import ENLACES, TELEFONO, CORREO, CIUDAD, REPOS, CAMPUS, ATS

AQUI = os.path.dirname(os.path.abspath(__file__))
SALIDA = os.path.join(AQUI, 'salida')
RAIZ = os.path.dirname(AQUI)
os.makedirs(SALIDA, exist_ok=True)

NAVY = '#16295a'

ICONOS = {  # trazos de 24x24 para "Datos personales"
    'linkedin': '<path d="M6.5 9.5v8M6.5 6.5v.01M10.5 17.5v-4.5a2.5 2.5 0 0 1 5 0v4.5M10.5 9.5v8" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>',
    'github': '<path d="M12 3.5a8.5 8.5 0 0 0-2.7 16.6c.4 0 .6-.2.6-.4v-1.6c-2.4.5-2.9-1-2.9-1-.4-1-1-1.3-1-1.3-.8-.5 0-.5 0-.5.9.1 1.4.9 1.4.9.8 1.3 2 1 2.5.7.1-.6.3-1 .6-1.2-1.9-.2-3.9-1-3.9-4.2 0-.9.3-1.7.9-2.3-.1-.2-.4-1.1.1-2.2 0 0 .7-.2 2.3.9a8 8 0 0 1 4.2 0c1.6-1.1 2.3-.9 2.3-.9.5 1.1.2 2 .1 2.2.6.6.9 1.4.9 2.3 0 3.2-2 4-3.9 4.2.3.3.6.8.6 1.6v2.4c0 .2.2.5.6.4A8.5 8.5 0 0 0 12 3.5z" fill="currentColor"/>',
    'portafolio': '<circle cx="12" cy="12" r="8" fill="none" stroke="currentColor" stroke-width="1.8"/><path d="M4 12h16M12 4c2.2 2.3 3.2 5 3.2 8s-1 5.7-3.2 8c-2.2-2.3-3.2-5-3.2-8s1-5.7 3.2-8z" fill="none" stroke="currentColor" stroke-width="1.6"/>',
}


# ------------------------------------------------------------------ formato Campus
def campus(lang):
    d = CAMPUS[lang]
    perfil, formacion, experiencia, habilidades, competencias, datos, idiomas = d['secciones']
    form = ''.join(f'''
        <div class="item"><h4>{e(t)}</h4><div class="meta"><span>{e(lugar)}</span><span>{e(fecha)}</span></div></div>'''
                   for t, lugar, fecha in d['formacion'])
    exp = ''.join(f'''
        <div class="item"><h4><a href="{REPOS[k]}">{e(t)}</a></h4><p class="tec">{e(tec)}</p><p class="txt">{e(txt)}</p></div>'''
                  for k, t, tec, txt in d['experiencia'])
    contacto = ''.join(f'''
        <li><a href="{ENLACES[k]}"><span class="ico"><svg viewBox="0 0 24 24">{ICONOS[k]}</svg></span>{e(n)}</a></li>'''
                       for k, n in d['datos'])
    return f'''<!doctype html><html lang="{lang}"><head><meta charset="utf-8"><title>Camilo Andrés García Almeida</title><style>
@page {{ size: A4; margin: 0; }}
* {{ box-sizing: border-box; margin: 0; padding: 0; }}
body {{ width: 210mm; height: 297mm; position: relative; font-family: 'Liberation Sans', Arial, sans-serif; color: #222; font-size: 8.6pt; }}
a {{ color: inherit; text-decoration: none; }}
header {{ display: grid; grid-template-columns: 52mm 1fr; height: 46mm; }}
.foto {{ position: relative; background: url(foto.jpg) center 28% / cover; }}
.foto::after {{ content: ''; position: absolute; right: 0; top: 0; bottom: 0; width: 9mm; background: {NAVY}; clip-path: polygon(100% 0, 100% 100%, 0 100%); }}
.cab {{ background: {NAVY}; color: #fff; display: grid; grid-template-rows: 1fr 11mm; }}
.cab h1 {{ align-self: center; text-align: center; font: 700 24pt/1.12 'Liberation Serif', serif; }}
.cab p {{ border-top: 1px solid rgba(255,255,255,.4); display: grid; place-items: center; font: 400 12pt 'Liberation Serif', serif; letter-spacing: .06em; }}
main {{ display: grid; grid-template-columns: 1fr 1px 70mm; gap: 0 9mm; padding: 9mm 10mm 0 10mm; height: calc(297mm - 46mm - 17mm); }}
.sep {{ background: #d9dbe0; margin-top: -9mm; }}
h3 {{ font: 700 13.5pt 'Liberation Serif', serif; letter-spacing: .3em; text-transform: uppercase; color: #111; margin-bottom: 3.6mm; line-height: 1.15; }}
section {{ padding-bottom: 4.6mm; margin-bottom: 5mm; border-bottom: 1px solid #d9dbe0; }}
section:last-child {{ border-bottom: 0; }}
.perfil {{ text-align: justify; line-height: 1.5; }}
.item {{ margin-bottom: 3mm; }}
.item:last-child {{ margin-bottom: 0; }}
h4 {{ font-size: 10.6pt; font-weight: 700; color: #1a1a1a; line-height: 1.25; }}
.meta {{ display: flex; justify-content: space-between; gap: 4mm; color: #8d929b; font-size: 8.2pt; margin-top: .4mm; }}
.meta span:last-child {{ white-space: nowrap; }}
.tec {{ color: #8d929b; font-size: 8pt; margin: .4mm 0 .8mm; }}
.txt {{ text-align: justify; line-height: 1.45; }}
ul {{ list-style: none; }}
.puntos li {{ position: relative; padding-left: 6mm; font-size: 9.8pt; line-height: 1.9; }}
.puntos li::before {{ content: ''; position: absolute; left: 0; top: 2.5mm; width: 2.4mm; height: 2.4mm; border-radius: 50%; background: {NAVY}; }}
.dos {{ display: grid; grid-template-columns: 1fr 1fr; gap: 0 3mm; }}
.dos li {{ font-size: 8.4pt; line-height: 1.5; padding-left: 4.6mm; margin-bottom: 1.4mm; }}
.dos li::before {{ top: 1.4mm; width: 1.8mm; height: 1.8mm; }}
.contacto li {{ margin-bottom: 2.6mm; font-size: 9.8pt; }}
.contacto a {{ display: flex; align-items: center; gap: 3mm; }}
.ico {{ width: 6mm; height: 6mm; border: 1.3px solid {NAVY}; border-radius: 1.4mm; display: grid; place-items: center; color: #111; }}
.ico svg {{ width: 4.2mm; height: 4.2mm; }}
footer {{ position: absolute; left: 0; right: 0; bottom: 0; height: 17mm; background: {NAVY}; display: flex; justify-content: flex-end; align-items: center; padding-right: 7mm; }}
footer img {{ height: 11.5mm; }}
</style></head><body>
<header>
  <div class="foto"></div>
  <div class="cab"><h1>Camilo Andrés<br>García Almeida</h1><p>{e(d['rol'])}</p></div>
</header>
<main>
  <div>
    <section><h3>{e(perfil)}</h3><p class="perfil">{e(d['perfil'])}</p></section>
    <section><h3>{e(formacion)}</h3>{form}</section>
    <section><h3>{e(experiencia)}</h3>{exp}</section>
  </div>
  <div class="sep"></div>
  <div>
    <section><h3>{e(habilidades)}</h3><ul class="puntos">{''.join(f'<li>{e(h)}</li>' for h in d['habilidades'])}</ul></section>
    <section><h3>{e(competencias)}</h3><ul class="puntos dos">{''.join(f'<li>{e(c)}</li>' for c in d['competencias'])}</ul></section>
    <section><h3>{e(datos)}</h3><ul class="contacto">{contacto}</ul></section>
    <section><h3>{e(idiomas)}</h3><ul class="puntos">{''.join(f'<li>{e(i)}</li>' for i in d['idiomas'])}</ul></section>
  </div>
</main>
<footer><img src="campuslands_horizontal.png" alt="Campuslands"></footer>
</body></html>'''


# ------------------------------------------------------------------ formato ATS (español)
def ats():
    a = ATS
    url = lambda u: f'<a href="{u}">{e(u)}</a>'
    contacto = (f'Correo: <a href="mailto:{CORREO}">{CORREO}</a> | Teléfono: {e(TELEFONO)} | {e(CIUDAD)}<br>'
                f'LinkedIn: {url(ENLACES["linkedin"])}<br>'
                f'GitHub: {url(ENLACES["github"])}<br>'
                f'Portafolio: {url(ENLACES["portafolio"])}')
    hab = ''.join(f'<li><b>{e(g)}:</b> {e(v)}</li>' for g, v in a['habilidades'])
    proy = ''.join(f'''
      <div class="item">
        <p class="fila"><b>{e(t)}</b><span>{e(f)}</span></p>
        <p>{e(tipo)} | {e(tec)}</p>
        <p class="repo">Repositorio: {url(REPOS[k])}</p>
        <ul>{''.join(f'<li>{e(x)}</li>' for x in pts)}</ul>
      </div>''' for k, t, tipo, f, tec, pts in a['proyectos'])
    form = ''.join(f'''
      <div class="item"><p class="fila"><b>{e(t)}</b><span>{e(f)}</span></p><p>{e(lugar)}</p>{f'<p>{e(x)}</p>' if x else ''}</div>'''
                   for t, lugar, f, x in a['formacion'])
    cert = ''.join(f'''
      <div class="item"><p class="fila"><b>{e(t)}</b><span>{e(f)}</span></p><p>{e(org)}</p><p>{e(x)}</p></div>'''
                   for t, org, f, x in a['certificaciones'])
    return f'''<!doctype html><html lang="es"><head><meta charset="utf-8"><title>Camilo Andrés García Almeida - Hoja de vida</title><style>
@page {{ size: A4; margin: 15mm 17mm; }}
* {{ margin: 0; padding: 0; }}
body {{ font-family: 'Liberation Sans', Arial, sans-serif; color: #000; font-size: 10.3pt; line-height: 1.38; }}
a {{ color: #000; }}
h1 {{ font-size: 19pt; }}
.cargo {{ font-size: 11pt; font-weight: bold; margin: .8mm 0 1.6mm; }}
h2 {{ font-size: 11pt; text-transform: uppercase; border-bottom: 1px solid #000; margin: 4.4mm 0 2mm; padding-bottom: .6mm; break-after: avoid; }}
.item {{ margin-bottom: 2.6mm; break-inside: avoid; }}
.fila {{ display: flex; justify-content: space-between; gap: 4mm; }}
.fila span {{ white-space: nowrap; }}
ul {{ padding-left: 5mm; }}
.hab {{ list-style: none; padding-left: 0; }}
.repo {{ font-size: 8.8pt; white-space: nowrap; }}
</style></head><body>
<h1>Camilo Andrés García Almeida</h1>
<p class="cargo">{e(a['cargo'])}</p>
<p>{contacto}</p>
<h2>Perfil profesional</h2><p>{e(a['perfil'])}</p>
<h2>Habilidades técnicas</h2><ul class="hab">{hab}</ul>
<h2>Experiencia en proyectos</h2>{proy}
<h2>Formación académica</h2>{form}
<h2>Certificaciones y logros</h2>{cert}
<h2>Habilidades blandas</h2><p>{e(a['blandas'])}</p>
<h2>Idiomas</h2><p>{e(a['idiomas'])}</p>
</body></html>'''


VERSIONES = {
    'HojaDeVida_Campus_ES_CamiloGarcia': campus('es'),
    'HojaDeVida_Campus_EN_CamiloGarcia': campus('en'),
    'HojaDeVida_ATS_CamiloGarcia': ats(),
}
for nombre, html in VERSIONES.items():
    with open(os.path.join(SALIDA, nombre + '.html'), 'w', encoding='utf-8') as f:
        f.write(html)
for rec in ('foto.jpg', 'campuslands_horizontal.png'):
    with open(os.path.join(AQUI, rec), 'rb') as src, open(os.path.join(SALIDA, rec), 'wb') as dst:
        dst.write(src.read())

subprocess.run(['node', os.path.join(AQUI, 'imprimir.js'), SALIDA, RAIZ, *VERSIONES.keys()], check=True)
