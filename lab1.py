import copy

class TreeNode:
    def __init__(self,value,move=(1,1)):
        self.value=value
        self.children=[]
        self.parent=None
        self.move=move
    
    def add_child(self,child):
        child.parent=self
        self.children.append(child)

def generate_next_state(state):
    moves = []
    for row in range(len(state)):
        for col in range(len(state[row])):
            if state[row][col] == 1:
                for direction in [[0,-1], [0,1], [-1,0], [1,0]]:
                    next_row = row + direction[0]
                    next_col = col + direction[1]
                    if 0 <= next_row < len(state) and 0 <= next_col < len(state[row]):
                        if state[next_row][next_col] == 2:
                            moves.append(direction)
    return moves

    
def find_sold_tile(state):
    for row in range(len(state)):
        for col in range(len(state)):
            if state[row][col]==2:
                return row, col

possible_moves = [[0,-1], [0,1], [-1,0], [1,0]]

def breadth_first_search(initial_state):
    queue = []
    visited_states = []
    queue.append([initial_state, []])
    visited_states.append([initial_state, []])
    (current_state, move) = queue.pop(0)
    while current_state != 3:
        possible_moves = [[0,-1], [0,1], [-1,0], [1,0]]
        for i in range(len(possible_moves)):
            next_state = generate_next_state(current_state)
            if next_state is not None:
                if next_state not in visited_states:
                    queue.append([next_state, possible_moves[i]])
                    visited_states.append([next_state, possible_moves[i]])
        current_state, move = queue.pop(0)
    solution_path = []
    solution_path.append(current_state)
    backtrack_state = current_state
    backtrack_move = move
    while backtrack_state != initial_state:
        for i in range(2):
            backtrack_move[i] = -backtrack_move[i]
        previous_state = generate_next_state(backtrack_state, backtrack_move)
        for k in visited_states:
            if k[0] == previous_state:
                backtrack_move = k[1]
                solution_path.insert(0, (previous_state, k[1]))
                backtrack_state = previous_state
                break
    return solution_path


start_state = [[2,2,0,0],[0,1,2,2],[0,2,3,2],[2,0,2,0]]

solution_bfs = breadth_first_search(start_state)
if solution_bfs:
    for steps in solution_bfs:
        state=steps
        # print_puzzle(state)
        print(f'No of steps in bfs-{len(solution_bfs)}')
else:
    print("No solution")

