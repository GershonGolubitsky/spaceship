""" This file contains the Fire class, which represents a fire object in the spaceship game. """
import pygame
from settings import Settings


class Fire(pygame.sprite.Sprite):
    """ The constructor takes three parameters:
            - location: A tuple containing the x and y coordinates of the fire object.
            - direction: The direction in which the fire object is moving.
            - img_type: The type of image to use for the fire object. """
    def __init__(self, location, direction, img_type):
        """Call the parent class constructor."""
        super().__init__()

        """Set the x and y coordinates of the fire object's rectangle."""
        self.rect_x = location[0]
        self.rect_y = location[1]

        """Set the image of the fire object."""
        if img_type == 'spaceship':
            self.image = Settings.img_fire_spaceship
        elif img_type == 'invaders':
            self.image = Settings.img_fire_inviders

        """Create a rectangle for the fire object."""
        self.rect = self.image.get_rect(midbottom=(self.rect_x, self.rect_y))

        """Set the direction of the fire object."""
        self.direction = direction

    """The update() method is called every frame to update the position of the fire object."""
    def update(self):
        """ Move the fire object up by 10 pixels, multiplied by its direction. """
        self.rect.top += 10 * self.direction
