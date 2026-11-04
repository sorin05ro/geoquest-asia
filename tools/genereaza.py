# Generează fișierele din data/ pentru GeoQuest – Expediția Asia (clasa a VII-a).
# Sursa: Testul nr. 1 și Testul nr. 2 „Asia fizico-geografică” ale prof. Negraru Sorin Norocel.
# Rulare (din rădăcina proiectului):  python3 tools/genereaza.py
import json, os
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data')

# ================================================================ FIȘELE DE RECAPITULARE
LECTII_INDEX = [
    {"id": "pozitie", "nume": "Poziție, limite și țărmuri", "icon": "🧭", "culoare": "#1e4f80"},
    {"id": "relief", "nume": "Relieful", "icon": "🏔️", "culoare": "#94532a"},
    {"id": "ape", "nume": "Apele", "icon": "🌊", "culoare": "#0f766e"},
    {"id": "clima", "nume": "Climă, vegetație și faună", "icon": "🌿", "culoare": "#2d7a3e"},
]
L = {
 "pozitie": [
  ("Poziția Asiei", [
   "Asia este cel mai mare continent: circa 44 de milioane de km², aproape o treime din uscatul planetei.",
   "Se află în emisfera nordică și, cea mai mare parte, în emisfera estică.",
   "Este unită cu Europa: împreună formează Eurasia."]),
  ("Limite și vecini", [
   "Nord: Oceanul Arctic.",
   "Est: Oceanul Pacific. Strâmtoarea Bering o desparte de America de Nord.",
   "Sud: Oceanul Indian.",
   "Vest: Europa. Limita trece prin Munții Ural, râul Ural, Marea Caspică, Munții Caucaz, Marea Neagră și strâmtorile Bosfor și Dardanele.",
   "Sud-vest: Africa, prin Istmul Suez și Marea Roșie.",
   "Atenție: Munții Himalaya NU sunt limita dintre Europa și Asia. Limita este dată de Munții Ural."]),
  ("Punctele extreme", [
   "Nord: Capul Celiuskin (Peninsula Taimîr).",
   "Est: Capul Dejnev (Peninsula Ciukotka), la Strâmtoarea Bering.",
   "Sud: Capul Piai (Peninsula Malacca).",
   "Vest: Capul Baba (Peninsula Asia Mică).",
   "Capul Roca nu aparține Asiei: este punctul extrem vestic al Europei (Portugalia)."]),
  ("Peninsule", [
   "Vest: Peninsula Asia Mică.",
   "Sud-vest: Peninsula Arabia, cea mai mare peninsulă de pe Glob.",
   "Sud: Peninsula India.",
   "Sud-est: peninsulele Indochina și Malacca. Peninsula Malacca NU se află în vestul Asiei.",
   "Est: peninsulele Coreea, Kamciatka și Ciukotka. Nord: Peninsula Taimîr."]),
  ("Insule, arhipelaguri și golfuri", [
   "Insula Borneo (Kalimantan) este cea mai mare insulă a Asiei. Alte insule: Sumatera, Java, Sri Lanka.",
   "Arhipelaguri: Arhipelagul Japonez (în est, în Oceanul Pacific), Arhipelagul Filipine, Arhipelagul Indoneziei.",
   "Golful Bengal, între Peninsula India și Peninsula Indochina, este cel mai mare golf de pe Glob.",
   "Alte golfuri și mări: Golful Persic, Marea Arabiei, Marea Chinei de Sud, Marea Japoniei."]),
 ],
 "relief": [
  ("Munții", [
   "Munții Himalaya sunt cei mai înalți munți ai Asiei și ai Globului. Vârful Everest (Chomolungma) are 8 848 m.",
   "Alți munți: Karakorum (Vf. K2, 8 611 m), Hindukuș, Tian Shan, Altai, Caucaz.",
   "Munții Ural sunt munți vechi, mai joși, și marchează limita dintre Europa și Asia."]),
  ("Podișurile", [
   "Podișul Tibet este cel mai înalt și cel mai întins podiș înalt de pe Glob (4 000–5 000 m).",
   "Pamirul este numit „Acoperișul lumii”: un nod de munți și podișuri înalte, de peste 4 000 m.",
   "Dintre variantele Dekan, Pamir, Iranian și Arabiei, cel mai înalt este Pamirul. Dintre Dekan, Tibet, Iranian și Arabiei, cel mai înalt este Tibetul.",
   "Alte podișuri: Podișul Iranian, Podișul Arabiei, Podișul Dekan (în Peninsula India), Podișul Siberiei Centrale."]),
  ("Câmpiile și depresiunile", [
   "Câmpia Siberiei de Vest, străbătută de râul Obi.",
   "Câmpia Indo-Gangetică, străbătută de râurile Indus și Gange (și Brahmaputra).",
   "Marea Câmpie Chineză, străbătută de Huang He și Yangtze.",
   "Câmpia Mesopotamiei, străbătută de Tigru și Eufrat.",
   "Depresiunea Mării Moarte este cel mai coborât punct de pe uscat (circa –430 m)."]),
 ],
 "ape": [
  ("Râurile Oceanului Arctic", [
   "Obi, Enisei și Lena curg spre nord, prin Siberia, și se varsă în Oceanul Arctic.",
   "Enisei primește apele lacului Baikal prin râul Angara.",
   "Lena izvorăște lângă lacul Baikal și formează o deltă la vărsare.",
   "Iarna îngheață. Primăvara, gheața se topește mai întâi în sud, iar apa produce inundații."]),
  ("Râurile Oceanului Pacific", [
   "Amur, Huang He, Yangtze (Chang Jiang) și Mekong.",
   "Huang He (Fluviul Galben) are apa colorată de loessul pe care îl transportă; formează o mare buclă în nordul Chinei.",
   "Yangtze este cel mai lung fluviu al Asiei (circa 6 300 km)."]),
  ("Râurile Oceanului Indian", [
   "Indus izvorăște din Tibet și se varsă în Marea Arabiei.",
   "Gange izvorăște din Himalaya și se varsă în Golful Bengal.",
   "Indus și Gange străbat Câmpia Indo-Gangetică.",
   "Tigru și Eufrat se varsă în Golful Persic."]),
  ("Lacurile", [
   "Marea Caspică este cel mai mare lac de pe Glob.",
   "Lacul Baikal este cel mai adânc lac de pe Glob (1 642 m) și păstrează cea mai mare cantitate de apă dulce dintr-un lac. Nu este cel mai sărat lac.",
   "Marea Moartă este unul dintre cele mai sărate lacuri de pe Glob.",
   "Lacul Aral se află la est de Marea Caspică și și-a micșorat mult suprafața.",
   "Lacul Balhaș este un lac alungit, în formă de semilună, la est de Aral."]),
 ],
 "clima": [
  ("Zonele climatice", [
   "De la nord la sud, Asia are climat subpolar, temperat, subtropical, tropical (uscat și umed) și ecuatorial. În munții înalți este climat montan.",
   "Fiecare zonă climatică are propria zonă de vegetație și propriile animale."]),
  ("Zona subpolară – tundra", [
   "Localizare: în nordul Asiei, de-a lungul țărmului Oceanului Arctic (nordul Siberiei).",
   "Temperaturi scăzute: ierni lungi și geroase, veri scurte și răcoroase (sub 10°C).",
   "Precipitații reduse (200–300 mm/an), mai ales sub formă de zăpadă. Vânturi polare, reci.",
   "Vegetația de tundră este scundă: mușchi, licheni și arbuști pitici. Tundra NU are vegetație ierboasă înaltă.",
   "Vegetația e scundă pentru că vara este scurtă și rece, solul este înghețat în adâncime (permafrost) și bat vânturi puternice și reci.",
   "Animale: renul, vulpea polară, lemingul."]),
  ("Zona temperată – taiga și stepa", [
   "Taiga este pădurea de conifere: pin, brad, molid, zadă. Mușchii, lichenii și arbuștii pitici sunt specifici tundrei, nu taigăi.",
   "Animale în taiga: ursul brun, lupul, râsul, samurul. Ursul brun trăiește în climatul temperat.",
   "Stepa are vegetație ierboasă."]),
  ("Zona tropical-uscată – deșerturile", [
   "Localizare: în sud-vestul Asiei – Peninsula Arabia, Podișul Iranian, deșertul Thar.",
   "Temperaturi foarte ridicate vara (peste 40°C ziua), cu diferențe mari între zi și noapte.",
   "Precipitații foarte reduse (sub 200 mm/an). Vânturi: alizee uscate și vânturi fierbinți de deșert (samum).",
   "Vegetație rară, adaptată secetei. Animal tipic: cămila."]),
  ("Zona tropical-umedă – climatul musonic", [
   "Localizare: în sudul și sud-estul Asiei – peninsulele India și Indochina, sud-estul Chinei.",
   "Temperaturi ridicate tot anul (peste 20°C).",
   "Precipitații bogate, căzute mai ales vara, în sezonul musonic. La Cherrapunji (India) se înregistrează cele mai mari cantități.",
   "Vânturi: musonii. Vara bat dinspre ocean (umed), iarna dinspre uscat (uscat).",
   "Vegetație: păduri musonice, junglă, savane. Animale: tigrul, elefantul indian."]),
  ("Zona ecuatorială", [
   "Localizare: în jurul Ecuatorului – în sudul Peninsulei Malacca și în Indonezia.",
   "Temperaturi ridicate și constante tot anul (medii de 25–28°C), fără anotimpuri.",
   "Precipitații foarte bogate (peste 2 000 mm/an), aproape zilnic, sub formă de averse.",
   "Vânturi: calm ecuatorial – aerul cald și umed urcă (mișcări ascendente).",
   "Vegetația este abundentă pentru că este cald și umed tot anul, iar plantele cresc continuu: pădurea ecuatorială este deasă, etajată și mereu verde. Animal tipic: urangutanul."]),
 ],
}
SURSA = {}  # (lectie, index fișă) -> text scurt pentru „Din lecție”

