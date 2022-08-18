from z3 import *

def find_minimal(graph,s,t):

	num_edges = len(graph)   #number of edges
	n=0
	for i in range(num_edges):
		n = max(n,graph[i][1])
	n+=1			#number of vertices

	vs = [Bool('v_{}'.format(i)) for i in range(n)]		#encodes each vertex (true if connected to source)
	e = [Bool('e_{}'.format(i)) for i in range(num_edges)]		#encodes each edge (true if edge is included)
	cost = Int('cost')
	F = Optimize()

	for i in range(num_edges):
		F.add(Or(Not(e[i]),Not(vs[graph[i][0]]),vs[graph[i][1]]))		#edge between vertices imply both vertices get same value
		F.add(Or(Not(e[i]),Not(vs[graph[i][1]]),vs[graph[i][0]]))

	F.add(vs[s])
	F.add(Not(vs[t]))
	F.add(cost == Sum([If(x,1,0) for x in e]))
	h = F.maximize(cost)							#maximise number of edges

	while F.check() == sat:
		return num_edges-int(str(h.value()))

