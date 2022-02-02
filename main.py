import sys
# The first round you manually select "AROSE"
game = ["A", 0, 0, 0, 0]

# If there are no matches select "UNTIL"
if game == [0, 0, 0, 0, 0]:
    print("UNTIL")
    sys.exit()

with open("fives.txt", "r") as fives:
    for word in fives:
        x = range(5)
        for y in x:
            if game[y] != 0:
                if word[y] != game[y]:
