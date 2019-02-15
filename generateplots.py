import os
import pandas as pd
import matplotlib.pyplot as plt
from pylab import figure, axes, pie, title, show

import numpy as np

df = pd.read_csv('15data.csv')

# overall time
# print("overall time: ", df.sum()[8]/1000/60/60)

options = ["RDUL", "RDLU", "DRUL", "DRLU", "LUDR", "LURD", "ULDR", "ULRD"]

# series categorized by strategy and depth
df_bfs, df_dfs, df_dfs_positive_length, df_astr = [[],[],[],[]]
for i in range(1,8):
        df_bfs.append(df.loc[(df['depth'] == i) & (df['strategy'] == "bfs")])
        df_dfs.append(df.loc[(df['depth'] == i) & (df['strategy'] == "dfs")])
        df_dfs_positive_length.append(df.loc[(df['depth'] == i) & (df['strategy'] == "dfs") & (df['solution_length'] != -1)])
        df_astr.append(df.loc[(df['depth'] == i) & (df['strategy'] == "astr")])

# mean time stats
df_bfs_time, df_dfs_time, df_astr_time = [[],[],[]]
for i in range(0,7):
        df_bfs_time.append(df_bfs[i]["time"].mean())
        df_dfs_time.append(df_dfs[i]["time"].mean())
        df_astr_time.append(df_astr[i]["time"].mean())

# mean visited states count stats
df_bfs_visited, df_dfs_visited, df_astr_visited = [[],[],[]]
for i in range(0,7):
        df_bfs_visited.append(df_bfs[i]["visited_states_count"].mean())
        df_dfs_visited.append(df_dfs[i]["visited_states_count"].mean())
        df_astr_visited.append(df_astr[i]["visited_states_count"].mean())

# mean explored states count stats
df_bfs_explored, df_dfs_explored, df_astr_explored = [[],[],[]]
for i in range(0,7):
        df_bfs_explored.append(df_bfs[i]["explored_states_count"].mean())
        df_dfs_explored.append(df_dfs[i]["explored_states_count"].mean())
        df_astr_explored.append(df_astr[i]["explored_states_count"].mean())

# mean max achieved depth stats
df_bfs_maxdepth, df_dfs_maxdepth, df_astr_maxdepth = [[],[],[]]
for i in range(0,7):
        df_bfs_maxdepth.append(df_bfs[i]["max_achieved_depth"].mean())
        df_dfs_maxdepth.append(df_dfs[i]["max_achieved_depth"].mean())
        df_astr_maxdepth.append(df_astr[i]["max_achieved_depth"].mean())

# mean solution length stats
df_bfs_length, df_dfs_length, df_astr_length = [[],[],[]]
for i in range(0,7):
        df_bfs_length.append(df_bfs[i]["solution_length"].mean())
        df_dfs_length.append(df_dfs_positive_length[i]["solution_length"].mean())
        df_astr_length.append(df_astr[i]["solution_length"].mean())

# strategy series splitted by strategy options
df_bfs_split, df_dfs_split, df_dfs_split_positive_length = [[],[],[]]
for k in range(len(options)):
        df_bfs_split.append([])
        df_dfs_split.append([])
        df_dfs_split_positive_length.append([])
        for i in range(0,7):
                df_bfs_split[k].append(df.loc[(df['depth'] == i+1) & (df['strategy'] == "bfs") & (df['strategy_option'] == options[k].lower())])
                df_dfs_split[k].append(df.loc[(df['depth'] == i+1) & (df['strategy'] == "dfs") & (df['strategy_option'] == options[k].lower())])
                df_dfs_split_positive_length[k].append(df.loc[(df['depth'] == i+1) & (df['strategy'] == "dfs") 
                                & (df['strategy_option'] == options[k].lower()) & (df['solution_length'] != -1)])

