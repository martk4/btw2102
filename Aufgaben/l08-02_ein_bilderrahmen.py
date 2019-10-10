sentence = "In just two days, tomorrow will be yesterday"

words = sentence.split(" ")


longest_word = ''
for word in words:
    if len(word) > len(longest_word):
        longest_word = word
length = len(longest_word)

length_rec = length +2
height_rec = len(words)+2



def liner():
    for s in range(length_rec +4):
        print("*", end="")
    print()

liner()
for i in range(len(words)):
    diff_numb= length_rec-len(words[i])
    print("* ",words[i], end= "")
    for spaced in range(diff_numb):
        print(" ", end= "")
    print("*")
liner()
