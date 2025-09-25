from random import choice


class Decor_box:
    """Classe qui représente une case du décor, cases qui ne sont associées ni au chemin que parcoureront les monstres, ni l'endroit ou peuvent aller nos unités"""

    def __init__(self, couple_x_y):
        self.x = couple_x_y[0]
        self.y = couple_x_y[1]
        self.image = choice(
            ("images/decor1.jpeg", "images/decor2.jpeg", "images/decor3.jpeg")
        )
