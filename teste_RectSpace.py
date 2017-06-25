
class Point2D():
	def __init__(self, coordinates=(0.0,0.0)):
		self.x = coordinates[0]
		self.y = coordinates[1]
	def getCoord(self):
		return (self.x,self.y)

class RectSpace():
	
	def __init__(self,elements=[],origin=Point2D((0.0,0.0)),size=(800.0,600.0)):
		self.elements = elements
		self.origin = origin
		self.Width = size[0]
		self.Height = size[1]
	#==================================
	#Assegura a iclusão se pontos que pertençam ao espaço
	def insertPoints(self,elements):
		pass

def testePoint2D(mode="empty",coordinates = (0.0,0.0)):
	if mode=="empty":
		p1 = Point2D()
	elif mode == "full":
		p1 = Point2D(coordinates)
	print("testePoint2D mode: "+mode)
	print("(x,y) = "+str(p1.getCoord()))
	print("\t"+"x = "+str(p1.x))
	print("\t"+"y = "+str(p1.y))
	
	

def testeRectSpace(mode="empty",elements = [Point2D((300.0,225.0))],origin = (200.0,150.0),size = (400.0,300.0)):
	if mode=="empty":
		r1 = RectSpace()
	elif mode=="full":
		r1 = RectSpace(elements,Point2D(origin),size)
	print("testeRectSpace mode: "+mode)
	print("\t"+"origin = "+str(r1.origin.getCoord()))
	print("\t"+"Width = "+str(r1.Width))
	print("\t"+"Height = "+str(r1.Height))
	


print("Hello World!")
#=========================================================
std_Coord = (100.0,50.0)
testePoint2D()
testePoint2D("full")
testePoint2D("full",std_Coord)
#=========================================================
std_origin = (20.0,15.0)
std_size = (200.0,150.0)
#Ultimo ponto não deve entrar
std_elements = [Point2D(std_origin),
	Point2D(((std_origin[0]+std_size[0])/2,(std_origin[1]+std_size[1])/2)),
	Point2D(std_size),
	Point2D(((std_origin[0]+std_size[0]),(std_origin[1]+std_size[1]))),
	Point2D((std_origin[0]+std_size[0]+1,std_origin[1]+std_size[1]+1)),
	Point2D((std_origin[0]+std_size[0]+10,std_origin[1]+std_size[1]+10))
]
testeRectSpace()
testeRectSpace("full")
testeRectSpace("full",std_elements,std_origin,std_size)
