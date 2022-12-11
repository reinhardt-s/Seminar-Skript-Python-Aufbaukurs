from prettytable import PrettyTable

from modules.brew_module import BrewModule
from modules.display_module import DisplayModule
from modules.database_module import DatabaseModule
from modules.resource_subject import ResourceSubject
from modules.log import log


class AutomaticCoffeeBrewer(ResourceSubject):
    """
    Generische ACB-Klasse.
    Alle Kaffeeautomaten der Firma Kreide benutzen diese Funktionen.
    """
    def __init__(self):
        super().__init__()
        self.name = "ACB Default"
        log.debug(f"Initialisiere {self.name}")
        # Die standardmäßig zur Verfügung stehenden Ressourcen.
        self._resources = {
            "water": 1000,
            "beans": 500,
            "milk": 500,
            "coffee_ground": 500,
        }
        # TODO-2:  Füge die Module brew_module, display_module und database_module
        # als parameter hinzu

        # TODO-3:  Füge Module brew_module, display_module als Observer hinzu


    def brew(self, beverage: str):
        """
        Ruft das Brühmodul auf, um ein Getränk zuzubereiten.
        Passt anschließend die zur Verfügung stehenden Ressourcen an
        und informiert alles Observer über die Änderung.

        :param beverage: Name des Getränks
        """

        recipe = self.database.get_beverage_by_name(name=beverage)
        self.brew_module.brew(beverage, recipe)

        self._resources["water"] -= recipe["water"]
        self._resources["beans"] -= recipe["beans"]
        self._resources["milk"] -= recipe["milk"]
        self._resources["coffee_ground"] -= recipe["coffee_ground"]

        # TODO-4: Benachrichtige alles Observer, dass ein Getränk gebrüht wurde

    def get_resources(self):
        """
        Getter für die Ressourcen, da diese in einer privaten Variable gespeichert werden.

        :return: Dictionary mit den Ressourcen.
        """
        return self._resources

    def display_beverage_count(self):
        # TODO-5: Rufe das brew_module auf um die Anzahl an zubereiteten Getränken zu erhalten.
        #       Lasse das Ergebnis über das display_module ausgeben
        self.display.show(f"Gebrühte Getränke: {self.brew_module.get_beverage_count()}")

    def display_resources(self):
        """
        Ruft das Display-Modul auf, um anzuzeigen, wie viele Ressourcen noch z.V. stehen.
        :return:
        """
        resources_table = PrettyTable()
        resources_table.field_names = ["Ressource", "Menge"]
        resources_table.add_rows([[k, v] for k, v in self.get_resources().items()])
        self.display.show(resources_table)
