# https://www.geeksforgeeks.org/with-statement-in-python/
# with open("log.txt", mode="a") as file:
#     file.write(f"Meine Nachricht\n")
#
# __name__

# Schreibe einen Decorator log(message) der folgenden Funktionen erfüllt:
# > Der Decorator nimmt ein string Argument "message" an
# > Die dekorierte Funktion kann 1 - n Argumente haben
# > Der Decorator schreibt in die Datei log.txt folgende Zeilen:
#   > "Von: {name_der_aufrufenden_funktion}: {message}\n
#   > "Kosten: {value Argument}\n"

bill = 0

# Hier dein Decorator

@log(message="Füge Steuern hinzu.")
def add_tax(value):
    return round(value * 1.19, 2)


@log(message="Füge Artikel hinzu.")
def add_article_to_bill(value):
    global bill
    bill += value


add_article_to_bill(value=14.50)
add_article_to_bill(value=32.60)
add_article_to_bill(value=14.33)

print(add_tax(value=bill))
