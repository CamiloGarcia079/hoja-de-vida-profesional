"""Hoja de vida personalizada (diseño propio, dos páginas A4, español).

Uso (desde la carpeta fuente/):
    python3 personalizada.py
Genera HojaDeVida_Personalizada_CamiloGarcia.pdf en la raíz del repositorio.
El contenido coincide con el portafolio, el perfil de GitHub y las otras hojas de vida.
"""
import json
import os
import subprocess
from html import escape as e
from datos import ENLACES, TELEFONO, CORREO, REPOS

AQUI = os.path.dirname(os.path.abspath(__file__))
SALIDA = os.path.join(AQUI, 'salida')
RAIZ = os.path.dirname(AQUI)
NOMBRE = 'HojaDeVida_Personalizada_CamiloGarcia'
os.makedirs(SALIDA, exist_ok=True)

QR = json.load(open(os.path.join(AQUI, 'qr.json')))
MARCA = json.load(open(os.path.join(AQUI, 'iconos.json')))
REPO_MINDCONNECT = 'https://github.com/CamiloGarcia079/trabajo-bound-context-con-spring-security'
REPO_CV = 'https://github.com/CamiloGarcia079/Hojas-de-vida-Chatbot---IA---Camilo-'
REPO_SST = 'https://github.com/CamiloGarcia079/PROYECTO---EVALUACION-Camilo-Garc-a-'
REPO_ADUANA = 'https://github.com/CamiloGarcia079/Aduana-Copilot-CamiloGarcia-DanielOsorio'
REPO_GUARDIAN = 'https://github.com/andresguerra321/GUARDIAN'
CERTIFICADO = 'https://github.com/CamiloGarcia079/hoja-de-vida-profesional/blob/main/Certificado_Hackathon_VisualAgents.pdf'

# ------------------------------------------------------------------ contenido
ACERCA = [
    'Me gusta construir cosas que le quiten trabajo repetitivo a las personas. Esa idea me llevó a la '
    'programación y hoy guía casi todo lo que hago: <b>si una tarea se repite todos los días, se puede automatizar.</b>',
    'Soy Técnico en Desarrollo de Software e Inteligencia Artificial, formado durante un año intensivo en CampusLands. '
    'En ese tiempo pasé de maquetar páginas en HTML a construir APIs seguras con Java y Spring Boot, bots que atienden '
    'clientes por Telegram y agentes de inteligencia artificial que consultan datos reales en lugar de inventar respuestas.',
    'Lo que me diferencia es que cuido que lo que entrego funcione y se entienda: escribo pruebas, documento las '
    'decisiones y explico lo técnico en palabras simples. En diciembre de 2026 inicio mi etapa productiva en <b>Globant</b>.',
]

CIFRAS = [('850+', 'pruebas automatizadas<br>en mis proyectos'), ('5', 'proyectos con IA<br>o automatización'),
          ('1 año', 'de formación<br>intensiva'), ('3', 'idiomas: español,<br>inglés y portugués')]

# Habilidades técnicas: qué uso y dónde lo demostré
HARD = [
    ('Backend con Java', ['Java 21', 'Spring Boot', 'Spring Security', 'JWT'],
     f'Construí la API de <a href="{REPOS["renta"]}">Renta de Herramientas</a> con tres roles y 113 pruebas, y la de '
     f'<a href="{REPO_MINDCONNECT}">MindConnect</a> con arquitectura hexagonal, 52 tablas y más de 600 pruebas.'),
    ('Automatización e IA', ['n8n', 'Python', 'LangChain', 'Gemini', 'Telegram'],
     f'<a href="{REPOS["deliverybot"]}">DeliveryBot</a> toma pedidos con 39 pasos automáticos; el '
     f'<a href="{REPO_CV}">Analizador de CVs</a> evalúa hojas de vida con LangChain y Gemini.'),
    ('Tiempo real y web', ['TypeScript', 'Node.js', 'Socket.IO', 'React', 'JavaScript'],
     f'En <a href="{REPOS["vitalroute"]}">VitalRoute</a> hice el servidor, los canales en tiempo real y el panel con mapa.'),
    ('Bases de datos', ['SQL', 'MySQL', 'PostgreSQL', 'Flyway'],
     f'Modelos relacionales, migraciones versionadas y la base multiempresa de la '
     f'<a href="{REPO_SST}">Plataforma SST</a> con vistas, funciones y triggers.'),
    ('Calidad y entrega', ['JUnit 5', 'pytest', 'Docker', 'Postman', 'Git'],
     'Más de 850 pruebas automatizadas en mis repositorios y proyectos que arrancan con un comando o con Docker.'),
]

