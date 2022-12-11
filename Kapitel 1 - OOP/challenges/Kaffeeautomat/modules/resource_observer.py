from abc import abstractmethod, ABC


class ResourceObserverInterface(ABC):
    """Interface für die Observer"""

    @abstractmethod
    def update(self, caller):
        """
        Wird vom Subject aufgerufen, sofern ein beobachteter Zustand sich ändert

        :param caller: Der Observer.
        """
        pass
