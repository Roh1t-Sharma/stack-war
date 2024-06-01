# building_factory.py
from core.units.WanderZone import WanderZone

class BuildingFactory:
    @staticmethod
    def create_building(building_type):
        """ Factory method to create buildings based on the building type. """
        if building_type == "wander_zone":
            return WanderZone()
        else:
            raise ValueError("Unknown building type")

# As with the unit factory, this structure allows for easy expansion
# by adding new building types as needed.
