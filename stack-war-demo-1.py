import pygame
import random

pygame.init()

clock = pygame.time.Clock()
fps = 60

# Game window
bottom_panel = 150
screen_width = 800
screen_height = 400 + bottom_panel

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Battle')


# Singleton pattern for game state management
class GameState:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(GameState, cls).__new__(cls)
            cls._instance.state = "Running"
        return cls._instance

    def get_state(self):
        return self._instance.state

    def set_state(self, state):
        self._instance.state = state


# Factory Method pattern for creating characters
class CharacterFactory:
    @staticmethod
    def create_character(type, x, y):
        if type == "knight":
            return Fighter(x, y, 'Knight', 30, 10, 3)
        elif type == "bandit":
            return Fighter(x, y, 'Bandit', 20, 6, 1)
        else:
            raise ValueError("Unknown character type")


# Abstract Factory pattern for creating different groups of characters
class AbstractCharacterFactory:
    def create_knight(self, x, y):
        pass

    def create_bandit(self, x, y):
        pass


class ConcreteCharacterFactory(AbstractCharacterFactory):
    def create_knight(self, x, y):
        return CharacterFactory.create_character("knight", x, y)

    def create_bandit(self, x, y):
        return CharacterFactory.create_character("bandit", x, y)


# Prototype pattern for copying characters
class Prototype:
    def clone(self):
        pass


class Fighter(Prototype):
    def __init__(self, x, y, name, max_hp, strength, potions):
        self.name = name
        self.max_hp = max_hp
        self.hp = max_hp
        self.strength = strength
        self.start_potions = potions
        self.potions = potions
        self.alive = True
        self.animation_list = []
        self.frame_index = 0
        self.action = 0  # 0: idle, 1: attack, 2: hurt, 3: dead
        self.update_time = pygame.time.get_ticks()
        # Load idle images
        temp_list = []
        for i in range(8):
            img = pygame.image.load(f'img/{self.name}/Idle/{i}.png')
            img = pygame.transform.scale(img, (img.get_width() * 3, img.get_height() * 3))
            temp_list.append(img)
        self.animation_list.append(temp_list)
        # Load attack images
        temp_list = []
        for i in range(8):
            img = pygame.image.load(f'img/{self.name}/Attack/{i}.png')
            img = pygame.transform.scale(img, (img.get_width() * 3, img.get_height() * 3))
            temp_list.append(img)
        self.animation_list.append(temp_list)
        # Load hurt images
        temp_list = []
        for i in range(3):
            img = pygame.image.load(f'img/{self.name}/Hurt/{i}.png')
            img = pygame.transform.scale(img, (img.get_width() * 3, img.get_height() * 3))
            temp_list.append(img)
        self.animation_list.append(temp_list)
        # Load death images
        temp_list = []
        for i in range(10):
            img = pygame.image.load(f'img/{self.name}/Death/{i}.png')
            img = pygame.transform.scale(img, (img.get_width() * 3, img.get_height() * 3))
            temp_list.append(img)
        self.animation_list.append(temp_list)
        self.image = self.animation_list[self.action][self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def update(self):
        animation_cooldown = 100
        # Handle animation
        # Update image
        self.image = self.animation_list[self.action][self.frame_index]
        # Check if enough time has passed since the last update
        if pygame.time.get_ticks() - self.update_time > animation_cooldown:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
        # If the animation has run out then reset back to the start
        if self.frame_index >= len(self.animation_list[self.action]):
            if self.action == 3:
                self.frame_index = len(self.animation_list[self.action]) - 1
            else:
                self.idle()

    def idle(self):
        # Set variables to idle animation
        self.action = 0
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()

    def attack(self, target):
        # Deal damage to enemy
        rand = random.randint(-5, 5)
        damage = self.strength + rand
        target.hp -= damage
        # Run enemy hurt animation
        target.hurt()
        # Check if target has died
        if target.hp < 1:
            target.hp = 0
            target.alive = False
            target.death()
        damage_text = DamageText(target.rect.centerx, target.rect.y, str(damage), red)
        damage_text_group.add(damage_text)
        # Set variables to attack animation
        self.action = 1
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()

    def hurt(self):
        # Set variables to hurt animation
        self.action = 2
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()

    def death(self):
        # Set variables to death animation
        self.action = 3
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()

    def reset(self):
        self.alive = True
        self.potions = self.start_potions
        self.hp = self.max_hp
        self.frame_index = 0
        self.action = 0
        self.update_time = pygame.time.get_ticks()

    def draw(self):
        screen.blit(self.image, self.rect)

    def clone(self):
        return Fighter(self.rect.centerx, self.rect.centery, self.name, self.max_hp, self.strength, self.potions)


# Builder pattern for constructing complex objects
class FighterBuilder:
    def __init__(self):
        self.reset()

    def reset(self):
        self._fighter = Fighter(0, 0, '', 0, 0, 0)

    def set_position(self, x, y):
        self._fighter.rect.center = (x, y)
        return self

    def set_name(self, name):
        self._fighter.name = name
        return self

    def set_stats(self, max_hp, strength, potions):
        self._fighter.max_hp = max_hp
        self._fighter.hp = max_hp
        self._fighter.strength = strength
        self._fighter.potions = potions
        self._fighter.start_potions = potions
        return self

    def build(self):
        result = self._fighter
        self.reset()
        return result


# Adapter pattern for interfacing with the button library
class Button:
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self):
        action = False
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
                self.clicked = True
                action = True
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False
        screen.blit(self.image, (self.rect.x, self.rect.y))
        return action


