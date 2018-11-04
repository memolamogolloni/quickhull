from .lib.calculus import *
from .lib.data_structures import *



class Point(Point_structure):
	def __init__(self, x_init, y_init):
		Point_structure.__init__(self, x_init, y_init)


class Polygon(Polygon_structure):
	def __init__(self, points=None):
		Polygon_structure.__init__(self, points=None)

	@property
	def convex_hull(self):
		return Quick_hull().get_convex_hull(self.points)