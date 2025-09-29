from random import choice


class Box:
    def __init__(self, x, y, images):
        self.x = x
        self.y = y
        self.image = choice(images)


class DecorBox(Box):
    def __init__(self, x, y):
        super().__init__(
            x, y, ("images/decor1.jpeg", "images/decor2.jpeg", "images/decor3.jpeg")
        )


class PathBox(Box):
    def __init__(self, x, y):
        super().__init__(x, y, ("imagepath",))


class UnitBox(Box):
    def __init__(self, x, y):
        super().__init__(x, y, ("imageunit",))
