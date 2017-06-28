import hash_table as ht
class Node():
	ROOT = 0
	BRANCH = 1
	LEAF = 2
	minsize = 1   # Set by QuadTree
	#_______________________________________________________
	# In the case of a root node "parent" will be None. The
	# "rect" lists the minx,minz,maxx,maxz of the rectangle
	# represented by the node.
	def __init__(self, parent, rect, quadrant = ()):
		self.parent = parent
		self.children = [None,None,None,None]
		if parent == None:
			self.depth = 0
			self.mor_code = tuple([1])
		else:
			self.depth = parent.depth + 1
			self.mor_code = parent.mor_code+quadrant
		self.rect = rect
		x0,z0,x1,z1 = rect.twoPoints()
		if self.parent == None:
			self.type = Node.ROOT
		elif (x1 - x0) <= Node.minsize:
			self.type = Node.LEAF
		else:
			self.type = Node.BRANCH
		print(self.mor_code)
	#_______________________________________________________
	# Recursively subdivides a rectangle. Division occurs 
	# ONLY if the rectangle spans a "feature of interest".
	def subdivide(self):
		if self.type == Node.LEAF:
			return
		rects = self.rect.subdivide()
		# x0,z0,x1,z1 = self.rect
		# h = (x1 - x0)/2
		# rects = []
		# rects.append( (x0, z0, x0 + h, z0 + h) ) #00
		# rects.append( (x0 + h, z0, x1, z0 + h) ) #01
		# rects.append( (x0, z0 + h, x0 + h, z1) ) #10
		# rects.append( (x0 + h, z0 + h, x1, z1) ) #11
		for n in range(len(rects)):
			span = self.spans_feature(rects[n])
			if span == True:
				#esse pedaço de código realmente me incomoda, estou tratando tudo como se fosse para utilizar z-order
				quadrant = (n//2,n%2)
				print("\t"),
				self.children[n] = self.getinstance(rects[n],quadrant)#Quadrant
				self.children[n].subdivide() # << recursion
	#_______________________________________________________
	# A utility proc that returns True if the coordinates of
	# a point are within the bounding box of the node.
	def contains(self, x, z):
		x0,z0,x1,z1 = self.rect
		if x >= x0 and x <= x1 and z >= z0 and z <= z1:
			return True
		return False
	#_______________________________________________________
	# Sub-classes must override these two methods.
	def getinstance(self,rect,quadrant):
		return Node(self,rect,quadrant)			
	def spans_feature(self, rect):
		return rect.spans_feature()

#===========================================================			
class QuadTree():
	maxdepth = 1 # the "depth" of the tree
	leaves = []
	allnodes = []
	#_______________________________________________________
	def __init__(self, rootnode, minrect):
		Node.minsize = minrect
		self.hash_table = ht.HashTable()
		rootnode.subdivide() # constructs the network of nodes
		self.prune(rootnode)
		self.traverse(rootnode)
	#_______________________________________________________
	# Sets children of 'node' to None if they do not have any
	# LEAF nodes.		
	def prune(self, node):
		if node.type == Node.LEAF:
			return 1
		leafcount = 0
		removals = []
		for child in node.children:
			if child != None:
				leafcount += self.prune(child)
				if leafcount == 0:
					removals.append(child)
		for item in removals:
			n = node.children.index(item)
			node.children[n] = None		
		return leafcount
	#_______________________________________________________
	# Appends all nodes to a "generic" list, but only LEAF 
	# nodes are appended to the list of leaves.
	def traverse(self, node):
		#QuadTree.allnodes.append(node)
		self.hash_table.insert(node,lambda x: x.mor_code)
		if node.type == Node.LEAF:
			#QuadTree.leaves.append(node)
			if node.depth > QuadTree.maxdepth:
				QuadTree.maxdepth = node.depth
		for child in node.children:
			if child != None:
				self.traverse(child) # << recursion
	#_______________________________________________________
	#Point to leaf
	def pointToLeaf(self,point):
		x,y = point.getCoord()
		x0,y0,x1,y1 = self.rect
		assert x>=0 and x<=x1 and y>=y0 and y<=y1,"Given point not in this rect"
		hash_code = (y%2,x%2)
		xt = ht.HashTable.factorby2(x)
		yt = ht.HashTable.factorby2(y)
		dif = len(xt)-len(yt)
		id = ()
		if dif<0:
			for i in range(-dif):
				xt = (0,)+xt
		elif dif>0:
			for i in range(dif):
				yt = (0,)+yt
		assert len(xt)-len(yt)==0,"=========FALT=========\nin QuadTree.pointToLeaf()\n\t, len(xt)-len(yt) != 0"
		
		for i in range(len(xt)):
			xti = xt[i]
			yti = yt[i]
			id = di+(yti,xti)
		node = self.hash_table.findLeaf(hash_code,id)
		assert node==None,"Could not find suitable node for given point"
		return node
#===========================================================
	
#===========================================================.
if __name__ == "__main__":
	
	print ("Hello World!")
	qt = QuadTree(Node(None,(0,0,1,1)),0.1)
	print(Node.minsize)
	print(qt.maxdepth,qt.leaves)
	