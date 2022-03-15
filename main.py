import pygame
import colors
import functions


pygame.init()

screen = pygame.display.set_mode([500, 500])

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(colors.BLACK)

    functions.draw_cube(screen)

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()
