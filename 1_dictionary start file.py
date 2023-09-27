import random

phonebook = {'Chris': '555−1111',
             'Katie': '555−2222',
             'Joanne': '555−3333'}


print()
print('*****  start section 1 - print dictionary ********')
print()

print(phonebook)
print(len(phonebook))

mydictionary = {}  # to create a dictionary step 1/2
print(mydictionary)  # step 2/2

mydictionary = dict(m=8, n=9)  # another way to create a dictionary 1/2
print(mydictionary)  # 2/2
# key is m and n and its values are 8 and 9 respectively

# casing of the letters matter; KeyError if not done correctly
phone = phonebook['Chris']
print(phone)


print()
print('*****  end section 1 ********')
print()


print()
print('*****  start section 2 - search dictionary ********')
print()

name = 'Chris'

if name in phonebook:  # looks through all the keys by default
    print(f"{name} has the phone number: {phonebook[name]}")
else:
    print(f"{name} not found")


print()
print('*****  end section 2 ********')
print()


print()
print('*****  start section 3 - edit/append dictionary ********')
print()

print(phonebook)
phonebook['Joe'] = '555-0123'
phonebook['Chris'] = '555-4444'
print(phonebook)


print()
print('*****  end section 3 ********')
print()


print()
print('*****  start section 4 - delete/remove from dictionary ********')
print()

del phonebook['Joe']
print(phonebook)

print()
print('*****  end section 4 ********')
print()


print()
print('*****  start section 5 - iterate through keys, values, items ********')
print()

for k in phonebook:  # first method
    print(f"the key is {k} and the value is {phonebook[k]}")


for v in phonebook.values():  # 2nd method
    print(v)

for phone_tuple in phonebook.items():  # 3rd method tuple iterator
    print(phone_tuple)  # gets both the key and value together as a tuple

for k, v in phonebook.items():  # 3rd method tuple iterator, but separates the key and value
    print(f"the key is {k} and the value is {v}")


print()
print('*****  end section 5 ********')
print()


print()
print('*****  start section 6 - using get and clear ********')
print()

phone = phonebook.get('Jack', '911')  # method 1
print(phone)

phonebook.clear()  # method 2
print(phonebook)  # clears out dictionary; makes it empty


print()
print('*****  end section 6 ********')
print()


print()
print('*****  start section 7 - using pop method ********')
print()

phonebook = {'Chris': '555−1111',
             'Katie': '555−2222',
             'Joanne': '555−3333'}
# allows deletion of a variable, but it is saved under a new variable; dictionary shrinks
print(phonebook)
phone = phonebook.pop('Katie')
print(phone)
print(phonebook)


print()
print('*****  end section 7 ********')
print()


print()
print('*****  start section 8 - using popitem ********')
print()

phone = phonebook.popitem()
print(phone)
print(phonebook)
# it's supposed to be random, but it's picking off the last one


print()
print('*****  end section 8 ********')
print()


print()
print('*****  start section 9 - using random and converting to list ********')
print()

list_of_keys = list(phonebook)
print(list_of_keys)
random_key = random.choice(list_of_keys)
print(random_key)
print(phonebook[random_key])

# condensing the previous lines of code without using variables
print(phonebook[random.choice(list(phonebook))])


print()
print('*****  end section 9 ********')
print()
