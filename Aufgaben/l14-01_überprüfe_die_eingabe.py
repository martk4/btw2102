print("\n\n")

weekdays = ["monday","tuesday","wednesday","thursday","friday"]


def validate_weekday(x):
    
    
    if type(x)== str:
        y = x.lower()
        if y in weekdays:
            return y.capitalize()
        elif y not in weekdays:
            return None
    
    else:
        raise TypeError

    

#print(validate_weekday("Sunday"))

def assertRaises(ex_type, arg, msg):
    try:
        validate_weekday(arg)
    except Exception as e:
        if type(e) is ex_type:
            return True
    print(msg)
    return False

assert validate_weekday('Monday') == 'Monday', 'Monday should be the result'
assert validate_weekday('tuesday') == 'Tuesday', 'Tuesday should be the result'
assert validate_weekday('WEDNESDAY') == 'Wednesday', 'Wednesday should be the result'
assert validate_weekday('ThUrSdAy') == 'Thursday', 'Thursday should be the result'
assert validate_weekday('friday') == 'Friday', 'Friday should be the result'
assert validate_weekday('Sunday') is None, 'Sunday is not a weekday'
assert validate_weekday('saturday') is None, "Saturday is not a weekday"
assert validate_weekday('') is None, "invalid string is not a weekday"
assert validate_weekday('something') is None, "invalid string is not a weekday"
import sys
assertRaises(TypeError, 1, "Int should lead to TypeError") or sys.exit(-1)
assertRaises(TypeError, 5.3, "Float should lead to TypeError") or sys.exit(-1)
assertRaises(TypeError, None, "None should lead to TypeError") or sys.exit(-1)
assertRaises(TypeError, ['a'], "list should lead to TypeError") or sys.exit(-1)

print("You'r validation of weekday's works flawlessly.")