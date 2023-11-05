
from manager import Manager_game
import pygame

"""Create a clock object to control the frame rate"""
clock = pygame.time.Clock()
"""Create a new game object"""
game = Manager_game()
"""Start the game"""
game.start_game()
"""Initialize the run loop"""
run = True
"""While the game is running, do the following:"""
while run:
    # Handle all events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # If the user quits, exit the game
            quit()

    """Run the game loop"""
    game.run_game()
    """Handle the player's direction input"""
    game.direction()
    """Fire the spaceship's weapon"""
    game.fire_spaceship()
    """Fire the invaders' weapons"""
    game.fire_invaders()
    """Update the positions of all objects in the game"""
    game.all_fire()
    game.all_invaders()
    """Check for collisions"""
    game.collision()
    """Update the display"""
    pygame.display.update()
    """Limit the frame rate to 60 FPS"""
    clock.tick(60)
    """If the game is over, exit the loop"""
    if game.game_over:
        run = False

"""If the game is over, print a message to the console"""
if game.game_over:
    print("Game Over")
