def get_max(lister,count=1):# definition with named parameters
    themax= sorted(lister,reverse=True)#sort the list as a new variable
    return themax[0:count] #return right result


print("\n\n\n")
input_list = [2, 3, 10, 22, 23, 41, 9, 7, 3, 0]
assert get_max(input_list) == [41], "Maximum not found."
assert input_list == [2, 3, 10, 22, 23, 41, 9, 7, 3, 0], "List was changed"
assert get_max(input_list, count=5) == [41, 23, 22, 10, 9], "Maximum not found."
assert input_list == [2, 3, 10, 22, 23, 41, 9, 7, 3, 0], "List was changed"
print("Your get_max function works flawlessly. Nice job!")

