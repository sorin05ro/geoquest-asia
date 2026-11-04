// Hărțile din teste: imaginea originală (cu cifrele și literele tipărite) + un strat SVG care încercuiește marcajele cerute.
import { D } from './engine.js';
import { h } from './ui.js';

const NS = 'http://www.w3.org/2000/svg';

/**
 * @param {object} o
 *  - id: 't1' | 't2' (harta din Testul nr. 1 sau nr. 2)
 *  - marcaje: ['1','2','A'] marcajele încercuite
 *  - activ: marcajul evidențiat mai puternic (de ex. pe un flashcard)
 */
export function harta({ id = 't1', marcaje = [], activ = null, clasa = '', zoom = null } = {}) {
  const H = D.harta.harti[id];
  if (zoom) return decupaj(H, zoom, clasa);
  const cutie = h('div', { class: `harta ${clasa}` });
  const img = h('picture', {},
    h('source', { srcset: H.imagine, type: 'image/webp' }),
    h('img', { src: H.imagine_png, alt: `Harta Asiei din Testul nr. ${H.test}, cu marcajele ${Object.keys(H.marcaje).join(', ')}`, width: H.latime, height: H.inaltime, draggable: 'false', loading: 'lazy' }));
  const svg = document.createElementNS(NS, 'svg');
  svg.setAttribute('viewBox', `0 0 ${H.latime} ${H.inaltime}`);
  svg.setAttribute('class', 'harta-strat');
  svg.setAttribute('aria-hidden', 'true');
  for (const m of marcaje) {
    const p = H.marcaje[m]; if (!p) continue;
    const c = document.createElementNS(NS, 'circle');
    c.setAttribute('cx', p[0]); c.setAttribute('cy', p[1]); c.setAttribute('r', activ === m ? 40 : 34);
    c.setAttribute('class', 'inel' + (activ === m ? ' activ' : '')); c.dataset.m = m;
    svg.append(c);
  }
  cutie.append(img, svg);
  cutie.marcheaza = (m, cls) => svg.querySelector(`circle[data-m="${m}"]`)?.classList.add(cls);
  cutie.svg = svg;
  return cutie;
}

/** decupaj din hartă în jurul unui marcaj (pentru flashcard-uri) */
function decupaj(H, m, clasa) {
  const [x, y] = H.marcaje[m]; const L = 560, I = 420;
  const x0 = Math.max(0, Math.min(H.latime - L, x - L / 2)), y0 = Math.max(0, Math.min(H.inaltime - I, y - I / 2));
  const svg = document.createElementNS(NS, 'svg');
  svg.setAttribute('viewBox', `${x0} ${y0} ${L} ${I}`); svg.setAttribute('class', 'decupaj');
  svg.setAttribute('role', 'img'); svg.setAttribute('aria-label', `Fragment din harta Testului nr. ${H.test}, marcajul ${m}`);
  const im = document.createElementNS(NS, 'image');
  im.setAttribute('href', H.imagine_png); im.setAttribute('width', H.latime); im.setAttribute('height', H.inaltime);
  const c = document.createElementNS(NS, 'circle');
  c.setAttribute('cx', x); c.setAttribute('cy', y); c.setAttribute('r', 40); c.setAttribute('class', 'inel activ');
  svg.append(im, c);
  return h('div', { class: `harta decupat ${clasa}` }, svg);
}
