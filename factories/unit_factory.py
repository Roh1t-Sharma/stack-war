# unit_factory.py
from core.units.LightSoldier import LightSoldier
from core.units.Magician import Magician
from core.units.HeavySoldier import HeavySoldier
from core.units.Archer import Archer
from core.units.Healer import Healer

class UnitFactory:
    @staticmethod
    def create_unit(unit_type):
        """ Factory method to create units based on the unit type. """
        if unit_type == "light_soldier":
            return LightSoldier()
        elif unit_type == "magician":
            return Magician()
        elif unit_type == "heavy_soldier":
            return HeavySoldier()
        elif unit_type == "archer":
            return Archer()
        elif unit_type == "healer":
            return Healer()
        else:
            raise ValueError("Unknown unit type")

# This makes it easy to add new unit types without modifying existing code,
# adhering to the Open/Closed Principle.
