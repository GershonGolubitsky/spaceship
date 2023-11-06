from settings import Settings
from spaceship import Spaceship
from fire import Fire
from invaders import Invaders
import random
import pygame


class Manager_game(pygame.sprite.Sprite):
    """Class definition for the game manager, responsible for controlling game flow and elements."""
    """The constructor for the Manager_game class"""

    def __init__(self):
        """Invokes the constructor of the parent class"""
        super().__init__()
        self.spaceship = Spaceship()
        """Create the spaceship object"""
        self.invaders = Invaders()
        """Create the invaders object"""
        self.grop_fire_invaders = pygame.sprite.Group()
        """Create a group for invaders' projectiles"""
        self.grop_fire_spaceship = pygame.sprite.Group()
        """Create a group for spaceship-fired projectiles"""
        self.screen = pygame.display.set_mode((Settings.SCREEN_WIDTH, Settings.SCREEN_HEIGHT))
        """Initialize the game window with the specified dimensions"""
        self.space_pressed = False
        """Flag to track if the spacebar is pressed"""
        self.test = 0
        """Counter for controlling firing frequency"""
        self.game_over = False
        """Flag to indicate if the game is over"""
        self.spaceship_lives = 3
        """Initialize the number of spaceship lives"""
        self.score = 0
        """Nitialize the player's score"""
        self.speed_invaders = 3
        """Set the initial speed of invaders"""
        self.speed_invaders_y = 0
        """Initialize the vertical speed of invaders"""

    def start_game(self):
        """Initialize the Pygame library"""
        pygame.init()
        """Set the window title"""
        pygame.display.set_caption('INVADERS_SPACE')
        """Create the group of all invaders"""
        self.invaders.all_invaders_group()

    def run_game(self):
        self.screen.blit(Settings.img_background, (0, 0))
        """Display the game background on the screen"""
        self.screen.blit(self.spaceship.image, self.spaceship.rect_spaceship)
        """Display the spaceship on the screen at its current position"""
        pygame.draw.line(self.screen, (0, 255, 0), (0, self.spaceship.rect_spaceship.bottom),
                         (Settings.SCREEN_WIDTH, self.spaceship.rect_spaceship.bottom), 2)
        """Draw a green line at the bottom of the screen to separate the spaceship from the game area"""
        font = pygame.font.Font(None, 36)
        lives_text = font.render(f"Lives: {self.spaceship_lives}", True, (255, 255, 255))
        self.screen.blit(lives_text, (10, 10))
        """Display the remaining lives of the spaceship in the top-left corner"""
        score_text = font.render(f"Score: {self.score}", True, (255, 255, 255))
        self.screen.blit(score_text, (Settings.SCREEN_WIDTH - 150, 10))
        """Display the player's score in the top-right corner"""

    def direction(self):
        """Updates the direction of the spaceship based on the keyboשard keys that are pressed."""

        # Get all of the keys that are currently pressed
        all_key = pygame.key.get_pressed()

        # If the right arrow key is pressed, move the spaceship to the right
        if all_key[pygame.K_RIGHT]:
            self.spaceship.fly('right')

        # If the left arrow key is pressed, move the spaceship to the left
        if all_key[pygame.K_LEFT]:
            self.spaceship.fly('left')

    def fire_spaceship(self):
        all_key = pygame.key.get_pressed()
        if all_key[pygame.K_SPACE] and not self.space_pressed:
            # Check if the spacebar is pressed and the space is not already pressed
            self.grop_fire_spaceship.add(self.spaceship.firing_spaceShip())
            # Create a spaceship-fired projectile and add it to the group
            self.space_pressed = True
            # Set the space_pressed flag to True to prevent continuous firing
        elif not all_key[pygame.K_SPACE]:
            # If the spacebar is not pressed
            self.space_pressed = False
            # Reset the space_pressed flag to allow firing when spacebar is pressed again

    def fire_invaders(self):
        """Create a list of invaders"""
        invaders_list = list(self.invaders.grop_invaders)
        if invaders_list:
            # Check if there are any invaders left to shoot
            # If there are invaders, select one randomly from the list
            invader = random.choice(invaders_list)
            # Create a fire projectile from just below the selected invader
            fire = Fire(invader.rect.midbottom, 1, 'invaders')
            # Add the fire projectile to the invaders' projectile group
            if self.test == 0:
                # Check if the "test" variable is equal to 0
                # If it is, add the fire projectile to the group
                self.grop_fire_invaders.add(fire)
                # Reset the "test" variable to 1 after adding the projectile
                self.test = (self.test + 1) % 50
            else:
                # If the "test" variable is not equal to 0, do nothing
                # This controls the frequency of firing projectiles
                self.test = (self.test + 1) % 50

    def all_fire(self):
        """Draws all of the projectiles to the screen and updates their positions."""

        # Draw the spaceship's projectiles to the screen
        self.grop_fire_spaceship.draw(self.screen)

        # Draw the invaders' projectiles to the screen
        self.grop_fire_invaders.draw(self.screen)

        # Update the positions of the spaceship's projectiles
        self.grop_fire_spaceship.update()

        # Update the positions of the invaders' projectiles
        self.grop_fire_invaders.update()

    def invaders_direction(self):
        """Updates the movement direction of the invaders."""

        for invader in self.invaders.grop_invaders:
            # Check if the invader has reached the left edge of the screen
            if invader.rect.left < 0:
                # Move the invader back to the left edge of the screen
                invader.rect.left = 0
                # Reverse the horizontal movement direction of the invaders
                self.speed_invaders *= -1
                # Set the vertical movement direction of the invaders to zero
                self.speed_invaders_y = 0

            # Check if the invader has reached the right edge of the screen
            if invader.rect.right >= Settings.SCREEN_WIDTH:
                # Move the invader back to the right edge of the screen
                invader.rect.right = Settings.SCREEN_WIDTH
                # Reverse the horizontal movement direction of the invaders
                self.speed_invaders *= -1
                # Set the vertical movement direction of the invaders to one
                self.speed_invaders_y = 1

            # Otherwise, the invader is not at either edge of the screen
            else:
                # Set the vertical movement direction of the invaders to zero
                self.speed_invaders_y = 0

    def all_invaders(self):
        """Draws all of the invaders to the screen, updates their movement, and checks for collisions with the spaceship and the spaceship's projectiles."""

        # Draw all of the invaders to the screen
        self.invaders.grop_invaders.draw(self.screen)

        # Update the movement of the invaders
        self.invaders_direction()

        # Update the invaders' positions
        self.invaders.grop_invaders.update(self.speed_invaders, self.speed_invaders_y)

    def collision(self):
        """Detects collisions between the spaceship's projectiles, the invaders, and the spaceship."""

        # Iterate over the invaders and the spaceship's projectiles
        for invader in self.invaders.grop_invaders:
            for fire in self.grop_fire_spaceship:
                # Check if there is a collision between the invader and the projectile
                if invader.rect.colliderect(fire.rect):
                    # Kill the invader and the projectile
                    invader.kill()
                    fire.kill()

                    # Increase the player's score
                    self.score += 10

        for fire_invader in self.grop_fire_invaders:
            # Check if there is a collision between the invader's projectile and the spaceship
            if fire_invader.rect.colliderect(self.spaceship.rect_spaceship):
                # Reduce the number of lives the spaceship has remaining
                self.spaceship_lives -= 1

                # Kill the invader's projectile
                fire_invader.kill()

        # Check if the spaceship has no lives remaining
        if self.spaceship_lives <= 0:
            # Reduce the number of lives the spaceship has remaining by one
            self.spaceship_lives -= 1

            # Set the number of invaders the spaceship has hit to zero
            self.spaceship_hits = 0

        # Check if the spaceship has no lives remaining
        if self.spaceship_lives <= 0:
            # Set the game over flag to True
            self.game_over = True
