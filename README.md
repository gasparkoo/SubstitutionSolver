# SubstitutionSolver
Zápočtový program z predmetu PROG 2

## Spúšťanie programu
Na spustenie je potrebná verzia Python 3.9 alebo vyššia. Na spustenie programu stačí spustiť súbor `main.py` príkazom `python main.py`. 

Po spustení sa program opýta na zašifrovaný text. Program používa anglické slovníky, teda rozšifrovaný text bude v angličtine tiež. Program zatiaľ **nepodporuje slová s apostrofmi**. Po nájdení prvého riešenia vypíše rozšifrovaný text, ináč vypíše *riesenie sa nenaslo :(*.   

## Fungovanie programu
### Kanonický strom: 
Kanonický tvar slova je taká substitúcia písmen, ktorá je lexikograficky čo najmenšia (napr. leep zmení na abbc). Kanonický strom je špeciálny písmenkový strom. Program postupne slová zo slovníka zmení na ich kanonický tvar, ktorý uloží do kanonického stromu. Na konci kanonického slova v strome je list obsahujúci slová daného tvaru. V tomto strome ide rýchlo vyhľadávať všetky slová idúce získať substitúciou zadaného slova tak, že slovo najskôr zmení na kanonický tvar, a potom vyhľadá zpermutované slová v strome.
### Funkcia doriešenie:
Funkcia postupne prechádza jednotlivé slová a pomocou kanonického stromu zistí podobné slová. Následne ich rekurzívne vyskúša s tým, že vždy overí, či dané slovo nejde proti už doteraz vyriešenej permutácií. Používa na to triedu `Permutácia`, ktorá kontroluje nové permutácie. Takto dokáže nájsť prvú správnu permutáciu.


## Možné zlepšenia
- nechať užívateľovi možnosť vybrať si zo slovníka
- vyriešiť slová s apostrofmi
- tipovanie časti permutácie pomocou heuristiky
- nájdenie všetkých možných rozšifrovaní
- zrýchlenie programu (napr. orezanie/ohodnotenie nevýhodných slov, ktoré idú získať substitúciou zašifrovaného slova)


