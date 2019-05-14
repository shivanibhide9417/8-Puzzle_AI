from queue import Queue
from board import Board


def breadth_first_search(initial_state):
    statesEnqueued=0
    
    start_node = Board(initial_state, None, None, 0,False,0)
    if start_node.goal_test():
        return start_node.find_solution()
    q = Queue()
    q.put(start_node)
    explored=[]
    while not(q.empty()):
        node=q.get()
        explored.append(node.state)
        children=node.generate_child()
       
        for child in children:
                if child.state not in explored:
                   
                    if child.goal_test():
                        print("number of states enqueued:",statesEnqueued)
                        return child.find_solution()
                    q.put(child)
                   # print("BFS tree depth:",child.depth)
        statesEnqueued=statesEnqueued+1;
        
                    
              
   
    return 
