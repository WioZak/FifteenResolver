import sys
import numpy as np
from Sets import set

class Node():
    id = 0
    state_matrix = []
    children = {}  # {'u' : Node()}
    parent_id = -1
    possible_moves = []
    path = []
    depth_level = -1

    def __init__(self, state_matrix):
        self.state_matrix = state_matrix

    def setID(self,id):
        self.id = id

    def generateChildrenStates(self):
        pass

    


def main():

    if len(sys.argv) == 4:
        strategy = sys.argv[1]
        strategy_option = sys.argv[2]
        path_to_in_file = sys.argv[3]
        
    else:
        print("Wrong number of arguments!")

    data = readDataFromFile(path_to_in_file)

    target_state_matrix = generateTargetState(data["rows"], data["columns"])

    print(target_state_matrix)

    state = data["state"]
    state_matrix = generateMatrix(state, data["rows"], data["columns"])
    print(state_matrix)
    
    print(checkStateIsTarget(state_matrix, target_state_matrix))


    # check strategy
    if strategy == "bfs":
        solveBfs(strategy_option, state)
    elif strategy == "dfs":
        solveDfs(strategy_option)
    elif strategy == "astr":
        solveAstar(strategy_option)
    else:
        print("Wrong strategy name")


    # checkIfValidOption(strategy, strategy_option)

    print(strategy, strategy_option, path_to_in_file) 

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

    print("data: " + str(data))
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

def checkStateIsTarget(state, target):
    if state == target:
        return True
    else: 
        return False

def solveBfs(strategy_option, state):
    strategy_option = list(strategy_option)

    frontier = []
    visited = Set([])


def solveDfs(strategy_option):
    frontier = []

def solveAstar(strategy_option):
    frontier = []

def generateStateByMoveChar(state, char, rows, columns, x_0, y_0):
    if char == "U":
        pass
    elif char == "D":
        pass
    elif char == "L":
        pass
    elif char == "R":
        pass

def calculateHammingCost(state, target_state, rows, columns): # binary cost for every tile except 0
    cost = 0
    for i in range(rows):
        for j in range(columns):
            if state[i][j] != 0:
                if state[i][j] != target_state[i][j]:
                    cost += 1         
    return cost

def calculateManhattanCost(state, target_state, rows, columns): # for every pair except 0
    sum = 0
    for i in range(rows):
        for j in range(columns):
            if state[i][j] != 0:
                target_state = i*columns + j + 1
                if state[i][j] != target_state:
                    #find the wanted state coordinates
                    wanted_i = state[i][j] // columns
                    wanted_j = (state[i][j] % columns) - 1
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