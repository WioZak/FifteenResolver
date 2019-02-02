import sys
import numpy as np
from copy import deepcopy
import time
import os

class State(): # aka node
    visited_states_count = 0
    explored_states_count = 0
    max_achieved_depth = 0 # shared variable

    def __init__(self, state_matrix = None, rows = 0, columns = 0, parent = None, path = [], solution_length = 0):
        self.state_matrix = state_matrix
        self.rows = rows
        self.columns = columns
        self.parent = parent
        self.path = path
        self.solution_length = solution_length

    def checkStateIsTarget(self, target_state_matrix):
        if self.state_matrix == target_state_matrix:
            return True
        else: 
            return False

    def __hash__(self):
        return hash(str(self.state_matrix))

    def __eq__(self, other):
        return (
            self.__class__ == other.__class__ and
            self.state_matrix == other.state_matrix
        )

    def addPathStep(self, char):
        self.path.append(char)

def main():

    max_possible_depth = 20

    if len(sys.argv) == 4:
        strategy = sys.argv[1].lower()
        strategy_option = sys.argv[2].upper()
        path_to_in_file = sys.argv[3]
        
    else:
        print("Wrong number of arguments!")

    data = readDataFromFile(path_to_in_file)

    target_state_matrix = generateTargetState(data["rows"], data["columns"])

    state_data = data["state"]
    state_matrix = generateMatrix(state_data, data["rows"], data["columns"])

    root_state = State(state_matrix, data["rows"], data["columns"])

    # check strategy
    start = time.time()
    if strategy == "bfs":
        solution = solveBfs(strategy_option, root_state, target_state_matrix)
    elif strategy == "dfs":
        solution = solveDfs(strategy_option, root_state, target_state_matrix, max_possible_depth)
    elif strategy == "astr":
        solution = solveAstar(strategy_option, root_state, target_state_matrix)
    else:
        print("Wrong strategy name")
    end = time.time()
    saveSolution(solution.solution_length, solution.path, strategy, strategy_option.lower(), path_to_in_file)
    solution_time = end-start

    saveStats(solution.solution_length, solution.visited_states_count, solution.explored_states_count, 
            State.max_achieved_depth, solution_time, strategy, strategy_option.lower(), path_to_in_file)

def readDataFromFile(path_to_in_file):
    with open(path_to_in_file) as f:
        read_data = f.read()
    f.closed   

    splitted = read_data.split()

    data = {}
    data["rows"] = int(splitted[0])
    data["columns"] = int(splitted[1])
    data["state"] = []

    for i in range(1, data["rows"]*data["columns"]+1):
        data["state"].append(int(splitted[i+1]))
    return data

def generateTargetState(rows, columns):
    target_state = []
    for i in range(1, rows * columns):
        target_state.append(i)
    target_state.append(0)
    matrix = generateMatrix(target_state, rows, columns)
    return matrix

def generateMatrix(vector, rows, columns):
    matrix = []
    start_index = 0
    for i in range(rows):
        matrix.append(vector[start_index:start_index + columns])
        start_index += columns
    return matrix

def stateIsTarget(state, target):
    if state == target:
        return True
    else: 
        return False

def solveBfs(strategy_option, root_state, target_state_matrix): # FIFO approach
    strategy_option = list(strategy_option)
    frontier = []
    explored = set()

    current_state = root_state

    while stateIsTarget(current_state.state_matrix, target_state_matrix) != True:
        children_matrices = generateChildren(current_state)
        for symbol in strategy_option: 
            if symbol in children_matrices:
                child = State(children_matrices[symbol], current_state.rows, current_state.columns, 
                                    current_state, current_state.path[:], current_state.solution_length + 1)
                if child not in explored:
                    child.addPathStep(symbol)
                    frontier.append(child) 
                    if child.solution_length > State.max_achieved_depth:
                        State.max_achieved_depth = child.solution_length
        explored.add(current_state)
        if frontier != []:
            current_state = frontier.pop(0) #next state to check
            last_state = current_state
        else:
            print("cannot find solution")
            current_state.solution_length = -1
            return current_state
    print("found solution for bfs") 
    last_state.visited_states_count = len(explored) + len(frontier)
    last_state.explored_states_count = len(explored)
    return last_state

def solveDfs(strategy_option, root_state, target_state_matrix, max_possible_depth): # LIFO approach
    strategy_option = list(strategy_option)
    frontier = []
    explored = set()

    current_state = root_state

    counter = 1000000 # big number to avoid dfs cannot find solution 
    while (stateIsTarget(current_state.state_matrix, target_state_matrix) != True) and counter > 0: #different than bfs
        children_matrices = generateChildren(current_state)
        for symbol in strategy_option[::-1]: #different than bfs
            if symbol in children_matrices:
                child = State(children_matrices[symbol], current_state.rows, current_state.columns, 
                                    current_state, current_state.path[:], current_state.solution_length + 1) 
                if child not in explored:
                    # assure that we won't go further than max recursion
                    if child.solution_length > max_possible_depth:
                        pass
                    else:
                        child.addPathStep(symbol)
                        frontier.append(child) 
                        # increment max achieved recursion level 
                        if child.solution_length > State.max_achieved_depth:
                            State.max_achieved_depth = child.solution_length
        explored.add(current_state)
        if frontier != []:
            current_state = frontier.pop()  #different than bfs
            last_state = current_state
        else:
            print("cannot find solution")
            current_state.solution_length = -1
            return current_state
        counter -= 1
    last_state.visited_states_count = len(explored) + len(frontier)
    last_state.explored_states_count = len(explored)
    if (stateIsTarget(current_state.state_matrix, target_state_matrix) != True) and counter == 0:
        print("cannot find solution")
        current_state.solution_length = -1
        return current_state
    print("found solution for dfs")
    return last_state

