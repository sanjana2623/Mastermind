import random

M_nodes = 50



#tmp = random.sample(range(M_nodes),2)



for cc in range(10):
	gr=[]
	vs=[]
	for i in range(random.randint(int(M_nodes*(M_nodes-1)/4), (M_nodes*(M_nodes-1)/2) -2)):
		tmp = random.sample(range(M_nodes),2)
		gr.append(tuple([min(tmp), max(tmp)]))
		vs.append(tmp[0])
		vs.append(tmp[1])

	fin = list(set(gr))
	finv= list(set(vs))

	for ed in fin:
		with open('./test/edges_{}.txt'.format(cc), 'a') as the_file:
			the_file.write('{},{}\n'.format(ed[0],ed[1]))

	for i in range(20):
		tmp1= random.sample(finv,2)
		with open('./test/s_t_{}.txt'.format(cc) , 'a') as the_file:
			the_file.write('{},{}\n'.format(min(tmp1), max(tmp1)))
