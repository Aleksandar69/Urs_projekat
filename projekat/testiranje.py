import unittest
from test1 import eat
from Logika.polica_rukovanje import Polica_rukovanje

class ActivityTests(unittest.TestCase):
    def test_eat_healthy(self):
        self.assertEqual(
            eat("broccoli", is_healthy=True),
                        "I'm eating broccoli")
    def test_eat_unhealthy(self):
        self.assertEqual(                
            eat("pizza", is_healthy=False),
                        "I'm eating pizza and I love it")


    def polica_entitet_duzina(self):
        police = Polica_rukovanje("police.txt")
        lista_polica = police.citanje_svih()
        print(len(lista_polica))