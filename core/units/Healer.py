from core.units.unit import Unit
from core.interfaces.healable import Healable

class Healer(Unit, Healable):
    def __init__(self):
        super().__init__(hp=100, defense=150, close_range_damage=50, long_range_damage=0, dodge_chance=0.2,
                         cost=150, heal_amount=0)

    def heal(self, unit):
        if hasattr(unit, 'heal_amount'):
            unit.hp += unit.heal_amount
            return f"Healing {unit} for {unit.heal_amount} HP"
        return "Can't heal this unit"

    def __str__(self):
        return super().__str__() + ", Healing Power: Self-healing not available"
