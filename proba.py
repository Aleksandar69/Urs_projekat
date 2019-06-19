from Logika.artikal_rukovanje import Artikal_rukovanje
from Entiteti.artikal import Artikal
from Logika.sekcija_rukovanje import Sekcija_rukovanje
from Entiteti.sekcija import Sekcija
from Entiteti.polica import Polica
from Logika.polica_rukovanje import Polica_rukovanje
from Entiteti.stavka import Stavka
from Logika.stavka_rukovanje import Stavka_rukovanje
from Entiteti.racun import Racun
from Logika.racun_rukvanje import Racun_rukovanje

if __name__ == "__main__":
    # a = Artikal_rukovanje("artikli.txt")

    # artikal = Artikal("1", "Mlijeko", "2.3 MM", 100.20, "20.06.2019", "polica1")
    # a.upis_jednog(artikal)

    # s = Sekcija_rukovanje("sekcije.txt")

    # sekcija = Sekcija("1", "hrana", "jestiva", "Gore Lijevo" )
    # s.upis_jednog(sekcija)

    # p = Polica_rukovanje("polica.txt")

    # polica = Polica("1", "1", "1", "1", "2.3", "10.12", "4")

    # p.upis_jednog(polica)


    # s1 = Stavka_rukovanje("stavka.txt")
    # stavka = Stavka("1", 5, 20.1, "Persun", "a")
    # s1.upis_jednog(stavka)

    # r = Racun_rukovanje("racun.txt")
    # racun = Racun("Petar", 105.43, "02.04.2019")
    # r.upis_jednog(racun)

    # a = Artikal_rukovanje("artikli.txt")
    # lista1 = a.citanje_svih()

    # b = Sekcija_rukovanje("sekcije.txt")
    # lista2 = b.citanje_svih()

    # for i in lista1:
    #     print(str(i))

    # print("___________")

    # pretrazeno = a.pretraga_po_oznaci(lista1, "1")
    # for i in pretrazeno:
    #     print(str(i))

    # pretrazeno1 = a.pretraga_po_nazivu(lista1, "k")
    # for i in pretrazeno1:
    #     print(str(i))

    # pretrazeno2 = a.pretraga_po_opisu(lista1, "a")
    # for i in pretrazeno2:
    #     print(str(i))

    # pretrazeno3 = a.pretraga_po_cijeni(lista1, 60)
    # for i in pretrazeno3:
    #     print(str(i))

    # pretrazeno4 = a.pretraga_po_roku_trajanja(lista1, "20.06.2022")
    # for i in pretrazeno4:
    #     print(str(i))

    # a = Artikal_rukovanje("artikli.txt")
    # lista1 = a.citanje_svih()
        
    # pretrazeno5 = a.sortiranje_po_cijeni(lista1, "+")
    # for i in pretrazeno5:
    #     print(str(i))
    
    # pretrazeno6 = a.sortiranje_po_roku_trajanja(lista1, "-")
    # for i in pretrazeno6:
    #     print(str(i))

    # pretrazeno7 = b.pretraga_po_oznaci(lista2, "5")
    # for i in pretrazeno7:
    #     print(str(i))

    # pretrazeno8 = b.pretraga_po_nazivu(lista2, "o")
    # for i in pretrazeno8:
    #     print(str(i))

    # pretrazeno9 = b.pretraga_po_opisu(lista2, "malo")
    # for i in pretrazeno9:
    #     print(str(i))

    # pretrazeno10 = b.pretraga_po_poziciji(lista2, "lije")
    # for i in pretrazeno10:
    #     print(str(i))

    # c = Polica_rukovanje("polica.txt")
    # lista = c.citanje_svih()

    # b = Sekcija_rukovanje("sekcije.txt")
    # lista1 = b.citanje_svih()
    # for i in lista1:
    #         print(str(i))

    # oznaka_sekcije = input("faberite ID sekcije: ")
    # pretrazeno = b.izlistaj_police(oznaka_sekcije, lista)


    # for i in pretrazeno:
    #     print(str(i))


    # c = Polica_rukovanje("polica.txt")
    # lista = c.citanje_svih()

    # b = Sekcija_rukovanje("sekcije.txt")
    # lista1 = b.citanje_svih()
    # for i in lista1:
    #         print(str(i))

    # d = Artikal_rukovanje("artikli.txt")
    # lista2 = d.citanje_svih()

    # e = Racun_rukovanje("racun.txt")
    # lista3 = e.citanje_svih()

    # f = Stavka_rukovanje("stavka.txt")
    # lista4 = f.citanje_svih()

    # for i in lista3:
    #     print(str(i))

    # racun = input("Izaberite ID racuna: ")
    # racun1 = e.stavke_u_racunu(racun, lista4, lista2)

    # for i in racun1:
    #     print("stavka" + str(i["stavka"]) + ", artikal" + str(i["artikal"]))
    # # lista = a.citanje_svih()

    # pretrazeno = a.pretraga_po_oznaci(lista, "1")
    # for i in pretrazeno:
    #     print(str(i))

    # b = Artikal_rukovanje("artikli.txt")
    # lista1 = b.citanje_svih()

    # pretrazeno1 = b.pretraga_po_oznaci(lista1, "1")
    # for i in pretrazeno1:
    #     print(str(i))

    # a = Racun_rukovanje("racun.txt")
    # lista = a.citanje_svih()

    # pretrazeno = a.pretraga_po_oznaci(lista, "1")
    # for i in pretrazeno:
    #     print(str(i))

    # a = Artikal_rukovanje("artikli.txt")
    # lista1 = a.citanje_svih()

    # sortiranje = a.sortiranje_po_cijeni(lista1, "+")
    # for i in sortiranje:
    #     print(str(i))

    a = Polica_rukovanje("police.txt")
    lista = a.citanje_svih()

    sortiranje = a.sortiranje_po_poziciji(lista, "+")
    for i in sortiranje:
        print(str(i))