# add

class Multiply:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f'Multiply({self.x}, {self.y})'

    def forward(self, x, y):
        self.x = x
        self.y = y
        z = x * y
        return z