def solveAstar(strategy_option, root_state, target_state_matrix): #best first
    frontier = []
    explored = set()

    current_state = root_state

    while stateIsTarget(current_state.state_matrix, target_state_matrix) != True:
        children_matrices = generateChildren(current_state)
        sorted_keys = orderChildren(strategy_option, children_matrices, current_state.rows, current_state.columns)
        for sorted_key in sorted_keys:
            child = State(children_matrices[sorted_key[0]], current_state.rows, current_state.columns, 
                                current_state, current_state.path[:], current_state.solution_length + 1)
            if child not in explored:
                child.addPathStep(sorted_key[0])
                frontier.append(child) 
                if child.solution_length > State.max_achieved_depth:
                        State.max_achieved_depth = child.solution_length
        explored.add(current_state)
        if frontier != []:
            current_state = frontier.pop(0) #next state to check
            last_state = current_state
        else:
            print("cannot find solution")
            current_state.solution_length = -1
            return current_state
    print("found solution for astar") 
    last_state.visited_states_count = len(explored) + len(frontier)
    last_state.explored_states_count = len(explored)
    return last_state

def orderChildren(strategy_option, children_matrices, rows, columns):
    order = {}
    for key in children_matrices:
        if strategy_option == "HAMM":
            state_cost = calculateHammingCost(children_matrices[key], rows, columns)
            order[key] = state_cost
        elif strategy_option == "MANH":
            state_cost = calculateManhattanCost(children_matrices[key], rows, columns)
            order[key] = state_cost
    sorted_order = [(k, order[k]) for k in sorted(order, key=order.get)]
    return sorted_order

def calculateHammingCost(state_matrix, rows, columns): # binary cost for every tile except 0		 
    cost = 0		
    for i in range(rows):		
        for j in range(columns):
            if state_matrix[i][j] != 0:	
                target_state = i * columns + j + 1	
                if state_matrix[i][j] != target_state:
                    cost += 1         	       
    return cost	

def calculateManhattanCost(state_matrix, rows, columns): # manh distance for every tile except 0		
    sum = 0		
    for i in range(rows):	
        for j in range(columns):	
            if state_matrix[i][j] != 0:		
                target_state = i * columns + j + 1		
                if state_matrix[i][j] != target_state:  			
                    #find the wanted state coordinates		
                    wanted_i = state_matrix[i][j] // columns	
                    wanted_j = (state_matrix[i][j] % columns) - 1 #callibrate index	
                    #exception for end of the row		
                    if wanted_j == -1:		
                        wanted_j = columns - 1		
                        wanted_i = wanted_i - 1	
                    sum += abs(i - wanted_i) + abs(j - wanted_j)
    return sum

def generateChildren(state):
    rows = len(state.state_matrix)
    columns = len(state.state_matrix[0])
    i_0, j_0 = find0Tile(state.state_matrix, rows, columns)
    children = {}
    #up
    if i_0 != 0:
        state_matrix_up = deepcopy(state.state_matrix)
        state_matrix_up[i_0][j_0] = state.state_matrix[i_0 - 1][j_0]
        state_matrix_up[i_0 - 1][j_0] = 0
        children.update({"U":state_matrix_up})
    #down
    if i_0 != (rows - 1):
        state_matrix_down = deepcopy(state.state_matrix)
        state_matrix_down[i_0][j_0] = state.state_matrix[i_0 + 1][j_0]
        state_matrix_down[i_0 + 1][j_0] = 0
        children.update({"D":state_matrix_down})
    #left
    if j_0 != 0:
        state_matrix_left = deepcopy(state.state_matrix)
        state_matrix_left[i_0][j_0] = state.state_matrix[i_0][j_0 - 1]
        state_matrix_left[i_0][j_0 - 1] = 0
        children.update({"L":state_matrix_left})
    #right
    if j_0 != (columns - 1):
        state_matrix_right = deepcopy(state.state_matrix)
        state_matrix_right[i_0][j_0] = state.state_matrix[i_0][j_0 + 1]
        state_matrix_right[i_0][j_0 + 1] = 0
        children.update({"R":state_matrix_right})
    return children

def find0Tile(state_matrix, rows, columns):
    index = []
    for i in range(rows):
        for j in range(columns):
            if state_matrix[i][j] == 0:   
                index = [i,j]   
    return index

def saveSolution(solution_length, solution_path, strategy, strategy_option, path_to_in_file):
    dir_name = "solutions"
    makeDir(dir_name)

    f = open(dir_name + "/" + path_to_in_file + "_" + strategy + "_" + strategy_option + "_sol.txt", 'w')
    f.write(str(solution_length))
    if solution_length != -1:
        f.write("\n" + ''.join(solution_path))
    f.close()

def saveStats(solution_length, visited_states_count, explored_states_count, max_achieved_depth,
                                            time, strategy, strategy_option, path_to_in_file):
    dir_name = "stats"
    makeDir(dir_name)

    f = open(dir_name + "/" + path_to_in_file + "_" + strategy + "_" + strategy_option + "_stats.txt", 'w')
    f.write(str(solution_length) + "\n" + str(visited_states_count) + "\n" + str(explored_states_count) + "\n" 
                                            + str(max_achieved_depth) + "\n" + str(time))
    f.close()

def makeDir(dir_name):
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)
        print("Directory \"" + dir_name + "\" Created ")
    else:    
        print("Directory \"" + dir_name + "\" already exists")

if __name__ == "__main__":
    main()