# Decorator pattern for extending functionality of Fighter class
class FighterDecorator(Fighter):
    def __init__(self, fighter, x, y, name, max_hp, strength, potions):
        super().__init__(x, y, name, max_hp, strength, potions)
        self._fighter = fighter

    def attack(self, target):
        print(f"{self._fighter.name} is attacking!")
        self._fighter.attack(target)

    def draw(self):
        self._fighter.draw()

    def __getattr__(self, name):
        return getattr(self._fighter, name)


# Facade pattern to simplify interaction with complex subsystems
class GameFacade:
    def __init__(self):
        self.state = GameState()
        self.character_factory = ConcreteCharacterFactory()

    def create_knight(self, x, y):
        return self.character_factory.create_knight(x, y)

    def create_bandit(self, x, y):
        return self.character_factory.create_bandit(x, y)

    def get_game_state(self):
        return self.state.get_state()

    def set_game_state(self, state):
        self.state.set_state(state)


# Proxy pattern for controlling access to the fighter's health
class HealthProxy:
    def __init__(self, fighter):
        self._fighter = fighter

    def get_hp(self):
        return self._fighter.hp

    def set_hp(self, value):
        if value < 0:
            self._fighter.hp = 0
        elif value > self._fighter.max_hp:
            self._fighter.hp = self._fighter.max_hp
        else:
            self._fighter.hp = value


# Composite pattern for grouping game objects
class Composite:
    def __init__(self):
        self.children = []

    def add(self, child):
        self.children.append(child)

    def remove(self, child):
        self.children.remove(child)

    def draw(self):
        for child in self.children:
            child.draw()


# Bridge pattern for separating abstraction from implementation
class HealthBar:
    def __init__(self, x, y, hp, max_hp):
        self.x = x
        self.y = y
        self.hp = hp
        self.max_hp = max_hp

    def draw(self, hp):
        self.hp = hp
        ratio = self.hp / self.max_hp
        pygame.draw.rect(screen, red, (self.x, self.y, 150, 20))
        pygame.draw.rect(screen, green, (self.x, self.y, 150 * ratio, 20))


# Command pattern for handling player actions
class Command:
    def execute(self):
        pass


class AttackCommand(Command):
    def __init__(self, attacker, target):
        self.attacker = attacker
        self.target = target

    def execute(self):
        self.attacker.attack(self.target)


class PotionCommand(Command):
    def __init__(self, fighter, potion_effect):
        self.fighter = fighter
        self.potion_effect = potion_effect

    def execute(self):
        if self.fighter.potions > 0:
            if self.fighter.max_hp - self.fighter.hp > self.potion_effect:
                heal_amount = self.potion_effect
            else:
                heal_amount = self.fighter.max_hp - self.fighter.hp
            self.fighter.hp += heal_amount
            self.fighter.potions -= 1
            damage_text = DamageText(self.fighter.rect.centerx, self.fighter.rect.y, str(heal_amount), green)
            damage_text_group.add(damage_text)


# Strategy pattern for different enemy behaviors
class Strategy:
    def execute(self, fighter, target):
        pass


class AggressiveStrategy(Strategy):
    def execute(self, fighter, target):
        fighter.attack(target)


class DefensiveStrategy(Strategy):
    def execute(self, fighter, target):
        if (fighter.hp / fighter.max_hp) < 0.5 and fighter.potions > 0:
            potion_command = PotionCommand(fighter, 15)
            potion_command.execute()
        else:
            fighter.attack(target)


# Define fonts
font = pygame.font.SysFont('Times New Roman', 26)

# Define colors
red = (255, 0, 0)
green = (0, 255, 0)

# Load images
background_img = pygame.image.load('img/Background/game_background_2.png').convert_alpha()
panel_img = pygame.image.load('img/Icons/panel.png').convert_alpha()
potion_img = pygame.image.load('img/Icons/potion.png').convert_alpha()
restart_img = pygame.image.load('img/Icons/restart.png').convert_alpha()
victory_img = pygame.image.load('img/Icons/victory.png').convert_alpha()
defeat_img = pygame.image.load('img/Icons/defeat.png').convert_alpha()
sword_img = pygame.image.load('img/Icons/sword.png').convert_alpha()


