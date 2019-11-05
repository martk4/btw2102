sent = "yeah dude!"

def border_around_text(sentence,symbol = '+',padding = 1):
    #SETUP#
    words = sentence.split(" ")
    longest_word = ''
    for i in words:
        if len(i)>len(longest_word):
            longest_word=i
    len_long_word = len(longest_word)
    total_space = 2+(2*padding)+len(longest_word)
    #LINER#
    liner = ""
    for a in range(total_space):
        liner += symbol
    #STARTSPACER
    spaces_start= ""
    for b in range(padding):
        spaces_start += " "
    #ENDSPACER
    spaces_end= []
    difference = []
    for c in range(len(words)):
        diff = len(longest_word)-len(words[c])
        difference.append(diff)
    #DIFFERENCE READ FOR SPACER LIST 
    for d in range(len(difference)):
        space_temp = ""
        for f in range(difference[d]+padding):
            space_temp += " "
        spaces_end.append(space_temp)
    #REARRANGE
    final_words=[]
    for g in range(len(words)):
        combine = "".join(words[g]+spaces_end[g])
        final_words.append(combine)
    #PRINTING#
    s = symbol+"\n"+symbol+spaces_start
    final= liner+ "\n"+symbol+spaces_start+s.join(final_words)+symbol+"\n"+liner
    return final

print(border_around_text(sent,symbol= "*", padding=6))