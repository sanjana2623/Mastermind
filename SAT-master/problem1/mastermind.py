from z3 import *
import random

k_loc = 0
num_colors = 0

F = []			#formula to make satisfiable
var = [[Bool('v_{}_{}'.format(i,j)) for j in range(num_colors)] for i in range(k_loc)] 			#boolean variables to encode colour at each position
p_move = [0]*k_loc
Q = []			#encodes which clause is true

def initialize(n,k):
	global p_move
	global F
	global k_loc
	global num_colors
	global var

	k_loc=k
	num_colors=n
	var = [[Bool('v_{}_{}'.format(i,j)) for j in range(num_colors)] for i in range(k_loc)]
	for i in range(k_loc):
		F.append(Sum([If(x,1,0) for x in var[i]]) == 1)			#each position should have only on colour

def put_first_player_response( red, white ):
	global p_move
	global F
	global k_loc
	global num_colors
	global var
	global cnt
	global Q

	def minn(a,b):
		return If(a<b,a,b)
	def column(matrix, i):
		return [row[i] for row in matrix]

	a = red
	b = white
	p = len(Q)
	Q.append(Bool('q_{}'.format(p)))

	F.append(Or(Not(Q[p]),(Sum([If(var[i][p_move[i]],1,0) for i in range(k_loc)]) == a)))		#encoding for reds

	Fs = []
	Ls = [0]*num_colors

	for i in range(k_loc):
		Ls[p_move[i]]+=1

	for i in range(num_colors):
		Fs.append(minn(Sum([If(x,1,0) for x in column(var,i)]),Ls[i]))
	F.append(Or(Not(Q[p]),(Sum(Fs)==(a+b))))			#encoding for whites
	


def get_second_player_move(): 
	global p_move
	global F
	global k_loc
	global num_colors
	global var
	global Q

	move = []
	cost = Int('cost')
	S = Optimize()
	S.add(F)
	S.add(cost == Sum([If(x,1,0) for x in Q]))
	h = S.maximize(cost)			# we assume that maximum responses given are true

	while S.check() == sat:
		t=S.model()
		x=BoolSort().cast(True)
		l_true=[]
		move = []
		for i in range(k_loc):
			rt=[j for j in range(num_colors) if t.evaluate(var[i][j])==x ]
			move.extend(rt)

		p_move = move.copy()
		return move

# It works even if colours are repeated at positions
# It also works for unreliable player1