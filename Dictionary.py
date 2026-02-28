# Count in dictionary --------------

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

# ------- Merge two dictionaries ---------

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

# ---------- Create dictionary of multiply squares using range -------------

d = {}

for i in range(1,11):
    d[i] = i*i

print(d)

# ---------- Extract all values of a key from list of dictionaries ------------
# age's values --

arr = [
    {"name":"Ram","age":25},
    {"name":"Sam","age":30},
    {"name":"Tom","age":35}
]

ages = []

for i in range(len(arr)):
    d = arr[i]
    ages += [d["age"]]

print(ages)

# ------- Find key whose value is "Lucknow" -------

d = [
    {"a":10, "b":20, "c":30},
    {"name":"pradeep", "address":"Lucknow", "subject":"python"}
]

target = "Lucknow"

for i in range(len(d)):
    current_dict = d[i]
    for key in current_dict:
        if current_dict[key] == target:
            print(key)

# Find the dictionary where "name" == "Ram" ----------

arr = [
    {"name":"Ram", "age":25},
    {"name":"Shyam", "age":30}
]

target = "Ram"

for i in range(len(arr)):
    d = arr[i]
    if d["name"] == target:
        print(d)