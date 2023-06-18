# Erstelle eine Datenbank mit folgenden Tabellen:
# warehouse:
# id (integer, primary key)
# product (text)
# amount (integer)
# price (real)
# reorder_level (integer)
#
# sales:
# id (integer, primary key)
# product (id aus warehouse)
# amount (integer)
# price (real)
# customer (integer aus customer)
# date (text)
#
# customer:
# id (integer, primary key)
# name (text)
# address (text)
# city (text)
# country (text)
#
# Benutze folgende Insert-Befehle, um Daten in die Tabellen einzufügen:
# warehouse:
# INSERT INTO warehouse (product, amount, price, reorder_level) VALUES ('Schraube 3x30 metrisch', 312, 0.17, 50)
# INSERT INTO warehouse (product, amount, price, reorder_level) VALUES ('Stahlplatte 5000x2000x5', 15, 2494, 7)
# INSERT INTO warehouse (product, amount, price, reorder_level) VALUES ('Drallrohr', 40, 4994, 10)
#
# customer:
# INSERT INTO customer (name, address, city, country) VALUES ('Müller GmbH', 'Hauptstraße 1', 'Berlin', 'Deutschland')
# INSERT INTO customer (name, address, city, country) VALUES ('Schmidt KG', 'Hauptstraße 2', 'Wien', 'Österreich
# INSERT INTO customer (name, address, city, country) VALUES ('Meyer AG', 'Hauptstraße 3', 'Zürich', 'Schweiz')
#
# sales:
# INSERT INTO sales (product, amount, price, customer, date) VALUES (1, 100, 0.17, 1, '2023-01-01')
# INSERT INTO sales (product, amount, price, customer, date) VALUES (2, 1, 2494, 2, '2023-01-01')
# INSERT INTO sales (product, amount, price, customer, date) VALUES (3, 1, 4994, 3, '2023-01-01')
# INSERT INTO sales (product, amount, price, customer, date) VALUES (1, 100, 0.17, 1, '2023-01-02')
# INSERT INTO sales (product, amount, price, customer, date) VALUES (2, 1, 2494, 2, '2023-01-02')
# INSERT INTO sales (product, amount, price, customer, date) VALUES (3, 1, 4994, 3, '2023-01-02')
#
# Gebe auf der Konsole alle Produkte aus die an die Schmid KG verkauft wurden.


