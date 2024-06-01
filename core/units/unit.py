from abc import ABC, abstractmethod

class Unit(ABC):
    """
    Abstract base class for all units in the game.
    """
    def __init__(self, hp, defense, close_range_damage, long_range_damage, dodge_chance, cost, heal_amount):
        self.hp = hp
        self.defense = defense
        self.close_range_damage = close_range_damage
        self.long_range_damage = long_range_damage
        self.dodge_chance = dodge_chance
        self.cost = cost
        self.heal_amount = heal_amount

    @abstractmethod
    def perform_action(self):
        """
        Perform an action unique to the unit.
        This needs to be implemented by all subclasses.
        """
        pass

    def take_damage(self, amount):
        """
        Reduces the unit's hp by the damage amount after considering defense.
        """
        effective_damage = max(amount - self.defense, 0)
        self.hp -= effective_damage
        return effective_damage

    def __str__(self):
        """
        Returns a string representation of the unit.
        """
        return f"{self.__class__.__name__} - HP: {self.hp}, Defense: {self.defense}, Heal Amount: {self.heal_amount}"