# Habilidades blandas: las mismas del portafolio, con un ejemplo real
SOFT = [
    ('Liderazgo y coordinación', 'En el hackathon GUARDIAN coordiné la integración entre módulos, revisé el código '
     'antes de la entrega y presenté el resultado. Hoy lidero mi equipo de proyecto.'),
    ('Comunicación clara', 'Documento cada proyecto para que cualquiera lo ejecute sin preguntarme y explico lo '
     'técnico en palabras simples.'),
    ('Trabajo en equipo', 'VitalRoute, Fórmula 1, Aduana-Copilot y Banco ACME los hice en pareja o en equipo, con '
     'tareas repartidas y revisiones entre nosotros.'),
    ('Aprendizaje rápido', 'En un año pasé de HTML y CSS a Spring Boot, automatización con n8n e inteligencia artificial.'),
    ('Resolución de problemas', 'En DeliveryBot, Google Sheets no actualizaba el carrito de cada usuario por una '
     'diferencia de tipos de datos; encontré la causa y cambié la forma de guardarlo.'),
    ('Responsabilidad y calidad', 'En Renta de Herramientas corregí que el navegador diera acceso sin el servidor y '
     'moví el cálculo del precio al servidor.'),
]

EXPERIENCIA = [
    ('Etapa productiva · Globant', 'Desarrollador en práctica', 'Desde dic 2026', None, None,
     ['Práctica profesional como desarrollador en una empresa global de tecnología.'], []),
    ('Renta de Herramientas', 'Plataforma de alquiler de maquinaria · Proyecto individual', 'Oct 2026', REPOS['renta'],
     'Las reservas cruzadas, los cobros a mano y los daños sin registro son los problemas típicos de un alquiler.',
     ['Desarrollé una API REST con tres roles: reservas por fechas, pagos con IVA del 19 %, devoluciones con mora y reporte de daños.',
      'Moví el cálculo del precio al servidor y tomé al cliente del token JWT para evitar manipulaciones desde el navegador.',
      'Escribí 113 pruebas automatizadas y documenté la API con Swagger y Postman; arranca con un comando o con Docker.'],
     ['Java 21', 'Spring Boot', 'Spring Security', 'JWT', 'MySQL', 'Docker']),
    ('VitalRoute', 'Triaje y despacho médico en tiempo real · Proyecto en pareja', 'Oct 2026', REPOS['vitalroute'],
     'En una emergencia hay que decidir rápido a qué clínica llevar al paciente y avisar a todos al mismo tiempo.',
     ['Desarrollé el servidor en Node.js con Express y TypeScript, con rutas de despacho y estado de la red.',
      'Implementé la comunicación en tiempo real con Socket.IO: canales para ambulancias, clínicas y centro de mando.',
      'Construí el panel en React con mapa y alertas, y un agente de IA con herramienta de despacho (43 commits).'],
     ['TypeScript', 'Node.js', 'Express', 'Socket.IO', 'React', 'MySQL']),
    ('Fórmula 1 en Java', 'Simulador de carreras de escritorio · Proyecto en pareja', 'Ago 2026', REPOS['f1'],
     'Simular una carrera donde muchos autos avanzan a la vez sin que el programa se trabe.',
     ['Cada piloto corre en su propio hilo y todos se sincronizan al cerrar cada vuelta (CyclicBarrier).',
      'Clima dinámico, consumo de combustible, desgaste de neumáticos, paradas en boxes e historial en SQLite.'],
     ['Java 21', 'Swing', 'Threads', 'SQLite']),
    ('DeliveryBot', 'Bot de pedidos en Telegram · Proyecto individual', 'Jun 2026', REPOS['deliverybot'],
     'En una cafetería pequeña los pedidos por chat se toman a mano.',
     ['Automaticé la toma de pedidos con un flujo de 39 pasos en n8n: menú, carrito, total, registro y avisos a cocina y al cliente.',
      'El negocio cambia el menú en Google Sheets sin tocar código; lo dejé funcionando en Windows y en Linux.'],
     ['n8n', 'JavaScript', 'Telegram Bot API', 'Google Sheets']),
]

