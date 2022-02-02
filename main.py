import sys, collections, random

# The first round you manually select "AROSE"
literal = [0, "O", "I", "S", "T"]
contains = []
# Manually entered, like everything.
skips = ["A", "E", "R", "Y", "U", "L", "C", "J", "Z"]

allLetters = []

for l in literal:
    if l != 0:
        # Add the letter to set of all letters
        allLetters.append(l)
        for skip in skips:
            # If the letter matched we don't skip it, it could be there again
            if skip == l:
                skips.remove(l)

print("Kicking off script...")
print("Checking for literal matches for " + str(literal))

# If there are no matches select "UNTIL"
if literal == [0, 0, 0, 0, 0]:
    print("UNTIL")
    # This causes an issue if we use it. The script assumes we use "AROSE" for letter frequency calcs
    sys.exit()

# Initializing valid. This variable will hold all valid answers for literal assignment (full match)
valid = set()

with open("fives2.txt", "r") as fives:
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
            if word[y] in skips:
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
        # This does not ignore fixed letters, yet.
        if contained not in word:
            if word in validAndContains:
                validAndContains.remove(word)

for contain in contains:
    allLetters.append(contain)

# First check if we have any options

if len(validAndContains) == 0:
    print("Wow, such empty.")
    sys.exit()
elif len(validAndContains) == 1:
    print(validAndContains)
else:
    print(str(len(validAndContains)) + " valid after literal check.")

letters = list()

# Getting all the letters that are not literals in all the words to get the top
for word in validAndContains:
    x = range(5)
    for y in x:
        if literal[y] == 0:
            letters.append(word[y])

for skip in skips:
    if skip in letters:
        letters.remove(skip)

letters = collections.Counter(letters).most_common(5 - len(allLetters))

print("We need words with " + str(allLetters))
print("The most common remaining letters are:" + str(letters))

for thing in letters:
    allLetters.append(thing[0])

finalAnswer = []

for word in validAndContains:
    if allLetters[0] in word and allLetters[1] in word and allLetters[2] in word and allLetters[3] in word and \
            allLetters[4] in word:
        finalAnswer.append(word)

if finalAnswer:
    print(random.sample(validAndContains, 1))

else:
    print(finalAnswer)