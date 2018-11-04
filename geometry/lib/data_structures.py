from . import calculus


class Point_structure:
	def __init__(self,x_init,y_init):
		self.x = x_init
		self.y = y_init

	def __repr__(self):
		return "".join(["Point(", str(self.x), ",", str(self.y), ")"])


class Polygon_structure:
	def __init__(self, points=None):
		if points == None:
			points = []
		self.points = points

	def add_point(self, point):
		self.points.append(point)

	def __repr__(self):
		return ''.join(['Polygon(', str([str(p) + ' ' for p in self.points]), ')'])
