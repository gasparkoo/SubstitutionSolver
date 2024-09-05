from typing import List, Dict
from kan_strom_slov import Kanon

class Permutacia:
    def __init__(self):
        self.perm = dict()
        self.inv_perm = dict()
    def pridaj(self, kluc, hodnota):
        self.perm[kluc] = hodnota
        self.inv_perm[hodnota] = kluc
    def kontrola(self, kluc, hodnota):
        if kluc in self.perm:
            return self.perm[kluc] == hodnota
        else:
            return hodnota not in self.inv_perm
    def obsahuje_a_ok(self, kluc, hodnota):
        return self.kontrola(kluc, hodnota) and kluc in self.perm
    def odober(self, kluc, hodnota):
        del self.perm[kluc]
        del self.inv_perm[hodnota]

def zmena_permut(permut : Permutacia,povod_slovo,vysledne_slovo):
    zmeny = Permutacia()
    for j in range(len(povod_slovo)):
        kluc = povod_slovo[j].lower()
        hodnota = vysledne_slovo[j].lower()

        if not permut.kontrola(kluc, hodnota) or not zmeny.kontrola(kluc, hodnota):
            return None
        elif permut.obsahuje_a_ok(kluc, hodnota):
            pass
        else:
            zmeny.pridaj(kluc, hodnota)
    return zmeny


def doriesenie(text : List[str],permut : Permutacia,strom : Kanon,i=0) -> Permutacia | None:
    if len(text)>i:
        nedoriesene = set()
        for j in text[i]:
            if j not in permut.perm:
                nedoriesene.add(j)
        if len(j) == 0:
            return doriesenie(text, permut, strom, i+1)
        moznosti = strom.najdi(text[i])
        if moznosti is None:
            return None
        else:
            for slovo in moznosti.slova:
                zmeny = zmena_permut(permut,text[i],slovo)
                if zmeny is None:
                    continue
                for kluc,hodnota in zmeny.perm.items():
                    permut.pridaj(kluc, hodnota)
                vysledok = doriesenie(text,permut,strom,i+1)
                if vysledok != None:
                    return vysledok
                for kluc,hodnota in zmeny.perm.items():
                    permut.odober(kluc, hodnota)
    else:
        return permut

if __name__ == "__main__":
    strom = Kanon()
    for i in "abecdefghijkl":
        for j in "abecdefghijkl":
                for k in "abecdefghijkl":
                    strom.pridaj(i+j+k)

    for slovo in ["The", "trouble", "with", "having", "an", "open", "mind"]:
        strom.pridaj(slovo)
    t = input().split()
    print(doriesenie(t, dict(), strom))
    