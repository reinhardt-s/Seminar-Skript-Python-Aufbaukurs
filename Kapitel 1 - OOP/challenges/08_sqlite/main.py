# Frage die Nutzer*in via Kommandozeile, für welche Stadt sie die Geo-Koordinaten sehen möchten
#
# Laden sie vorher alle Städte bzw. Gemeinden-Namen aus der Tabelle communities in die Liste communities.
#
# Durchsuche die Liste communities nach allen Einträgen,
# welche die Nutzer-Eingabe beinhalten: 'lin' findet unter anderem 'Berlin' und auch 'Lingenfeld'
#
# Präsentiere der Nutzer*in die Treffer und frage, welcher gemeint ist: 0: Berlin 1: Lingenfeld ...
#
# Frage abschließend von der Datenbank den Eintrag für community = gewählter Treffer ab und
# präsentiere in einem print-Statement, die Längen- und Breitengrade des Treffers
import sqlite3

DB_FILE = "./weather_data.db"


communities = []

