def game(literals=[0, 0, 0, 0, 0], contains=[], skips=[]):
    global l
    import sys, collections, random
    from bestword import bestword

    # Pre alg checks for corner cases
    #
    if literals[0] != 0 and literals[1] != 0 and literals[2] != 0 and literals[3] != 0 and literals[4] != 0:
        return []

    # If nothing is skipped we must not have played, so it is round 1
    if not skips and literals == [0, 0, 0, 0, 0] and contains == []:
        return []

    # There are skips, but no matches. On to plan B. If this doesn't work, it doesn't have a vowel. Words fucked
    if skips and literals == [0, 0, 0, 0, 0] and not contains:
        return []

    # Pre alg checks done. Now we start the code
    #

    # Initializing variables
    #

    # Variable holding all letters we know are on the board
    all_letters = []
    # This variable will hold all valid answers for literal assignment (full match)
    valids = set()
    # We have to do a shallow copy because we remove elements while iterating
    valid_and_contains = set()

    # Adding literals to all letters
    for l in literals:
        if l != 0:
            all_letters.append(l)

    # Adding contains to all letters
    for contained in contains:
        all_letters.append(contained)

    with open("fives2.txt", "r") as fives:
        for v in fives:
            # We add the word to valid, then check if it is invalid. We do this because one failure removes,
            # but all tests have to be successful to add.
            valids.add(v)
            x = range(5)
            for y in x:
                if literals[y] != 0:
                    # If any literal letter doesn't match we remove. "If" statement to prevent breaking on
                    # multiple failed letters
                    if v[y] != literals[y]:
                        if v in valids:
                            valids.remove(v)
                if v[y] in skips:
                    if v in valids:
                        valids.remove(v)

    # This checks we have at least one word that works in our dictionary
    if len(valids) == 0:
        return []
        sys.exit()

    # Check for solution
    if len(valids) == 1:
        return valids

    # We have to do a shallow copy because we remove elements while iterating
    valid_and_contains = valids.copy()

    # Contains check
    for v in valids:
        v2 = v
        for l in literals:
            if l != 0:
                v2 = v2.replace(l, "",1)

        for contained in contains:
            if contained in v2:
                v2 = v2.replace(contained, "", 1)
            else:
                if v in valid_and_contains:
                    valid_and_contains.remove(v)

    # Re-check we didn't remove everything
    if len(valid_and_contains) == 0:
        return []

    # Check for solution
    if len(valid_and_contains) == 1:
        return valid_and_contains

    # All letters contained in valid words that we don't already know to be out
    letters = list()

    for v in valid_and_contains:
        x = range(5)
        for y in x:
            if v[y] not in skips:
                letters.append(v[y])

    if valid_and_contains:
        return bestword(valid_and_contains)

    else:
        return valid_and_contains