"""Datos de la hoja de vida.
Todo lo que aparece en los PDF sale de aquí. Debe coincidir con el portafolio y con el perfil de GitHub:
mismos lenguajes, mismos cuatro proyectos destacados, mismas habilidades blandas y mismos idiomas.
"""

ENLACES = {
    'linkedin': 'https://www.linkedin.com/in/camilo-andr%C3%A9s-garc%C3%ADa-almeida-7570693b7/',
    'github': 'https://github.com/CamiloGarcia079',
    'portafolio': 'https://camilogarcia079.github.io/portafolio/',
}
TELEFONO = '+57 304 396 2022'
CORREO = 'kaliko2411@gmail.com'
CIUDAD = 'Bucaramanga, Santander, Colombia'

REPOS = {
    'f1': 'https://github.com/santiagoosorio0708e-wq/Formula1-java',
    'vitalroute': 'https://github.com/santiagoosorio0708e-wq/Vital-Route',
    'deliverybot': 'https://github.com/CamiloGarcia079/Proyecto_DeliveryBot_GarciaCamilo',
    'renta': 'https://github.com/CamiloGarcia079/Evaluacion-Springboot-Herramientas---Camilo-Garcia-Almeida',
}

# ------------------------------------------------------------------ formato Campus (español e inglés)
# Misma estructura de la hoja Campus original: Perfil, Formación, Experiencia | Habilidades,
# Competencias, Datos personales, Idiomas.
CAMPUS = {
    'es': {
        'rol': 'Desarrollador Junior',
        'secciones': ['Perfil', 'Formación', 'Experiencia', 'Habilidades', 'Competencias', 'Datos personales', 'Idiomas'],
        'perfil': ('Técnico en Desarrollo de Software e Inteligencia Artificial formado en CampusLands, enfocado en '
                   'automatización, bots y desarrollo web. Construyo APIs con Java y Spring Boot, flujos automáticos con '
                   'n8n y asistentes con inteligencia artificial en Python y TypeScript. Me caracterizo por el liderazgo, '
                   'la comunicación clara y el trabajo en equipo, y entrego proyectos probados y documentados. En '
                   'diciembre de 2026 inicio mi etapa productiva en Globant.'),
        'formacion': [
            ('Técnico en Desarrollo de Software e Inteligencia Artificial', 'CampusLands, Floridablanca', 'Dic 2025 – Nov 2026'),
            ('Bachiller Académico', 'Fundación Colegio UIS', 'Nov 2025'),
        ],
        'experiencia': [
            ('f1', 'Fórmula 1 en Java — Simulador de carreras', 'Java · Swing · Hilos · SQLite',
             'Simulador de escritorio hecho en pareja: cada piloto corre en su propio hilo, con clima dinámico, '
             'consumo de combustible, desgaste de neumáticos, paradas en boxes e historial de carreras.'),
            ('vitalroute', 'VitalRoute — Triaje médico en tiempo real', 'TypeScript · Node.js · Socket.IO · React · MySQL',
             'Proyecto en pareja que decide a qué clínica llevar a un paciente. Desarrollé el servidor, la comunicación '
             'en tiempo real, el panel con mapa y el agente de inteligencia artificial que despacha la emergencia.'),
            ('deliverybot', 'DeliveryBot — Bot de pedidos', 'n8n · JavaScript · Telegram · Google Sheets',
             'Bot de Telegram para una cafetería: muestra el menú, arma el carrito, calcula el total, guarda el pedido '
             'y avisa a cocina y al cliente. Automatización de 39 pasos sin intervención manual.'),
            ('renta', 'Renta de Herramientas — Plataforma de alquiler', 'Java · Spring Boot · Spring Security · MySQL · Docker',
             'API REST individual con tres tipos de usuario: reservas por fechas, pagos con IVA, devoluciones con '
             'mora y reporte de daños. Incluye 113 pruebas automatizadas.'),
        ],
        # Los mismos cinco lenguajes del perfil de GitHub y del portafolio, más las dos herramientas principales
        'habilidades': ['Java', 'Python', 'TypeScript', 'JavaScript', 'SQL', 'Spring Boot', 'n8n'],
        # Las mismas seis habilidades blandas del portafolio
        'competencias': ['Liderazgo', 'Comunicación', 'Trabajo en equipo', 'Aprendizaje rápido', 'Resolución de problemas', 'Responsabilidad'],
        'datos': [('linkedin', 'LinkedIn'), ('github', 'GitHub'), ('portafolio', 'Portafolio')],
        'idiomas': ['Español – Nativo', 'Inglés – A2', 'Portugués – A1'],
    },
    'en': {
        'rol': 'Junior Developer',
        'secciones': ['Profile', 'Education', 'Experience', 'Skills', 'Competencies', 'Personal data', 'Languages'],
        'perfil': ('Software Development and Artificial Intelligence Technician trained at CampusLands, focused on '
                   'automation, bots and web development. I build APIs with Java and Spring Boot, automated workflows '
                   'with n8n and AI assistants in Python and TypeScript. I stand out for leadership, clear communication '
                   'and teamwork, and I deliver tested, documented projects. In December 2026 I start my professional '
                   'internship at Globant.'),
        'formacion': [
            ('Software Development and Artificial Intelligence Technician', 'CampusLands, Floridablanca', 'Dec 2025 – Nov 2026'),
            ('High School Diploma', 'Fundación Colegio UIS', 'Nov 2025'),
        ],
        'experiencia': [
            ('f1', 'Formula 1 in Java — Race simulator', 'Java · Swing · Threads · SQLite',
             'Desktop simulator built in a pair: each driver runs on its own thread, with dynamic weather, fuel '
             'consumption, tyre wear, pit stops and race history.'),
            ('vitalroute', 'VitalRoute — Real-time medical triage', 'TypeScript · Node.js · Socket.IO · React · MySQL',
             'Pair project that decides which clinic a patient should go to. I built the server, the real-time '
             'communication, the map dashboard and the AI agent that dispatches the emergency.'),
            ('deliverybot', 'DeliveryBot — Ordering bot', 'n8n · JavaScript · Telegram · Google Sheets',
             'Telegram bot for a coffee shop: shows the menu, builds the cart, calculates the total, saves the order '
             'and notifies kitchen and customer. A 39-step automation with no manual work.'),
            ('renta', 'Tool Rental Platform', 'Java · Spring Boot · Spring Security · MySQL · Docker',
             'Individual REST API with three user types: date bookings, payments with VAT, returns with late fees and '
             'damage reports. Includes 113 automated tests.'),
        ],
        'habilidades': ['Java', 'Python', 'TypeScript', 'JavaScript', 'SQL', 'Spring Boot', 'n8n'],
        'competencias': ['Leadership', 'Communication', 'Teamwork', 'Fast learner', 'Problem solving', 'Ownership'],
        'datos': [('linkedin', 'LinkedIn'), ('github', 'GitHub'), ('portafolio', 'Portfolio')],
        'idiomas': ['Spanish – Native', 'English – A2', 'Portuguese – A1'],
    },
}

