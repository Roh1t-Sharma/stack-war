from .command_base import Command

class HealCommand(Command):
    def __init__(self, healer, target, amount):
        self.healer = healer
        self.target = target
        self.amount = amount
        self.healed_amount = None  # To store the actual healed amount for undoing

    def execute(self):
        print(f"{self.healer} heals {self.target} for {self.amount} HP.")
        self.healed_amount = self.target.heal(self.amount)  # Assuming heal method correctly returns healed amount

    def undo(self):
        if self.healed_amount:
            print(f"Reverting {self.healed_amount} healing from {self.target}.")
            self.target.take_damage(self.healed_amount)  # Apply damage to revert healing
