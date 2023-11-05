from settings import Settings
from fire import Fire


class Spaceship:
    """A class to represent the player's spaceship."""

    def __init__(self):
        """Initialize the spaceship."""

        self.image = Settings.img_spaceship
        self.rect_spaceship = self.image.get_rect(midbottom=(600, 550))
        self.speed_x_spaceShip = 0

    def fly(self, direction_spaceship):
        """Move the spaceship in the specified direction."""

        if direction_spaceship == 'right':
            self.rect_spaceship.x += 5
        elif direction_spaceship == 'left':
            self.rect_spaceship.x -= 5

        # Keep the spaceship within the bounds of the screen.
        if self.rect_spaceship.left <= 0:
            self.rect_spaceship.left = 0
        elif self.rect_spaceship.right >= Settings.SCREEN_WIDTH:
            self.rect_spaceship.right = Settings.SCREEN_WIDTH

    def firing_spaceShip(self):
        """Return a new Fire object representing the spaceship's fire."""

        return Fire(self.rect_spaceship.midtop, -1, "spaceship")