# ================================================================ TĂRÂMURI ȘI NIVELURI (itemi amestecați din ambele teste)
TARAMURI = [
 {"id": "t1", "nume": "Poziție, relief și ape", "icon": "🏔️", "culoare": "#1e4f80", "niveluri": [
   {"id": "n1", "titlu": "Vecini, puncte extreme și țărmuri"},
   {"id": "n2", "titlu": "Relief și ape"},
   {"id": "n3", "titlu": "Harta Asiei"}]},
 {"id": "t2", "nume": "Climă, vegetație și faună", "icon": "🌿", "culoare": "#2d7a3e", "niveluri": [
   {"id": "n4", "titlu": "Zone climatice, plante și animale"},
   {"id": "n5", "titlu": "Compară și explică"}]},
]
TARAM_NIVEL = {n["id"]: t["id"] for t in TARAMURI for n in t["niveluri"]}

# structura testului (folosită de Marea Expediție)
STRUCTURA = [
 {"subiect": "A", "cerinta": "Analizând harta alăturată, precizați elementele marcate.", "sloturi": ["A-a", "A-b"]},
 {"subiect": "B", "cerinta": "Încercuiți litera corespunzătoare răspunsului corect.", "sloturi": ["B-1", "B-2", "B-3", "B-4", "B-5"]},
 {"subiect": "C", "cerinta": "Pentru afirmațiile de mai jos specificați dacă acestea sunt adevărate sau false.", "sloturi": ["C-1", "C-2", "C-3", "C-4", "C-5"]},
 {"subiect": "D", "cerinta": "Comparați din punct de vedere climatic cele două zone (localizare, temperaturi, precipitații, vânturi).", "sloturi": ["D"]},
 {"subiect": "E", "cerinta": "Explicați fenomenul cerut.", "sloturi": ["E"]},
]