EDUCACION = [
    ('Técnico en Desarrollo de Software e Inteligencia Artificial', 'CampusLands · Floridablanca', 'Dic 2025 – Nov 2026',
     'Un año intensivo basado en proyectos: Java y Spring Boot, Python, JavaScript y TypeScript, MySQL y PostgreSQL, '
     'automatización con n8n e inteligencia artificial aplicada.'),
    ('Bachiller Académico', 'Fundación Colegio UIS', 'Nov 2025', ''),
]

LOGROS = [
    ('Hackathon Visual Agents', 'Certificado de participación · Jun 2026', CERTIFICADO,
     f'Sistema de seguridad vial <a href="{REPO_GUARDIAN}">GUARDIAN</a> con visión por computadora y Gemini. Rol: integración y presentación.'),
    ('Reto Agente 2026 · Platica.mx', 'Con CampusLands · 2026', REPO_ADUANA,
     'Aduana-Copilot: asistente con IA que cotiza importaciones de medicamentos. Me encargué del agente, el servidor y la interfaz.'),
]

IDIOMAS = [('Español', 'Nativo', 5), ('Inglés', 'A2', 2), ('Portugués', 'A1', 1)]

# ------------------------------------------------------------------ íconos (24x24)
I = {
    'correo': '<path d="M3 6h18v12H3z M3 7l9 6 9-6" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/>',
    'tel': '<path d="M6.6 3.5h3l1.5 4-2 1.3a11 11 0 0 0 6.1 6.1l1.3-2 4 1.5v3c0 1.1-.9 2-2 2A17 17 0 0 1 4.6 5.5c0-1.1.9-2 2-2z" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/>',
    'lugar': '<path d="M12 21s7-6.2 7-11.5A7 7 0 0 0 5 9.5C5 14.8 12 21 12 21z" fill="none" stroke="currentColor" stroke-width="1.8"/><circle cx="12" cy="9.5" r="2.5" fill="none" stroke="currentColor" stroke-width="1.8"/>',
    'web': '<circle cx="12" cy="12" r="8.5" fill="none" stroke="currentColor" stroke-width="1.7"/><path d="M3.5 12h17M12 3.5c2.3 2.4 3.4 5.2 3.4 8.5s-1.1 6.1-3.4 8.5c-2.3-2.4-3.4-5.2-3.4-8.5s1.1-6.1 3.4-8.5z" fill="none" stroke="currentColor" stroke-width="1.5"/>',
    'linkedin': f'<path d="{MARCA["linkedin"]}" fill="currentColor"/>',
    'github': f'<path d="{MARCA["github"]}" fill="currentColor"/>',
}
ico = lambda k: f'<svg class="i" viewBox="0 0 24 24" aria-hidden="true">{I[k]}</svg>'
LOGO = ('<svg class="logo" viewBox="0 0 64 64" aria-hidden="true"><rect width="64" height="64" rx="14" fill="#0e1726"/>'
        '<path d="M46.97 20.30 A19 19 0 1 0 46.97 43.70 L41.46 39.39 A12 12 0 1 1 41.46 24.61 Z" fill="#fff"/>'
        '<rect x="43" y="34" width="7" height="7" fill="#c9a04f"/></svg>')


def chips(lista):
    return ''.join(f'<span class="chip">{e(x)}</span>' for x in lista)


def h2(num, texto):
    return f'<h2><span>{num}</span>{texto}</h2>'


