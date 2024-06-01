from .command_base import Command

class MoveCommand(Command):
    def __init__(self, unit, new_position):
        self.unit = unit
        self.new_position = new_position
        self.prev_position = unit.position  # Assuming unit has a position attribute

    def execute(self):
        print(f"Moving {self.unit} to position {self.new_position}.")
        self.unit.position = self.new_position  # Update unit's position

    def undo(self):
        print(f"Moving {self.unit} back to position {self.prev_position}.")
        self.unit.position = self.prev_position  # Revert to previous position
