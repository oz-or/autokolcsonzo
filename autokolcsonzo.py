from berles import Berles


class Autokolcsonzo:
    def __init__(self, nev):
        self.nev = nev
        self.autok = []
        self.berlesek = []

    def auto_hozzaadas(self, auto):
        self.autok.append(auto)

    def berel(self, rendszam, datum):
        for berles in self.berlesek:
            if berles.auto.rendszam == rendszam:
                return "Az autó már foglalt."
        for auto in self.autok:
            if auto.rendszam == rendszam:
                uj_berles = Berles(auto, datum)
                self.berlesek.append(uj_berles)
                return f"Bérlés sikeres! Ár: {auto.berleti_dij} Ft"
        return "Nincs ilyen autó."

    def lemond(self, rendszam):
        for berles in self.berlesek:
            if berles.auto.rendszam == rendszam:
                self.berlesek.remove(berles)
                return "Bérlés lemondva."
        return "Nincs ilyen bérlés."

    def listaz_berlesek(self):
        return "\n".join(str(berles) for berles in self.berlesek) if self.berlesek else "Nincsenek aktív bérlések."
