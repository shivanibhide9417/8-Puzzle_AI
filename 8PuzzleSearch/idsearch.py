from queue import LifoQueue
from board import Board

def idsearch(initial_state):
        depth = 1
        result = None
        while result == None:
            result = depthLimited(initial_state,depth)
            depth +=1
        return result

def depthLimited(initial_state,depth):
    statesEnqueued=0
    currentDepth=depth
   # print("depth reqiured for this iteration:",currentDepth)
   
    
    start_node = Board(initial_state, None, None, 0,False,0)
    if start_node.goal_test():
        return start_node.find_solution()
    q = LifoQueue()
    q.put(start_node)
    explored=[]
    while not(q.empty()):
        node=q.get()
        explored.append(node.state)
        children=node.generate_child()
       
        for child in children:
                if child.state not in explored:
                   # print("child depth:",child.depth)
                    if child.goal_test():
                        print("number of states enqueued:",statesEnqueued)
                        return child.find_solution()
                    if child.depth==currentDepth:
                        return None
                    q.put(child)
        statesEnqueued=statesEnqueued+1
        
                    
              
   
    return 

