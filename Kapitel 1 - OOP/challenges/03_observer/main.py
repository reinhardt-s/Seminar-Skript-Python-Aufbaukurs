# Erstelle eine Observerklasse und implementiere diese in der zu erstellenden Klasse FireAlertSystem (Brandmeldeanlage)
# Erstelle in FireAlertSystem die Methode fire_detected() welche alle Observer benachrichtigt.
# Implementiere in den Klassen ExtinguishingSystem und EmergencyCall, die update() Methode:
# > ExtinguishingSystem: sobald die Brandmeldeanlage auslöst, sollen die Wasserzufuhr-Ventile geöffnet werden
#   und der aktuelle Restwasserstand ausgegeben werden.
# > EmergencyCall setzt einen Text-Notruf bei der Leitstelle ab.
from observer import Observer


class ExtinguishingSystem:
    def __init__(self):
        self.name = "Dam Break 22"
        self.water_supply = 2500
        self.valves_open_state = False

    def show_water_supply(self):
        """
        Gibt den aktuellen Restwasserstand aus.
        """
        print(f'Restlöschwasserstand: {self.water_supply} Liter')

    def set_valves_open(self, state: bool):
        """
        Öffnet oder schließt die Ventile zum Löschwasser

        :param state: True = offen, False = geschlossen
        """
        self.valves_open_state = state
        state = 'offen' if state is True else 'geschlossen'
        print(f'Die Ventile sind nun {state}.')


class EmergencyCall:
    """
    Setzt im Brandfall einen Notruf bei der Leitstelle ab.
    """

    def __init__(self):
        self.name = "E-Call 1433"

    def make_call(self):
        print(f'Setze Notruf ab.')
        print(f'...')
        print(f'Notruf abgesetzt.')


class FireAlertSystem(Observer):
    """
    Diese Brandmeldeanlage dient dazu, im Brandfall, alle angeschlossenen Systeme zu informieren,
    sodass diese entsprechend handeln können.
    """

    def __init__(self):
        self.name = "BAM!"
        super(FireAlertSystem, self).__init__()
        self.attach(ExtinguishingSystem())
        self.attach(EmergencyCall())


fas = FireAlertSystem()
fas.fire_detected()
