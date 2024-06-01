from core.units.unit import Unit
from core.interfaces.clonable import Cloneable
from .HeavySoldier import HeavySoldier  # Assuming HeavySoldier is in the same directory

class LightSoldier(Unit, Cloneable):
    def __init__(self):
        super().__init__(hp=100, defense=100, close_range_damage=75, long_range_damage=0, dodge_chance=0.5,
                         cost=50, heal_amount=20)

    def clone(self):
        return LightSoldier()

    def buff(self, other):
        if isinstance(other, HeavySoldier):
            other.hp += 20
            other.damage += 10
        return "Buffing heavy soldier!"

    def __str__(self):
        return super().__str__()
