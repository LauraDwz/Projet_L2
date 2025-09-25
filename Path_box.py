class Path_box:
    """Classe qui représente une case de la carte, associée à un chemin
    Le couple correspond au numéro de la cases et pas aux vraies coordonnées"""

    def __init__(self, couple_x_y):
        self.x = couple_x_y[0]
        self.y = couple_x_y[1]
        self.image = "images/path.jpeg"