df_astr_hamm, df_astr_manh = [[],[]]
for i in range(0,7):
        df_astr_hamm.append(df.loc[(df['depth'] == i+1) & (df['strategy'] == "astr") & (df['strategy_option'] == "hamm")])
        df_astr_manh.append(df.loc[(df['depth'] == i+1) & (df['strategy'] == "astr") & (df['strategy_option'] == "manh")])

# explored stats for splitted data
df_bfs_split_explored, df_dfs_split_explored = [[],[]]
for k in range(len(options)):
        df_bfs_split_explored.append([])
        df_dfs_split_explored.append([])
        for i in range(0,7):
                df_bfs_split_explored[k].append(df_bfs_split[k][i].mean()["explored_states_count"])
                df_dfs_split_explored[k].append(df_dfs_split[k][i].mean()["explored_states_count"])

df_astr_hamm_explored, df_astr_manh_explored = [[],[]]

for i in range(0,7):
        df_astr_hamm_explored.append(df_astr_hamm[i].mean()["explored_states_count"])
        df_astr_manh_explored.append(df_astr_manh[i].mean()["explored_states_count"])

# visited stats for splitted data
df_bfs_split_visited, df_dfs_split_visited = [[],[]]
for k in range(len(options)):
        df_bfs_split_visited.append([])
        df_dfs_split_visited.append([])
        for i in range(0,7):
                df_bfs_split_visited[k].append(df_bfs_split[k][i].mean()["visited_states_count"])
                df_dfs_split_visited[k].append(df_dfs_split[k][i].mean()["visited_states_count"])

df_astr_hamm_visited, df_astr_manh_visited = [[],[]]

for i in range(0,7):
        df_astr_hamm_visited.append(df_astr_hamm[i].mean()["visited_states_count"])
        df_astr_manh_visited.append(df_astr_manh[i].mean()["visited_states_count"])

# time stats for splitted data
df_bfs_split_time, df_dfs_split_time = [[],[]]
for k in range(len(options)):
        df_bfs_split_time.append([])
        df_dfs_split_time.append([])
        for i in range(0,7):
                df_bfs_split_time[k].append(df_bfs_split[k][i].mean()["time"])
                df_dfs_split_time[k].append(df_dfs_split[k][i].mean()["time"])

df_astr_hamm_time, df_astr_manh_time = [[],[]]

for i in range(0,7):
        df_astr_hamm_time.append(df_astr_hamm[i].mean()["time"])
        df_astr_manh_time.append(df_astr_manh[i].mean()["time"])

# solution length stats for splitted data
df_bfs_split_length, df_dfs_split_length = [[],[]]
for k in range(len(options)):
        df_bfs_split_length.append([])
        df_dfs_split_length.append([])
        for i in range(0,7):
                df_bfs_split_length[k].append(df_bfs_split[k][i].mean()["solution_length"])
                df_dfs_split_length[k].append(df_dfs_split_positive_length[k][i].mean()["solution_length"])

df_astr_hamm_length, df_astr_manh_length = [[],[]]

for i in range(0,7):
        df_astr_hamm_length.append(df_astr_hamm[i].mean()["solution_length"])
        df_astr_manh_length.append(df_astr_manh[i].mean()["solution_length"])

# maxdepth for splitted data
df_bfs_split_maxdepth, df_dfs_split_maxdepth = [[],[]]
for k in range(len(options)):
        df_bfs_split_maxdepth.append([])
        df_dfs_split_maxdepth.append([])
        for i in range(0,7):
                df_bfs_split_maxdepth[k].append(df_bfs_split[k][i].mean()["max_achieved_depth"])
                df_dfs_split_maxdepth[k].append(df_dfs_split[k][i].mean()["max_achieved_depth"])

df_astr_hamm_maxdepth, df_astr_manh_maxdepth = [[],[]]

for i in range(0,7):
        df_astr_hamm_maxdepth.append(df_astr_hamm[i].mean()["max_achieved_depth"])
        df_astr_manh_maxdepth.append(df_astr_manh[i].mean()["max_achieved_depth"])

