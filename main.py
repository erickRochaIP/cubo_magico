import pygame
import colors
import cube


pygame.init()

pygame.font.init()  # you have to call this at the start,
# if you want to use this module.
myfont = pygame.font.SysFont('Comic Sans MS', 30)

screen = pygame.display.set_mode([500, 500])

c = cube.Cube()

wait = 300
tries = 0

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
        if not c.check_solved() or tries == 0:
            c.ra()
            c.u()
            tries += 1

    textsurface = myfont.render(str(tries), False, (100, 100, 100))
    screen.blit(textsurface, (0, 0))

    c.draw_cube(screen)

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()
