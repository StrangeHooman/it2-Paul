# 1. Idé

Aksjespill som renderer grafer i terminalen.

Game-ifiserte elementer

Gameloop som er seperat fra input

Du skal kunne klikke på menyer med musen

15 tidsintervaller per dag

<br>

<br>

# 2. Programmer

<br>

## launch.py
Dette er en launcher som åpner hovvedkoden i et nytt terminalvindu. Den endrer på utføring basert på operativsystemet.

<br>

## ui.py
Denne definerer en hel del forskjellige klasser knyttet til rendering. Dette inkluderer UI klassen, med underklasser, og Vector2 klassen, som jeg bruker for blant annet koordinater.

<br>

## main.py
Slik som navnet antyder er dette hovvedkoden. Denne blir kjørt i et nytt terminalvindu og tar i bruk klasser fra *ui.py*. 

**Rendering** skjer i tre steg.
1. Buffer blir resatt
2. Objekter blir lagt til i bufferen
3. Bufferen blir printet som én string

Jeg bruker en buffer for å unngå flimring av skjermen

<br>

**Spillet** fortsetter uavhengig av brukerinput. Dette gir en mer autentisk, stressende følelse tilknyttet salg og kjøp av aksjer.

<br>

<br>

# 3. Biblioteker

## Blessed:
Blessed er et bibliotek som åpner opp for enkel kontroll av printing til terminalen.
Jeg bruker det for å enkelt kunne endre farge på celler, og bevege på cursoren.

## Re:
Re er et bilbiotek som gir deg verktøy for å finne deler av tekst som følger et visst format i en string. Jeg bruker dette i `textToCell()` funksjonen for å "dra ut" ANSI escape codes og legge de til i `Cell` objekter som lister av strings heller enn som et char element av en `Cell`.

## Time:
Time er et innebygd bilbiotek i python som har diverse verktøy for å behandle nettop tid.
Jeg bruker biblioteket for å regne ut totaltid av programmet og tid mellom frames.

## Math:
Math er et annet innebygd bilbiotek i python som gir mange matteverktøy.
Jeg bruker dette biblioteket hovvedsakelig for funksjonene 
`math.floor` og `math.ceil`.

<br>

<br>

# 4. Kjøring

For å kjøre koden starter du launch.py i valgfri omgivelse. Den skal i teorien, og praksis på min egen maskin, åpne et nytt terminalvindu hvor hovvedkoden kjører. Den er foreløpig kun konfigurert for Windows og Macos. Jeg har selv kun testet koden på Windows.

<br>

<br>

# 5. KI-bruk

Jeg har tatt i bruk ki for veiledning og forståelse av hvordan terminalen oppfører seg samt hjelp ved debugging og restrukturering. 

Ki er også brukt for å finne en god måte å lage en ny terminal på, som koden skal kjøre i. Ki har mer eller mindre skrevet launch.py, men jeg mener jeg forstår den og er åpen for spørsmål anngående den også. Jeg tenkte det var akseptabelt å la den skrive mer av koden her ettersom den ikke er hovvedpoenget av mine koder.

Det er også noen dictionaries for forskjellige UNICODE tegn, som jeg bruker for å lage penere UI elementer, som er laget av KI. Ellers har jeg fokusert på å bruke ki til å planlegge struktur og bedre forstå kode.