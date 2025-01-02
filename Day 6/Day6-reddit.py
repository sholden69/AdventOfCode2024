import os
# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the file path
file_path = os.path.join(script_dir, "input.txt")

#Grid Representation (G): The map is stored in a dictionary where:
#
# Key: A complex number i + j * 1j (representing grid coordinates where i is x and j is y).
# Value: The character at that grid position (., #, or ^).
# Complex numbers are used for positional representation:#

# 1j represents movement in the imaginary direction (y-axis).
# 1 represents movement in the real direction (x-axis).


G = {i+j*1j: c for i,r in enumerate(open(file_path))
               for j,c in enumerate(r.strip())}
# Outer Loop: for i, r in enumerate(open(file_path)) reads the file line by  line
#  enumerate provides:
# i: The row index (starting from 0).
# r: The content of each row as a string.

# Inner Loop: 
# for j, c in enumerate(r.strip()) r.strip() removes any trailing newline characters from the row string.
# enumerate provides:
# j: The column index (starting from 0).
# c: The character at that column.

# find the smallest coord of the starting position - there should only be one.
start = min(p for p in G if G[p] == '^')

def walk(G):
    pos, dir, seen = start, -1, set()
    while pos in G and (pos,dir) not in seen:
        seen |= {(pos,dir)}   #use union operator to update the seen set
        # rotate 90degrees if where at an obstacle
        if G.get(pos+dir) == "#":  
            dir *= -1j
        else: pos += dir  # else move
    return {p for p,_ in seen}, (pos,dir) in seen

path = walk(G)[0]
print('part 1:',len(path))
print('part 2:',sum(walk(G | {o: '#'})[1] for o in path))