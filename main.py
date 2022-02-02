import sys

# The first round you manually select "AROSE"
literal = ["A", 0, "G", "I", 0]
contains = ["R"]

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
                # If any literal letter doesn't match we remove. If to prevent breaking on
                # multiple failed letters
                if word[y] != literal[y]:
                    if word in valid:
                        valid.remove(word)

if len(valid) == 0:
    print("Wow, such empty.")
    sys.exit()
else:
    print(str(len(valid)) + " valid after literal check.")

print("Checking for words containing " + str(contains))
validAndContains = valid.copy()

# Contains check
for word in valid:
    for contained in contains:
        if contained not in word:
            validAndContains.remove(word)

print(validAndContains)