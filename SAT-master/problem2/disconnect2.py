from z3 import *

graph = [(2, 5), (2, 3), (3, 4), (4, 5), (3, 5), (5, 6), (3, 6)]
s = 2
t = 6
n = 6
num_edges = len(graph)

vs = []
e = []

for i in range(n):
	v = []
	for j in range(n):
		v.append(Bool("p_{}_{}".format(i,j)))
	vs.append(v)

for i in range(num_edges):
	e.append(Bool("e_{}".format(i)))

# print(vs)

def at_most(p,k):
	s = [[Bool("s_{}_{}".format(i,j)) for j in range(k)] for i in range(len(p))]
	first = []
	first.append(Or(Not(p[0]),s[0][0]))
	for j in range(1,k):
		first.append(Not(s[0][j]))
	# first = And(first)
	final = []
	final+=first
	for i in range(1,len(p)):
		F = []
		F.append(Or(Not(p[i]),Not(s[i-1][0]),s[i][0]))
		for j in range(1,k):
			F.append(And(Or(Not(p[i]),Not(s[i-1][j-1]),s[i][j]),Or(Not(s[i-1][j]),s[i][j])))
		# final.append(And(F))
		final+=F

	for i in range(1,n-1):
		final.append
	return And(final)

# solve(And(at_most(e,1),e[0],e[1]))

def find_minimal3(graph,s,t):

	num_edges = len(graph)
	n=0
	for i in range(num_edges):
		n = max(n,graph[i][1])
	n+=1

	# Adj = [[]]*n

	# for ed in graph:
	# 	l = Adj[ed[0]].copy()
	# 	l.append(ed[1])
	# 	Adj[ed[0]] = l
	# 	l = Adj[ed[1]].copy()
	# 	l.append(ed[0])
	# 	Adj[ed[1]] = l

	vs = [Bool('v_{}'.format(i)) for i in range(n)]
	e = [Bool('e_{}'.format(i)) for i in range(num_edges)]
	cost = Int('cost')
	# print(n)
	# for ii in range(num_edges):
	F = Optimize()
		# for i in range(n):
		# 	for j in Adj[i]:
		# 		F.append(Or(Not(vs[i]),vs[j]))

	for i in range(num_edges):
		F.add(Or(Not(e[i]),Not(vs[graph[i][0]]),vs[graph[i][1]]))
		F.add(Or(Not(e[i]),Not(vs[graph[i][1]]),vs[graph[i][0]]))

	F.add(vs[s])
	F.add(Not(vs[t]))
	F.add(cost == Sum([If(x,1,0) for x in e]))
	h = F.maximize(cost)
	while F.check() == sat:
		return num_edges-int(str(h.value()))
		# print(F)

		
def find_minimal(graph,s,t):

	num_edges = len(graph)
	n = 0
	for i in range(num_edges):
		n = max(n,graph[i][1])

	# print(n,num_edges)

	for ii in range(num_edges):
		# print(ii)
		F = []
		for i in range(n-2):
			for k in range(i+2,n):
				for j in range(i+1,k):
					F.append(Or(Not(vs[i][j]),Not(vs[j][k]),vs[i][k]))
		for i in range(num_edges):
			F.append(Or(Not(e[i]),vs[graph[i][0]-1][graph[i][1]-1]))
		F.append(Not(vs[s-1][t-1]))
		F.append(Sum([If(x,1,0) for x in e]) == num_edges-ii)
		S = Solver()
		S.add(And(F))
		# r = S.check()
		if S.check() == sat:
			return ii
	# print(S.check())
	# solve(And(F))

def find_minimal2(graph,s,t):

	num_edges = len(graph)
	n=0
	for i in range(num_edges):
		n = max(n,graph[i][1])
	n+=1

	# Adj = [[]]*n

	# for ed in graph:
	# 	l = Adj[ed[0]].copy()
	# 	l.append(ed[1])
	# 	Adj[ed[0]] = l
	# 	l = Adj[ed[1]].copy()
	# 	l.append(ed[0])
	# 	Adj[ed[1]] = l

	vs = [Bool('v_{}'.format(i)) for i in range(n)]
	e = [Bool('e_{}'.format(i)) for i in range(num_edges)]
	#print(vs)
	#print(e)
	
	for ii in range(num_edges):
		F = []
		# for i in range(n):
		# 	for j in Adj[i]:
		# 		F.append(Or(Not(vs[i]),vs[j]))

		for i in range(num_edges):
			F.append(Or(Not(e[i]),Not(vs[graph[i][0]]),vs[graph[i][1]]))
			F.append(Or(Not(e[i]),Not(vs[graph[i][1]]),vs[graph[i][0]]))

		F.append(vs[s])
		F.append(Not(vs[t]))
		F.append(Sum([If(x,1,0) for x in e]) == num_edges-ii)
		S = Solver()
		S.add(And(F))

		if S.check()==sat:
			return ii
		# print(F)


