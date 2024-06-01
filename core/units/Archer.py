from core.interfaces.clonable import Cloneable
from core.units.unit import Unit

class Archer(Unit, Cloneable):
    def __init__(self):
        # Initialize with the common properties defined in Unit
        super().__init__(hp=100, defense=50, close_range_damage=25, long_range_damage=75, dodge_chance=0.7,
                         cost=75, heal_amount=25)

    def clone(self):
        """
        Create a clone of this Archer using the Prototype pattern.
        """
        return Archer()

    def perform_action(self):
        """
        Implements the Archer's specific action.
        """
        return self.shoot()

    def shoot(self):
        """
        Represents the Archer shooting an arrow.
        """
        return "Shooting an arrow!"

    def __str__(self):
        return super().__str__() + f", Long Range Damage: {self.long_range_damage}"
