def game(literals=[0, 0, 0, 0, 0], contains=[], skips=[]):
    import sys, collections, random

    if literals[0] != 0 and literals[1] != 0 and literals[2] != 0 and literals[3] != 0 and literals[4] != 0:
        print("I can't believe you actually typed them in. You already won Tickles.")
        sys.exit()

    # If nothing is skipped we must not have played, so it is round 1
    if not skips:
        print("The first round you manually select 'AROSE'")

    # There are skips, but no matches. On to plan B. If this doesn't work, it doesn't have a vowel. Words fucked
    if skips and literals == [0, 0, 0, 0, 0]:
        print("I guess 'AROSE' didn't work :/. Try 'UNTIL'")

    # Variable holding all letters we know are on the board
    all_letters = []

    # Adding literals to all letters
    for literal in literals:
        all_letters.append(literal)

    # Adding contains to all letters
    for contained in contains:
        all_letters.append(contained)

    print("Kicking off script...")

    # Initializing valid. This variable will hold all valid answers for literal assignment (full match)
    valid = set()

    with open("fives2.txt", "r") as fives:
        for val in fives:
            # We add the word to valid, then check if it is invalid. We do this because one failure removes,
            # but all tests have to be successful to add.
            valid.add(val)
            x = range(5)
            for y in x:
                if literals[y] != 0:
                    # If any literal letter doesn't match we remove. "If" statement to prevent breaking on
                    # multiple failed letters
                    if val[y] != literals[y]:
                        if val in valid:
                            valid.remove(val)
                if val[y] in skips:
                    if val in valid:
                        valid.remove(val)

    # This checks we have at least one word that works in our dictionary
    if len(valid) == 0:
        print("Wow, such empty.")
        sys.exit()
    else:
        print(str(len(valid)) + " valid after literal check.")

    print("Checking for words containing " + str(contains))

    # We have to do a shallow copy because we remove elements while iterating
    valid_and_contains = valid.copy()

    # Contains check
    for val in valid:
        for contained in contains:
            # Val needs to be checked without the literals. Literals and contains are separate and they could duplicate
            #
            # TODO
            #
            if contained not in val:
                if val in valid_and_contains:
                    valid_and_contains.remove(val)

    # Re-check we didn't remove everything

    if len(valid_and_contains) == 0:
        print("Wow, such empty.")
        sys.exit()
    elif len(valid_and_contains) == 1:
        print(valid_and_contains)
    else:
        print(str(len(valid_and_contains)) + " valid after literal check.")

    # All letters contained in valid words that we don't already know to be out
    letters = list()

    for val in valid_and_contains:
        x = range(5)
        for y in x:
            if val[y] not in skips:
                letters.append(val[y])

    # Getting the top results in the same variable
    print(letters)
    #
    #
    #   YOU WERE HERE
    #
    #
    letters = collections.Counter(letters).most_common(5 - len(all_letters))

    print("We need words with " + str(all_letters))
    print("The most common remaining letters are:" + str(letters))

    for thing in letters:
        all_letters.append(thing[0])

    finalAnswer = []

    for val in valid_and_contains:
        if all_letters[0] in val and all_letters[1] in val and all_letters[2] in val and all_letters[3] in val and \
                all_letters[4] in val:
            finalAnswer.append(val)

    if finalAnswer:
        print(random.sample(valid_and_contains, 1))

    else:
        print(finalAnswer)
