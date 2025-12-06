s = "my name is pradeep"

word = ""
res = ""

for ch in s:
    if ch != " ":
        word = ch + word      # reverse logic
    else:
        res += word + " "     # add reversed word
        word = ""             # reset for next word

res += word                   # last word add
print(res)