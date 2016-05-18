class Square():
	def __init__(self, side_length):
		self._side_length = side_length

	def set_center(self, center):
		self._center = center

	def set_color(self, color):
		self._color = color

	def get_color(self):
		return self._color

	def get_center(self):
		return self._center

	def area(self):
		return (self._side_length * self._side_length)

	def print_square(self):
		if (self._side_length == 1): # make sure the square is big enough to print properly
			print "*"
		else:
			inner_size = self._side_length - 2
			print ('*' * self._side_length)
			for i in range(inner_size):
			    print ('*' + ' ' * inner_size + '*') # Print row
			print ('*' * self._side_length)
