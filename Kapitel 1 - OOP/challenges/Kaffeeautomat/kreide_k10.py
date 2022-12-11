# TODO-1:  Diese Klasse erbt von AutomaticCoffeeBrewer
#        Überschreibe sowohl name als auch resources
#        > name: ACB k10
#        > resources:
#        > water: 2500
#        > beans: 1000
#        > milk: 1000
#        > coffee_ground_max: 500

from kreide_standard import AutomaticCoffeeBrewer


class AutomaticCoffeeBrewerK10(AutomaticCoffeeBrewer):
    """
    Die ACB Kreide K10 erbt die Grundfunktionen der generischen ACB.
    Sie hat jedoch für die meisten Ressourcen, ein größeres Fassungsvermögen.
    """

    def __int__(self):
        pass