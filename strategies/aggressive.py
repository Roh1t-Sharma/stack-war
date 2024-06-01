from .strategy_base import StrategyBase

class AggressiveStrategy(StrategyBase):
    def execute(self, army):
        print("Aggressive Strategy: Maximizing attack on enemy positions.")
        for unit in army:
            unit.attack()  # Assuming each unit has an attack method
