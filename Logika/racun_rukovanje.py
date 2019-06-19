from Logika.entiteti_rukovanje import EntitetiRukovanje
from Entiteti.racun import Racun


class Racun_rukovanje(EntitetiRukovanje):
    def __init__(self, putanja):
        super().__init__(putanja)

    def citanje_svih(self):
        with open(self.putanja, "r") as file:
            podaci = []
            for linija in file.readlines():
                podaci.append(self.napravi_entitet(linija))
            return podaci

    def napravi_entitet(self, linija):
        polje = linija.strip().split(";")
        return Racun(polje[0], polje[1], polje[2], polje[3])

    def upis_jednog(self, entitet):
        with open(self.putanja, "a") as file:
            file.write(str(entitet))

    def izmjena_jednog(self, entitet):
        entiteti = self.citanje_svih()
        pronasao = False
        for i in range(len(entiteti)):
            if entiteti[i].oznaka == entitet.oznaka:
                entiteti.pop(i)
                if i >= len(entiteti):
                    entiteti.append(entitet)
                else:
                    entiteti.insert(i, entitet)
                pronasao = True
        with open(self.putanja, "w") as file:
            for entitet in entiteti:
                file.write(str(entitet))
        return pronasao

    def pretraga_po_oznaci(self, lst, rijec):
        pretrazeno = []
        for i in lst:
            if i.oznaka.lower().find(rijec.lower()) != -1:
                pretrazeno.append(i)
        return pretrazeno

    def pretraga_po_prodavcu(self, lst, rijec):
        pretrazeno = []
        for i in lst:
            if i.prodavac.lower().find(rijec.lower()) != -1:
                pretrazeno.append(i)
        return pretrazeno

    def pretraga_po_ukupnoj_cijeni(self, lst, broj):
        pretrazeno = []
        for i in lst:
            if i.ukupna_cijena == broj:
                pretrazeno.append(i)
        return pretrazeno

    def pretraga_po_datumu(self, lst, broj):
        pretrazeno = []
        for i in lst:
            if i.datum.lower().find(broj.lower()) != -1:
                pretrazeno.append(i)
        return pretrazeno

    def sortiranje_po_ukupnoj_cijeni(self, lst, smjer):
        for i in range(len(lst)-1):
            najmanji = i
            for j in range(i+1, len(lst)):
                if smjer == "+":
                    if lst[najmanji].ukupna_cijena > lst[j].ukupna_cijena:
                        najmanji = j
                elif smjer == "-":
                    if lst[najmanji].ukupna_cijena < lst[j].ukupna_cijena:
                        najmanji = j
                skladiste = lst[i]
                lst[i] = lst[najmanji]
                lst[najmanji] = skladiste
        return lst

    def sortiranje_po_datumu(self, lst, smjer):
        for i in range(len(lst)-1):
            najmanji = i
            for j in range(i+1, len(lst)):
                if smjer == "+":
                    if lst[najmanji].datum > lst[j].datum:
                        najmanju = j
                elif smjer == "-":
                    if lst[najmanji].datum < lst[j].datum:
                        najmanji = j
                skladiste = lst[i]
                lst[i] = lst[najmanji]
                lst[najmanji] = skladiste
        return lst

    def stavke_i_artikli_u_racunu(self, racun, lista_stavki, lista_artikala):
        stavke_i_artikli = []
        for i in lista_stavki:
            if i.racun == racun:
                for j in lista_artikala:
                    if i.artikal == j.oznaka:
                        stavke_i_artikli.append({'stavka': i, 'artikal': j})
        return stavke_i_artikli