# ------------------------------------------------------------------ plantilla
def html():
    contacto = [
        ('correo', CORREO, f'mailto:{CORREO}'), ('tel', TELEFONO, 'tel:+573043962022'),
        ('lugar', 'Bucaramanga, Colombia', None), ('web', 'camilogarcia079.github.io/portafolio', ENLACES['portafolio']),
        ('linkedin', 'in/camilo-garcia-7570693b7', ENLACES['linkedin']), ('github', 'github.com/CamiloGarcia079', ENLACES['github']),
    ]
    contacto_html = ''.join(
        f'<li>{ico(k)}{f"<a href={chr(34)}{u}{chr(34)}>{e(t).replace(".io/", ".io/<wbr>")}</a>" if u else e(t)}</li>' for k, t, u in contacto)
    cifras = ''.join(f'<div><b>{n}</b><span>{t}</span></div>' for n, t in CIFRAS)
    hard = ''.join(f'''
      <div class="hard"><div class="hard__top"><h4>{e(t)}</h4><div class="chips">{chips(c)}</div></div><p>{ev}</p></div>''' for t, c, ev in HARD)
    soft = ''.join(f'<div class="soft"><h4>{e(t)}</h4><p>{e(x)}</p></div>' for t, x in SOFT)

    def exp(item):
        t, sub, fecha, url, ctx, pts, tec = item
        titulo = f'<a href="{url}">{e(t)}</a>' if url else e(t)
        link = f'<a class="ver" href="{url}">Ver repositorio ↗</a>' if url else ''
        return f'''
      <article class="exp{' exp--proximo' if not url else ''}">
        <div class="exp__top"><h3>{titulo}</h3><span class="fecha">{e(fecha)}</span></div>
        <p class="sub">{e(sub)}</p>
        {f'<p class="ctx">{e(ctx)}</p>' if ctx else ''}
        <ul>{''.join(f'<li>{e(p)}</li>' for p in pts)}</ul>
        {f'<div class="exp__pie"><div class="chips">{chips(tec)}</div>{link}</div>' if tec else ''}
      </article>'''
    experiencia = ''.join(exp(x) for x in EXPERIENCIA)
    educacion = ''.join(f'''
      <div class="edu"><span class="fecha">{e(f)}</span><h4>{e(t)}</h4>
        <p class="sub">{e(lugar)}</p>{f'<p>{e(x)}</p>' if x else ''}</div>''' for t, lugar, f, x in EDUCACION)
    logros = ''.join(f'''
      <div class="edu"><h4><a href="{u}">{e(t)}</a></h4><p class="sub">{e(sub)}</p><p>{x}</p></div>''' for t, sub, u, x in LOGROS)
    idiomas = ''.join(f'''
      <li><span>{e(n)}</span><i>{''.join(f'<b class="{"on" if k < v else ""}"></b>' for k in range(5))}</i><em>{e(nivel)}</em></li>''' for n, nivel, v in IDIOMAS)
    n = QR['n']
    qr = f'<svg class="qr" viewBox="-2 -2 {n + 4} {n + 4}"><rect x="-2" y="-2" width="{n + 4}" height="{n + 4}" fill="#fff"/><path d="{QR["d"]}" fill="#0e1726"/></svg>'

    fuente = lambda nombre, archivo, peso: f"@font-face {{ font-family: '{nombre}'; src: url('../fuentes/{archivo}'); font-weight: {peso}; }}"
    return f'''<!doctype html><html lang="es"><head><meta charset="utf-8"><title>Camilo Andrés García Almeida · Hoja de vida</title><style>
{fuente('Space Grotesk', 'SpaceGrotesk[wght].ttf', '300 700')}
{fuente('Noto Sans', 'NotoSans[wdth,wght].ttf', '100 900')}
@page {{ size: A4; margin: 0; }}
:root {{ --ink: #0e1726; --texto: #2b3240; --suave: #6b7280; --linea: #e4e2dc; --oro: #b08a3e; --fondo: #f6f4ef; }}
* {{ box-sizing: border-box; margin: 0; padding: 0; }}
body {{ font-family: 'Noto Sans', sans-serif; color: var(--texto); font-size: 8.9pt; line-height: 1.45; }}
a {{ color: inherit; text-decoration: none; }}
p a, .soft a {{ border-bottom: .2mm solid var(--oro); }}
.pagina {{ width: 210mm; height: 297mm; position: relative; overflow: hidden; display: grid; grid-template-columns: 1fr 64mm; }}
.pagina + .pagina {{ break-before: page; }}
main {{ padding: 13mm 9mm 12mm 13mm; }}
aside {{ background: var(--fondo); padding: 13mm 8mm 12mm 8mm; border-left: 1px solid var(--linea); }}
.barra {{ position: absolute; left: 0; top: 0; bottom: 0; width: 3.2mm; background: var(--ink); }}
.barra::after {{ content: ''; position: absolute; left: 0; top: 13mm; width: 3.2mm; height: 26mm; background: var(--oro); }}
/* Encabezado */
.cab {{ display: grid; grid-template-columns: 1fr auto; align-items: start; gap: 6mm; padding-bottom: 6mm; border-bottom: 1px solid var(--linea); margin-bottom: 6mm; }}
.marca {{ display: flex; align-items: center; gap: 2.4mm; font: 600 7.4pt 'Space Grotesk'; letter-spacing: .22em; text-transform: uppercase; color: var(--suave); margin-bottom: 3mm; }}
.logo {{ width: 7mm; height: 7mm; }}
h1 {{ font: 700 27pt/1.02 'Space Grotesk'; color: var(--ink); letter-spacing: -.02em; }}
h1 em {{ font-style: normal; color: var(--oro); }}
.rol {{ font: 500 11.5pt 'Space Grotesk'; color: var(--ink); margin-top: 2.6mm; }}
.lema {{ color: var(--suave); margin-top: 1.4mm; font-size: 9pt; }}
.foto {{ width: 34mm; height: 34mm; border-radius: 50%; object-fit: cover; border: 1mm solid #fff; box-shadow: 0 0 0 .35mm var(--oro); }}
/* Secciones */
h2 {{ font: 700 11.2pt 'Space Grotesk'; color: var(--ink); text-transform: uppercase; letter-spacing: .12em; display: flex; align-items: center; gap: 2.4mm; margin: 0 0 3mm; }}
h2 span {{ font: 500 8pt 'Space Grotesk'; color: var(--oro); letter-spacing: 0; }}
h2::after {{ content: ''; flex: 1; height: 1px; background: var(--linea); }}
section {{ margin-bottom: 6mm; }}
.acerca p {{ margin-bottom: 2mm; text-align: justify; }}
.acerca b {{ color: var(--ink); }}
.cifras {{ display: grid; grid-template-columns: repeat(4, 1fr); border: 1px solid var(--linea); border-radius: 2.4mm; margin-top: 3.6mm; }}
.cifras div {{ padding: 2.6mm 3mm; border-left: 1px solid var(--linea); }}
.cifras div:first-child {{ border-left: 0; }}
.cifras b {{ display: block; font: 700 15pt 'Space Grotesk'; color: var(--ink); }}
.cifras span {{ font-size: 7.2pt; color: var(--suave); line-height: 1.3; display: block; }}
.hard {{ padding: 2.6mm 0; border-bottom: 1px dashed var(--linea); }}
.hard:last-child {{ border-bottom: 0; }}
.hard__top {{ display: flex; justify-content: space-between; align-items: center; gap: 3mm; margin-bottom: 1mm; }}
h4 {{ font: 600 9.6pt 'Space Grotesk'; color: var(--ink); }}
.chips {{ display: flex; flex-wrap: wrap; gap: 1.2mm; justify-content: flex-end; }}
.chip {{ font-size: 6.9pt; padding: .45mm 1.8mm; border-radius: 1.2mm; border: 1px solid #d8d4ca; color: var(--ink); background: #fff; white-space: nowrap; }}
.hard p {{ color: var(--texto); }}
/* Lateral */
aside h2 {{ font-size: 9.6pt; }}
aside section {{ margin-bottom: 7mm; }}
.contacto li {{ list-style: none; display: grid; grid-template-columns: 4.6mm 1fr; gap: 2mm; align-items: center; margin-bottom: 2.2mm; font-size: 8pt; overflow-wrap: break-word; }}
.i {{ width: 4mm; height: 4mm; color: var(--ink); }}
.soft {{ margin-bottom: 3.2mm; }}
.soft h4 {{ font-size: 9pt; display: flex; gap: 1.6mm; align-items: center; }}
.soft h4::before {{ content: ''; width: 1.6mm; height: 1.6mm; background: var(--oro); }}
.soft p {{ font-size: 7.8pt; color: var(--texto); line-height: 1.4; margin-top: .6mm; }}
.idiomas li {{ list-style: none; display: grid; grid-template-columns: 17mm 1fr 8mm; align-items: center; gap: 2mm; margin-bottom: 2.2mm; font-size: 8.4pt; }}
.idiomas i {{ display: flex; gap: .9mm; }}
.idiomas i b {{ width: 3.2mm; height: 1.6mm; border-radius: .8mm; background: #dcd8cf; }}
.idiomas i b.on {{ background: var(--ink); }}
.idiomas em {{ font-style: normal; font-size: 7.6pt; color: var(--suave); text-align: right; }}
.qrbox {{ display: grid; grid-template-columns: 22mm 1fr; gap: 3mm; align-items: center; padding: 3mm; border-radius: 2.4mm; background: #fff; border: 1px solid var(--linea); }}
.qr {{ width: 22mm; height: 22mm; display: block; }}
.qrbox p {{ font-size: 7.6pt; color: var(--suave); }}
.qrbox b {{ display: block; font: 600 8.6pt 'Space Grotesk'; color: var(--ink); margin-bottom: .6mm; }}
/* Experiencia */
.exp {{ padding: 3.4mm 0; border-bottom: 1px solid var(--linea); }}
.exp:first-of-type {{ padding-top: 0; }}
.exp__top {{ display: flex; justify-content: space-between; align-items: baseline; gap: 3mm; }}
.exp h3 {{ font: 700 11pt 'Space Grotesk'; color: var(--ink); }}
.fecha {{ font: 500 7.8pt 'Space Grotesk'; color: var(--oro); white-space: nowrap; }}
.sub {{ color: var(--suave); font-size: 8pt; margin-top: .3mm; }}
.ctx {{ font-style: italic; color: var(--suave); margin-top: 1.4mm; }}
.exp ul {{ margin: 1.6mm 0 0 4mm; }}
.exp li {{ margin-bottom: .8mm; }}
.exp li::marker {{ color: var(--oro); }}
.exp__pie {{ display: flex; justify-content: space-between; align-items: center; margin-top: 2mm; gap: 3mm; }}
.exp__pie .chips {{ justify-content: flex-start; }}
.ver {{ font: 600 7.6pt 'Space Grotesk'; color: var(--oro); white-space: nowrap; }}
.exp--proximo {{ background: var(--fondo); border: 1px solid var(--linea); border-radius: 2.4mm; padding: 3mm 3.6mm !important; margin-bottom: 1mm; }}
.edu {{ margin-bottom: 3.2mm; }}
.edu .fecha {{ display: block; margin-bottom: .4mm; }}
.edu p:not(.sub) {{ margin-top: 1mm; }}
.pie {{ position: absolute; left: 13mm; right: 9mm; bottom: 6mm; display: flex; justify-content: space-between; font-size: 7pt; color: var(--suave); }}
</style></head><body>

<!-- ===================== PÁGINA 1 ===================== -->
<div class="pagina">
  <div class="barra"></div>
  <main>
    <header class="cab">
      <div>
        <div class="marca">{LOGO}Hoja de vida · 2026</div>
        <h1>Camilo Andrés<br><em>García Almeida</em></h1>
        <p class="rol">Desarrollador Junior · Técnico en Desarrollo de Software e IA</p>
        <p class="lema">Automatización, bots y desarrollo web · Próximo paso: etapa productiva en Globant</p>
      </div>
      <img class="foto" src="foto_hdv.jpg" alt="Camilo García">
    </header>

    <section class="acerca">{h2('01', 'Acerca de mí')}{''.join(f'<p>{p}</p>' for p in ACERCA)}
      <div class="cifras">{cifras}</div>
    </section>

    <section>{h2('02', 'Habilidades técnicas')}{hard}</section>
  </main>
  <aside>
    <section>{h2('', 'Contacto')}<ul class="contacto">{contacto_html}</ul></section>
    <section>{h2('', 'Habilidades blandas')}{soft}</section>
  </aside>
  <div class="pie"><span>Camilo Andrés García Almeida · Desarrollador Junior</span><span>1 / 2</span></div>
</div>

<!-- ===================== PÁGINA 2 ===================== -->
<div class="pagina">
  <div class="barra"></div>
  <main>
    <section>{h2('03', 'Experiencia y proyectos')}{experiencia}</section>
  </main>
  <aside>
    <section>{h2('', 'Educación')}{educacion}</section>
    <section>{h2('', 'Logros y certificaciones')}{logros}</section>
    <section>{h2('', 'Idiomas')}<ul class="idiomas">{idiomas}</ul></section>
    <section><div class="qrbox">{qr}<p><b>Portafolio</b>Escanea para ver mis proyectos funcionando, en español e inglés.</p></div></section>
  </aside>
  <div class="pie"><span>camilogarcia079.github.io/portafolio</span><span>2 / 2</span></div>
</div>
</body></html>'''


with open(os.path.join(SALIDA, NOMBRE + '.html'), 'w', encoding='utf-8') as f:
    f.write(html())
with open(os.path.join(AQUI, 'foto_hdv.jpg'), 'rb') as src, open(os.path.join(SALIDA, 'foto_hdv.jpg'), 'wb') as dst:
    dst.write(src.read())
subprocess.run(['node', os.path.join(AQUI, 'imprimir.js'), SALIDA, RAIZ, NOMBRE], check=True)
