import pygame
import sys
from .stats_view import StatsView  # Import StatsView

class GameView:
    def __init__(self, width=800, height=600):
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption('Game Title')
        self.clock = pygame.time.Clock()  # Clock to control game refresh rate
        self.running = True
        self.stats_view = StatsView(self)  # Initialize the stats view here

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.screen.fill((0, 0, 0))  # Clear the screen with black

            # Update game logic here (e.g., movement, collision detection)

            self.draw_units()  # You would implement this to draw game units
            self.stats_view.draw()  # Draw the stats view

            pygame.display.flip()  # Update the full display Surface to the screen
            self.clock.tick(60)  # Maintain 60 frames per second

        pygame.quit()
        sys.exit()

    def draw_units(self):
        # Placeholder function to draw game units
        # For example, drawing a sprite:
        # self.screen.blit(sprite_image, (x, y))
        pass

if __name__ == "__main__":
    game = GameView()
    game.run()
