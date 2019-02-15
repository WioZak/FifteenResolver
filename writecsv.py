import csv
from os import listdir
from os.path import isfile, join
import re

with open('15data.csv', mode='w') as data_file:
    writer = csv.writer(data_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    dir_name = "stats"
    statfiles = [f for f in listdir(dir_name) if isfile(join(dir_name, f))]
    statfiles = sorted(statfiles)
    
    writer.writerow(["depth", "number", "strategy", "strategy_option", "solution_length", 
                        "visited_states_count", "explored_states_count", "max_achieved_depth", "time"])

    for filename in statfiles:
        if re.match(r"\d[x]\d_\d{2}_\d{5}_\w{1,}_\w{1,}_stats.txt", filename):
            with open(dir_name + "/" + filename) as f:
                read_data = f.read()
            f.closed 
            splitted_name = filename.split("_")  
            splitted_data = read_data.split()

            writer.writerow([splitted_name[1], splitted_name[2], splitted_name[3], splitted_name[4], splitted_data[0], splitted_data[1], 
                                    splitted_data[2], splitted_data[3], splitted_data[4]])
