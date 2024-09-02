class Vrchol:
    def __init__(self):
        self.slova = []
        self.deti = dict()
    
    def novy_syn(self, pismeno):
        if pismeno in self.deti:
            return self.deti[pismeno]
        self.deti[pismeno] = Vrchol()
        return self.deti[pismeno]
            
class Strom:
    def __init__(self):
        self.koren = Vrchol()

    def najdi(self, slovo):
        slovo = slovo.lower()
        aktualny = self.koren
        for pismeno in slovo + '#':
            if pismeno in aktualny.deti:
                aktualny = aktualny.novy_syn(pismeno)
            else:
                return None
        return aktualny

    def pridaj(self, slovo):
        aktualny = self.koren
        for pismeno in slovo + '#':
            aktualny = aktualny.novy_syn(pismeno)
        return aktualny
    
    @classmethod
    def zo_slovnika(cls, cesta_k_slovniku):
        prazdny_strom = cls()
        subor = open(cesta_k_slovniku,"r")
        for riadok in subor.readlines():
            slovo,pocet = riadok.strip().split()
            slovo = slovo.lower()
            prazdny_strom.pridaj(slovo)
        return prazdny_strom

if __name__ == "__main__":
    novy_strom = Strom.zo_slovnika("slovniky/words.txt")
    print(novy_strom.najdi("aBase"))