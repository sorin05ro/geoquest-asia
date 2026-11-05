// Modul Profesor (PIN local): banca de întrebări, greșeli frecvente, export/import, hărțile cu răspunsuri.
import { incarca, salveaza, exporta, importa, reseteaza } from './storage.js';
import { h, geoSpune, toast, modal } from './ui.js';
import * as E from './engine.js';
import { creeaza, NUME_TIP } from './exercises.js';
import { harta } from './harta.js';
import { tabCalibrare } from './atlas-calibrare.js';

let deblocat = false;
const hashPin = async (p) => {
  try { const b = await crypto.subtle.digest('SHA-256', new TextEncoder().encode('gq-asia:' + p)); return [...new Uint8Array(b)].map(x => x.toString(16).padStart(2, '0')).join(''); }
  catch (e) { return 'p:' + p; }
};

export function ecranProfesor(app) {
  const s = incarca();
  app.append(h('nav', { class: 'pesmet' }, h('a', { href: '#/' }, '← Acasă')), h('h1', { class: 'titlu-sectiune' }, '🔐 Modul Profesor'));
  if (!deblocat) {
    const inp = h('input', { class: 'camp', type: 'password', inputmode: 'numeric', maxlength: 8, 'aria-label': 'PIN', autocomplete: 'off' });
    const nou = !s.pin;
    app.append(h('section', { class: 'card' },
      h('p', {}, nou ? 'Setează un PIN (4–8 cifre). Se păstrează doar pe acest dispozitiv.' : 'Introdu PIN-ul profesorului.'),
      h('label', { class: 'eticheta' }, 'PIN', inp),
      h('div', { class: 'rand-butoane' }, h('button', { class: 'btn', onclick: async () => {
        const v = inp.value.trim(); if (!/^\d{4,8}$/.test(v)) { toast('PIN-ul are 4–8 cifre.'); return; }
        const hp = await hashPin(v);
        if (nou) { s.pin = hp; salveaza(); deblocat = true; toast('PIN salvat.', 'ok'); }
        else if (hp === s.pin) deblocat = true; else { toast('PIN greșit.'); return; }
        app.replaceChildren(); ecranProfesor(app);
      } }, nou ? 'Setează PIN' : 'Intră'))));
    setTimeout(() => inp.focus(), 0);
    return;
  }
  const taburi = [['intrebari', '📚 Întrebări'], ['greseli', '📉 Greșeli frecvente'], ['date', '💾 Date și progres'], ['harti', '🗺️ Hărțile testelor'], ['atlas', '📍 Calibrare Atlas']];
  const zona = h('div'); let activ = 'intrebari';
  const bar = h('div', { class: 'taburi', role: 'tablist' }, taburi.map(([id, t]) => h('button', { role: 'tab', 'aria-selected': String(id === activ), onclick: (e) => { activ = id; bar.querySelectorAll('button').forEach(b => b.setAttribute('aria-selected', String(b === e.currentTarget))); desen(); } }, t)));
  app.append(bar, zona);
  const desen = () => zona.replaceChildren(({ intrebari: tabIntrebari, greseli: tabGreseli, date: tabDate, harti: tabHarti, atlas: tabCalibrare })[activ]());
  desen();
}

function tabIntrebari() {
  const s = incarca(); const dz = new Set(s.dezactivate);
  let filtru = '', taram = '';
  const lista = h('div', { class: 'lista-prof' });
  const toate = E.toateIntrebarile();
  const desen = () => {
    const f = toate.filter(q => (!taram || q.taram === taram || 'T' + q.test === taram) && (!filtru || JSON.stringify(q).toLowerCase().includes(filtru)));
    lista.replaceChildren(h('p', { class: 'mic' }, `${f.length} întrebări afișate · ${toate.length - dz.size} active din ${toate.length}`),
      ...f.map(q => h('div', { class: 'rand-prof' + (dz.has(q.id) ? ' inactiv' : '') },
        h('label', {}, h('input', { type: 'checkbox', checked: !dz.has(q.id), 'aria-label': 'Activă', onchange: (e) => { if (e.target.checked) dz.delete(q.id); else dz.add(q.id); s.dezactivate = [...dz]; salveaza(); e.target.closest('.rand-prof').classList.toggle('inactiv', !e.target.checked); } })),
        h('span', { class: 'id' }, q.id), h('span', { class: 'tip' }, NUME_TIP[q.tip]),
        h('span', { class: 'txt' }, q.enunt), h('button', { class: 'mini', onclick: () => modal(h('div', {}, h('h3', {}, q.enunt), creeaza(q, {}).solutie(), h('p', { class: 'mic' }, 'Sursa: ', q.sursa), h('p', { class: 'mic' }, 'Nivel: ', q.nivel, ' · Testul nr. ', q.test, ', itemul ', q.slot, ' · ', q.puncte, 'p')), { titlu: q.id }) }, 'Vezi'))));
  };
  desen();
  return h('section', { class: 'card' },
    h('div', { class: 'filtre' }, h('input', { class: 'camp', placeholder: 'Caută…', 'aria-label': 'Caută', oninput: (e) => { filtru = e.target.value.toLowerCase(); desen(); } }),
      h('select', { class: 'camp', 'aria-label': 'Tărâm', onchange: (e) => { taram = e.target.value; desen(); } }, h('option', { value: '' }, 'Toți itemii'), E.D.taramuri.map(t => h('option', { value: t.id }, t.nume)), h('option', { value: 'T1' }, 'Doar Testul nr. 1'), h('option', { value: 'T2' }, 'Doar Testul nr. 2'))),
    lista);
}

