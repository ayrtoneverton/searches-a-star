#%%

class Vertex():
	def __init__(self, name, position, parent = None, distance = 0, visited = False):
		self.name = name
		self.position = position
		self.parent = parent
		self.distance = distance
		self.visited = visited

def a_star(vertices_map, edges_map, start, end):
	path = []
	total = None
	next_list = [start]

	while len(next_list) > 0:
		current = min(next_list, key=lambda e: e.distance)
		current.visited = True
		next_list.remove(current)

		if path and total <= current.distance:
			continue
		if current.position == end.position:
			path = []
			total = current.distance
			while current:
				path.append(current.position)
				current = current.parent
			continue

		for edge in edges_map[current.name]:
			new_vertex = vertices_map[edge[0]]
			if new_vertex == end:
				new_vertex = Vertex(None, end.position)
			if not new_vertex.visited:
				new_vertex.parent = current
				new_vertex.distance = current.distance + edge[1]
				next_list.append(new_vertex)
		
	return '-'.join([c[2] for c in path[::-1]]) + ' (total: %d)' % total

def a_star_list(vertices_list, edges_list, start_char, end_char):
	edges_map = {}
	for edge in edges_list:
		e1 = edges_map.get(edge[0])
		if e1:
			e1.append((edge[1], edge[2]))
		else:
			edges_map[edge[0]] = [(edge[1], edge[2])]

		e2 = edges_map.get(edge[1])
		if e2:
			e2.append((edge[0], edge[2]))
		else:
			edges_map[edge[1]] = [(edge[0], edge[2])]

	start = end = None
	vertices_map = {}
	for v in vertices_list:
		vertices_map[v[2]] = Vertex(v[2], v)
		if v[2] == start_char:
			start = vertices_map[v[2]]
		elif v[2] == end_char:
			end = vertices_map[v[2]]
	return a_star(vertices_map, edges_map, start, end)


#%%

a_star_list([(0, 0, 'A'),(1, 0, 'B'),(2, 0, 'C'),(2, 1, 'D'),(2, 2, 'E'),(3, 0, 'F'),(3, 2, 'G')],
			[('A', 'B', 10),('B', 'C', 12),('C', 'D', 15),('D', 'E', 8),('C', 'F', 2),('F', 'G', 20),('G', 'E', 3)],
			'A', 'E')


#%%

a_star_list([(0, 0, 'A'),(3, 1, 'B'),(8, 1, 'C'),(3, 3, 'D'),(13, 1, 'E'),(16, 3, 'F'),(5, 4, 'G'),(12, 4, 'H'),(20, 5, 'I'),(17, 7, 'J'),(12, 5, 'K'),(7, 6, 'L'),(7, 9, 'M'),(14, 9, 'N'),(19, 10, 'O'),(8, 12, 'P'),(14, 13, 'Q'),(10, 15, 'R'),(3, 17, 'S'),(8, 17, 'T'),(12, 19, 'U'),(7, 21, 'V'),(11, 23, 'W'),(17, 21, 'X'),(24, 24, 'Z')],
			[('A', 'B', 85),('B', 'C', 125),('B', 'D', 50),('D', 'G', 60),('C', 'E', 125),('G', 'L', 70),('E', 'F', 95),('L', 'M', 75),('F', 'H', 110),('M', 'P', 85),('H', 'K', 25),('N', 'P', 180),('K', 'I', 200),('P', 'R', 135),('I', 'J', 95),('R', 'S', 225),('J', 'N', 95),('S', 'V', 140),('N', 'O', 35),('U', 'V', 145),('O', 'Q', 185),('V', 'W', 120),('Q', 'R', 120),('R', 'T', 70),('T', 'U', 120),('U', 'X', 145),('W', 'Z', 335),('X', 'Z', 205)],
			'A', 'Z')
