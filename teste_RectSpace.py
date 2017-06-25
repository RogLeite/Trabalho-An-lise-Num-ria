class RectSpace():
	
	def __init__(self,elements=[],size={"Widht":800.0,"Height":600.0},origin=Point2D()):
		self.elements = elements
		self.size = size
	
class Point2D():
	def __init__(self, coordinates={"x":0.0,"y":0.0}):
		self.coordinates = coordinates
	