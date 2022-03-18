import pygame
import colors
import cube


pygame.init()

screen = pygame.display.set_mode([500, 500])

c = cube.Cube()

wait = 300

last = pygame.time.get_ticks()

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(colors.BLACK)

    now = pygame.time.get_ticks()
    if now - last > wait:
        last = now
        c.f()
        c.u()

    c.draw_cube(screen)

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()
