import pygame
from settings import Settings

class Invaders(pygame.sprite.Sprite):
    """A class to represent an invader."""
    def __init__(self):
        """Initialize the invader."""
        super().__init__()
        self.image = Settings.img_invader
        self.rect = self.image.get_rect(midbottom=(80, 160))
        # The invader's direction of movement.
        self.direction = 2
        # The invader's all_direction.
        self.all_direction = 300
        # A group of all the invaders.
        self.grop_invaders = pygame.sprite.Group()

    def all_invaders_group(self):
        """Create a group of all the invaders."""
        for row in range(3):
            for column in range(8):
                invader = Invaders()
                invader.rect.x = column * 60
                invader.rect.y = row * 50
                self.grop_invaders.add(invader)

    def update(self, speed, speed_y):
        """Move the invader."""
        self.rect.x += speed
        self.rect.y += 20 * speed_y

