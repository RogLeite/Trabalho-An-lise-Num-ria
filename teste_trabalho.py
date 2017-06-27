
if __name__ == "__main__":
	from random import randrange
	import teste_quadtree as qt
	import RectSpace as rs
	import sys
	def perguntaRect():
		largura = int(raw_input("me informe uma largura: "))
		altura = int(raw_input("e me informe uma altura: "))
		return (largura,altura)
	def iniciaRetangulo(dimensoes=(800,600)):
		ptslist = criaPontos((0,0)+dimensoes)
		rect = rs.RectSpace(ptslist,rs.Point2D(0,0),dimensoes)
		return rect
	def criaPontos(bounds)
		qtd_points = int(raw_input("Quantos pontos devo gerar?"))
		pointlist = []
		for i in range(qtd_points):
			pointlist.append(Point2D(randrange(bounds[0],bounds[2]),randrange(bounds[1],bounds[3])))
		return pointlist
	def iniciaQuadTree(rect)
		rootnode = qt.Node(None,rect)
		minsize = raw_input("Qual o tamanho da menor largura?")
		quadTree = qt.QuadTree(rootnode, minsize)
		
	def mainMenu():
		command = int(raw_input("==Bem vindo ao teste de quadtrees!==\n\
		\n1. Usar retangulo padrao(800,600)\
		\n2. Definir o proprio retangulo\
		\n99. Sair"))
		
		if command==1:
			rect = iniciaRetangulo()
			return iniciaQuadTree(rect)
		elif command==2:
			print("Entao"),
			dimensoes = perguntaRect()
			rect = iniciaRetangulo(dimensoes)
			return iniciaQuadTree(rect)
		elif command==99:
			raw_input("Ate mais!\naperte \"enter\" para terminar")
			sys.exit()
		else:
			print("Opção não existe!")
			mainMenu()
			
	
	quadTree = mainMenu()
	if quadTree==None:
		raw_input("Não foi gerada quadtree\npressione \"enter\" para terminar")
		sys.exit()
	