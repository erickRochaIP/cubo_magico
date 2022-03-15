from re import S
import pygame
import colors
import math


def draw_square(screen, coords, color, size, rot):

    points = [(coords[0], coords[1]),
              (coords[0], coords[1] + size),
              (coords[0] + size*math.cos(rot),
               coords[1] + size*(math.sin(rot) + 1)),
              (coords[0] + size*math.cos(rot), coords[1] + size*math.sin(rot))
              ]
    pygame.draw.polygon(screen, color, points)


def draw_line(screen, coords, color, size, rot):

    for _ in range(3):
        coords = (coords[0] + size * math.cos(rot) * 1.1,
                  coords[1] + size * math.sin(rot) * 1.1)

        draw_square(screen, coords, color, size, rot)


def draw_cube(screen):
    size = 40
    coords = (250, 0)
    for _ in range(3):
        coords = (coords[0], coords[1] + size * 1.1)

        draw_line(screen, coords, colors.BLUE, size, math.pi/6)
        draw_line(screen, coords, colors.RED, size, 5*math.pi/6)