# ================================================================ ITEMII DIN TESTE
Q = []
def item(test, slot, nivel, tip, puncte, enunt, lectie, expl, sursa, **kw):
    sub = slot.split('-')[0]
    d = {"id": f"T{test}-{slot}", "test": test, "subiect": sub, "slot": slot, "puncte": puncte, "tip": tip,
         "taram": TARAM_NIVEL[nivel], "nivel": nivel, "enunt": enunt, "origine": "test",
         "explicatie_geo": expl, "sursa": sursa, "lectie": lectie, "dificultate": 2}
    d.update(kw); Q.append(d)

# ---------- Subiectul A – harta (a = 3 × 4p, b = 2 × 4p)
HIDRO = ["Enisei", "Indus", "Lacul Aral", "Huang He", "Lena", "Lacul Balhaș", "Obi", "Gange", "Amur", "Lacul Baikal", "Yangtze", "Marea Caspică"]
TARM = ["Peninsula India", "Insula Borneo (Kalimantan)", "Golful Bengal", "Arhipelagul Japonez", "Peninsula Arabia", "Peninsula Indochina",
        "Peninsula Malacca", "Insula Sri Lanka", "Golful Persic", "Arhipelagul Filipine"]
item(1, "A-a", "n3", "harta_test", 12, "Analizând harta, precizați elementele hidrografice notate cu cifrele 1, 2, 3.", "ape",
     "1 – Enisei curge spre nord, în Oceanul Arctic, și primește apele lacului Baikal prin Angara; 2 – Indus coboară din Tibet spre Marea Arabiei; 3 – Lacul Aral se află la est de Marea Caspică.",
     "Obi, Enisei și Lena se varsă în Oceanul Arctic. Indus se varsă în Marea Arabiei. Lacul Aral se află la est de Marea Caspică.",
     harta="t1", optiuni=HIDRO, itemi=[{"eticheta": "1", "corect": "Enisei"}, {"eticheta": "2", "corect": "Indus"}, {"eticheta": "3", "corect": "Lacul Aral"}])
