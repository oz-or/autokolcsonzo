from auto import Auto

class Szemelyauto(Auto):
    def __init__(self, rendszam, tipus, berleti_dij, utasok_szama):
        super().__init__(rendszam, tipus, berleti_dij)
        self.utasok_szama = utasok_szama

    def __str__(self):
        return f"Személyautó | Rendszám: {self.rendszam}, Típus: {self.tipus}, Díj: {self.berleti_dij} Ft/nap, Utasok: {self.utasok_szama}"
