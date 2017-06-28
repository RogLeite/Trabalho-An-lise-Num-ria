from math import log2,floor,ceil
#python's dictionaries provide a good structure for the table of a simple geographic hash
class HashTable():
	table = {}
	def factorby2(self,n):
		if n//2==0:
			if n%2==0:
				return tuple([])
			else:
				return tuple([n%2])
		else:
			return self.factorby2(n//2)+tuple([n%2])
	def fn(self,n,size):
		#print("log2(n)\n\t",log2(n))
		#print("\tfloor: ",floor(log2(n)))
		#print("\tceil: ",ceil(log2(n)))
		dif = ceil(log2(size))-ceil(log2(n))
		ret = tuple([0])*dif
		#print("\tdif: ",dif)
		#print("\tret: ",ret)
		return ret
	#Standard indexes of the table are :(0,0)(0,1)(1,0)(1,1)
	#Eventually will turn the size dinamic
	def __init__(self,size = 4):
		#print("===size===")
		#self.fn(size)
		for n in range(size):
			#print("==="+str(n+1)+"===")
			#self.fn(n+1,size)
			#==================================
			#Filling the table with Stacks
			self.table[self.fn(n+1,size)+self.factorby2(n)] = []
			#====================================
	def getIndexes(self):
		return self.table.keys()
	def criteria(self,key, id):
		keylen = len(key)
		idlen = len(id)
		sublen = idlen-keylen
		return (id[sublen::]==(key))

	def insert(self,elem, getid):
		# print("getid(): ",getid)
		# print("getid(elem): ",getid(elem))
		keys = self.table.keys()
		id = getid(elem)
		for key in keys:
			if self.criteria(key, id):
				index = self.findPlace(self.table[key], id, getid)
				self.table[key].insert(index,elem)
	#Returns index starting in 0
	def findPlace(self,list, id, getid):
		if not list or list==[] :
			return 0
		for i in range(len(list)):
			if len(getid(list[i])) < len(id):
				return i
		return len(list)
		
	def findLeaf(self, hash_code, id):
		for node in self.table[hash_code]:
			nodeidlen = len(node.mor_code)
			subid = id[len(id)-nodeidlen::]
			if(cmp(subid,node.mor_code)==0):
				return node
		return None
if __name__ == "__main__":

	"""
	def criteriaTest(keys,ids):
		for id in ids:
			for key in keys:
				print("id : ",id)
				print("/==================")
				print("\tkey : ",key)
				print("\tcriteria : ",HashTable.criteria(key, id))
				print("==================/\n\n")"""
	table = HashTable()
	inds = table.getIndexes()
	print(inds)
	elems = [(0,0,0),(1,0,0,1),(1,),(1,0,1),(0,0,1,0),(1,0),(0,1,1),(0,0,1,0),(1,1)]
	#criteriaTest(table.getIndexes(),elems)
	table.insert(elems,lambda x: x)
	for ind in inds:
		print(ind,": ",table.table[ind])