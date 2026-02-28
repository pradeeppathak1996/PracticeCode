s = [[2,50] , [3,90] , [1,40] , [4,30]]

flat = [item for item in s for item in item ]

print(flat)

# ----- find only second elements -----

s = [[2,50] , [3,90] , [1,40] , [4,30]]

second_col = [item[1] for item in s]

print(second_col)

# ----- Optimal way to flatten a list -----

s = [[1,2],[1,2,3],[4,5],[5,[6,7]]]

output = []

for item in s:
    if type(item) == list:
        for val in item:
            output.append(val)
    else:
        output.append(item)
print(output)