#!/usr/bin/python3

# sample harness; your code should play against this code without
# any modification in this code. For any issues in this code
# please report asap.

# your code lives in this file; we will import it
import disconnect

graph = [(2, 5), (2, 3), (3, 4), (4, 5), (3, 5), (5, 6), (3, 6)]
s = 3
t = 6

# ~~~~ API CALL: We tell your code our choice of n and k
# input:
#   graph : a list of pairs defining undirected graph
#       (assume edges do not repeat; for each (v1,v2) \in graph. v1 < v2  )
#   s : starting node
#   t : terminating node
# return value:
#  the minimal number of edges such that the graph is disconnected

num = disconnect.find_minimal(graph, s, t)

print("Edges to delete:")
print(num)

graph = [(1,2),(2,3),(3,4),(4,5),(1,6),(6,7),(5,7),(1,3),(2,6),(3,6),(1,8),(8,9),(9,10),(10,5),(7,9),(7,10),(5,9)]
s = 1
t = 5


num = disconnect.find_minimal(graph, s, t)

print("Edges to delete:")
print(num)