if not os.path.exists('plots'):
        os.mkdir('plots')

# 1
#-------Mean TIME all--------#
X = ['1', '2', '3', '4', '5', '6', '7']
fig, ax = plt.subplots()

df = pd.DataFrame(np.c_[df_dfs_time, df_bfs_time, df_astr_time], index=X)
df.plot(title='Średni czas przetwarzania', kind='bar', ax=ax, logy=True, rot=0, colormap='summer')
ax.legend(["DFS", "BFS", "A*"], loc=2)
ax.set_ylabel('milisekundy')

plt.savefig('plots/time_all.png')

#-------Mean time for dfs--------#
fig, ax = plt.subplots()

df = pd.DataFrame(np.c_[df_dfs_split_time[0],df_dfs_split_time[1], df_dfs_split_time[2],df_dfs_split_time[3], 
        df_dfs_split_time[4], df_dfs_split_time[5],df_dfs_split_time[6], df_dfs_split_time[7]], index=X)
df.plot(title='Średni czas przetwarzania DFS', kind='bar', ax=ax, logy=True, rot=0, colormap='summer')
ax.legend(options, loc=4)
ax.set_ylabel('milisekundy')

plt.savefig('plots/time_dfs.png')

#-------Mean time for bfs--------#
fig, ax = plt.subplots()

df = pd.DataFrame(np.c_[df_bfs_split_time[0],df_bfs_split_time[1], df_bfs_split_time[2],df_bfs_split_time[3], 
        df_bfs_split_time[4], df_bfs_split_time[5],df_bfs_split_time[6], df_bfs_split_time[7]], index=X)
df.plot(title='Średni czas przetwarzania BFS', kind='bar', ax=ax, rot=0, colormap='summer')
ax.legend(options, loc=2)
ax.set_ylabel('milisekundy')

plt.savefig('plots/time_bfs.png')

#-------Mean time for astr--------#
fig, ax = plt.subplots()

df = pd.DataFrame(np.c_[df_astr_hamm_time, df_astr_manh_time], index=X)
df.plot(title='Średni czas przetwarzania A*', kind='bar', ax=ax, rot=0, colormap='summer')
ax.legend(["HAMM", "MANH"], loc=2)
ax.set_ylabel('milisekundy')

plt.savefig('plots/time_astr.png')

#2
#-------Mean solution length all--------#
fig, ax = plt.subplots()

df = pd.DataFrame(np.c_[df_dfs_length, df_bfs_length, df_astr_length], index=X)
df.plot(title='Średnia długość rozwiązania', kind='bar', ax=ax, rot=0, colormap='summer')
ax.legend(["DFS", "BFS", "A*"], loc=2)
ax.set_ylabel('znaleziona długość')

plt.savefig('plots/length_all.png')


#-------Mean length for dfs--------#
fig, ax = plt.subplots()

df = pd.DataFrame(np.c_[df_dfs_split_length[0],df_dfs_split_length[1], df_dfs_split_length[2],df_dfs_split_length[3], 
        df_dfs_split_length[4], df_dfs_split_length[5],df_dfs_split_length[6], df_dfs_split_length[7]], index=X)
df.plot(title='Średnia długość rozwiązania DFS', kind='bar', ax=ax, rot=0, colormap='summer')
ax.legend(options, loc=4)
ax.set_ylabel('znaleziona długość')

plt.savefig('plots/length_dfs.png')

#-------Mean length for bfs--------#
fig, ax = plt.subplots()

df = pd.DataFrame(np.c_[df_bfs_split_length[0],df_bfs_split_length[1], df_bfs_split_length[2],df_bfs_split_length[3], 
        df_bfs_split_length[4], df_bfs_split_length[5],df_bfs_split_length[6], df_bfs_split_length[7]], index=X)
