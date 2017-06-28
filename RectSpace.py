from copy import deepcopy
class Point2D():
	def __init__(self, coordinates=(0.0,0.0)):
		self.x = coordinates[0]
		self.y = coordinates[1]
	def getCoord(self):
		return (self.x,self.y)

class RectSpace():
	elements = []
	#==================================
	#Confirma se está no espaço
	def isinRange(self,point):
		bound = self.getBounds()
		print("Bound: ",bound)
		x = point.getCoord()[0]
		y = point.getCoord()[1]
		return(((x>=bound[0][0])\
				and(x<=bound[0][1]))\
			and((y>=bound[1][0])\
				and(y<=bound[1][1])))
	
	#==================================
	#Assegura a iclusão se pontos que pertençam ao espaço
	def receivePoints(self,elems):
		print("-----------------------------------------")
		print("\tIn rect: x : "+str(self.getBounds()[0])+"; y : "+str(self.getBounds()[1]))
		for elem in elems:
			if self.isinRange(elem):
				self.elements.append(elem)
				print("Point: "+str(elem.getCoord())+"was appended")
			else:
				print("Point: "+str(elem.getCoord())+"was NOT appended")
		print("----------------------------------------")	
	#==================================
	#Devolve ((x0,xf),(y0,yf))
	def getBounds(self):
		return((self.origin.getCoord()[0],\
					self.origin.getCoord()[0]+self.Width),\
			(self.origin.getCoord()[1],\
					self.origin.getCoord()[1]+self.Height))
		
	#==================================
	def __init__(self,elements=[],origin=Point2D((0.0,0.0)),size=(800.0,600.0)):
		# print("Origin = ",origin)
		# print("origin getCoord() = ",origin.getCoord())
		self.origin = origin
		# print("self.Origin = ",self.origin)
		# print("self.origin getCoord() = ",self.origin.getCoord())
		
		self.Width = size[0]
		self.Height = size[1]
		self.receivePoints(elements)
	def twoPoints(self):
		origin = self.origin.getCoord()
		final = (origin[0]+self.Width,origin[1]+self.Height)
		return origin+final
	def isinThisRange(self,elems,origin,bounds):
		x0,y0 = origin.getCoord()
		x1 = x0+bounds[0]
		y1 = y0+bounds[1]
		for elem in elems:
			x,y = elem.getCoord()
			if (((x>=x0)and(x<=x1))and((y>=y0)and(y<=y1))):
				return True
		return False
		
	def subRect(self,elements, origin,subwidht,subheight):
		elemcopy = deepcopy(elements)
		# print("=====IN subRect=====\n")
		# print("Origin = ",origin)
		# print("origin getCoord() = ",origin.getCoord())
		origincopy = deepcopy(origin)
		# print("origincopy = ",origincopy)
		# print("origincopy.getCoord() = ",origincopy.getCoord())
		# print("==============================")
		subrect = RectSpace(elemcopy,origincopy,(subwidht,subheight))
		return subrect
		
	def subdivide(self):
		sub = []
		subwidht = self.Width/2
		subheight = self.Height/2
		# print("=====IN subdivide=====\n")
		# print("self.Origin = ",self.origin)
		# print("self.origin getCoord() = ",self.origin.getCoord())
		
		# print("origincopy = ",origincopy)
		# print("origincopy.getCoord() = ",origincopy.getCoord())
		# print("==============================")
		
		if self.isinThisRange(self.elements,self.origin,(subwidht,subheight)):
			# print("self.Origin = ",self.origin)
			# print("self.origin getCoord() = ",self.origin.getCoord())
			subrect = self.subRect(self.elements,self.origin,subwidht,subheight)
			sub.append(deepcopy(subrect))
		
		if self.isinThisRange(self.elements,Point2D((self.origin.getCoord()[0]+subwidht,self.origin.getCoord()[1])),(subwidht,subheight)):
			subrect = self.subRect(self.elements,Point2D((self.origin.getCoord()[0]+subwidht,self.origin.getCoord()[1])),subwidht,subheight)
			sub.append(deepcopy(subrect))
		
		if self.isinThisRange(self.elements,Point2D((self.origin.getCoord()[0],self.origin.getCoord()[1]+subheight)),(subwidht,subheight)):
			subrect = self.subRect(self.elements,Point2D((self.origin.getCoord()[0],self.origin.getCoord()[1]+subheight)),subwidht,subheight)
			sub.append(deepcopy(subrect))
		
		if self.isinThisRange(self.elements,Point2D((self.origin.getCoord()[0]+subwidht,self.origin.getCoord()[1]+subheight)),(subwidht,subheight)):
			subrect = self.subRect(self.elements,Point2D((self.origin.getCoord()[0]+subwidht,self.origin.getCoord()[1]+subheight)),subwidht,subheight)
			sub.append(deepcopy(subrect))
		
		return sub
	
	def spans_feature(self):
		return not(self.elements==[])
		
	

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
	

if __name__ == "__main__":
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
