from szemelyauto import Szemelyauto
from teherauto import Teherauto
from berles import Berles
from autokolcsonzo import Autokolcsonzo

def alap_adatok(kolcsonzo):
    kolcsonzo.auto_hozzaadas(Szemelyauto("ABC-123", "Opel Astra", 8000, 5))
    kolcsonzo.auto_hozzaadas(Szemelyauto("XYZ-999", "Suzuki Swift", 7000, 4))
    kolcsonzo.auto_hozzaadas(Teherauto("LMN-456", "Ford Transit", 12000, 1500))

    kolcsonzo.berel("ABC-123", "2025-05-10")
    kolcsonzo.berel("XYZ-999", "2025-05-11")
    kolcsonzo.berel("LMN-456", "2025-05-12")

def menu():
    kolcsonzo = Autokolcsonzo("Péter Autókölcsönző")
    alap_adatok(kolcsonzo)

    while True:
        print("\n--- Autókölcsönző Menü ---")
        print("1. Autó bérlése")
        print("2. Bérlés lemondása")
        print("3. Bérlések listázása")
        print("4. Kilépés")

        valasz = input("Válassz egy lehetőséget: ")
        if valasz == "1":
            rendszam = input("Add meg az autó rendszámát: ")
            datum = input("Add meg a bérlés dátumát (YYYY-MM-DD): ")
            print(kolcsonzo.berel(rendszam, datum))
        elif valasz == "2":
            rendszam = input("Add meg a rendszámot a lemondáshoz: ")
            print(kolcsonzo.lemond(rendszam))
        elif valasz == "3":
            print(kolcsonzo.listaz_berlesek())
        elif valasz == "4":
            print("Kilépés...")
            break
        else:
            print("Érvénytelen választás!")

if __name__ == "__main__":
    menu()
