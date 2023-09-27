some_text = open("sometext.txt", "r")  # probably cant use .split() for text

# shoudl display in terminal, not write to new folder
some_list = some_text.readline().rstrip('\n').split()

# print(some_list)  # now forever a list

# now need to count
count = 0
some_dictionary = {}
for word in some_list:
    if word not in some_dictionary:
        some_dictionary[word] = 1  # make dictionary here! it works
    else:
        some_dictionary[word] += 1


print(f"{some_dictionary}\n")

'''
# method 2
other_dictionary = {}
for word in some_list:
    other_dictionary[word] = 0

for word in some_list:
    if word in other_dictionary:
        other_dictionary[word] += 1

print(f"Comapring dictionary: {other_dictionary}\n ")

if some_dictionary == other_dictionary:
    print(f"Both dictionaries match! Either is correct")
else:
    print(f"One of them is wrong.")
 '''

some_text.close()
