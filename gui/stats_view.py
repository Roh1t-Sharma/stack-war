import pygame

class StatsView:
    def __init__(self, game_view):
        self.game_view = game_view
        self.font = pygame.font.Font(None, 36)  # Default font and size

    def draw(self):
        # Assuming you have some game state you want to display, like health
        health_text = self.font.render(f'Health: {self.game_view.game_state.health}', True, (255, 0, 0))
        self.game_view.screen.blit(health_text, (10, 10))

        # Display other stats similarly
        # score_text = self.font.render(f'Score: {self.game_view.game_state.score}', True, (255, 255, 255))
        # self.game_view.screen.blit(score_text, (10, 50))