def find_minimal3(graph,s,t):

	num_edges = len(graph)
	n=0
	for i in range(num_edges):
		n = max(n,graph[i][1])
	n+=1

	# Adj = [[]]*n

	# for ed in graph:
	# 	l = Adj[ed[0]].copy()
	# 	l.append(ed[1])
	# 	Adj[ed[0]] = l
	# 	l = Adj[ed[1]].copy()
	# 	l.append(ed[0])
	# 	Adj[ed[1]] = l

	vs = [Bool('v_{}'.format(i)) for i in range(n)]
	e = [Bool('e_{}'.format(i)) for i in range(num_edges)]
	#print(vs)
	#print(e)
	# print(n)

	m1 = 0
	m2 = 0

	for i in range(num_edges):
		if graph[i][0]==s or graph[i][1]==s:
			m1+=1
		if graph[i][0]==t or graph[i][1]==t:
			m2+=1

	maxi = min(m1,m2)

	# print(maxi)
	# print()

	for ii in range(num_edges):
		F = []
		# for i in range(n):
		# 	for j in Adj[i]:
		# 		F.append(Or(Not(vs[i]),vs[j]))

		for i in range(num_edges):
			F.append(Or(Not(e[i]),Not(vs[graph[i][0]]),vs[graph[i][1]]))
			F.append(Or(Not(e[i]),Not(vs[graph[i][1]]),vs[graph[i][0]]))

		F.append(vs[s])
		F.append(Not(vs[t]))
		F.append(Sum([If(x,1,0) for x in e]) == num_edges-maxi + ii)
		S = Solver()
		S.add(And(F))

		if S.check()!=sat:
			return maxi - ii + 1
		# print(F)
		

def find_minimal5(graph,s,t):

	num_edges = len(graph)
	n=0
	for i in range(num_edges):
		n = max(n,graph[i][1])
	n+=1

	Adj = [[]]*n

	for ed in graph:
		l = Adj[ed[0]].copy()
		l.append(ed[1])
		Adj[ed[0]] = l
		l = Adj[ed[1]].copy()
		l.append(ed[0])
		Adj[ed[1]] = l

	vs = [Bool('v_{}'.format(i)) for i in range(n)]
	e = [[Bool('e_{}_{}'.format(i,j)) for j in range(n)] for i in range(n)]

	print(Adj)

	F1 = []

	for v in Adj[s]:
		F1.append(e[s][v])
	F1 = Or(F1)

	F2 = []
	# print(len(Adj[s])-1)
	for i in range(len(Adj[s])-1):
		for j in range(i+1,len(Adj[s])):
			F2.append(Or(Not(e[min(s,Adj[s][i])][max(s,Adj[s][i])]),Not(e[min(s,Adj[s][j])][max(s,Adj[s][j])])))
	F2 = And(F2)

	# print(F2)
	F3 = []
	# print(len(Adj[s])-1)
	for i in range(len(Adj[t])-1):
		for j in range(i+1,len(Adj[t])):
			F3.append(Or(Not(e[min(t,Adj[t][i])][max(t,Adj[t][i])]),Not(e[min(t,Adj[t][j])][max(t,Adj[t][j])])))
	F3 = And(F3)

	# print(F3)

	







	#print(vs)
	#print(e)
	# print(n)

	# m1 = 0
	# m2 = 0

	# for i in range(num_edges):
	# 	if graph[i][0]==s or graph[i][1]==s:
	# 		m1+=1
	# 	if graph[i][0]==t or graph[i][1]==t:
	# 		m2+=1

	# maxi = min(m1,m2)

	# # print(maxi)
	# # print()

	# for ii in range(num_edges):
	# 	F = []
	# 	# for i in range(n):
	# 	# 	for j in Adj[i]:
	# 	# 		F.append(Or(Not(vs[i]),vs[j]))

	# 	for i in range(num_edges):
	# 		F.append(Or(Not(e[i]),Not(vs[graph[i][0]]),vs[graph[i][1]]))
	# 		F.append(Or(Not(e[i]),Not(vs[graph[i][1]]),vs[graph[i][0]]))

	# 	F.append(vs[s])
	# 	F.append(Not(vs[t]))
	# 	F.append(Sum([If(x,1,0) for x in e]) == num_edges-maxi + ii)
	# 	S = Solver()
	# 	S.add(And(F))

	# 	if S.check()!=sat:
	# 		return maxi - ii + 1
	# 	# print(F)




#solve(Sum([If(x,1,0) for x in e]) <= 2)
# print(vs,e)()