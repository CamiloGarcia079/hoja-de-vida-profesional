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
from urllib.parse import unquote
from datos import ENLACES, TELEFONO, CORREO, CIUDAD, REPOS, CAMPUS, ATS

AQUI = os.path.dirname(os.path.abspath(__file__))
SALIDA = os.path.join(AQUI, 'salida')
RAIZ = os.path.dirname(AQUI)
os.makedirs(SALIDA, exist_ok=True)

import json as _json
_ICONOS_MARCA = _json.load(open(os.path.join(AQUI, 'iconos.json')))
NAVY = '#0e2359'
FRANJA = '#394374'

# Íconos rellenos de "Datos personales", como en la plantilla oficial
ICONOS_CAMPUS = {
    'linkedin': f'<svg viewBox="0 0 24 24"><path fill="{NAVY}" d="{_ICONOS_MARCA["linkedin"]}"/></svg>',
    'github': f'<svg viewBox="0 0 24 24"><path fill="{NAVY}" d="{_ICONOS_MARCA["github"]}"/></svg>',
    'portafolio': (f'<svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="12" fill="{NAVY}"/>'
                   '<path fill="#fff" d="M9.5 7.5V6.6c0-.6.5-1.1 1.1-1.1h2.8c.6 0 1.1.5 1.1 1.1v.9h2.6c.8 0 1.4.6 1.4 1.4v2.3H5.5V8.9c0-.8.6-1.4 1.4-1.4h2.6zm1.4 0h2.2v-.6h-2.2v.6zM5.5 12.2h5.6v1.1h1.8v-1.1h5.6v4.4c0 .8-.6 1.4-1.4 1.4H6.9c-.8 0-1.4-.6-1.4-1.4v-4.4z"/></svg>'),
}


