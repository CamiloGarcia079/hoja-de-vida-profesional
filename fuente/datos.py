"""Datos de la hoja de vida en español (es) e inglés (en).
Todo lo que aparece en los PDF sale de aquí: para actualizar la hoja de vida se edita este archivo.
"""

CONTACTO = {
    'telefono': '+57 304 396 2022',
    'correo': 'kaliko2411@gmail.com',
    'linkedin': 'linkedin.com/in/camilo-garcia-7570693b7',
    'github': 'github.com/CamiloGarcia079',
    'portafolio': 'camilogarcia079.github.io/portafolio',
}

DATOS = {
    'es': {
        'nombre': ['Camilo Andrés', 'García Almeida'],
        'cargo': 'Junior Developer · Automatización, bots y desarrollo web',
        'titulo_corto': 'Técnico en Desarrollo de Software e Inteligencia Artificial',
        'ciudad': 'Bucaramanga, Colombia',
        'secciones': {
            'perfil': 'Perfil', 'formacion': 'Formación', 'experiencia': 'Proyectos y experiencia',
            'habilidades': 'Habilidades técnicas', 'competencias': 'Competencias', 'contacto': 'Datos personales',
            'idiomas': 'Idiomas', 'logros': 'Logros y certificaciones',
        },
        'perfil': ('Técnico en Desarrollo de Software e Inteligencia Artificial, formado durante un año intensivo en '
                   'CampusLands. Construyo APIs REST con Java y Spring Boot protegidas con JWT, automatizaciones con n8n '
                   'y asistentes con inteligencia artificial en Python y TypeScript. He trabajado en equipo con '
                   'metodologías ágiles, coordiné la integración de un equipo en un hackathon de IA y entrego proyectos '
                   'con pruebas automatizadas y documentación. En diciembre de 2026 inicio mi etapa productiva en Globant.'),
        'formacion': [
            ('Técnico en Desarrollo de Software e Inteligencia Artificial', 'CampusLands · Floridablanca', 'Dic 2025 – Nov 2026'),
            ('Bachiller Académico', 'Fundación Colegio UIS', 'Nov 2025'),
        ],
        'experiencia': [
            ('Etapa productiva · Globant', 'Desarrollador en práctica', 'Desde dic 2026',
             ['Práctica profesional como desarrollador en una empresa global de tecnología.']),
            ('Renta de Herramientas — Plataforma de alquiler', 'Java 21 · Spring Boot · Spring Security · JWT · MySQL · Docker', '2026',
             ['API REST con roles de administrador, proveedor y cliente: reservas por fechas, pagos con IVA, devoluciones con mora y reporte de daños.',
              '113 pruebas automatizadas, documentación con Swagger y Postman, y arranque con un solo comando o con Docker.']),
            ('VitalRoute — Triaje y despacho médico en tiempo real', 'TypeScript · Node.js · Express · Socket.IO · React · MySQL', '2026',
             ['Proyecto en pareja. Desarrollé el servidor, la comunicación en tiempo real por canales, el panel con mapa y un agente de IA con herramienta de despacho.']),
            ('DeliveryBot — Bot de pedidos en Telegram', 'n8n · JavaScript · Telegram Bot API · Google Sheets', '2026',
             ['Automatización de 39 pasos que toma pedidos, calcula el total, avisa a cocina y al cliente, y guarda todo en Google Sheets.']),
            ('MindConnect API — Plataforma de salud mental', 'Java 21 · Spring Boot · PostgreSQL · Flyway · JWT', '2026',
             ['Arquitectura hexagonal con 52 tablas, migraciones versionadas y más de 600 pruebas automatizadas.']),
        ],
        'habilidades': ['Java · Spring Boot', 'Python · LangChain', 'TypeScript · Node.js', 'JavaScript · React',
                        'SQL · MySQL · PostgreSQL', 'n8n · automatización', 'Docker · Git · GitHub', 'JUnit · pytest · Postman'],
        'competencias': ['Liderazgo', 'Comunicación', 'Trabajo en equipo', 'Aprendizaje rápido', 'Resolución de problemas', 'Responsabilidad'],
        'idiomas': [('Español', 'Nativo'), ('Inglés', 'A2'), ('Portugués', 'A1')],
        'logros': [
            ('Hackathon Visual Agents — Certificado de participación', 'Campuslands · Voxel51 · UPB · Cámara de Comercio de Bucaramanga', 'Jun 2026',
             'Rol de integración, contratos entre módulos y presentación del proyecto GUARDIAN (visión por computadora y Gemini).'),
            ('Reto Agente 2026 — Platica.mx con CampusLands', 'Aduana-Copilot', '2026',
             'Asistente con IA que cotiza importaciones de medicamentos; me encargué del agente, el servidor intermedio y la interfaz.'),
        ],
        'etq': {'telefono': 'Teléfono', 'correo': 'Correo', 'linkedin': 'LinkedIn', 'github': 'GitHub', 'portafolio': 'Portafolio', 'ciudad': 'Ciudad'},
    },
    'en': {
        'nombre': ['Camilo Andrés', 'García Almeida'],
        'cargo': 'Junior Developer · Automation, bots and web development',
        'titulo_corto': 'Software Development and Artificial Intelligence Technician',
        'ciudad': 'Bucaramanga, Colombia',
        'secciones': {
            'perfil': 'Profile', 'formacion': 'Education', 'experiencia': 'Projects and experience',
            'habilidades': 'Technical skills', 'competencias': 'Soft skills', 'contacto': 'Contact',
            'idiomas': 'Languages', 'logros': 'Achievements and certificates',
        },
        'perfil': ('Software Development and Artificial Intelligence Technician, trained for one intensive year at '
                   'CampusLands. I build REST APIs with Java and Spring Boot secured with JWT, automations with n8n and '
                   'AI assistants in Python and TypeScript. I have worked in teams using agile methods, coordinated a '
                   'team’s integration at an AI hackathon and deliver projects with automated tests and documentation. '
                   'In December 2026 I start my professional internship at Globant.'),
        'formacion': [
            ('Software Development and Artificial Intelligence Technician', 'CampusLands · Floridablanca, Colombia', 'Dec 2025 – Nov 2026'),
            ('High School Diploma', 'Fundación Colegio UIS', 'Nov 2025'),
        ],
        'experiencia': [
            ('Professional internship · Globant', 'Developer intern', 'From Dec 2026',
             ['Professional internship as a developer at a global technology company.']),
            ('Tool Rental Platform', 'Java 21 · Spring Boot · Spring Security · JWT · MySQL · Docker', '2026',
             ['REST API with admin, provider and customer roles: date bookings, payments with VAT, returns with late fees and damage reports.',
              '113 automated tests, Swagger and Postman documentation, and one-command or Docker startup.']),
            ('VitalRoute — Real-time medical triage and dispatch', 'TypeScript · Node.js · Express · Socket.IO · React · MySQL', '2026',
             ['Pair project. I built the server, real-time communication channels, the map dashboard and an AI agent with a dispatch tool.']),
            ('DeliveryBot — Telegram ordering bot', 'n8n · JavaScript · Telegram Bot API · Google Sheets', '2026',
             ['39-step automation that takes orders, calculates totals, notifies kitchen and customer, and stores everything in Google Sheets.']),
            ('MindConnect API — Mental health platform', 'Java 21 · Spring Boot · PostgreSQL · Flyway · JWT', '2026',
             ['Hexagonal architecture with 52 tables, versioned migrations and 600+ automated tests.']),
        ],
        'habilidades': ['Java · Spring Boot', 'Python · LangChain', 'TypeScript · Node.js', 'JavaScript · React',
                        'SQL · MySQL · PostgreSQL', 'n8n · automation', 'Docker · Git · GitHub', 'JUnit · pytest · Postman'],
        'competencias': ['Leadership', 'Communication', 'Teamwork', 'Fast learner', 'Problem solving', 'Ownership'],
        'idiomas': [('Spanish', 'Native'), ('English', 'A2'), ('Portuguese', 'A1')],
        'logros': [
            ('Visual Agents Hackathon — Certificate of participation', 'Campuslands · Voxel51 · UPB · Bucaramanga Chamber of Commerce', 'Jun 2026',
             'Integration, module contracts and presentation role in the GUARDIAN project (computer vision and Gemini).'),
            ('Agent Challenge 2026 — Platica.mx with CampusLands', 'Aduana-Copilot', '2026',
             'AI assistant that quotes medicine imports; I built the agent, the gateway server and the interface.'),
        ],
        'etq': {'telefono': 'Phone', 'correo': 'Email', 'linkedin': 'LinkedIn', 'github': 'GitHub', 'portafolio': 'Portfolio', 'ciudad': 'City'},
    },
}
