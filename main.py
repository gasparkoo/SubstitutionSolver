from riesenie import doriesenie, Permutacia
from kan_strom_slov import Kanon

strom = Kanon.zo_slovnika("slovniky/words.txt")

ciastocna_permutacia = Permutacia()

def filter_funkc(pismeno):
    return pismeno.isalpha() or pismeno == " "

text = input("Zadaj text: ")
if "'" in text:
    print("text nemá obsahovať `'` ")
    exit(1)
novy_text = "".join(filter(filter_funkc,text)).lower().split()
pocet_pismen = 0
zoznam,percent_vyskyt = [0]*26,[0]*26
jednopis_slova = set()

for slovo in novy_text:
    if len(slovo) == 1:
        jednopis_slova.add(slovo)
    slovo = slovo.lower()
    for pismeno in slovo:
        pocet_pismen += 1
        zoznam[ord(pismeno)-ord("a")] += 1
for i in range(len(percent_vyskyt)):
    percent_vyskyt[i] = 100/pocet_pismen*zoznam[i]

vysled_permutacia = doriesenie(novy_text, ciastocna_permutacia, strom)
if vysled_permutacia is None:
    print("riesenie sa nenaslo :(")
else:
    vystup = ""
    for i in text:
        if i.isalpha():
            if i.islower():
                vystup += vysled_permutacia.perm[i]
            else:
                vystup += vysled_permutacia.perm[i.lower()].upper()
        else:
            vystup += i
    print("Riešenie: ",vystup)
