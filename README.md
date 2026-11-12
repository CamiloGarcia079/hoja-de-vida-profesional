# Hoja de vida · Camilo García

Hoja de vida de **Camilo Andrés García Almeida**, Técnico en Desarrollo de Software e Inteligencia Artificial (CampusLands) y Junior Developer enfocado en automatización, bots y desarrollo web.

## Versiones

| Formato | Español | Inglés | Para qué sirve |
|---|---|---|---|
| **Campus** | [PDF](HojaDeVida_Campus_ES_CamiloGarcia.pdf) | [PDF](HojaDeVida_Campus_EN_CamiloGarcia.pdf) | Versión visual de una página, con foto y el formato de CampusLands. Para enviar directamente a una persona. |
| **ATS** | [PDF](HojaDeVida_ATS_ES_CamiloGarcia.pdf) | [PDF](HojaDeVida_ATS_EN_CamiloGarcia.pdf) | Una sola columna, sin imágenes ni tablas. Para plataformas de empleo que filtran hojas de vida de forma automática. |

También está el [certificado del Hackathon Visual Agents](Certificado_Hackathon_VisualAgents.pdf) (junio de 2026).

## Cómo se generan

Los PDF salen de [`fuente/`](fuente):

- `datos.py`: todo el contenido, en español e inglés.
- `generar.py`: arma un HTML por versión (Campus y ATS) y los imprime como PDF tamaño A4.
- `imprimir.js`: imprime los HTML con Chromium (Playwright).

Para actualizar la hoja de vida se edita `datos.py` y se ejecuta:

```bash
cd fuente
python3 generar.py
```
