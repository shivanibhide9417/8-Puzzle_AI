from queue import PriorityQueue
from board import Board


def Astar_search(initial_state,mode):
    count=0
    explored=[]
    htype=mode
    enqueued=0
    if htype==1:
        start_node=Board(initial_state,None,None,0,True,1)
    if htype==2:
        start_node=Board(initial_state,None,None,0,True,2)
    q = PriorityQueue()
    q.put((start_node.evaluation_function,count,start_node))

    while not q.empty():
        node=q.get()
        node=node[2]
        explored.append(node.state)
        if node.goal_test():
            print("Number of states enqueued :",enqueued)
            return node.find_solution()

        children=node.generate_child()
        for child in children:
            if child.state not in explored:
                count += 1
                q.put((child.evaluation_function,count,child))
                enqueued=enqueued+1;

    return

