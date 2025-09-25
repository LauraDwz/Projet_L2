class Unit_box:
    """Classe qui représente les cases où les unités seront stationnées"""

    def __init__(self, couple_x_y):
        self.x = couple_x_y[0]
        self.y = couple_x_y[1]
        self.image = "images/units.jpeg"
