import pygame
from random import choice

COTE_CASE = 60
list_decor = [
    pygame.transform.scale(
        pygame.image.load("images/decor1.jpeg"), (COTE_CASE, COTE_CASE)
    ),
    pygame.transform.scale(
        pygame.image.load("images/decor2.jpeg"), (COTE_CASE, COTE_CASE)
    ),
    pygame.transform.scale(
        pygame.image.load("images/decor3.jpeg"), (COTE_CASE, COTE_CASE)
    ),
]


class Map:
    """Classe qui représente la carte du jeu. Il y aura plusieurs cartes différentes en fonction du niveau"""

    def __init__(
        self, nb_boxes_width, nb_boxes_height, path_boxes, decor_boxes, unit_boxes
    ):
        self.nb_boxes_width = nb_boxes_width
        self.nb_boxes_height = nb_boxes_height
        self.width = COTE_CASE * self.nb_boxes_width
        print(self.width)
        self.height = COTE_CASE * self.nb_boxes_height
        print(self.height)
        pygame.display.init()
        self.fenetre = pygame.display.set_mode((self.width, self.height))
        self.path_boxes = [Path_box(path_boxes[i]) for i in range(len(path_boxes))]
        self.decor_boxes = [Decor_box(decor_boxes[i]) for i in range(len(decor_boxes))]
        self.unit_boxes = [Unit_box(unit_boxes[i]) for i in range(len(unit_boxes))]

    def draw(self):
        for box in self.path_boxes:
            box.draw(self.fenetre)
        for box in self.decor_boxes:
            box.draw(self.fenetre)
        for box in self.unit_boxes:
            box.draw(self.fenetre)
        pygame.display.flip()


class Path_box:
    """Classe qui représente une case de la carte, associée à un chemin
    Le couple correspond au numéro de la cases et pas aux vraies coordonnées"""

    def __init__(self, couple_x_y):
        self.x = couple_x_y[0]
        self.y = couple_x_y[1]
        self.image = pygame.transform.scale(
            pygame.image.load("images/path.jpeg"), (COTE_CASE, COTE_CASE)
        )

    def draw(self, surface):
        surface.blit(self.image, (self.x * COTE_CASE, self.y * COTE_CASE))


class Decor_box:
    """Classe qui représente une case du décor, cases qui ne sont associées ni au chemin que parcoureront les monstres, ni l'endroit ou peuvent aller nos unités"""

    def __init__(self, couple_x_y):
        self.x = couple_x_y[0]
        self.y = couple_x_y[1]
        self.image = choice(list_decor)

    def draw(self, surface):
        surface.blit(self.image, (self.x * COTE_CASE, self.y * COTE_CASE))


class Unit_box:
    """Classe qui représente les cases où les unités seront stationnées"""

    def __init__(self, couple_x_y):
        self.x = couple_x_y[0]
        self.y = couple_x_y[1]
        self.image = pygame.transform.scale(
            pygame.image.load("images/units.jpeg"), (COTE_CASE, COTE_CASE)
        )

    def draw(self, surface):
        surface.blit(self.image, (self.x * COTE_CASE, self.y * COTE_CASE))


class Unit:
    """Classe qui représente nos unités"""

    ...


class Monster:
    """Classe qui représente les monstres"""

    ...


carte = Map(
    11,
    11,
    [
        (0, 5),
        (0, 6),
        (0, 7),
        (0, 8),
        (0, 9),
        (0, 10),
        (1, 5),
        (2, 5),
        (3, 5),
        (4, 5),
        (5, 5),
        (6, 5),
        (7, 5),
        (8, 5),
        (9, 5),
        (10, 5),
        (10, 4),
        (10, 3),
        (10, 2),
        (10, 1),
        (10, 0),
    ],
    [
        (0, 0),
        (1, 0),
        (2, 0),
        (3, 0),
        (4, 0),
        (5, 0),
        (6, 0),
        (7, 0),
        (8, 0),
        (9, 0),
        (0, 4),
        (1, 4),
        (2, 4),
        (3, 4),
        (4, 4),
        (5, 4),
        (6, 4),
        (7, 4),
        (8, 4),
        (9, 4),
        (1, 6),
        (2, 6),
        (3, 6),
        (4, 6),
        (5, 6),
        (6, 6),
        (7, 6),
        (8, 6),
        (9, 6),
        (10, 6),
        (1, 10),
        (2, 10),
        (3, 10),
        (4, 10),
        (5, 10),
        (6, 10),
        (7, 10),
        (8, 10),
        (9, 10),
        (10, 10),
        (0, 1),
        (0, 2),
        (0, 3),
        (1, 1),
        (1, 2),
        (1, 3),
        (9, 1),
        (9, 2),
        (9, 3),
        (1, 7),
        (1, 8),
        (1, 9),
        (9, 7),
        (9, 8),
        (9, 9),
        (10, 7),
        (10, 8),
        (10, 9),
    ],
    [
        (2, 1),
        (2, 2),
        (2, 3),
        (3, 1),
        (3, 2),
        (3, 3),
        (4, 1),
        (4, 2),
        (4, 3),
        (5, 1),
        (5, 2),
        (5, 3),
        (6, 1),
        (6, 2),
        (6, 3),
        (7, 1),
        (7, 2),
        (7, 3),
        (8, 1),
        (8, 2),
        (8, 3),
        (2, 7),
        (2, 8),
        (2, 9),
        (3, 7),
        (3, 8),
        (3, 9),
        (4, 7),
        (4, 8),
        (4, 9),
        (5, 7),
        (5, 8),
        (5, 9),
        (6, 7),
        (6, 8),
        (6, 9),
        (7, 7),
        (7, 8),
        (7, 9),
        (8, 7),
        (8, 8),
        (8, 9),
    ],
)
carte.draw()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    carte.draw()

pygame.quit()
