from itertools import permutations
import os
# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the file path
file_path = os.path.join(script_dir, "input.txt")


G = {i+j*1j: c for i,r in enumerate(open(file_path))
               for j,c in enumerate(r.strip())}

for r in [1], range(50):
    anti = []
    for freq in {*G.values()} - {'.'}:
        ants = [p for p in G if G[p] == freq]
        pairs = permutations(ants, 2)
        anti += [a+n*(a-b) for a,b in pairs
                           for n in r]

    print(len(set(anti) & set(G)))