df.plot(title='Średnia długość rozwiązania BFS', kind='bar', ax=ax, rot=0, colormap='summer')
ax.legend(options, loc=2)
ax.set_ylabel('znaleziona długość')

plt.savefig('plots/length_bfs.png')

#-------Mean length for astr--------#
fig, ax = plt.subplots()

df = pd.DataFrame(np.c_[df_astr_hamm_length, df_astr_manh_length], index=X)
df.plot(title='Średnia długość rozwiązania A*', kind='bar', ax=ax, rot=0, colormap='summer')
ax.legend(["HAMM", "MANH"], loc=2)
ax.set_ylabel('znaleziona długość')

plt.savefig('plots/length_astr.png')

#3
#-------Mean explored states all--------#
fig, ax = plt.subplots()

df = pd.DataFrame(np.c_[df_dfs_explored, df_bfs_explored, df_astr_explored], index=X)
df.plot(title='Średnia liczba przetworzonych stanów', kind='bar', ax=ax, logy=True, rot=0, colormap='summer')
ax.legend(["DFS", "BFS", "A*"], loc=2)
ax.set_ylabel('liczba stanów')

plt.savefig('plots/explored_all.png')

#-------Mean explored for dfs--------#
fig, ax = plt.subplots()

df = pd.DataFrame(np.c_[df_dfs_split_explored[0],df_dfs_split_explored[1], df_dfs_split_explored[2],df_dfs_split_explored[3], 
        df_dfs_split_explored[4], df_dfs_split_explored[5],df_dfs_split_explored[6], df_dfs_split_explored[7]], index=X)
df.plot(title='Średnia liczba przetworzonych stanów DFS', kind='bar', ax=ax, logy=True, rot=0, colormap='summer')
ax.legend(options, loc=4)
ax.set_ylabel('ilość stanów')

plt.savefig('plots/explored_dfs.png')

#-------Mean explored for bfs--------#
fig, ax = plt.subplots()

df = pd.DataFrame(np.c_[df_bfs_split_explored[0],df_bfs_split_explored[1], df_bfs_split_explored[2],df_bfs_split_explored[3], 
        df_bfs_split_explored[4], df_bfs_split_explored[5],df_bfs_split_explored[6], df_bfs_split_explored[7]], index=X)
df.plot(title='Średnia liczba przetworzonych stanów BFS', kind='bar', ax=ax, rot=0, colormap='summer')
ax.legend(options, loc=2)
ax.set_ylabel('ilość stanów')

plt.savefig('plots/explored_bfs.png')

#-------Mean explored for astr--------#
fig, ax = plt.subplots()

df = pd.DataFrame(np.c_[df_astr_hamm_explored, df_astr_manh_explored], index=X)
df.plot(title='Średnia liczba przetworzonych stanów A*', kind='bar', ax=ax, rot=0, colormap='summer')
ax.legend(["HAMM", "MANH"], loc=2)
ax.set_ylabel('ilość stanów')

plt.savefig('plots/explored_astr.png')

#4
#-------Mean visited states all--------#
fig, ax = plt.subplots()

df = pd.DataFrame(np.c_[df_dfs_visited, df_bfs_visited, df_astr_visited], index=X)
df.plot(title='Średnia liczba odwiedzonych stanów', kind='bar', ax=ax, logy=True, rot=0, colormap='summer')
ax.legend(["DFS", "BFS", "A*"], loc=2)
ax.set_ylabel('liczba stanów')

plt.savefig('plots/visited_all.png')

#-------Mean visited for dfs--------#
fig, ax = plt.subplots()

df = pd.DataFrame(np.c_[df_dfs_split_visited[0],df_dfs_split_visited[1], df_dfs_split_visited[2],df_dfs_split_visited[3], 
        df_dfs_split_visited[4], df_dfs_split_visited[5],df_dfs_split_visited[6], df_dfs_split_visited[7]], index=X)
