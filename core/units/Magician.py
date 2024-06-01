from core.units.unit import Unit
from core.interfaces.clonable import Cloneable

class Magician(Unit, Cloneable):
    def __init__(self):
        super().__init__(hp=50, defense=50, close_range_damage=25, long_range_damage=75, dodge_chance=0.5,
                         cost=200, heal_amount=15)

    def clone_unit(self, unit):
        if hasattr(unit, "clone"):
            return unit.clone()
        else:
            return None

    def tilt_and_place(self, most_expensive_unit):
        return "Moving most expensive unit in front."

    def __str__(self):
        return super().__str__() + ", Special Abilities: Clone and Tilt/Place"
