
if __name__ == "__main__":
	from random import randrange
	import teste_quadtree as qt
	import RectSpace as rs
	import sys
	def perguntaRect():
		largura = int(input("me informe uma largura: "))
		altura = int(input("e me informe uma altura: "))
		return (largura,altura)
	def iniciaRetangulo(dimensoes=(800,600)):
		ptslist = criaPontos((0,0)+dimensoes)
		origem = rs.Point2D((0,0))
		print("\n==========\n\torigem: ",origem,"\n==========")
		rect = rs.RectSpace(ptslist,origem,dimensoes)
		return rect
	def criaPontos(bounds):
		qtd_points = int(input("Quantos pontos devo gerar? "))
		pointlist = []
		for i in range(qtd_points):
			pointlist.append(rs.Point2D((randrange(bounds[0],bounds[2]),randrange(bounds[1],bounds[3]))))
		return pointlist
	def iniciaQuadTree(rect):
		rootnode = qt.Node(None,rect)
		minsize = int(input("Qual o tamanho da menor largura? "))
		quadTree = qt.QuadTree(rootnode, minsize)
		# print("\nIn iniciaQuadTree(); quadtree==None :",quadTree==None,"\n")
		return quadTree
		
	def mainMenu():
		command = int(input("==Bem vindo ao teste de quadtrees!==\n\
		\n1. Usar retangulo padrao(800,600)\
		\n2. Definir o proprio retangulo\
		\n99. Sair\
		\n-->"))
		
		if command==1:
			rect = iniciaRetangulo()
			return iniciaQuadTree(rect),rect.elements
		#Isso está comentado pois não implementei plt.axis() para um tamanho dinâmico
		# elif command==2:
			# print("Entao"),
			# dimensoes = perguntaRect()
			# rect = iniciaRetangulo(dimensoes)
			# return iniciaQuadTree(rect),rect.elements
		elif command==99:
			input("Ate mais!\naperte \"enter\" para terminar")
			sys.exit()
		else:
			print("Opção não existe!")
			return mainMenu()
			
	# import plotly
	import matplotlib.pyplot as plt
	# plt.plot([1,2,3,4])
	# plt.ylabel('some numbers')
	# plt.show()
	
	quadTree,points = mainMenu()
	if quadTree==None:
		input("Não foi gerada quadtree\npressione \"enter\" para terminar")
		sys.exit()
	if points == None or points == []:
		intput("Não foi gerada lista de pontos\npressione \"enter\" para terminar")
		sys.exit()
	for point in points :
		plt.plot([point.getCoord()[0]],[point.getCoord()[1]],'b.')
	plt.axis([0,800,0,600])
	plt.show()
	