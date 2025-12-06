# count in dictionary --------------

d = {}
for i in range(1,11):
    d[i] = i
print(d)

# Reverse a dictionary (key → value swap)

d = {"a":1, "b":2, "c":3}
rev = {}

for k,v in d.items():
    rev[v] = k
print(rev)

# ------- Merge two dictionaries ----------------

d1 = {1: "A", 2: "B"}
d2 = {3: "C", 4: "D"}

merge = {}

for i in d1:
    merge[i] = d1[i]
for i in d2:
    merge[i] = d2[i]

print(merge)

# --------- Find key with maximum value --------------

d = {"a":10, "b":50, "c":20}

max_key = ""
max_value = 0

for k,v in d.items():
    if v > max_value:
        max_value = v
        max_key = k
print(max_key,":",max_value)

# ----------Create dictionary of squares using range-------------

d = {}

for i in range(1,11):
    d[i] = i*i

print(d)

# ---------- Check if two dictionaries are equal (without ==)------------

d1 = {1:10, 2:20}
d2 = {1:10, 2:20}