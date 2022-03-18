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
            [[colors.BLUE for i in range(3)] for j in range(3)],
            [[colors.YELLOW for i in range(3)] for j in range(3)],
            [[colors.GREEN for i in range(3)] for j in range(3)],
            [[colors.RED for i in range(3)] for j in range(3)],
            [[colors.ORANGE for i in range(3)] for j in range(3)],
        ]

    """
    Rotating functions
    """

    def r(self):
        c = self.squares

        c[0][0][2], c[5][0][2], c[2][2][0], c[4][0][0] = c[4][0][0], c[0][0][2], c[5][0][2], c[2][2][0]
        c[0][1][2], c[5][0][1], c[2][1][0], c[4][0][1] = c[4][0][1], c[0][1][2], c[5][0][1], c[2][1][0]
        c[0][2][2], c[5][0][0], c[2][0][0], c[4][0][2] = c[4][0][2], c[0][2][2], c[5][0][0], c[2][0][0]

        self.rotate_anti_face(3)

    def ra(self):
        c = self.squares

        c[4][0][0], c[0][0][2], c[5][0][2], c[2][2][0] = c[0][0][2], c[5][0][2], c[2][2][0], c[4][0][0]
        c[4][0][1], c[0][1][2], c[5][0][1], c[2][1][0] = c[0][1][2], c[5][0][1], c[2][1][0], c[4][0][1]
        c[4][0][2], c[0][2][2], c[5][0][0], c[2][0][0] = c[0][2][2], c[5][0][0], c[2][0][0], c[4][0][2]

        self.rotate_face(3)

    def l(self):
        c = self.squares

        c[0][0][0], c[5][2][2], c[2][2][2], c[4][2][0] = c[4][2][0], c[0][0][0], c[5][2][2], c[2][2][2]
        c[0][1][0], c[5][2][1], c[2][1][2], c[4][2][1] = c[4][2][1], c[0][1][0], c[5][2][1], c[2][1][2]
        c[0][2][0], c[5][2][0], c[2][0][2], c[4][2][2] = c[4][2][2], c[0][2][0], c[5][2][0], c[2][0][2]

        self.rotate_face(1)

    def la(self):
        c = self.squares

        c[4][2][0], c[0][0][0], c[5][2][2], c[2][2][2] = c[0][0][0], c[5][2][2], c[2][2][2], c[4][2][0]
        c[4][2][1], c[0][1][0], c[5][2][1], c[2][1][2] = c[0][1][0], c[5][2][1], c[2][1][2], c[4][2][1]
        c[4][2][2], c[0][2][0], c[5][2][0], c[2][0][2] = c[0][2][0], c[5][2][0], c[2][0][2], c[4][2][2]

        self.rotate_anti_face(1)

    def f(self):
        c = self.squares

        c[4][2][2], c[3][0][0], c[5][0][2], c[1][2][2] = c[1][2][2], c[4][2][2], c[3][0][0], c[5][0][2]
        c[4][1][2], c[3][1][0], c[5][1][2], c[1][1][2] = c[1][1][2], c[4][1][2], c[3][1][0], c[5][1][2]
        c[4][0][2], c[3][2][0], c[5][2][2], c[1][0][2] = c[1][0][2], c[4][0][2], c[3][2][0], c[5][2][2]

        self.rotate_face(0)

    def fa(self):
        c = self.squares

        c[1][2][2], c[4][2][2], c[3][0][0], c[5][0][2] = c[4][2][2], c[3][0][0], c[5][0][2], c[1][2][2]
        c[1][1][2], c[4][1][2], c[3][1][0], c[5][1][2] = c[4][1][2], c[3][1][0], c[5][1][2], c[1][1][2]
        c[1][0][2], c[4][0][2], c[3][2][0], c[5][2][2] = c[4][0][2], c[3][2][0], c[5][2][2], c[1][0][2]

        self.rotate_anti_face(0)

    def b(self):
        c = self.squares

        c[4][2][0], c[3][0][2], c[5][0][0], c[1][2][0] = c[1][2][0], c[4][2][0], c[3][0][2], c[5][0][0]
        c[4][1][0], c[3][1][2], c[5][1][0], c[1][1][0] = c[1][1][0], c[4][1][0], c[3][1][2], c[5][1][0]
        c[4][0][0], c[3][2][2], c[5][2][0], c[1][0][0] = c[1][0][0], c[4][0][0], c[3][2][2], c[5][2][0]

        self.rotate_anti_face(2)

    def ba(self):
        c = self.squares

        c[1][2][0], c[4][2][0], c[3][0][2], c[5][0][0] = c[4][2][0], c[3][0][2], c[5][0][0], c[1][2][0]
        c[1][1][0], c[4][1][0], c[3][1][2], c[5][1][0] = c[4][1][0], c[3][1][2], c[5][1][0], c[1][1][0]
        c[1][0][0], c[4][0][0], c[3][2][2], c[5][2][0] = c[4][0][0], c[3][2][2], c[5][2][0], c[1][0][0]

        self.rotate_face(2)

    def d(self):
        c = self.squares

        c[0][2][0], c[1][2][0], c[2][2][0], c[3][2][0] = c[3][2][0], c[0][2][0], c[1][2][0], c[2][2][0]
        c[0][2][1], c[1][2][1], c[2][2][1], c[3][2][1] = c[3][2][1], c[0][2][1], c[1][2][1], c[2][2][1]
        c[0][2][2], c[1][2][2], c[2][2][2], c[3][2][2] = c[3][2][2], c[0][2][2], c[1][2][2], c[2][2][2]

        self.rotate_anti_face(5)

    def da(self):
        c = self.squares

        c[3][2][0], c[0][2][0], c[1][2][0], c[2][2][0] = c[0][2][0], c[1][2][0], c[2][2][0], c[3][2][0]
        c[3][2][1], c[0][2][1], c[1][2][1], c[2][2][1] = c[0][2][1], c[1][2][1], c[2][2][1], c[3][2][1]
        c[3][2][2], c[0][2][2], c[1][2][2], c[2][2][2] = c[0][2][2], c[1][2][2], c[2][2][2], c[3][2][2]

        self.rotate_face(5)

    def u(self):
        c = self.squares

        c[0][0][0], c[1][0][0], c[2][0][0], c[3][0][0] = c[3][0][0], c[0][0][0], c[1][0][0], c[2][0][0]
        c[0][0][1], c[1][0][1], c[2][0][1], c[3][0][1] = c[3][0][1], c[0][0][1], c[1][0][1], c[2][0][1]
        c[0][0][2], c[1][0][2], c[2][0][2], c[3][0][2] = c[3][0][2], c[0][0][2], c[1][0][2], c[2][0][2]

        self.rotate_face(4)

    def ua(self):
        c = self.squares

        c[3][0][0], c[0][0][0], c[1][0][0], c[2][0][0] = c[0][0][0], c[1][0][0], c[2][0][0], c[3][0][0]
        c[3][0][1], c[0][0][1], c[1][0][1], c[2][0][1] = c[0][0][1], c[1][0][1], c[2][0][1], c[3][0][1]
        c[3][0][2], c[0][0][2], c[1][0][2], c[2][0][2] = c[0][0][2], c[1][0][2], c[2][0][2], c[3][0][2]

        self.rotate_anti_face(4)

    def rotate_face(self, face):
        f = self.squares[face]

        f[0][0], f[0][1], f[0][2], f[1][2], f[2][2], f[2][1], f[2][0], f[1][0] = f[2][0], f[1][0], f[0][0], f[0][1], f[0][2], f[1][2], f[2][2], f[2][1]

    def rotate_anti_face(self, face):
        f = self.squares[face]

        f[2][0], f[1][0], f[0][0], f[0][1], f[0][2], f[1][2], f[2][2], f[2][1] = f[0][0], f[0][1], f[0][2], f[1][2], f[2][2], f[2][1], f[2][0], f[1][0]

    """
    Drawing functions
    """

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
            coords = (coords[0] + self.size * math.cos(self.rot) * 1.1,
                      coords[1] + self.size * math.sin(self.rot) * 1.1)

    def draw_side_face(self, screen, coords, face, reverse=1):

        for i in range(3):
            self.draw_side_line(screen, coords, (face, i), reverse)
            coords = (coords[0], coords[1] + self.size * 1.1)

    def draw_top_face(self, screen, coords):

        for i in range(3):
            self.draw_top_line(screen, coords, (4, i))
            coords = (coords[0] - self.size * math.cos(self.rot) * 1.1,
                      coords[1] + self.size * math.sin(self.rot) * 1.1)

    def draw_cube(self, screen):

        self.draw_side_face(screen, (self.coords[0], self.coords[1] + 3*1.1 *
                                     math.sin(self.rot)*self.size), 1)
        self.draw_side_face(screen, (self.coords[0] + 3*1.1*math.cos(self.rot)*self.size,
                                     self.coords[1] + 2*3*1.1*math.sin(self.rot)*self.size), 0, -1)
        self.draw_top_face(screen, (self.coords[0] + 3*1.1*math.cos(self.rot)*self.size,
                                    self.coords[1]))
