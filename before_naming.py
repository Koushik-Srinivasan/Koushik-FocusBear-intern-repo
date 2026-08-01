# Poorly named variables/functions example (before refactor) - issue #42

def calc(d, x):
    r = []
    for i in d:
        if i["t"] > x:
            n = i["u"].strip().title()
            v = i["t"] - x
            r.append((n, v))
    return r

data = [
    {"u": "  koushik  ", "t": 90},
    {"u": "priya", "t": 45},
    {"u": "sam", "t": 120},
]

print(calc(data, 60))
