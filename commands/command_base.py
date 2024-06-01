from abc import ABC, abstractmethod

class Command(ABC):
    """
    Abstract base class for all commands in the game.
    """
    @abstractmethod
    def execute(self):
        """
        Execute the command.
        """
        pass

    @abstractmethod
    def undo(self):
        """
        Undo the command.
        """
        pass
