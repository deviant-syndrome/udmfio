from .mixins import PropertyMixin


class Vertex(PropertyMixin):
    def __init__(self, x=None, y=None, zfloor=None, zceiling=None):
        self.x = x
        self.y = y
        self.zfloor = zfloor
        self.zceiling = zceiling
        super().__init__(kwargs={
            'x': self.x, 'y': self.y, 'zfloor': self.zfloor, 'zceiling': self.zceiling
        })
        