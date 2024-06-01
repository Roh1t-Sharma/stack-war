from abc import ABC, abstractmethod


class StrategyBase(ABC):
    """
    Abstract base class for all strategies in the game. Defines the common interface for all concrete strategies.
    """

    @abstractmethod
    def execute(self, army):
        """
        Executes the strategy for the given army.

        :param army: The army to execute the strategy on
        """
        pass
