import pygame
from geometry import Point, Polygon



class Canvas:

	#  ------------------------------- Public functions ---------------------------------
	def setup(self, width, height):
		self.width = width
		self.height = height
		self.color = {
			'BLACK': (  0,   0,   0),
			'WHITE': (255, 255, 255),
			'BLUE':  (  0,   0, 255),
			'GREEN': (  0, 255,   0),
			'RED':   (255,   0,   0)
		}
		self.polygon = Polygon()
		self.screen = pygame.display.set_mode([self.width, self.height])
		self.exit = False

		pygame.init()
		pygame.display.set_caption("Convex hull")

	def update(self, fps): 

		clock = pygame.time.Clock()

		while not self.exit:
			clock.tick(fps)
			self.__update_events()
			self.__render()
			pygame.display.flip()
		 
		pygame.quit()
	#  ---------------------------------------------------------------------------------



	#  --------------------------- Executed on each update -----------------------------
	def __update_events(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.exit = True
			if event.type == pygame.MOUSEBUTTONUP:
				pos_x, pos_y = pygame.mouse.get_pos()
				self.polygon.add_point(Point(pos_x, pos_y))

	def __render(self):
		self.__fill_background(self.color['BLACK'])
		self.__draw_polyline(self.polygon.points, self.color['BLUE'])
		self.__draw_points(self.polygon.points, self.color['RED'])
		self.__draw_points(self.polygon.convex_hull, self.color['GREEN'])
		self.__draw_polyline(self.polygon.convex_hull, self.color['WHITE'], 'CLOSED')
	#  ---------------------------------------------------------------------------------


	#  -------------------------------- Drawing utils ----------------------------------
	def __fill_background(self, color):
		self.screen.fill(color)


	def __draw_points(self, points, color):
		for p in points:
			pygame.draw.circle(self.screen, color, [p.x, p.y], 3)

	def __draw_polyline(self, points, color, type='OPEN'):
		if len(points) < 2:
			return

		point = points[0]
		points = points[1:] + [points[0]] if type == 'CLOSED' else points[1:]

		for p in points:
			pygame.draw.line(self.screen, color, [point.x, point.y], [p.x, p.y], 2)
			point = p
	#  ---------------------------------------------------------------------------------




if __name__ == '__main__':
	canvas = Canvas()
	canvas.setup(400, 400)
	canvas.update(30)