item(1, "A-b", "n3", "harta_test", 8, "Analizând harta, precizați peninsula și insula notate cu literele A și B.", "pozitie",
     "A – Peninsula India, în sudul Asiei, între Marea Arabiei și Golful Bengal; B – Insula Borneo (Kalimantan), cea mai mare insulă a Asiei, pe Ecuator.",
     "Peninsula India se află în sudul Asiei. Insula Borneo (Kalimantan) este cea mai mare insulă a Asiei.",
     harta="t1", optiuni=TARM, itemi=[{"eticheta": "A", "corect": "Peninsula India"}, {"eticheta": "B", "corect": "Insula Borneo (Kalimantan)"}])
item(2, "A-a", "n3", "harta_test", 12, "Analizând harta, precizați elementele hidrografice notate cu cifrele 1, 2, 3.", "ape",
     "1 – Huang He (Fluviul Galben), cu marea sa buclă din nordul Chinei; 2 – Lena, care se varsă printr-o deltă în Oceanul Arctic; 3 – Lacul Balhaș, lac alungit la est de Aral.",
     "Huang He se varsă în Oceanul Pacific. Lena se varsă în Oceanul Arctic. Lacul Balhaș este un lac alungit, la est de Aral.",
     harta="t2", optiuni=HIDRO, itemi=[{"eticheta": "1", "corect": "Huang He"}, {"eticheta": "2", "corect": "Lena"}, {"eticheta": "3", "corect": "Lacul Balhaș"}])
item(2, "A-b", "n3", "harta_test", 8, "Analizând harta, precizați golful și arhipelagul notate cu literele A și B.", "pozitie",
     "A – Golful Bengal, cel mai mare golf de pe Glob, la est de Peninsula India; B – Arhipelagul Japonez, în estul Asiei, în Oceanul Pacific.",
     "Golful Bengal este cel mai mare golf de pe Glob. Arhipelagul Japonez se află în Oceanul Pacific.",
     harta="t2", optiuni=TARM, itemi=[{"eticheta": "A", "corect": "Golful Bengal"}, {"eticheta": "B", "corect": "Arhipelagul Japonez"}])

