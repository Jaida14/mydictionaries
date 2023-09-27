person = {}
person["fname"] = "Joe"
person["lname"] = "Fonebone"
person["age"] = 51
person["spouse"] = "Edna"
# what kind of object is this? a list object
person["children"] = ["Ralph", "Betty", "Joey"]
# what kind of object is this? a list object, but you gave a dictionary to the list
person["pets"] = {"dog": "Fido", "cat": "Sox"}

# you can have a list within a dictionary and all kinds of combos (complex)

print(person)

# print out the name of the second child
# person is the dictionary, but with children, it's a list
children = person["children"]
print(person["children"][1])  # keep going within, without setting new variable
print(children[1])  # another way, but must set a new variable first
print(type(children))

# print out the name of the cat
pets = person["pets"]
print(type(pets))
print(pets["cat"])
print(person["pets"]["cat"])

# 9/14 jueves
# use a loop to print out the names of each child
for child in person['children']:  # person is the dict, children is the key
    print(child)

# use a loop to print out the pets in the following format:
# The type of pet is: dog and the name of the pet is: Fido
# for key and value in the dictionary of the whole thing
for k, v in person["pets"].items():
    print(f"The type of pet is: {k} and the name of the pet is: {v}.")