# ------------------------------------------------------------------ formato ATS (solo español)
ATS = {
    'cargo': 'Desarrollador Junior | Técnico en Desarrollo de Software e Inteligencia Artificial',
    'perfil': ('Técnico en Desarrollo de Software e Inteligencia Artificial (CampusLands, 2026) con enfoque en '
               'automatización de procesos, bots y desarrollo web. Experiencia práctica construyendo APIs REST con Java '
               'y Spring Boot protegidas con Spring Security y JWT, automatizaciones con n8n, asistentes con inteligencia '
               'artificial en Python y TypeScript, y bases de datos MySQL y PostgreSQL. Trabajo en equipo con metodologías '
               'ágiles, coordiné la integración de un equipo en un hackathon de inteligencia artificial y entrego proyectos '
               'con pruebas automatizadas y documentación. Inicio mi etapa productiva en Globant en diciembre de 2026.'),
    # Mismos grupos y tecnologías que la sección "Lenguajes y tecnologías" del portafolio
    'habilidades': [
        ('Lenguajes', 'Java, Python, TypeScript, JavaScript, SQL'),
        ('Frameworks', 'Spring Boot, Spring Security, JWT, Express, React, Streamlit'),
        ('Automatización e IA', 'n8n, Telegram Bot API, LangChain, Gemini, Pydantic'),
        ('Bases de datos', 'MySQL, PostgreSQL, Flyway, Google Sheets'),
        ('Calidad y entrega', 'JUnit 5, pytest, Docker, Postman, Git, GitHub'),
    ],
    'proyectos': [
        ('renta', 'Renta de Herramientas — Plataforma de alquiler de maquinaria', 'Proyecto individual', 'Oct 2026',
         'Java 21, Spring Boot, Spring Security, JWT, MySQL, Docker',
         ['Desarrollé una API REST con tres roles (administrador, proveedor y cliente) para reservas por fechas, pagos con IVA del 19 %, devoluciones con mora y reporte de daños.',
          'Implementé el cálculo del precio en el servidor y la identificación del cliente desde el token JWT para evitar manipulaciones desde el navegador.',
          'Escribí 113 pruebas automatizadas y documenté la API con Swagger y colecciones de Postman; el proyecto arranca con un solo comando o con Docker.']),
        ('vitalroute', 'VitalRoute — Triaje y despacho médico en tiempo real', 'Proyecto en pareja', 'Oct 2026',
         'TypeScript, Node.js, Express, Socket.IO, React, MySQL',
         ['Desarrollé el servidor en Node.js con Express y TypeScript, con rutas de despacho y estado de la red.',
          'Implementé la comunicación en tiempo real con Socket.IO mediante canales separados para ambulancias, clínicas y centro de mando.',
          'Construí el panel en React con mapa, alertas e historial de eventos, y un agente de inteligencia artificial con herramienta de despacho.']),
        ('f1', 'Fórmula 1 en Java — Simulador de carreras', 'Proyecto en pareja', 'Ago 2026',
         'Java 21, Swing, hilos (Threads, CyclicBarrier), SQLite',
         ['Simulador de escritorio en el que cada piloto corre en su propio hilo y todos se sincronizan al cerrar cada vuelta.',
          'Incluye clima dinámico, consumo de combustible, desgaste de neumáticos, paradas en boxes e historial de carreras guardado en SQLite.']),
        ('deliverybot', 'DeliveryBot — Bot de pedidos en Telegram', 'Proyecto individual', 'Jun 2026',
         'n8n, JavaScript, Telegram Bot API, Google Sheets',
         ['Automaticé la toma de pedidos de una cafetería con un flujo de 39 pasos en n8n: menú, carrito, total, registro del pedido y avisos a cocina y al cliente.',
          'Resolví fallas de actualización en Google Sheets y dejé el bot funcionando en Windows y en Linux.']),
    ],
    'formacion': [
        ('Técnico en Desarrollo de Software e Inteligencia Artificial', 'CampusLands, Floridablanca', 'Dic 2025 – Nov 2026',
         'Java y Spring Boot, Python, JavaScript y TypeScript, MySQL y PostgreSQL, automatización con n8n e inteligencia artificial aplicada.'),
        ('Bachiller Académico', 'Fundación Colegio UIS', 'Nov 2025', ''),
    ],
    'certificaciones': [
        ('Hackathon Visual Agents — Certificado de participación', 'CampusLands, Voxel51, UPB y Cámara de Comercio de Bucaramanga', 'Jun 2026',
         'Rol de integración, contratos entre módulos y presentación final del proyecto GUARDIAN (visión por computadora y Gemini).'),
        ('Reto Agente 2026 — Platica.mx con CampusLands', 'Proyecto Aduana-Copilot, en pareja', '2026',
         'Asistente con inteligencia artificial que cotiza importaciones de medicamentos; me encargué del agente, el servidor y la interfaz.'),
    ],
    'blandas': 'Liderazgo, comunicación, trabajo en equipo, aprendizaje rápido, resolución de problemas, responsabilidad.',
    'idiomas': 'Español: nativo. Inglés: A2. Portugués: A1.',
}
