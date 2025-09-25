from Path_box import Path_box
from Decor_box import Decor_box
from Unit_box import Unit_box
from constantes import COTE_CASE


class Map:
    """Classe qui représente la carte du jeu. Il y aura plusieurs cartes différentes en fonction du niveau"""

    def __init__(
        self, nb_boxes_width, nb_boxes_height, path_boxes, decor_boxes, unit_boxes
    ):
        self.nb_boxes_width = nb_boxes_width
        self.nb_boxes_height = nb_boxes_height
        self.width = COTE_CASE * self.nb_boxes_width
        self.height = COTE_CASE * self.nb_boxes_height
        self.path_boxes = [Path_box(path_boxes[i]) for i in range(len(path_boxes))]
        self.decor_boxes = [Decor_box(decor_boxes[i]) for i in range(len(decor_boxes))]
        self.unit_boxes = [Unit_box(unit_boxes[i]) for i in range(len(unit_boxes))]