# Create function for drawing text
def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))


# Function for drawing background
def draw_bg():
    screen.blit(background_img, (0, 0))


# Function for drawing panel
def draw_panel():
    screen.blit(panel_img, (0, screen_height - bottom_panel))
    draw_text(f'{knight.name} HP: {knight.hp}', font, red, 100, screen_height - bottom_panel + 10)
    for count, i in enumerate(bandit_list):
        draw_text(f'{i.name} HP: {i.hp}', font, red, 550, (screen_height - bottom_panel + 10) + count * 60)


class DamageText(pygame.sprite.Sprite):
    def __init__(self, x, y, damage, colour):
        pygame.sprite.Sprite.__init__(self)
        self.image = font.render(damage, True, colour)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.counter = 0

    def update(self):
        self.rect.y -= 1
        self.counter += 1
        if self.counter > 30:
            self.kill()


damage_text_group = pygame.sprite.Group()

# Initialize the game state and character factory
game_facade = GameFacade()

# Create characters
knight = game_facade.create_knight(200, 260)
bandit1 = game_facade.create_bandit(550, 270)
bandit2 = game_facade.create_bandit(700, 270)
bandit_list = [bandit1, bandit2]

# Create health bars
knight_health_bar = HealthBar(100, screen_height - bottom_panel + 40, knight.hp, knight.max_hp)
bandit1_health_bar = HealthBar(550, screen_height - bottom_panel + 40, bandit1.hp, bandit1.max_hp)
bandit2_health_bar = HealthBar(550, screen_height - bottom_panel + 100, bandit2.hp, bandit2.max_hp)

# Create buttons
potion_button = Button(100, screen_height - bottom_panel + 70, potion_img, 0.5)
restart_button = Button(330, 120, restart_img, 0.5)

# Set initial variables
current_fighter = 1
total_fighters = 3
action_cooldown = 0
action_wait_time = 90
attack = False
potion = False
potion_effect = 15
clicked = False
game_over = 0

# Main game loop
run = True
while run:

    clock.tick(fps)

    # Draw background
    draw_bg()

    # Draw panel
    draw_panel()
    knight_health_bar.draw(knight.hp)
    bandit1_health_bar.draw(bandit1.hp)
    bandit2_health_bar.draw(bandit2.hp)

    # Draw fighters
    knight.update()
    knight.draw()
    for bandit in bandit_list:
        bandit.update()
        bandit.draw()

    # Draw the damage text
    damage_text_group.update()
    damage_text_group.draw(screen)

    # Control player actions
    attack = False
    potion = False
    target = None
    pygame.mouse.set_visible(True)
    pos = pygame.mouse.get_pos()
    for count, bandit in enumerate(bandit_list):
        if bandit.rect.collidepoint(pos):
            pygame.mouse.set_visible(False)
            screen.blit(sword_img, pos)
            if clicked and bandit.alive:
                attack = True
                target = bandit_list[count]
    if potion_button.draw():
        potion = True
    draw_text(str(knight.potions), font, red, 150, screen_height - bottom_panel + 70)

    if game_over == 0:
        if knight.alive:
            if current_fighter == 1:
                action_cooldown += 1
                if action_cooldown >= action_wait_time:
                    if attack and target:
                        attack_command = AttackCommand(knight, target)
                        attack_command.execute()
                        current_fighter += 1
                        action_cooldown = 0
                    if potion:
                        potion_command = PotionCommand(knight, potion_effect)
                        potion_command.execute()
                        current_fighter += 1
                        action_cooldown = 0
        else:
            game_over = -1

        for count, bandit in enumerate(bandit_list):
            if current_fighter == 2 + count:
                if bandit.alive:
                    action_cooldown += 1
                    if action_cooldown >= action_wait_time:
                        strategy = AggressiveStrategy() if random.random() < 0.5 else DefensiveStrategy()
                        strategy.execute(bandit, knight)
                        current_fighter += 1
                        action_cooldown = 0
                else:
                    current_fighter += 1

        if current_fighter > total_fighters:
            current_fighter = 1

    alive_bandits = sum(bandit.alive for bandit in bandit_list)
    if alive_bandits == 0:
        game_over = 1

    if game_over != 0:
        if game_over == 1:
            screen.blit(victory_img, (250, 50))
        if game_over == -1:
            screen.blit(defeat_img, (290, 50))
        if restart_button.draw():
            knight.reset()
            for bandit in bandit_list:
                bandit.reset()
            current_fighter = 1
            action_cooldown = 0
            game_over = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            clicked = True
        else:
            clicked = False

    pygame.display.update()

pygame.quit()
