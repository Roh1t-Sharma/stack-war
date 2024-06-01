from abc import ABC, abstractmethod
from core.units.unit import Unit  # Assuming unit.py is in the units directory and has a base Unit class

class Cloneable(ABC):
    @abstractmethod
    def clone(self) -> Unit:
        """Creates and returns a clone of this unit."""
        pass
