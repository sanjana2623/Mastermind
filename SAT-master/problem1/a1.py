from z3 import *

# def initialize(n,k):
# 	k_loc=k
# 	num_colors=n

# def put_first_player_response( red, white ):
# 	m=red  #correct colors in correct position
# 	n=white

# def get_second_player_move(): 

num_colors=4
k=2
var = [[Bool('v_{}{}'.format(i,j)) for j in range(num_colors)] for i in range(k) ]
# print(var)
S = Optimize()
F = []
for i in range(k):
	F.append(Sum([If(x,1,0) for x in var[i]]) == 1)
cost = Int('cost')

S.add(F)
a1 = Int('a1')
a2 = Int('a2')
mini = Int('mini')

a1 = Sum([If(var[0][1],1,0),If(var[1][2],1,0)])
a2 = Sum([If(var[0][1],1,0),If(var[1][2],1,0),If(var[1][3],1,0)])
a2 = 1
a3 = If(a1<a2,a1,a2)

S.add(cost == a3)
h = S.maximize(cost)

move = []
while S.check() == sat:
	t=S.model()
	print(h.value())
	# print(t)
	# print(type(t.evaluate(var[0][0])))
	x=BoolSort().cast(True)
	# print(x)
	l_true=[]
	# print(move)
	for i in range(k):
		rt=[j for j in range(num_colors) if t.evaluate(var[i][j])==x ]
		move.extend(rt)
	print(move)

	
	break

def column(matrix, i):
    return [row[i] for row in matrix]

print(column(var,0))

# print(F)
# a = 1
# b = 1
# F.append(Sum([If(var[i][move[i]],1,0) for i in range(k)]) == a)
# F.append(Sum([If(var[i][j],1,0) for i in range(k) for j in set(move)]) >= a+b)

# a1 = Int('a1')
# a2 = Int('a2')
# mini = Int('mini')

# a1 = Sum([If(var[0][1],1,0),If(var[1][2],1,0)])
# a2 = Sum([If(var[0][1],1,0),If(var[1][2],1,0),If(var[1][3],1,0)])

# a3 = If(a1<a2,a1,a2)

# print(F)


# cost=Int('Cost')

# F.add(cost==)
# F.maximize(cost)
# print(F.model())

#-------------initial assignment ------------------

#--------------m,n----------







# print(F)







	

