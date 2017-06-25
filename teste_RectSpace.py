
class Point2D():
	def __init__(self, coordinates=(0.0,0.0)):
		self.x = coordinates[0]
		self.y = coordinates[1]

class RectSpace():
	
	def __init__(self,elements=[],size=(800.0,600.0),origin=Point2D()):
		self.elements = elements
		self.size["Widht"] = size[0]
		self.size["Height"] = size[1]		
	

def testePoint2D(mode="empty",coordinates = (0.0,0.0)):
	if mode=="empty":
		p1 = Point2D()
	elif mode == "full":
		p1 = Point2D(coordinates)
	print("x = "+str(p1.x))
	print("y = "+str(p1.y))
	
	
	
std_Coord = (100.0,50.0)
print("Hello World!")
testePoint2D()
testePoint2D("full")
testePoint2D("full",std_Coord)