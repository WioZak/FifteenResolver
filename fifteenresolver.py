import sys
import numpy as np
from copy import deepcopy

class State(): # aka node
    id = 0
    children = {}  # {'u' : State()}
    path = [] #this should be copied from a parent and appended with last move

    def __init__(self, state_matrix, rows, columns, parent_id = -1, depth_level = 0):
        self.state_matrix = state_matrix
        self.rows = rows
        self.columns = columns
        self.parent_id = parent_id
        self.depth_level = depth_level

    def setID(self,id):
        self.id = id

    def calculateHammingCost(self, target_state): # binary cost for every tile except 0
        cost = 0
        for i in range(self.rows):
            for j in range(self.columns):
                if self.state_matrix[i][j] != 0:
                    if self.state_matrix[i][j] != target_state[i][j]:
                        cost += 1         
        return cost

    def calculateManhattanCost(self): # for every pair except 0
        sum = 0
        for i in range(self.rows):
            for j in range(self.columns):
                if self.state_matrix[i][j] != 0:
                    target_state = i * self.columns + j + 1
                    if self.state_matrix[i][j] != target_state:
                        #find the wanted state coordinates
                        wanted_i = self.state_matrix[i][j] // self.columns
                        wanted_j = (self.state_matrix[i][j] % self.columns) - 1 #callibrate index
                        #exception for end of the row
                        if wanted_j == -1:
                            wanted_j = self.columns - 1
                            wanted_i = wanted_i - 1
                        sum += abs(i - wanted_i) + abs(j - wanted_j)
        return sum

    def checkStateIsTarget(self, target_state_matrix):
        if self.state_matrix == target_state_matrix:
            return True
        else: 
            return False
    
    def stateMatrix(self):
        return self.state_matrix

    def addChildren(self, children):
        self.children = children

    def __hash__(self):
        return hash(self.state_matrix) #??? check if OK

    def __eq__(self, other):
        return (
            self.__class__ == other.__class__ and
            self.state_matrix == other.state_matrix
        )

def main():

    if len(sys.argv) == 4:
        strategy = sys.argv[1].lower()
        strategy_option = sys.argv[2].upper()
        path_to_in_file = sys.argv[3]
        
    else:
        print("Wrong number of arguments!")

    data = readDataFromFile(path_to_in_file)

    target_state_matrix = generateTargetState(data["rows"], data["columns"])

    #print(target_state_matrix)

    state_data = data["state"]
    state_matrix = generateMatrix(state_data, data["rows"], data["columns"])

    root_state = State(state_matrix, data["rows"], data["columns"])
    #print(state_matrix)
    #print(find0Tile(state_matrix, data["rows"], data["columns"]))
    
    #print(checkStateIsTarget(state_matrix, target_state_matrix))


    # check strategy
    if strategy == "bfs":
        solveBfs(strategy_option, root_state, target_state_matrix)
    elif strategy == "dfs":
        solveDfs(strategy_option)
    #elif strategy == "astr":
     #   solveAstar(strategy_option, node)
    else:
        print("Wrong strategy name")


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

    #print("data: " + str(data))
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

def solveBfs(strategy_option, root_state, target_state_matrix):
    strategy_option = list(strategy_option)
    frontier = []
    explored = set()

    frontier.append(root_state)
    current_state = frontier.pop(0)
    print(current_state)

    while stateIsTarget(current_state.state_matrix, target_state_matrix) != True:
        children = generateChildren(current_state)
        for symbol in strategy_option: 
            if symbol in frontier:
                frontier.append(children[symbol])
        explored.add(current_state)
        if frontier != []:
            current_state = frontier.pop(0) #next state to check
        else:
            return "cannot find solution"

    print("bfs") 
    return "found resolution"



def solveDfs(strategy_option):
    frontier = []
    explored = set()

def solveAstar(strategy_option):
    frontier = []
    explored = set()
    if strategy_option == "manh":
        pass
    if strategy_option == "hamm":
        pass

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

def calculateHammingCost(state_matrix, target_state, rows, columns): # binary cost for every tile except 0
    cost = 0
    for i in range(rows):
        for j in range(columns):
            if state_matrix[i][j] != 0:
                if state_matrix[i][j] != target_state[i][j]:
                    cost += 1         
    return cost

def calculateManhattanCost(state_matrix, rows, columns): # for every pair except 0
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

def saveSolution(solution_length, solution_trace):
    pass

def saveStats(solution_length, visited_states_count, checked_states_count, max_recursion_depth, time):
    pass




if __name__ == "__main__":
    main()