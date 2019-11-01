import math

def safe_sqrt(x):

    try:
        x = int(x) 
        try:
            x > -1
            return int(math.sqrt(x))
        except:
            return 1
    except:
        return 0

assert safe_sqrt(-1) == 1, "-1 should lead to 1"
assert safe_sqrt('a') == 0, "Character should lead to 0"
assert safe_sqrt(None) == 0, "None should lead to 0"
assert safe_sqrt(49.0) == 7, "float should lead to 7"
assert sum([safe_sqrt(a) for a in ['a', 36, None, 1, -5, 25.0, False]]) == 13, "safe_sqrt is not working"
print("Your safe_sqrt is working just fine.")
