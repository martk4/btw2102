def upper_and_lower_count(x):
    upper = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','Ä','Ö','Ü']
    sonder = "abcdefghijklmnopqrstuvwxyzäöü"
    count_u = 0
    count_l = 0
    for i in x:
       if i in upper:
           count_u += 1
       if i in sonder:
        count_l += 1
    return (count_u,count_l)





tests = [
    'Wo sich die Füchse gute Nacht sagen.',
    'Äpfel mit Birnen vergleichen.',
    'Wer reitet so spät durch Nacht und Wind?',
    'Die Welt ist nicht gross genug für uns Beide.'
]
assert upper_and_lower_count(tests[0]) == (3, 26)
assert upper_and_lower_count(tests[1]) == (2, 23)
assert upper_and_lower_count(tests[2]) == (3, 29)
assert upper_and_lower_count(tests[3]) == (3, 33)
print("Your function works flawlessly!")