from os import listdir
from os.path import isfile, join
import os
import re

testdir = 'test_files'
statfiles = [f for f in listdir(testdir) if isfile(join(testdir, f))]
statfiles = sorted(statfiles)

for strategy_option in ["hamm", "manh"]:
        for file in statfiles:
                if re.match(r"\d[x]\d_\d{2}_\d{5}.txt", file):
                        os.system("python fifteenresolver.py astr " +  strategy_option + " " + testdir + "/" + file)
                        print("astr", strategy_option, file)


for strategy in ["bfs", "dfs"]:
        for strategy_option in ["RDUL", "RDLU", "DRUL", "DRLU", "LUDR", "LURD", "ULDR", "ULRD"]:
                for file in statfiles:
                        if re.match(r"\d[x]\d_\d{2}_\d{5}.txt", file):
                                os.system("python fifteenresolver.py " + strategy + " " +  strategy_option + " " + testdir + "/" + file)
                                print(strategy, strategy_option, file)


