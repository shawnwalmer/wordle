import sys

# The first round you manually select "AROSE"
literal = ["A", 0, "G", "I", 0]
contains = []

print("Kicking off script...")
print("Checking for literal matches for " + str(literal))

# If there are no matches select "UNTIL"
if literal == [0, 0, 0, 0, 0]:
    print("UNTIL")
    sys.exit()

# Initializing valid. This variable will hold all valid answers for literal assignment (full match)
valid = set()

with open("fives.txt", "r") as fives:
    for word in fives:
        valid.add(word)
        x = range(5)
        for y in x:
            if literal[y] != 0:
                if word[y] != literal[y]:
                    if word in valid:
                        valid.remove(word)

if len(valid) == 0:
    print("Wow, such empty.")
    sys.exit()
else:
    print(str(len(valid)) + " valid after literal check.")

