from Entiteti.identifikacija import Identifikacija

class Stavka(Identifikacija):
    
    def __init__(self, oznaka, kolicina, ukupna_cijena, artikal, racun):
        super().__init__(oznaka)
        self.kolicina = kolicina
        self.ukupna_cijena = ukupna_cijena
        self.artikal = artikal
        self.racun = racun

    
        # if self.kolicina <0:
        #     raise ValueError("Kolicina mora biti veca od 0!")
        # if self.ukupna_cijena <0:
        #     raise ValueError("Kolicina mora biti veca od 0!")
            
    
    def __str__(self):
        return f"{self.oznaka};{self.kolicina};{self.ukupna_cijena};{self.artikal};{self.racun}\n"