# ---------- Subiectul B – grilă (5 × 4p)
OCEANE = ["Oceanul Pacific", "Oceanul Indian", "Marea Caspica", "Oceanul Arctic"]
CAPURI = ["Capul Roca", "Capul Baba", "Capul Dejnev", "Capul Celeuskin"]
CLIME = ["ecuatorial", "tropical", "subpolar", "temperat"]
item(1, "B-1", "n1", "grila", 4, "Asia se învecinează la est cu:", "pozitie",
     "La est, Asia este scăldată de Oceanul Pacific. La nord are Oceanul Arctic, la sud Oceanul Indian.", "Est: Oceanul Pacific.", variante=OCEANE, corect=0)
item(2, "B-1", "n1", "grila", 4, "Asia se învecinează la sud cu:", "pozitie",
     "La sud, Asia este scăldată de Oceanul Indian. La est are Oceanul Pacific, la nord Oceanul Arctic.", "Sud: Oceanul Indian.", variante=OCEANE, corect=1)
item(1, "B-2", "n1", "grila", 4, "Punctul extrem nordic al Asiei este:", "pozitie",
     "Capul Celiuskin, în Peninsula Taimîr, este punctul extrem nordic. Dejnev este în est, Baba în vest, iar Roca aparține Europei.", "Nord: Capul Celiuskin (Peninsula Taimîr).", variante=CAPURI, corect=3)
item(2, "B-2", "n1", "grila", 4, "Punctul extrem estic al Asiei este:", "pozitie",
     "Capul Dejnev, în Peninsula Ciukotka, la Strâmtoarea Bering, este punctul extrem estic. Celiuskin este în nord, Baba în vest, iar Roca aparține Europei.", "Est: Capul Dejnev (Peninsula Ciukotka).", variante=CAPURI, corect=2)
item(1, "B-3", "n2", "grila", 4, "Cel mai înalt podiș este:", "relief",
     "Dintre variantele date, Pamirul – „Acoperișul lumii” – este cel mai înalt (peste 4 000 m). Dekan, Iranian și Arabiei sunt mult mai joase.",
     "Pamirul este numit „Acoperișul lumii”.", variante=["Podișul Dekan", "Podișul Pamir", "Podișul Iranian", "Podișul Arabiei"], corect=1)
item(2, "B-3", "n2", "grila", 4, "Cel mai înalt podiș este:", "relief",
     "Podișul Tibet (4 000–5 000 m) este cel mai înalt și mai întins podiș înalt de pe Glob.",
     "Podișul Tibet este cel mai înalt și cel mai întins podiș înalt de pe Glob.", variante=["Podișul Dekan", "Podișul Tibet", "Podișul Iranian", "Podișul Arabiei"], corect=1)
item(1, "B-4", "n2", "grila", 4, "Străbate Câmpia Indo-Gangetică râul:", "relief",
     "Gange (și Indus) străbat Câmpia Indo-Gangetică – de aici îi vine numele. Huang He este în China, Amur și Obi sunt în nord.",
     "Câmpia Indo-Gangetică este străbătută de Indus și Gange.", variante=["Huang He", "Amur", "Gange", "Obi"], corect=2)
item(2, "B-4", "n2", "grila", 4, "Străbate Câmpia Indo-Gangetică râul:", "relief",
     "Indus (și Gange) străbat Câmpia Indo-Gangetică – de aici îi vine numele. Huang He este în China, Amur și Obi sunt în nord.",
     "Câmpia Indo-Gangetică este străbătută de Indus și Gange.", variante=["Huang He", "Amur", "Indus", "Obi"], corect=2)
item(1, "B-5", "n4", "grila", 4, "Renul trăiește în climatul:", "clima",
     "Renul trăiește în tundră, în climatul subpolar din nordul Asiei.", "Animale în tundră: renul, vulpea polară, lemingul.", variante=CLIME, corect=2)
item(2, "B-5", "n4", "grila", 4, "Ursul brun trăiește în climatul:", "clima",
     "Ursul brun trăiește în taiga, în climatul temperat.", "Animale în taiga: ursul brun, lupul, râsul, samurul.", variante=CLIME, corect=3)

# ---------- Subiectul C – adevărat / fals (5 × 4p)
def af(test, slot, nivel, enunt, adevarat, lectie, expl, sursa):
    item(test, slot, nivel, "adevarat_fals", 4, enunt, lectie, expl, sursa, adevarat=adevarat)