df.plot(title='Średnia liczba odwiedzonych stanów DFS', kind='bar', ax=ax, logy=True, rot=0, colormap='summer')
ax.legend(options, loc=4)
ax.set_ylabel('ilość stanów')

plt.savefig('plots/visited_dfs.png')

#-------Mean visited for bfs--------#
fig, ax = plt.subplots()

df = pd.DataFrame(np.c_[df_bfs_split_visited[0],df_bfs_split_visited[1], df_bfs_split_visited[2],df_bfs_split_visited[3], 
        df_bfs_split_visited[4], df_bfs_split_visited[5],df_bfs_split_visited[6], df_bfs_split_visited[7]], index=X)
df.plot(title='Średnia liczba odwiedzonych stanów BFS', kind='bar', ax=ax, rot=0, colormap='summer')
ax.legend(options, loc=2)
ax.set_ylabel('ilość stanów')

plt.savefig('plots/visited_bfs.png')

#-------Mean visited for astr--------#
fig, ax = plt.subplots()

df = pd.DataFrame(np.c_[df_astr_hamm_visited, df_astr_manh_visited], index=X)
df.plot(title='Średnia liczba odwiedzonych stanów A*', kind='bar', ax=ax, rot=0, colormap='summer')
ax.legend(["HAMM", "MANH"], loc=2)
ax.set_ylabel('ilość stanów')

plt.savefig('plots/visited_astr.png')

#5
#-------mean maxdepth all--------#
fig, ax = plt.subplots()

df = pd.DataFrame(np.c_[df_dfs_maxdepth, df_bfs_maxdepth, df_astr_maxdepth], index=X)
df.plot(title='Średnia maksymalna głębokość rekursji', kind='bar', ax=ax, rot=0, colormap='summer')
ax.legend(["DFS", "BFS", "A*"], loc=2)
ax.set_ylabel('głębokość rekursji')

plt.savefig('plots/depth_all.png')

#-------Mean maxdepth for dfs--------#
fig, ax = plt.subplots()

df = pd.DataFrame(np.c_[df_dfs_split_maxdepth[0],df_dfs_split_maxdepth[1], df_dfs_split_maxdepth[2],df_dfs_split_maxdepth[3], 
        df_dfs_split_maxdepth[4], df_dfs_split_maxdepth[5],df_dfs_split_maxdepth[6], df_dfs_split_maxdepth[7]], index=X)
df.plot(title='Średnia maksymalna głębokość rekursji DFS', kind='bar', ax=ax, rot=0, colormap='summer')
ax.legend(options, loc=4)
ax.set_ylabel('głębokość rekursji')

plt.savefig('plots/depth_dfs.png')

#-------Mean maxdepth for bfs--------#
fig, ax = plt.subplots()

df = pd.DataFrame(np.c_[df_bfs_split_maxdepth[0],df_bfs_split_maxdepth[1], df_bfs_split_maxdepth[2],df_bfs_split_maxdepth[3], 
        df_bfs_split_maxdepth[4], df_bfs_split_maxdepth[5],df_bfs_split_maxdepth[6], df_bfs_split_maxdepth[7]], index=X)
df.plot(title='Średnia maksymalna głębokość rekursji BFS', kind='bar', ax=ax, rot=0, colormap='summer')
ax.legend(options, loc=2)
ax.set_ylabel('głębokość rekursji')

plt.savefig('plots/depth_bfs.png')

#-------Mean maxdepth for astr--------#
fig, ax = plt.subplots()

df = pd.DataFrame(np.c_[df_astr_hamm_maxdepth, df_astr_manh_maxdepth], index=X)
df.plot(title='Średnia maksymalna głębokość rekursji A*', kind='bar', ax=ax, rot=0, colormap='summer')
ax.legend(["HAMM", "MANH"], loc=2)
ax.set_ylabel('głębokość rekursji')

plt.savefig('plots/depth_astr.png')
