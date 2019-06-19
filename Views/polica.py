from Meni.polica_menu import PolicaMenu
from Logika.polica_rukovanje import Polica_rukovanje
from Entiteti.polica import Polica


class PolicaView:
    def __init__(self):
        self.polica_handler = Polica_rukovanje("police.txt")

    def rad_sa_policama(self):
        self.polica_menu = PolicaMenu()
        self.polica_menu.print_welcome_message()

        option = "-1"
        while "0" != option:
            option = self.polica_menu.ask_for_menu_option()

            if "1" == option:
                self.prikaz_polica()
            elif "2" == option:
                self.dodavanje_polica()
            elif "3" == option:
                self.menjanje_polica()

        return 0

    def prikaz_polica(self):
        self.lista_polica = self.polica_handler.citanje_svih()
        for polica in self.lista_polica:
            print(polica)
        return 0

    def dodavanje_polica(self):
        oznaka = input("Unesite oznaku: ")
        red = int(input("Unesite red: "))
        if red <= 0:
            raise Exception
        kolona = int(input("Unesite kolonu: "))
        if kolona <= 0:
            raise Exception
        pozicija = input("Unesite poziciju: ")
        duzina = float(input("Unesite duzinu: "))
        if duzina <= 0:
            raise Exception
        sirina = float(input("Unesite sirinu: "))
        if sirina <= 0:
            raise Exception
        visina = float(input("Unesite visinu: "))
        if visina <= 0:
            raise Exception
        sekcija = input("Unesite sekciju: ")

        polica = Polica(oznaka, red, kolona, pozicija,
                        duzina, sirina, visina, sekcija)
        self.polica_handler.upis_jednog(polica)

    def menjanje_polica(self):
        oznaka = input(
            "Unesite oznaku police koji zelite da zamjenite: ")
        oznaka = str(oznaka)
        red = input("Unesite red nove police: ")
        red = int(red)
        kolona = input("Unesite kolonu nove police: ")
        kolona = int(kolona)
        pozicija = input("Unesite poziciju nove police: ")
        pozicija = str(pozicija)
        duzina = input("Unesite duzinu nove police: ")
        duzina = float(duzina)
        sirina = input("Unesite sirinu nove police: ")
        sirina = float(sirina)
        visina = input("Unesite visinu nove police: ")
        visina = float(visina)
        sekcija = input("Unesite sekciju nove police: ")
        polica = Polica(oznaka, red, kolona, pozicija,
                        duzina, sirina, visina, sekcija)
        self.polica_handler.izmjena_jednog(polica)
