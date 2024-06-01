from abc import ABC, abstractmethod

class Healable(ABC):
    @abstractmethod
    def heal(self, amount: int):
        """Heals the unit by the given amount."""
        pass
2