from boxes import *
from src.utils.constantes import COTE_CASE


class Map:
    """Classe qui représente la carte du jeu. Il y aura plusieurs cartes différentes en fonction du niveau"""

    def __init__(
        self, path_file
    ):
        #Remplacer par le résultat de la fonction
        self.nb_boxes_width = nb_boxes_width
        self.nb_boxes_height = nb_boxes_height
        self.width = COTE_CASE * self.nb_boxes_width
        self.height = COTE_CASE * self.nb_boxes_height
        self.path_boxes = [Path_box(path_boxes[i]) for i in range(len(path_boxes))]
        self.decor_boxes = [Decor_box(decor_boxes[i]) for i in range(len(decor_boxes))]
        self.unit_boxes = [Unit_box(unit_boxes[i]) for i in range(len(unit_boxes))]
        
    def parse_file(path_file) -> tuple:
        blabla je parse
        nb_boxes = 
        
        return nbwidth, nbheight, width, height