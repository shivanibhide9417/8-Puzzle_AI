from time import time
from BFS_search import breadth_first_search
from Astar_search import Astar_search
from RBFS_search import recursive_best_first_search
from board import Board
from idsearch import idsearch


#example input:[1, 3, 4, 8, *, 5,7, 2, 6]
#Accept input from the user
print("enter input array:")
s=[]
for k in range(0,9):
    n=input("Enter element of input array : ")
    if(n=="*"):
        s.append(int(0))
    else:
        s.append(int(n))


#call the fours algorithms in sequence

print('----------------BREADTH FIRST SEARCH----------------------')
state=s
bfs=breadth_first_search(state)
val=str(bfs)
print('BFS:', val.replace("0","*"))
print()



print('-----------------ITERATIVE DEEPENING SEARCH------------------------')

astar = idsearch(state)
val=str(astar)
print("ids:", val.replace("0","*"))
print()

print('--------------ASTAR SEARCH:NUMBER OF TILES OUT OF ORDER---------------------------')

t0 = time()
astar = Astar_search(state,1)
val=str(astar)
print("Astar out-of-place distance:", val.replace("0","*"))
t1 = time() - t0
print('time:', t1)
print()


print('-----------------ASTAR SEARCH:MANHATTAN DISTANCE------------------------')
t0 = time()
astar = Astar_search(state,2)
val=str(astar)
print("Astar manhattan:", val.replace("0","*"))
t1 = time() - t0
print('time:', t1)
print()

print('-----------------------------------------')
