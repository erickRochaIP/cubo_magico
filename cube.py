import math
import colors
import pygame


class Cube:

    def __init__(self, coords=(100, 100), size=40, rot=math.pi/6):
        self.coords = coords
        self.size = size
        self.rot = rot
        self.squares = [
            [[colors.WHITE for i in range(3)] for j in range(3)],
            [[colors.YELLOW for i in range(3)] for j in range(3)],
            [[colors.BLUE for i in range(3)] for j in range(3)],
            [[colors.GREEN for i in range(3)] for j in range(3)],
            [[colors.RED for i in range(3)] for j in range(3)],
            [[colors.ORANGE for i in range(3)] for j in range(3)],
        ]

    def draw_side_square(self, screen, coords, square, reverse=1):

        points = [(coords[0], coords[1]),
                  (coords[0], coords[1] + self.size),
                  (coords[0] + self.size*math.cos(self.rot*reverse),
                   coords[1] + self.size*(math.sin(self.rot*reverse) + 1)),
                  (coords[0] + self.size*math.cos(self.rot*reverse),
                   coords[1] + self.size*math.sin(self.rot*reverse))
                  ]
        pygame.draw.polygon(
            screen, self.squares[square[0]][square[1]][square[2]], points)

    def draw_top_square(self, screen, coords, square):

        points = [(coords[0], coords[1]),
                  (coords[0] - self.size*math.cos(self.rot),
                   coords[1] + self.size*math.sin(self.rot)),
                  (coords[0], coords[1] + 2*self.size*math.sin(self.rot)),
                  (coords[0] + self.size*math.cos(self.rot),
                   coords[1] + self.size*math.sin(self.rot)),
                  ]
        pygame.draw.polygon(
            screen, self.squares[square[0]][square[1]][square[2]], points)

    def draw_side_line(self, screen, coords, line, reverse=1):

        for i in range(3):

            self.draw_side_square(
                screen, coords, (line[0], line[1], i), reverse)
            coords = (coords[0] + self.size * math.cos(self.rot*reverse) * 1.1,
                      coords[1] + self.size * math.sin(self.rot*reverse) * 1.1)

    def draw_top_line(self, screen, coords, line):

        for i in range(3):
            self.draw_top_square(screen, coords, (line[0], line[1], i))
            coords = (coords[0] - self.size * math.cos(self.rot) * 1.1,
                      coords[1] + self.size * math.sin(self.rot) * 1.1)

    def draw_side_face(self, screen, coords, face, reverse=1):

        for i in range(3):
            self.draw_side_line(screen, coords, (face, i), reverse)
            coords = (coords[0], coords[1] + self.size * 1.1)

    def draw_top_face(self, screen, coords):

        for i in range(3):
            self.draw_top_line(screen, coords, (4, i))
            coords = (coords[0] + self.size * math.cos(self.rot) * 1.1,
                      coords[1] + self.size * math.sin(self.rot) * 1.1)

    def draw_cube(self, screen):

        self.draw_side_face(screen, (self.coords[0], self.coords[1] + 3*1.1 *
                                     math.sin(self.rot)*self.size), 1)
        self.draw_side_face(screen, (self.coords[0] + 3*1.1*math.cos(self.rot)*self.size,
                                     self.coords[1] + 2*3*1.1*math.sin(self.rot)*self.size), 0, -1)
        self.draw_top_face(screen, (self.coords[0] + 3*1.1*math.cos(self.rot)*self.size,
                                    self.coords[1]))
