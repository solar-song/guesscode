``` Clue format: (guess, digits_correct, positions_correct)
   "2"     -> exactly 2
   "2+"    -> at least 2
   "2-"    -> at most 2
   "0-2"   -> between 0 and 2 (inclusive)
   "?"     -> unknown, not checked
```

edit your puzzle conditions in the file like this:
```
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



clues = [
    ("9546", "2", '0'),
    ("0498", "2", "0"),
    ("3109", "2", '0'),
    ("8063", "2", '0'),
    ("7329", "2", "0"),
]
```

**how to run:**
in the script folder:
```
python3 -m venv .venv
source .venv/bin/activate
python3 puz3.py
```
