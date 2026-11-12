# Hoja de vida · Camilo García

Hoja de vida de **Camilo Andrés García Almeida**, Técnico en Desarrollo de Software e Inteligencia Artificial (CampusLands) y Junior Developer enfocado en automatización, bots y desarrollo web.

## Versiones

| Formato | Archivo | Para qué sirve |
|---|---|---|
| **ATS** (español) | [HojaDeVida_ATS_CamiloGarcia.pdf](HojaDeVida_ATS_CamiloGarcia.pdf) | Una sola columna, solo texto y enlaces completos. Es la que leen bien las plataformas de empleo que filtran hojas de vida de forma automática. |
| **Campus** (español) | [HojaDeVida_Campus_ES_CamiloGarcia.pdf](HojaDeVida_Campus_ES_CamiloGarcia.pdf) | Formato oficial de CampusLands, de una página y con foto. |
| **Campus** (inglés) | [HojaDeVida_Campus_EN_CamiloGarcia.pdf](HojaDeVida_Campus_EN_CamiloGarcia.pdf) | La misma hoja Campus en inglés. |

Todos los enlaces dentro de los PDF se pueden hacer clic: LinkedIn, GitHub, portafolio y el repositorio de cada proyecto.

También está el [certificado del Hackathon Visual Agents](Certificado_Hackathon_VisualAgents.pdf) (junio de 2026).

## Cómo se generan

Los PDF salen de [`fuente/`](fuente):

- `datos.py`: todo el contenido, en español e inglés.
- `generar.py`: arma un HTML por versión (Campus en español e inglés, ATS en español) y los imprime como PDF tamaño A4.
- `imprimir.js`: imprime los HTML con Chromium (Playwright).

Para actualizar la hoja de vida se edita `datos.py` y se ejecuta:

```bash
cd fuente
python3 generar.py
```

Las fuentes de `fuente/fuentes/` (Libre Baskerville, Poppins y Noto Sans) son de Google Fonts, con licencia SIL Open Font License.
