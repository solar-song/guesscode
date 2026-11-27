from itertools import permutations, product

# Clue format: (guess, digits_correct, positions_correct)
#   "2"     -> exactly 2
#   "2+"    -> at least 2
#   "2-"    -> at most 2
#   "0-2"   -> between 0 and 2 (inclusive)
#   "?"     -> unknown, not checked

clues1 = [
    ("2071", "2+", "1-3"),
    ("7196", "2+", "1+"),
    ("3254", "2+", "0-1"),
    ("6843", "2-", "1-2"),
]


clues2 = [
    ("3852", "1-3", '1'),
    ("9168", "2+", "1-2"),
    ("5067", "2+", '0'),
    ("6849", "3-", '1'),
    ("3920", "2+", "1+"),
]


clues3 = [
    ("8759", "2", '?'),
    ("6083", "1-", "1"),
    ("8127", "2+", '0'),
    ("8765", "1+", '1'),
    ("2389", "3+", "?"),
]



clues4 = [
    ("9546", "2", '0'),
    ("0498", "2", "0"),
    ("3109", "2", '0'),
    ("8063", "2", '0'),
    ("7329", "2", "0"),
]


clues5 = [
    ("2791", "2", '0'),
    ("0164", "2", "0"),
    ("4205", "2", '0'),
    ("4208", "2", '0'),
    ("3784", "2", "1"),
]

clues6 = [
    ("2738", "2", '0'),
    ("0495", "2", "0"),
    ("7816", "2", '0'),
    ("4280", "2", '1'),
    ("3986", "1", "0"),
]

clues = [
    ("5921", "1", '0'),
    ("3695", "2", "0"),
    ("1793", "1", '0'),
    ("7236", "2", '1'),
    ("2470", "1", "0"),
]


def matches(actual, spec):
    if spec == "?":
        return True
    spec = spec.strip()
    if spec.endswith("+"):                 # "2+" -> at least 2
        return actual >= int(spec[:-1])
    if spec.endswith("-"):                 # "2-" -> at most 2
        return actual <= int(spec[:-1])
    if "-" in spec:                        # "0-2" -> between 0 and 2
        low, high = spec.split("-")
        return int(low) <= actual <= int(high)
    return actual == int(spec)             # "2" -> exactly 2


def count_matches(code, guess):
    # Digits correct: each guessed digit counted up to how often it appears in the code
    digits_correct = sum(min(guess.count(d), code.count(d)) for d in set(guess))
    # Positions correct: exact matches in the same spot
    positions_correct = sum(1 for c, g in zip(code, guess) if c == g)
    return digits_correct, positions_correct


def satisfies(code, guess, digits_spec, positions_spec):
    digits, positions = count_matches(code, guess)
    return matches(digits, digits_spec) and matches(positions, positions_spec)


def solve(allow_repeats=False):
    if allow_repeats:
        candidates = product("0123456789", repeat=4)
    else:
        candidates = permutations("0123456789", 4)

    solutions = []
    for digits in candidates:
        code = "".join(digits)
        if all(satisfies(code, guess, d, p) for guess, d, p in clues):
            solutions.append(code)
    return solutions


if __name__ == "__main__":
    distinct = solve(allow_repeats=False)
    repeats = solve(allow_repeats=True)
    print("clues are:")
    for clue in clues:
        print(clue)
    print("Distinct digits only:", len(distinct), distinct)
    #print("Repeats allowed:     ", len(repeats), repeats)

