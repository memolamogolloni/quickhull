from math import atan2



class Quick_hull:

	# Get points in convex hull
	def get_convex_hull(self, points):
		if len(points) < 3:
			return []
			
		result = []

		extremes = self.__get_endings(points)

		# Begin recursivity for each side
		self.__add_farthest(points, extremes['left'], extremes['right'], 1, result)
		self.__add_farthest(points, extremes['left'], extremes['right'], -1, result)

		return self.__sort_by_angle(result, extremes['left'])


	# Recursive function looking for farthest point in a group from two given points
	def __add_farthest(self, points, p1, p2, side, result):
		farthest = None
		max_area2 = 0

		# Check if any point is farther than p1, p2
		for p in points:
			if self.__get_side(p1, p2, p) == side:
				area2 = abs(self.__area2(p1, p2, p))
				if area2 > max_area2:
					farthest = p
					max_area2 = area2

		# If there is no farther point, stop recursivity and add p1 and p2 to the convex
		# hull  list if they aren't already in it
		if farthest == None:
			self.__add_extremes(p1, p2, result)
			return

		# If there is, new recursivity calls checking for new farthest points on each side
		self.__add_farthest(points, farthest, p1, - self.__get_side(farthest, p1, p2), result)
		self.__add_farthest(points, farthest, p2, - self.__get_side(farthest, p2, p1), result)


	# Get most left and most right points
	def __get_endings(self, points):
		left = points[0]
		right = points[0]
		for p in points[1:]:
			if p.x < left.x:
				left = p
			if p.x > right.x:
				right = p
		return { 'left': left, 'right': right }


	# Add candidates to the output list if they are not already in it
	def __add_extremes(self, p1, p2, points):
		if p1 not in points:
			points.append(p1)
		if p2 not in points:
			points.append(p2)


	# Return 1 if p is above p1 and p2, 0 if it's collinear and -1 if it's below 
	def __get_side(self, p1, p2, p):
		val = self.__area2(p1, p2, p)
		return val and 1 - 2 * (val < 0)


	# Calculate double of the area between p1, p2 and p 
	def __area2(self, p1, p2, p):
		return (p.y - p1.y) * (p2.x - p1.x) - \
			(p2.y - p1.y) * (p.x - p1.x)


	# Sort a group of points by the angle between each one and a given point
	def __sort_by_angle(self, points, init_point):
		points.remove(init_point)
		angles = list(map(lambda p: atan2(p.y - init_point.y, p.x - init_point.x), points))
		return [init_point] + [p for _, p in sorted(zip(angles, points))]

