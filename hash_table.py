#python's dictionaries provide a good structure for the table of a simple geographic hash
class HashTable():
	table = {}
	def factorby2(self,n):
		if n//2==0:
			return tuple([0,n%2])
		else:
			return self.factorby2(n//2)+tuple([n%2])
	
	#Standard indexes of the table are :(0,0)(0,1)(1,0)(1,1)
	#Eventually will turn the size dinamic
	def __init__(self,size = 4):
		for n in range(size):
			self.table[self.factorby2(n)] = []
	def getIndexes(self):
		return self.table.keys()
	
if __name__ == "__main__":
	table = HashTable()
	print(table.getIndexes())
	elem0 = (0,0)
	elem1 = (0,1)
	elem2 = (1,0)
	elem3 = (1,1)
	elem4 = (1,1)