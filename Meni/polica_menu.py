from Meni.menu import Menu


class PolicaMenu(Menu):
    def __init__(self):
        self.options = {"0": "Nazad", "1": "Prikaz polica", "2": "Dodavanje polica",
                        "3": "Izmjena polica", "4": "Pretraga polica", "5": "Sortiranje polica", "6": "Prikaz artikala na polici"}
        super().__init__(self.options)

    def print_welcome_message(self):
        print()
        print("Rad sa policama")
