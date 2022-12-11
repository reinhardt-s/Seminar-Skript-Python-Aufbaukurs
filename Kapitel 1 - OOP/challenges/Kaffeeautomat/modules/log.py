from enum import Enum


# TODO-14: Führe den Enumerator LogLeve ein. Die LogLevel sind
#       DEBUG = 3
#       INFO = 2
#       PRODUCTION = 1
#       Ersetze in der Klasse Logger die entsprechenden int-Werte durch den passenden Enum
#       Ersetze auch den Wert in LOG_LEVEL durch den passenden Enum

class LogLevel(Enum):
    DEBUG = 3
    INFO = 2
    PRODUCTION = 1


LOG_LEVEL = 2


class Logger:
    def debug(self, message):
        if LOG_LEVEL >= 3:
            print(f'DEBUG:\t{message}')

    def info(self, message):
        if LOG_LEVEL >= 2:
            print(f'INFO:\t{message}')

    def production(self, message):
        if LOG_LEVEL >= 1:
            print(f'PRODUCTION:\t{message}')


log = Logger()
