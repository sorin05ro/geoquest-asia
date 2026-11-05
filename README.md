# GeoQuest – Expediția Asia 🦉🌏

Aplicație gamificată pentru **clasa a VII-a**: **Asia fizico-geografică**. Elevii învață prin joc toate întrebările din **Testul nr. 1** și **Testul nr. 2**. Itemii din cele două teste sunt **amestecați pe teme**, nu separați pe teste.

Aplicația este un modul al proiectului GeoQuest. Mascota este **Geo, bufnița-cartograf**.

**Deschide aplicația:** https://sorin05ro.github.io/geoquest-asia/

## Ce conține

- **Doar itemii din cele două teste: 28 de itemi** (14 poziții × 2 teste). Nu există întrebări inventate.
- **2 tărâmuri tematice cu 5 niveluri.** Fiecare nivel amestecă itemi din ambele teste:
  - *Poziție, relief și ape*: vecini, puncte extreme și țărmuri · relief și ape · harta Asiei;
  - *Climă, vegetație și faună*: zone, plante și animale · compară și explică.
- **Marea Expediție:** un test nou la fiecare încercare. Pentru fiecare item (A.a … E), aplicația alege la întâmplare varianta din Testul nr. 1 sau din Testul nr. 2. Punctajul este 90p + 10p din oficiu.
- **Hărțile originale din teste**, cu marcajele cerute încercuite.
- **4 fișe de recapitulare:** Poziție și țărmuri, Relieful, Apele, Climă, vegetație și faună.
- **Recompense:**
  - XP și 6 ranguri, de la Călător la Maestrul Asiei;
  - 14 insigne, serie zilnică de învățare și 1–3 stele pe nivel;
  - 30 de flashcard-uri cu repetiție spațiată (sistem Leitner), inclusiv fiecare marcaj de pe hărți;
  - greșelile revin la sfârșitul nivelului.
- **Mod Clasă** pentru tabla interactivă: 2–4 echipe și „Roata norocului” pe subiectele A–E.
- **Mod Profesor**, protejat cu PIN:
  - activarea sau dezactivarea itemilor;
  - greșelile frecvente;
  - export și import al progresului;
  - deblocarea expediției;
  - hărțile testelor, cu răspunsurile.
- **Funcționează offline** după prima deschidere și se poate instala pe telefon. Nu are conturi, cookie-uri sau reclame; elevul folosește doar o poreclă.

## Atlasul Asiei (localizare pe hartă)

Secțiunea **Atlasul Asiei** (`#/atlas`) folosește cele trei hărți din manual: hidrografia, poziția geografică și țărmurile, relieful. Denumirile tipărite pe hărți sunt **acoperite cu măști** în timpul jocului.

- **174 de elemente** în 3 regiuni-hartă și **20 de niveluri**, plus **Marele Atlas** (12 itemi amestecați din toate hărțile).
- **5 tipuri de exerciții:** Găsește pe hartă, Ce e aici?, Pune etichetele, Spre ce ocean curge?, Ce formă de relief este?
- **Explorează:** harta fără măști; atingi un loc și afli ce este acolo.
- **Stele:** 1★ de la 60%, 2★ de la 80%, 3★ de la 95%. XP, ranguri și seria zilnică sunt comune cu restul aplicației.
- **5 insigne noi:** Hidrograful Siberiei, Cuceritorul Himalayei, Inelul de Foc, Cele patru vânturi, Cartograful.
- Elementele greșite intră în **flashcard-uri** (Leitner), cu decupajul de hartă.
- **Harta interactivă:** zoom cu două degete sau cu butoanele, atingere confirmată prin „Verifică”. Elevii care nu pot atinge precis pot alege dintre marcaje numerotate.
- **Modul Profesor → Calibrare Atlas:**
  - mutarea zonelor de răspuns și desenarea măștilor;
  - bifarea elementelor verificate;
  - activarea sau dezactivarea elementelor;
  - export și import `atlas.json`.

Coordonatele au fost puse aproximativ, după hărți, și sunt marcate `"verificat": false` până la calibrare.

| Fișier | Conținut |
|---|---|
| `tools/genereaza_atlas.py` | Elementele, zonele și măștile (în pixeli), nivelurile și insignele Atlasului. Generează `data/atlas.json` |
| `data/atlas.json` | Datele Atlasului, cu coordonate fracționare (0–1) |
| `assets/atlas/` | Cele trei hărți (WebP + JPG) |
| `js/atlas.js`, `js/harta-interactiva.js`, `js/atlas-geo.js`, `js/atlas-calibrare.js` | Ecranele, harta cu zoom, geometria, editorul de calibrare |

## Cum se folosește la clasă

1. Pe tablă, deschide **Setări → Mod proiecție**.
2. Alege **Mod Clasă**, setează echipele și sursa întrebărilor: toți itemii, un tărâm sau Roata norocului.
3. Pentru teme, elevii deschid aceeași adresă pe telefon.

## Cum se modifică itemii

Itemii, fișele, tărâmurile și punctajele se află în `tools/genereaza.py`. După o modificare:

```bash
python3 tools/genereaza.py        # regenerează data/*.json
python3 -m http.server 8765
node tests/ruleaza.mjs            # are nevoie de Playwright
```

| Fișier | Conținut |
|---|---|
| `data/intrebari_teste.json` | Cei 28 de itemi. Câmpul `slot` (de exemplu `B-3`) dă poziția în test, `test` arată testul de proveniență, `nivel` arată nivelul |
| `data/lectii.json` | Tărâmurile, nivelurile, structura testului (A–E) și fișele |
| `data/harta.json` | Cele două hărți și poziția fiecărui marcaj (în pixeli) |
| `data/insigne.json` | Insignele |

Testele automate verifică:
- dacă fiecare nivel conține itemi din ambele teste;
- dacă răspunsul corect primește punctaj maxim, iar cel greșit 0;
- dacă testul amestecat dă mereu 100p (90 + 10 din oficiu);
- dacă ecranele nu au scroll orizontal la 375, 768 și 1920 px.

## Meta-prompt

`META_PROMPT.md` descrie complet aplicația și poate fi refolosit pentru alte teste.

## Autor și licență

**Autor:** prof. Negraru Sorin Norocel, Școala Gimnazială Nr. 6, Râmnicu Sărat.

**Licență:**
- conținutul educațional: [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/);
- codul: MIT (vezi `LICENSE`).
