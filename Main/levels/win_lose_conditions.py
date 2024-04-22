import pygame

def show_game_over_screen(display):
    # Load the game over screen image (ensure the path is correct relative to the main script execution)
    game_over_screen = pygame.image.load(r"Main\Level1_Img\backgrounds\game_over_level1.png")
    
    # Clear the display and show the game over image
    display.fill((0, 0, 0))  # Optionally clear the screen
    display.blit(game_over_screen, (0, 0))
    
    # Set up the font and text for 'Game Over!'
    font = pygame.font.Font(None, 48)
    text_surface = font.render('Game Over!', True, (255, 255, 255))
    text_rect = text_surface.get_rect(center=(display.get_width() // 2, display.get_height() // 2))
    
    # Display the text
    display.blit(text_surface, text_rect)
    
    # Update the display to show everything
    pygame.display.update()
