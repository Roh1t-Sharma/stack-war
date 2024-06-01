from .strategy_base import StrategyBase

class DefensiveStrategy(StrategyBase):
    def execute(self, army):
        print("Defensive Strategy: Strengthening defensive positions and protecting key units.")
        for unit in army:
            unit.defend()  # Assuming each unit has a defend method
