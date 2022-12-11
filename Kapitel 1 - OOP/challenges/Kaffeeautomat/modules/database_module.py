import sqlite3
from datetime import datetime
from .log import log


class DatabaseModule:
    """
    Dieses Modul ermöglicht den Zugriff auf die ACB-Datenbank
    """
    def __init__(self):
        log.debug("Database module initialized")
        # TODO-10: Baue Verbindung zu Datenbank 'acb.db' auf
        #       und wähle als row_factory sqlite3.Row
        #       Setze anschließend den Cursor
        self.con = None
        self.con.row_factory = None
        self.cur = None

    def get_brew_count(self):
        """
        Gibt an, wie viele Getränke zubereitet wurden.

        :return: Gibt eine Row aus. In [0][0] ist gespeichert, wie viele Getränke zubereitet wurden.
        """
        res = self.cur.execute("SELECT COUNT(*) FROM statistics")
        count = res.fetchall()
        return count

    def add_entry(self, beverage: str):
        """
        Schreibt einen neuen Getränkeeintrag in die Datenbank.

        :param beverage: Name des Getränkes
        """
        self.cur.execute(f'INSERT INTO statistics VALUES (?, ?)', (datetime.now(), beverage))
        self.con.commit()

    def get_beverage_by_name(self, name):
        """
        Läd die für die Zubereitung eines Getränkes benötigten Ressourcen aus der Datenbank.

        :param name: Name des Getränkes
        :return: Dictionary mit den Ressourcennamen als Schlüssel und der benötigten Menge als Wert
        """
        res = self.cur.execute(f'SELECT water, beans, milk, coffee_ground FROM beverages where beverage_name = "{name}"')
        beverage = res.fetchone()
        return dict(zip(beverage.keys(), beverage))

    # TODO-11: Destructor aufrufen, darin die Datenbankverbindung schließe,
    #       anschließen über log die debug-Meldung "Database module closed" ausgeben
