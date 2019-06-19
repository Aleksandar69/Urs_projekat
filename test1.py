from Entiteti.artikal import Artikal
from Logika.entiteti_rukovanje import EntitetiRukovanje
from Logika.artikal_rukovanje import Artikal_rukovanje
from Entiteti.polica import Polica
from Logika.polica_rukovanje import Polica_rukovanje
from Entiteti.sekcija import Sekcija
from Logika.sekcija_rukovanje import Sekcija_rukovanje
from Entiteti.stavka import Stavka
from Logika.stavka_rukovanje import Stavka_rukovanje
from Entiteti.racun import Racun
from Logika.racun_rukovanje import Racun_rukovanje

# a = Artikal_rukovanje("artikli.txt")
# artikal1 = Artikal("1", "test", "test", 23, "23.2.2019", "polica1")
# zamjeni = a.izmjena_jednog(artikal1)


# p = Polica_rukovanje("police.txt")
# polica1 = Polica("50", "1", "1", "1", "1", "1", "1", "1")
# p.izmjena_jednog(polica1)

# p = Polica_rukovanje("police.txt")
# lista_polica = p.citanje_svih()

# duzina_za_pretragu = 1.3
# pretrazeno = p.pretraga_po_duzini(lista_polica, duzina_za_pretragu)
# for i in pretrazeno:
#     print(i)


# p = Polica_rukovanje("police.txt")
# lista_polica = p.citanje_svih()

# sortirano = p.sortiranje_po_poziciji(lista_polica, "-")
# for i in lista_polica:
#     print(i)

# r = Racun_rukovanje("racuni.txt")
# lista_racuna = r.citanje_svih()

# sortirano = r.sortiranje_po_ukupnoj_cijeni(lista_racuna, "+")
# print(sortirano)


# a = Artikal_rukovanje("artikli.txt")
# lista_artikala = a.citanje_svih()
# sortirano = a.sortiranje_po_cijeni(lista_artikala, "+")
# for i in sortirano:
#     print(i)

# a = Artikal_rukovanje("artikli.txt")
# lista_artikala = a.citanje_svih()
# sortirano = a.sortiranje_po_roku_trajanja(lista_artikala, "+")
# for i in sortirano:
#     print(i)

#     opt_sortiranje = int(input("Izaberite jednu od opcija za sortiranje: "))


# a = Artikal_rukovanje("artikli.txt")
# lista_artikala = a.citanje_svih()
# p = Polica_rukovanje("police.txt")

# id_police = input("Unesite ID police: ")
# artikli_u_polici = p.izlistaj_artikle(id_police, lista_artikala)
# for i in artikli_u_polici:
#     print(i)


# p = Polica_rukovanje("police.txt")
# lista_polica = p.citanje_svih()

# s = Sekcija_rukovanje("sekcije.txt")
# lista_sekcija = s.citanje_svih()

# a = Artikal_rukovanje("artikli.txt")
# lista_aritkala = a.citanje_svih()

# r = Racun_rukovanje("racuni.txt")
# lista_racuna = r.citanje_svih()

# st = Stavka_rukovanje("stavke.txt")
# lista_stavki = st.citanje_svih()

# for l in lista_sekcija:
#     print(l)

# id_sekcije = input("Unesite ID sekcije: ")
# police = s.izlistaj_police(id_sekcije, lista_polica)
# for i in police:
#     print(i)

# for l in lista_polica:
#     print(l)
# id_police = input("Unesite ID police: ")
# artikli = s.izlistaj_artikle(id_police, lista_aritkala)
# for i in artikli:
#     print(i)

# for i in lista_racuna:
#     print(i)
# id_racuna = input("Unesite ID racuna: ")
# stavke_i_artikli = r.stavke_i_artikli_u_racunu(id_racuna, lista_stavki, lista_aritkala)
# for i in stavke_i_artikli:
#     print("stavka" + str(i["stavka"]) + ", artikal" + str(i["artikal"]))


# a = "konj;"
# b = "riba;"
# c = "petar;"

# rezultat = "{:^10}|{:^10}|{:^10}".format(a,b,c)
# print(rezultat)

# artikal = Artikal("7", "cips", "paprika", 60, "06.09.2019", "3")

# a.upis_jednog(artikal)


# def bubbleSort(alist):
#     for num in range(len(alist)-1,0,-1):
#         for i in range(num):
#             if alist[i]>alist[i+1]:
#                 temp = alist[i]
#                 alist[i] = alist[i+1]
#                 alist[i+1] = temp

# alist = [54,26,93,17,77,31,44,55,20]
# bubbleSort(alist)
# print(alist)

# def eat(food, is_healthy):

#     if is_healthy == True:
#         return f"I'm eating {food}"
#     if is_healthy == False:
#         return f"I'm eating {food} and I love it"

def citanje_svih(self):
    """Citanje svih podataka iz fajlova"""
    with open(self.putanja, "r") as file:
        podaci = []
        for linija in file.readlines():
            podaci.append(self.napravi_entitet(linija))
        return podaci


help(citanje_svih)
