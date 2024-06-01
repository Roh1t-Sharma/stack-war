import pygame
import sys

pygame.init()

# Screen dimensions
bottom_panel = 225
screen_width = 1440
screen_height = 560 + bottom_panel
screen = pygame.display.set_mode((screen_width, screen_height))

# Colors
WHITE = (255, 255, 255)

# Clock for controlling frame rate
clock = pygame.time.Clock()

class Soldier(pygame.sprite.Sprite):
    def __init__(self, images, x, y, scale=1):
        super().__init__()
        self.images = [pygame.transform.scale(pygame.image.load(image).convert_alpha(),
                        (int(pygame.image.load(image).get_width() * scale),
                         int(pygame.image.load(image).get_height() * scale)))
                       for image in images]
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.animation_speed = 0.2
        self.current_time = 0

    def update(self, *args):
        self.current_time += self.animation_speed
        if self.current_time >= 1:
            self.current_time = 0
            self.index = (self.index + 1) % len(self.images)
            self.image = self.images[self.index]

        # Constrain movement within screen bounds
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.x + self.rect.width > screen_width:
            self.rect.x = screen_width - self.rect.width
        if self.rect.y < 0:
            self.rect.y = 0
        elif self.rect.y + self.rect.height > screen_height - bottom_panel:
            self.rect.y = screen_height - bottom_panel - self.rect.height

class Enemy(pygame.sprite.Sprite):
    def __init__(self, image, x, y, scale=1):
        super().__init__()
        self.image = pygame.image.load(image).convert_alpha()
        self.image = pygame.transform.scale(self.image, (int(self.image.get_width() * scale), int(self.image.get_height() * scale)))
        self.image = pygame.transform.flip(self.image, True, False)  # Flip the image horizontally
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        # Constrain movement within screen bounds
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.x + self.rect.width > screen_width:
            self.rect.x = screen_width - self.rect.width
        if self.rect.y < 0:
            self.rect.y = 0
        elif self.rect.y + self.rect.height > screen_height - bottom_panel:
            self.rect.y = screen_height - bottom_panel - self.rect.height

# BattleGround Background
background_image = pygame.image.load('/Users/rohitsharma/PycharmProjects/stack-war/Battleground_forest/PNG/game_background_4/game_background_4.png')
background_image = pygame.transform.scale(background_image, (screen_width, screen_height - bottom_panel))

# Panel
panel_image = pygame.image.load('/Users/rohitsharma/PycharmProjects/stack-war/Battleground_forest/PNG/panel.png')
panel_image = pygame.transform.scale(panel_image, (screen_width, bottom_panel))

# soldier walking animation images
soldier_images = ['Units/PNG/Knight/Walk/walk1.png', 'Units/PNG/Knight/Walk/walk2.png', 'Units/PNG/Knight/Walk/walk3.png', 'Units/PNG/Knight/Walk/walk4.png', 'Units/PNG/Knight/Walk/walk5.png', 'Units/PNG/Knight/Walk/walk6.png']

# Create a soldier instance
soldier = Soldier(soldier_images, 80, 220)
# Create enemy instances
enemy = Enemy('/Users/rohitsharma/PycharmProjects/stack-war/Units/PNG/Rogue/rogue.png', 1270, 220)

all_sprites = pygame.sprite.Group()
enemy_sprites = pygame.sprite.Group()

all_sprites.add(soldier)
all_sprites.add(enemy)
enemy_sprites.add(enemy)

# Load and play background music
pygame.mixer.music.load('/Users/rohitsharma/PycharmProjects/stack-war/Pixel Song 3.mp3')
pygame.mixer.music.play(-1)  # Loop indefinitely

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Handle keyboard input for soldier movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        soldier.rect.x -= 5
    if keys[pygame.K_RIGHT]:
        soldier.rect.x += 5
    if keys[pygame.K_UP]:
        soldier.rect.y -= 5
    if keys[pygame.K_DOWN]:
        soldier.rect.y += 5

    # Check for collision
    if pygame.sprite.spritecollideany(soldier, enemy_sprites):
        print("Collision detected!")

    # Update sprites
    all_sprites.update()

    # Drawing code
    screen.blit(background_image, (0, 0))
    screen.blit(panel_image, (0, screen_height - bottom_panel))

    all_sprites.draw(screen)

    # Flip the display
    pygame.display.flip()

    # Limit frames per second
    clock.tick(60)
