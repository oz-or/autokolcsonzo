from auto import Auto

class Teherauto(Auto):
    def __init__(self, rendszam, tipus, berleti_dij, teherbiras):
        super().__init__(rendszam, tipus, berleti_dij)
        self.teherbiras = teherbiras

    def __str__(self):
        return f"Teherautó | Rendszám: {self.rendszam}, Típus: {self.tipus}, Díj: {self.berleti_dij} Ft/nap, Teherbírás: {self.teherbiras} kg"