# ------------------------------------------------------------------ formato Campus
# Réplica de la plantilla oficial de CampusLands: foto grande a la izquierda, encabezado azul con el
# nombre, franja con el rol, columnas de perfil/formación/experiencia y habilidades/competencias/
# datos personales/idiomas, y pie con el logo.
def campus(lang):
    d = CAMPUS[lang]
    perfil, formacion, experiencia, habilidades, competencias, datos, idiomas = d['secciones']
    form = ''.join(f'''
        <div class="form"><h4>{e(t)}</h4><div class="meta"><span>{e(lugar)}</span><span>{e(fecha)}</span></div></div>'''
                   for t, lugar, fecha in d['formacion'])
    exp = ''.join(f'''
        <div class="exp"><h4><a href="{REPOS[k]}">{e(t)}</a></h4><p class="tec">{e(tec)}</p><p class="txt">{e(txt)}</p></div>'''
                  for k, t, tec, txt in d['experiencia'])
    contacto = ''.join(f'''
        <li><a href="{ENLACES[k]}"><span class="ico">{ICONOS_CAMPUS[k]}</span><u>{e(n)}</u></a></li>'''
                       for k, n in d['datos'])
    dos_col = lambda items: ''.join(f'<li>{e(x)}</li>' for x in items)
    fuente = lambda nombre, archivo, peso: (f"@font-face {{ font-family: '{nombre}'; src: url('../fuentes/{archivo}'); "
                                            f"font-weight: {peso}; }}")
    return f'''<!doctype html><html lang="{lang}"><head><meta charset="utf-8"><title>Camilo Andrés García Almeida</title><style>
{fuente('Libre Baskerville', 'LibreBaskerville[wght].ttf', '400 700')}
{fuente('Poppins', 'Poppins-Light.ttf', 300)}
{fuente('Poppins', 'Poppins-Regular.ttf', 400)}
{fuente('Poppins', 'Poppins-Medium.ttf', 500)}
{fuente('Noto Sans', 'NotoSans[wdth,wght].ttf', '100 900')}
@page {{ size: A4; margin: 0; }}
* {{ box-sizing: border-box; margin: 0; padding: 0; }}
body {{ width: 210mm; height: 297mm; position: relative; overflow: hidden; font-family: 'Noto Sans', sans-serif; color: #1f1f1f; font-size: 9.2pt; line-height: 1.32; }}
a {{ color: inherit; text-decoration: none; }}
/* Encabezado */
.foto {{ position: absolute; left: 0; top: 0; width: 82.4mm; height: 57.3mm; background: url(foto_campus.jpg) 57% 30% / 125% auto no-repeat; }}
.cab {{ position: absolute; left: 82.4mm; right: 0; top: 0; height: 39.6mm; background: {NAVY}; display: grid; place-items: center; }}
.cab h1 {{ font: 700 25pt/1.22 'Libre Baskerville', serif; color: #fff; text-align: center; }}
.esquina {{ position: absolute; right: 0; top: 25.8mm; width: 14mm; height: 13.8mm; background: {FRANJA}; clip-path: polygon(100% 0, 100% 100%, 0 100%); }}
.franja {{ position: absolute; left: 82.4mm; right: 0; top: 39.6mm; height: 17.7mm; background: {FRANJA}; display: grid; place-items: center; }}
.franja p {{ font: 700 12.5pt 'Libre Baskerville', serif; color: #fff; letter-spacing: .08em; }}
/* Columnas */
.izq {{ position: absolute; left: 5mm; top: 59.5mm; width: 118mm; }}
.sep {{ position: absolute; left: 131.4mm; top: 61mm; width: .6mm; height: 219mm; background: #d6d6d6; }}
.der {{ position: absolute; left: 136mm; top: 61mm; right: 4mm; }}
h3 {{ font: 400 16pt/1.1 'Poppins', sans-serif; letter-spacing: .32em; text-transform: uppercase; color: #1f1f1f; }}
.izq section {{ padding-bottom: 3mm; margin-bottom: 3.2mm; border-bottom: .8mm solid #d6d6d6; margin-right: 4mm; }}
.der section {{ padding: 0 0 3.2mm 3.5mm; margin-bottom: 3.6mm; border-bottom: .8mm solid #d6d6d6; margin-left: -2mm; }}
section:last-child {{ border-bottom: 0 !important; }}
.perfil {{ margin-top: .8mm; }}
.izq h3 {{ margin-bottom: 2.2mm; }}
.form {{ margin-bottom: 2.2mm; }}
.form h4 {{ font: 400 12.2pt 'Noto Sans', sans-serif; color: #1f1f1f; }}
.meta {{ display: flex; justify-content: space-between; gap: 6mm; color: #7d7d7d; font-size: 10pt; margin-top: .8mm; }}
.meta span:last-child {{ white-space: nowrap; }}
.exp {{ margin-bottom: 3mm; }}
.exp h4 {{ font: 400 11pt 'Noto Sans', sans-serif; color: #1f1f1f; }}
.tec {{ color: #9a9a9a; font-size: 7.6pt; margin: .2mm 0 .8mm; }}
.txt {{ font-size: 9.3pt; text-align: justify; }}
.der h3 {{ margin-bottom: 2.6mm; }}
ul {{ list-style: none; }}
.cols {{ display: grid; grid-template-columns: 1fr 1fr; column-gap: 3mm; }}
.cols li {{ position: relative; padding-left: 4mm; }}
.cols li::before {{ content: ''; position: absolute; left: .4mm; width: 1.5mm; height: 1.5mm; border-radius: 50%; background: #1f1f1f; }}
.hab li {{ font-size: 12.2pt; line-height: 1.7; }}
.hab li::before {{ top: 2.7mm; }}
.hab li:last-child:nth-child(odd) {{ grid-column: 1 / -1; justify-self: center; }}
.comp li {{ font-size: 8.8pt; line-height: 1.6; }}
.comp li::before {{ top: 1.6mm; width: 1.1mm; height: 1.1mm; }}
.datos h3, .idiomas h3 {{ font-size: 13pt; letter-spacing: .34em; margin-left: 2.5mm; }}
.contacto {{ margin: 3.5mm 0 0 1mm; }}
.contacto li {{ margin-bottom: 2.8mm; font-size: 9.6pt; }}
.contacto a {{ display: flex; align-items: center; gap: 3.2mm; }}
.ico svg {{ width: 5.6mm; height: 5.6mm; display: block; }}
.idio {{ margin: 2.5mm 0 0 5mm; }}
.idio li {{ position: relative; padding-left: 4.5mm; font-size: 9.4pt; line-height: 2.2; }}
.idio li::before {{ content: ''; position: absolute; left: 0; top: 2.4mm; width: 1.4mm; height: 1.4mm; border-radius: 50%; background: #1f1f1f; }}
/* Pie */
footer {{ position: absolute; left: 0; right: 0; bottom: 0; height: 15.2mm; background: {NAVY}; }}
footer img {{ position: absolute; right: 5mm; top: 2mm; height: 11.2mm; }}
</style></head><body>
<div class="foto"></div>
<div class="cab"><h1>Camilo Andrés<br>García Almeida</h1></div>
<div class="esquina"></div>
<div class="franja"><p>{e(d['rol'])}</p></div>
<div class="izq">
  <section><h3>{e(perfil)}</h3><p class="perfil">{e(d['perfil'])}</p></section>
  <section><h3>{e(formacion)}</h3>{form}</section>
  <section><h3>{e(experiencia)}</h3>{exp}</section>
</div>
<div class="sep"></div>
<div class="der">
  <section><h3>{e(habilidades)}</h3><ul class="cols hab">{dos_col(d['habilidades'])}</ul></section>
  <section><h3>{e(competencias)}</h3><ul class="cols comp">{dos_col(d['competencias'])}</ul></section>
  <section class="datos"><h3>{e(datos)}</h3><ul class="contacto">{contacto}</ul></section>
  <section class="idiomas"><h3>{e(idiomas)}</h3><ul class="idio">{''.join(f'<li>{e(i)}</li>' for i in d['idiomas'])}</ul></section>
</div>
<footer><img src="campuslands_logo.png" alt="Campuslands"></footer>
</body></html>'''


# ------------------------------------------------------------------ formato ATS (español)
def ats():
    a = ATS
    url = lambda u: f'<a href="{u}">{e(unquote(u))}</a>'
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
for rec in ('foto_campus.jpg', 'campuslands_logo.png'):
    with open(os.path.join(AQUI, rec), 'rb') as src, open(os.path.join(SALIDA, rec), 'wb') as dst:
        dst.write(src.read())

subprocess.run(['node', os.path.join(AQUI, 'imprimir.js'), SALIDA, RAIZ, *VERSIONES.keys()], check=True)
