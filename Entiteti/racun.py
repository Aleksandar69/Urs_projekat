from Entiteti.identifikacija import Identifikacija

class Racun(Identifikacija):

    def __init__(self, oznaka, prodavac, ukupna_cijena, datum):
        super().__init__(oznaka)
        self.prodavac = prodavac
        self.ukupna_cijena = ukupna_cijena
        self.datum = datum

    def __str__(self):
        return f"{self.oznaka};{self.prodavac};{self.ukupna_cijena};{self.datum}\n"