# Analiza dhe Diskutimi i Rezultateve
## 1. Hyrje
Ky raport paraqet simulimin numerik të sistemeve dinamike jotritore, specifikisht Hartën e Henonit dhe Standard Map. Këto modele përdoren për të demonstruar kalimin nga sjellja e rregullt periodike në atë kaotike.
## 2. Analiza e Modeleve
 * *Atraktori i Henonit:* Rezultatet tona tregojnë formimin e një atraktori me strukturë fraktale. Pikat nuk shpërndahen rastësisht, por kufizohen në një zonë specifike (atraktor). Kjo tregon një ekuilibër midis determinizmit dhe kaosit.
 * *Standard Map:* Analiza tregon se rritja e parametrit K ndryshon rrënjësisht dinamikën. Për vlera të ulëta, sistemi ruan orbita të mbyllura, ndërsa për vlera të larta (K > 1), shfaqet "deti kaotik", ku pozicioni bëhet i paparashikueshëm.
## 3. Analiza e Ndjeshmërisë (Pjesa 4)
Një karakteristikë themelore e sistemit është ndjeshmëria ndaj kushteve fillestare.
 * *Eksperimenti:* Duke aplikuar një ndryshim infinitesimal delta = 10^-5 në pikën fillestare, kemi vëzhguar divergjencën e trajektoreve.
 * *Interpretimi:* Distanca midis trajektores bazë dhe asaj të perturbuar rritet në mënyrë eksponenciale. Kjo konfirmon fenomenin e "efektit flutur", ku edhe një gabim fare i vogël në matjen fillestare bëhet vendimtar për parashikimin afatgjatë.
## 4. Kufizimet e Modelimit Numerik
Rezultatet tona janë të kufizuara nga saktësia e numrave me pikë lundruese. Për shkak të akumulimit të gabimeve gjatë mijëra iteracioneve, simulimi numerik përfaqëson një përafrim të sjelljes fizike. Në një numër shumë të madh hapash, zhurma dixhitale mund të ndikojë në trajektoren, duke theksuar se simulimi është mjet për të kuptuar dinamikën, jo një kopje identike e realitetit fizik.