af(1, "C-1", "n2", "Munții Himalaya sunt cei mai înalți munți ai Asiei.", True, "relief",
   "Adevărat. Himalaya sunt cei mai înalți munți ai Asiei și ai Globului (Vf. Everest, 8 848 m).", "Munții Himalaya sunt cei mai înalți munți ai Asiei și ai Globului.")
af(2, "C-1", "n1", "Munții Himalaya sunt limita dintre Europa și Asia.", False, "pozitie",
   "Fals. Limita dintre Europa și Asia trece prin Munții Ural. Himalaya se află în sudul Asiei.", "Limita cu Europa trece prin Munții Ural, râul Ural, Marea Caspică și Munții Caucaz.")
af(1, "C-2", "n2", "Lacul Baikal este cel mai sărat lac.", False, "ape",
   "Fals. Baikal este cel mai ADÂNC lac de pe Glob și are apă dulce. Marea Moartă este unul dintre cele mai sărate lacuri.", "Lacul Baikal este cel mai adânc lac de pe Glob. Nu este cel mai sărat lac.")
af(2, "C-2", "n2", "Lacul Baikal este cel mai adânc lac.", True, "ape",
   "Adevărat. Baikal este cel mai adânc lac de pe Glob (1 642 m).", "Lacul Baikal este cel mai adânc lac de pe Glob (1 642 m).")
af(1, "C-3", "n4", "Mușchi, licheni, arbuști pitici întâlnim în zona de taiga.", False, "clima",
   "Fals. Mușchii, lichenii și arbuștii pitici sunt specifici tundrei. Taiga este pădurea de conifere (pin, brad, zadă).", "Mușchii, lichenii și arbuștii pitici sunt specifici tundrei, nu taigăi.")
af(2, "C-3", "n4", "Pin, brad, zadă întâlnim în zona de taiga.", True, "clima",
   "Adevărat. Taiga este pădurea de conifere: pin, brad, molid, zadă.", "Taiga este pădurea de conifere: pin, brad, molid, zadă.")
af(1, "C-4", "n4", "Zona de vegetație de stepă se caracterizează prin vegetație ierboasă.", True, "clima",
   "Adevărat. Stepa este zona vegetației ierboase, în climatul temperat.", "Stepa are vegetație ierboasă.")
af(2, "C-4", "n4", "Tundra se caracterizează prin vegetație ierboasă.", False, "clima",
   "Fals. Tundra are vegetație scundă de mușchi, licheni și arbuști pitici. Vegetația ierboasă este specifică stepei.", "Vegetația de tundră: mușchi, licheni și arbuști pitici.")
af(1, "C-5", "n1", "Peninsula Malacca o întâlnim în partea de vest a Asiei.", False, "pozitie",
   "Fals. Peninsula Malacca se află în sud-estul Asiei. În vest se află Peninsula Asia Mică.", "Sud-est: peninsulele Indochina și Malacca. Peninsula Malacca NU se află în vestul Asiei.")
af(2, "C-5", "n1", "Peninsula Asia Mică o întâlnim în partea de vest a Asiei.", True, "pozitie",
   "Adevărat. Asia Mică este în vestul Asiei; aici se află și Capul Baba, punctul extrem vestic.", "Vest: Peninsula Asia Mică.")

