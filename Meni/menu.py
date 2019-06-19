class Menu:
    def __init__(self, options):
        self.options = options

    def ask_for_menu_option(self):
        option = "-1"
        while option not in self.options:
            self.print_menu_options()
            option = input("Izaberite opciju: ")
        return option

    def print_menu_options(self):
        for key, value in self.options.items():
            print(f"{key} -> {value}")
