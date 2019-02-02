from os import listdir
from os.path import isfile, join
import os
import re

onlyfiles = [f for f in listdir('test_files') if isfile(join('test_files', f))]
onlyfiles = sorted(onlyfiles)

for strategy in ["bfs", "dfs"]:
        for strategy_option in ["RDUL", "RDLU", "DRUL", "DRLU", "LUDR", "LURD", "ULDR", "ULRD"]:
                for file in onlyfiles:
                        if re.match(r"[0-9][x][0-9]_[0-9]+_[0-9]+.txt", file):
                                os.system("python fifteenresolver.py " + strategy + " " +  strategy_option + " test_files/" + file)
                                print(strategy, strategy_option, file)


for strategy_option in ["hamm", "manh"]:
        for file in onlyfiles:
                if re.match(r"[0-9][x][0-9]_[0-9]+_[0-9]+.txt", file):
                        os.system("python fifteenresolver.py astr " +  strategy_option + " test_files/" + file)
                        print("astr", strategy_option, file)
