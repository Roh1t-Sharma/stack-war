from core.units.unit import Unit

class WanderZone(Unit):
    def __init__(self):
        # Initialize Wander Zone with high health and defense, but no damage capabilities
        super().__init__(hp=200, defense=200, close_range_damage=0, long_range_damage=0, dodge_chance=0, cost=100, heal_amount=0)

    def perform_action(self):
        """
        The Wander Zone does not perform conventional actions but enhances the defense of nearby units.
        This method would be implemented to simulate this effect in a game scenario.
        """
        return "Enhancing defense of nearby units"

    def __str__(self):
        return super().__str__() + ", Role: Defensive structure"
