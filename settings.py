import pygame

class Settings:
    """A class to store all the game settings."""

    """Load the images for the spaceship, background, fire, and invaders"""
    img_spaceship = pygame.image.load("/home/mefathim-tech-55/Desktop/image/ship.png")
    img_background = pygame.image.load("/home/mefathim-tech-55/Desktop/image/background_game.png")
    img_fire_spaceship = pygame.image.load("/home/mefathim-tech-55/Desktop/image/racket.png")
    img_fire_inviders = pygame.image.load("/home/mefathim-tech-55/Desktop/image/racket2.png")

    img_invader = pygame.image.load("/home/mefathim-tech-55/Desktop/image/alien.png")

    """Set the screen width and height"""
    SCREEN_WIDTH = 1200
    SCREEN_HEIGHT = 600

    """Create a clock object to control the game frame rate"""
    clock = pygame.time.Clock()

