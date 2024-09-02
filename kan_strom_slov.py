from strom_slov import Strom

def kanonicky_tvar(slovo):
    slovo = slovo.lower()
    slovnik = dict()
    vysledne_slovo = ""
    akt_pismeno = ord("a")
    for i in slovo:
        if i in slovnik:
            vysledne_slovo += slovnik[i]
        else:
            slovnik[i] = chr(akt_pismeno)
            akt_pismeno += 1
            vysledne_slovo += slovnik[i]
    return vysledne_slovo

class Kanon(Strom):
    def __init__(self):
        super().__init__()
    def najdi(self,slovo):
        kan_slovo = kanonicky_tvar(slovo)
        return super().najdi(kan_slovo)
    def pridaj(self,slovo):
        kan_slovo = kanonicky_tvar(slovo)
        koncovy_vrchol = super().pridaj(kan_slovo)
        koncovy_vrchol.slova.append(slovo.lower())

if __name__ == "__main__":
    novy_strom = Kanon.zo_slovnika("slovniky/words.txt")
    print(novy_strom.najdi("abbaa").slova)
