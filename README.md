# FifteenResolver

How to use:

```
python fifteenresolver.py <strategy> <strategy_option> <input_file>
```
Example:
```
python fifteenresolver.py bfs RLDU 4x4_01_00001.txt
```

Where:

| Strategy              | Acronym  |
| --------------------- | -------- |
| breadth-first search  | bfs      |
| depth-first search    | dfs      |
| A-star (heuristic)    | astr     |

| Strategy option               | Acronym                           |
| ----------------------------- | --------------------------------- |
| order of searching (bfs, dfs) | permutation of U, L, D, R letters |
| heuristic - Hamming metric    | hamm                              |
| heuristic - Manhattan metric  | manh                              |

Input file:
```
first line: <number_of_rows> <number_of_columns>
next lines: <puzzle_matrix>
```
For puzzle 2x2 we count tiles as follows: 1,2,3,0, where 0 is the missing tile.

Example file with 4x4 puzzle:
```
4 4
1 2 3 4
5 6 7 8
9 10 11 0
13 14 15 12
```

Program will solve the puzzle to match target state:
```
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 0
```

After running this script, two directories will be created - solutions and stats.\
Files in solutions contain solution length in first line and solution path in second line.\
Files in stats contain:
- solution length
- visited states count
- explored states count
- max achieved length
- time (in miliseconds)

Also, you can use batchresolver.py to generate solutions and statistics for every file in test_files directory.\
To generate csv with statistics (15data.csv), use writecsv.py script.\
To generate plots, use generateplots.py script (generated plots will be in plots directory).


