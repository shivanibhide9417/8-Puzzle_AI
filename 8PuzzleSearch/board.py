class Board:
    goal_state=[1, 2, 3,
        4, 5, 6,
        7, 8, 0]
    heuristic=None
    evaluation_function=None
    needs_hueristic=False
    num_of_instances=0
    mode=0
    depth=0
    def __init__(self,state,parent,action,path_cost,needs_hueristic=False,mode=0,depth=0):
        self.parent=parent
        self.state=state
        self.action=action
        self.mode=mode
        self.depth=depth
        if parent:
            self.path_cost = parent.path_cost + path_cost
        else:
            self.path_cost = path_cost
        if needs_hueristic:
            self.needs_hueristic=True
            if self.mode==1:
             self.generate_heuristic_distance()
            if self.mode==2:
             self.generate_heuristic_manhattan()
            self.evaluation_function=self.heuristic+self.path_cost
    

    def __str__(self):
        return str(self.state[0:3])+'\n'+str(self.state[3:6])+'\n'+str(self.state[6:9])

    def generate_heuristic_distance(self):
        self.heuristic=0
        for num in range(1,9):
          
            if self.state.index(num)!=self.goal_state.index(num):
                self.heuristic=self.heuristic+1

    def generate_heuristic_manhattan(self):
        self.heuristic=0
        for num in range(1,9):
            distance=abs(self.state.index(num) - self.goal_state.index(num))
            i=int(distance/3)
            j=int(distance%3)
            self.heuristic=self.heuristic+i+j

    def goal_test(self):
        if self.state == self.goal_state:
            return True
        if self.depth==10:
            print("Depth is already 10. No solution found!")
            return True
        return False

    @staticmethod
    def find_legal_actions(i,j):
        legal_action = ['U', 'D', 'L', 'R']
        if i == 0:  # up is disable
            legal_action.remove('U')
        elif i == 2:  # down is disable
            legal_action.remove('D')
        if j == 0:
            legal_action.remove('L')
        elif j == 2:
            legal_action.remove('R')
        return legal_action

    def generate_child(self):
        children=[]
        x = self.state.index(0)
        i = int(x / 3)
        j = int(x % 3)
        legal_actions=self.find_legal_actions(i,j)

        for action in legal_actions:
            new_state = self.state.copy()
            if action is 'U':
                new_state[x], new_state[x-3] = new_state[x-3], new_state[x]
            elif action is 'D':
                new_state[x], new_state[x+3] = new_state[x+3], new_state[x]
            elif action is 'L':
                new_state[x], new_state[x-1] = new_state[x-1], new_state[x]
            elif action is 'R':
                new_state[x], new_state[x+1] = new_state[x+1], new_state[x]
            
            children.append(Board(new_state,self,action,1,self.needs_hueristic,self.mode,self.depth+1))
           
            
        return children

    def find_solution(self):
        solution = []
        moves=0
        solution.append(self.state)
        path = self
        
        while path.parent != None:
            moves=moves+1
            path = path.parent
            solution.append(path.state)
        solution = solution[:-1]
        solution.reverse()
        print("total number of moves:",moves)
        return solution