# ---------- Subiectul D – comparare climatică (20p: 2 zone × 4 criterii)
ZONE = ["ecuatoriala", "tropical_uscata", "tropical_umeda", "subpolara"]
CRITERII = [
 ("Localizare", {
   "ecuatoriala": "în jurul Ecuatorului: sudul Peninsulei Malacca și Indonezia",
   "tropical_uscata": "în sud-vestul Asiei: Peninsula Arabia, Podișul Iranian, deșertul Thar",
   "tropical_umeda": "în sudul și sud-estul Asiei: peninsulele India și Indochina",
   "subpolara": "în nordul Asiei, de-a lungul țărmului Oceanului Arctic"}),
 ("Temperaturi", {
   "ecuatoriala": "ridicate și constante tot anul (25–28°C), fără anotimpuri",
   "tropical_uscata": "foarte ridicate vara (peste 40°C ziua), diferențe mari zi–noapte",
   "tropical_umeda": "ridicate tot anul (peste 20°C), vara caldă și ploioasă",
   "subpolara": "scăzute: ierni lungi și geroase, veri scurte și răcoroase"}),
 ("Precipitații", {
   "ecuatoriala": "foarte bogate (peste 2 000 mm/an), aproape zilnic",
   "tropical_uscata": "foarte reduse (sub 200 mm/an)",
   "tropical_umeda": "bogate, căzute mai ales vara, în sezonul musonic",
   "subpolara": "reduse (200–300 mm/an), mai ales sub formă de zăpadă"}),
 ("Vânturi", {
   "ecuatoriala": "calm ecuatorial: aerul cald și umed urcă",
   "tropical_uscata": "alizee uscate, vânturi fierbinți de deșert",
   "tropical_umeda": "musonii: vara dinspre ocean, iarna dinspre uscat",
   "subpolara": "vânturi polare, reci, dinspre Oceanul Arctic"}),
]
NUME_ZONA = {"ecuatoriala": "Zona ecuatorială", "tropical_uscata": "Zona tropical-uscată", "tropical_umeda": "Zona tropical-umedă", "subpolara": "Zona subpolară"}
def comparare(test, z1, z2, expl):
    criterii = [{"nume": n, "optiuni": [d[z] for z in ZONE], "corecte": [ZONE.index(z1), ZONE.index(z2)]} for n, d in CRITERII]
    item(test, "D", "n5", "tabel_comparativ", 20,
         f"Comparați din punct de vedere climatic {NUME_ZONA[z1].lower()} și {NUME_ZONA[z2].lower()} (localizare, temperaturi, precipitații, vânturi).",
         "clima", expl, "Fișele „Zona tropical-uscată”, „Zona tropical-umedă”, „Zona subpolară” și „Zona ecuatorială”.",
         zone=[NUME_ZONA[z1], NUME_ZONA[z2]], criterii=criterii)
comparare(1, "tropical_umeda", "subpolara",
   "Zona tropical-umedă (sudul și sud-estul Asiei) e caldă și primește ploi bogate vara, aduse de musoni. Zona subpolară (nordul Asiei) e rece, cu precipitații reduse, mai ales zăpadă, și vânturi polare.")
comparare(2, "tropical_uscata", "ecuatoriala",
   "Ambele zone sunt calde. Zona tropical-uscată (sud-vestul Asiei) are precipitații foarte reduse și vânturi uscate. Zona ecuatorială (în jurul Ecuatorului) are ploi aproape zilnic și calm ecuatorial.")

# ---------- Subiectul E – explicare (10p: alegi 2 cauze corecte)
item(1, "E", "n5", "selectie_multipla", 10, "Explicați de ce în zona ecuatorială vegetația este abundentă.", "clima",
     "În zona ecuatorială este cald și umed tot anul. Plantele au căldură, apă și lumină în fiecare lună, așa că pădurea crește continuu: deasă, etajată și mereu verde.",
     "Vegetația este abundentă pentru că este cald și umed tot anul, iar plantele cresc continuu.",
     de_selectat=2,
     corecte=["temperaturile sunt ridicate tot anul", "precipitațiile sunt foarte bogate, aproape zilnic", "nu există un anotimp rece, iar plantele cresc tot anul"],
     gresite=["verile sunt scurte și răcoroase", "solul este înghețat în adâncime", "bat vânturi uscate și fierbinți", "precipitațiile sunt sub 200 mm pe an"])
item(2, "E", "n5", "selectie_multipla", 10, "Explicați de ce în zona subpolară vegetația este scundă.", "clima",
     "În zona subpolară vara este scurtă și rece, iar solul rămâne înghețat în adâncime. Rădăcinile nu pot pătrunde adânc, iar vântul rece usucă plantele. Rezistă doar mușchii, lichenii și arbuștii pitici.",
     "Vegetația e scundă pentru că vara este scurtă și rece, solul este înghețat în adâncime (permafrost) și bat vânturi puternice și reci.",
     de_selectat=2,
     corecte=["temperaturile sunt scăzute, iar vara este scurtă și răcoroasă", "solul rămâne înghețat în adâncime (permafrost)", "bat vânturi puternice și reci"],
     gresite=["temperaturile sunt ridicate tot anul", "precipitațiile sunt foarte bogate, aproape zilnic", "solurile sunt groase și fertile", "plantele cresc tot anul"])

