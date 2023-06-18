# https://docs.python.org/3/library/re.html

# Reguläre Ausdrücke (regex) sind ein mächtiges Werkzeug in der Programmierung, um Textmuster zu finden, zu überprüfen und zu manipulieren. In Python wird das re-Modul verwendet, um mit regulären Ausdrücken zu arbeiten. Hier sind einige grundlegende Funktionen und Beispiele:
#
# re.match(pattern, string): Überprüft, ob das Muster am Anfang des Strings vorhanden ist.
#
# re.search(pattern, string): Sucht das Muster irgendwo im String.
#
# re.findall(pattern, string): Gibt alle Übereinstimmungen des Musters im String als Liste von Strings zurück. Die Liste enthält die Übereinstimmungen in der Reihenfolge, in der sie im String gefunden werden.
#
# re.split(pattern, string, [maxsplit=0]): Teilt den String durch das Auftreten des Musters.
#
# re.sub(pattern, repl, string, [count=0]): Ersetzt alle Übereinstimmungen des Musters im String durch eine Ersatzzeichenkette.
#
# Bevor wir in die Beispiele einsteigen, hier ist ein kurzer Überblick über einige übliche Regex-Muster:
#
# . : Jedes einzelne Zeichen außer Zeilenumbruch
# ^ : Start der Zeichenkette
# $ : Ende der Zeichenkette
# * : Null oder mehr Wiederholungen
# + : Eine oder mehr Wiederholungen
# ? : Null oder eine Wiederholung
# \d : Ziffern (0-9)
# \D : Nicht-Ziffern
# \s : Weißraum (Leerzeichen, Tab, Zeilenumbruch etc.)
# \S : Nicht-Weißraum
# \w : Alphanumerische Zeichen (a-z, A-Z, 0-9) und Unterstrich (_)
# \W : Nicht-Wort-Zeichen

