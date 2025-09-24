import pygame
from random import choice

COTE_CASE = 10
list_decor = [
    pygame.transform.scale(
        pygame.image.load("images/decor1.jpeg"), (COTE_CASE, COTE_CASE)
    ),
    pygame.transform.scale(pygame.image.load("decor2.jpeg"), (COTE_CASE, COTE_CASE)),
    pygame.transform.scale(pygame.image.load("decor3.jpeg"), (COTE_CASE, COTE_CASE)),
]


class Map:
    """Classe qui représente la carte du jeu. Il y aura plusieurs cartes différentes en fonction du niveau"""

    def __init__(
        self, nb_boxes_width, nb_boxes_height, path_boxes, decor_boxes, unit_boxes
    ):
        self.nb_boxes_width = nb_boxes_width
        self.nb_boxes_height = nb_boxes_height
        self.width = COTE_CASE * self.nb_boxes_width
        self.height = COTE_CASE * self.nb_boxes_height
        pygame.display.init()
        self.fenetre = pygame.display.set_mode(self.width, self.height)
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


class Path_box:
    """Classe qui représente une case de la carte, associée à un chemin
    Le couple correspond au numéro de la cases et pas aux vraies coordonnées"""

    def __init__(self, couple_x_y):
        self.x = couple_x_y[0]
        self.y = couple_x_y[1]
        self.image = pygame.transform.scale(
            pygame.image.load("path.jpeg"), (COTE_CASE, COTE_CASE)
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
            pygame.image.load("units.jpeg"), (COTE_CASE, COTE_CASE)
        )

    def draw(self, surface):
        surface.blit(self.image, (self.x * COTE_CASE, self.y * COTE_CASE))


class Unit:
    """Classe qui représente nos unités"""

    ...


class Monster:
    """Classe qui représente les monstres"""

    ...


carte = Map(2, 2, [(0, 0)], [(1, 0), (0, 1)], [(1, 1)])
carte.draw()
