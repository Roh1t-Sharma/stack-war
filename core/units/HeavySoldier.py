from abc import ABC

from core.units.unit import Unit


# noinspection PyCompatibility
class HeavySoldier(Unit, ABC):
    def __init__(self):
        super().__init__(hp=200, defense=200, close_range_damage=100, long_range_damage=0, dodge_chance=0.2,
                         cost=100, heal_amount=30)
        self.damage = 10

    def __str__(self):
        return super().__str__()