function tabGreseli() {
  const s = incarca(); const top = Object.entries(s.istoricGreseli).sort((a, b) => b[1] - a[1]).slice(0, 15);
  const toate = E.toateIntrebarile();
  return h('section', { class: 'card' }, geoSpune('Greșelile înregistrate pe acest dispozitiv (de exemplu, tabla din clasă).', 'gandeste'),
    atlasGreseli(),
    top.length ? h('ol', { class: 'lista-greseli' }, top.map(([id, n]) => { const q = toate.find(x => x.id === id); return h('li', {}, h('strong', {}, `${n}×`), ' ', q ? q.enunt : id, h('small', {}, ` (${id})`)); })) : h('p', {}, 'Încă nu există greșeli înregistrate.'));
}

function descarca(nume, text) {
  const a = h('a', { href: URL.createObjectURL(new Blob([text], { type: 'application/json' })), download: nume }); document.body.append(a); a.click(); setTimeout(() => { URL.revokeObjectURL(a.href); a.remove(); }, 500);
}
function tabDate() {
  const s = incarca();
  const fis = h('input', { type: 'file', accept: 'application/json,.json', 'aria-label': 'Fișier de progres', onchange: async (e) => {
    const f = e.target.files[0]; if (!f) return;
    try { importa(await f.text()); toast('Progres importat.', 'ok'); } catch (err) { toast(err.message || 'Fișier invalid.'); }
  } });
  return h('section', { class: 'card setari' },
    h('label', { class: 'comutator' }, h('input', { type: 'checkbox', checked: !!s.bossDeblocat, onchange: (e) => { s.bossDeblocat = e.target.checked; salveaza(); } }), h('span', {}, h('strong', {}, 'Deblochează Marea Expediție'), h('small', {}, 'Elevii pot da testul amestecat fără să fi strâns 60% din stele.'))),
    h('div', { class: 'rand-butoane stanga' },
      h('button', { class: 'btn sec', onclick: () => descarca(`progres-${s.porecla || 'elev'}.json`, exporta()) }, '⬇ Exportă progresul'),
      h('label', { class: 'btn sec' }, '⬆ Importă progresul', fis),
      h('button', { class: 'btn sec', onclick: () => descarca('intrebari-geoquest-asia.json', JSON.stringify({ teste: E.D.teste, extra: E.D.extra }, null, 1)) }, '⬇ Exportă banca de întrebări')),
    h('p', { class: 'mic' }, 'Pentru a modifica întrebările permanent: editează tools/genereaza.py și rulează-l (sau direct data/intrebari_teste.json) în repository – vezi README.'),
    h('div', { class: 'rand-butoane stanga' }, h('button', { class: 'btn pericol', onclick: () => { if (confirm('Ștergi tot progresul de pe acest dispozitiv? (PIN-ul rămâne)')) { reseteaza(true); toast('Progres resetat.', 'ok'); location.hash = '#/'; } } }, '🗑 Resetează progresul')));
}

function tabHarti() {
  const hartaItemi = E.D.teste.filter(q => q.tip === 'harta_test');
  return h('section', { class: 'card' },
    geoSpune('Hărțile din cele două teste, cu răspunsurile. Marcajele încercuite corespund cifrelor și literelor tipărite pe hartă.', 'gandeste'),
    h('div', { class: 'harti-prof' }, ['t1', 't2'].map(id => {
      const it = hartaItemi.filter(q => q.harta === id).flatMap(q => q.itemi);
      return h('div', {}, h('h3', {}, `Testul nr. ${E.D.harta.harti[id].test}`), harta({ id, marcaje: it.map(x => x.eticheta) }),
        h('ul', { class: 'sol' }, it.map(x => h('li', {}, h('strong', {}, x.eticheta), ' – ', x.corect))));
    })));
}

function atlasGreseli() {
  const g = Object.entries(incarca().atlas?.greseli || {}).sort((a, b) => b[1] - a[1]).slice(0, 15);
  if (!g.length) return null;
  return h('div', {}, h('h3', {}, 'Atlasul Asiei – cele mai greșite elemente'),
    h('ol', { class: 'lista-greseli' }, g.map(([id, n]) => { const e = E.D.atlas.elemente.find(x => x.id === id); return h('li', {}, h('strong', {}, `${n}×`), ' ', e ? e.nume : id, h('small', {}, e ? ` (${E.D.atlas.harti[e.harta].nume})` : '')); })),
    h('h3', {}, 'Itemii din teste'));
}
