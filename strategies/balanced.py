from .strategy_base import StrategyBase

class BalancedStrategy(StrategyBase):
    def execute(self, army):
        print("Balanced Strategy: Adapting to current battlefield conditions.")
        for unit in army:
            if unit.should_attack():  # Assuming units can decide if they should attack
                unit.attack()
            else:
                unit.defend()
