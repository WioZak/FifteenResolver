import sys
import numpy as np

class Node():
    id = 0
    state = []
    children = []
    parent_id = -1
    possible_moves = []
    path = []
    depth_level = -1

    def checkPossibleMoves(self):
        pass

    def generateChildrenStates(self):
        pass
    


def main():
    strategy = "" 
    strategy_option = ""
    path_to_in_file = ""

    if len(sys.argv) == 4:
        strategy = sys.argv[1]
        strategy_option = sys.argv[2]
        path_to_in_file = sys.argv[3]
        
    else:
        print("Wrong number of arguments!")

    data = readDataFromFile(path_to_in_file)

    target_state = generateTargetState(data["rows"], data["columns"])

    print(target_state)

    state = data["state"]
    
    print(checkStateIsTarget(state, target_state))


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

    #print(generateMatrix())

    
    print(strategy, strategy_option, path_to_in_file) 

def readDataFromFile(path_to_in_file):
    with open(path_to_in_file) as f:
        read_data = f.read()
    f.closed   

    splitted = read_data.split()

    data = {}
    data["rows"] = splitted[0]
    data["columns"] = splitted[1]
    data["state"] = []

    for i in range(1, int(data["rows"])*int(data["columns"])):
        data["state"].append(int(splitted[i+1]))

    print("data: " + str(data))
    return data


def generateTargetState(rows, columns):
    target_state = []
    for i in range(1, int(rows)*int(columns)):
        target_state.append(i)
    target_state.append(0)
    return target_state

def checkStateIsTarget(state, target):
    if state == target:
        return True
    else: 
        return False

def solveBfs(strategy_option, state):
    frontier = []
    visited = []

def solveDfs(strategy_option):
    frontier = []

def solveAstar(strategy_option):
    frontier = []

def saveSolution(solution_length, solution_trace):
    pass

def saveStats(solution_length, visited_states_count, checked_states_count, max_recursion_depth, time):
    pass

def generateMatrix(vector, rows, columns):
    matrix = []
    start_index = 0
    for i in range(rows):
        matrix.append(vector[start_index:start_index + columns])
        start_index += columns
    return matrix

if __name__ == "__main__":
    main()