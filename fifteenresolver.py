import sys

class Node():
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
    



    # switch case for strategy and strategy option

    # checkIfValidOption(strategy, strategy_option)



    
    print(strategy, strategy_option, path_to_in_file) 

def readDataFromFile(path_to_in_file):
    with open(path_to_in_file) as f:
        read_data = f.read()
    f.closed   

    splitted = read_data.split()

    data = {}
    data["rows"] = splitted[0]
    data["columns"] = splitted[1]
    data["state"] = splitted[2:]

    print("data: " + str(data))
    return data


def generateTargetState(rows, columns):
    target_state = []
    for i in range(1, int(rows)*int(columns)):
        target_state.append(i)
    target_state.append(0)
    return target_state
    

def solveBfs(strategy_option):
    pass

def solveDfs(strategy_option):
    pass

def solveAstar(strategy_option):
    pass

def saveOutput():
    pass

def saveInfo():
    pass


if __name__ == "__main__":
    main()