from .command_base import Command

class AttackCommand(Command):
    def __init__(self, attacker, defender):
        self.attacker = attacker
        self.defender = defender
        self.damage_done = None  # To store the damage done for undoing

    def execute(self):
        print(f"{self.attacker} attacks {self.defender}.")
        self.damage_done = self.defender.take_damage(self.attacker.damage)  # Assuming units have damage attribute and method

    def undo(self):
        if self.damage_done is not None:
            print(f"Reverting {self.damage_done} damage to {self.defender}.")
            self.defender.heal(self.damage_done)  # Heal back the damage