# ================================================================ HĂRȚI (marcajele tipărite pe hărțile din teste, în pixeli)
HARTA = {"harti": {
  "t1": {"test": 1, "imagine": "assets/harta-t1.webp", "imagine_png": "assets/harta-t1.png", "latime": 1054, "inaltime": 1395,
         "marcaje": {"1": [531, 362], "2": [227, 697], "3": [280, 585], "A": [290, 966], "B": [810, 1171]}},
  "t2": {"test": 2, "imagine": "assets/harta-t2.webp", "imagine_png": "assets/harta-t2.png", "latime": 1054, "inaltime": 1395,
         "marcaje": {"1": [620, 608], "2": [731, 266], "3": [420, 610], "A": [444, 993], "B": [985, 615]}}}}

# ================================================================ INSIGNE
INSIGNE = [
 ("primul-pas", "Primul pas", "👣", "Primul nivel terminat."),
 ("trei-stele", "Trei stele", "⭐", "Un nivel terminat cu 3 stele."),
 ("toate-nivelurile", "Toate nivelurile", "🧭", "Cel puțin o stea în fiecare nivel."),
 ("navigatorul", "Navigatorul", "⛵", "6 răspunsuri corecte despre vecini, puncte extreme și țărmuri."),
 ("acoperisul-lumii", "Acoperișul lumii", "🏔️", "4 răspunsuri corecte despre relief."),
 ("stapanul-apelor", "Stăpânul apelor", "🌊", "5 răspunsuri corecte despre râuri și lacuri."),
 ("climatologul", "Climatologul", "🌦️", "6 răspunsuri corecte despre climă, vegetație și animale."),
 ("ochi-de-cartograf", "Ochi de cartograf", "🗺️", "2 hărți rezolvate perfect, una după alta."),
 ("comparatorul", "Comparatorul", "⚖️", "O comparație climatică rezolvată perfect."),
 ("explicatorul", "De ce? Pentru că…", "💡", "O explicație rezolvată perfect."),
 ("seria-de-foc", "Seria de foc", "🔥", "Ai învățat 5 zile la rând."),
 ("expeditia", "Expediția în Asia", "🏅", "Marea Expediție terminată cu nota cel puțin 9."),
 ("expeditia-perfecta", "Nota 10", "🏆", "Marea Expediție terminată cu nota 10."),
 ("memorie-de-bufnita", "Memorie de bufniță", "🦉", "10 flashcard-uri ajunse în cutia 5."),
]

# ================================================================ SCRIERE
def scrie(nume, obj):
    with open(os.path.join(OUT, nume), 'w', encoding='utf-8') as f:
        json.dump(obj, f, ensure_ascii=False, indent=1)

os.makedirs(OUT, exist_ok=True)
scrie("lectii.json", {"taramuri": TARAMURI, "structura_test": STRUCTURA, "lectii_index": LECTII_INDEX,
                      "lectii": {k: [{"titlu": t, "puncte": p} for t, p in v] for k, v in L.items()}})
scrie("intrebari_teste.json", Q)
scrie("intrebari_extra.json", [])
scrie("harta.json", HARTA)
scrie("insigne.json", [{"id": a, "nume": b, "icon": c, "descriere": d} for a, b, c, d in INSIGNE])

# verificări rapide
tot = {}
for q in Q: tot[q["test"]] = tot.get(q["test"], 0) + q["puncte"]
assert tot == {1: 90, 2: 90}, tot
for n in TARAM_NIVEL: assert {q["test"] for q in Q if q["nivel"] == n} == {1, 2}, n
print(f"{len(Q)} itemi · punctaj pe test: {tot} · niveluri: " + ", ".join(f"{n}={sum(q['nivel']==n for q in Q)}" for n in TARAM_NIVEL))
