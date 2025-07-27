from itertools import permutations

cases = [["sa4"], ["sA4"], ["se3"], ["sE3"], ["so0"], ["sO0"], ["si1"], ["sI1"]]

for combo in permutations(cases):
    print(str(i) for i in combo)