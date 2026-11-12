// Imprime cada HTML de salida/ como PDF A4 con Chromium (Playwright).
// Uso: node imprimir.js carpeta_html carpeta_pdf nombre1 nombre2 ...
const { chromium } = require('playwright');
const path = require('path');

(async () => {
  const [entrada, salida, ...nombres] = process.argv.slice(2);
  const navegador = await chromium.launch();
  const pagina = await navegador.newPage();
  for (const n of nombres) {
    await pagina.goto('file://' + path.join(entrada, n + '.html'));
    await pagina.waitForLoadState('networkidle');
    await pagina.pdf({ path: path.join(salida, n + '.pdf'), format: 'A4', printBackground: true, preferCSSPageSize: true });
    console.log('PDF:', n);
  }
  await navegador.close();
})();
