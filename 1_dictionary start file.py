'''
import random

phonebook = {'Chris':'555−1111',
             'Katie':'555−2222',
             'Joanne':'555−3333'}



print()
print('*****  start section 1 - print dictionary ********')
print()

print(phonebook)

print(len(phonebook))

mydict = {}
print(mydict)

mydict = dict(m=8, n=9)
print(mydict)

print(type(phonebook))



print()
print('*****  end section 1 ********')
print()


'''


print()
print('*****  start section 2 - search dictionary ********')
print()







print()
print('*****  end section 2 ********')
print()







print()
print('*****  start section 3 - edit/append dictionary ********')
print()





print()
print('*****  end section 3 ********')
print()






print()
print('*****  start section 4 - delete/remove from dictionary ********')
print()




print()
print('*****  end section 4 ********')
print()



'''


print()
print('*****  start section 5 - iterate through keys, values, items ********')
print()



for k in phonebook:
    print(f"The name is {k} and the phone number is {phonebook[k]}")

for value in phonebook.values():
    print(f"The phone number is {value}")

for item in phonebook.items():


print()
print('*****  end section 5 ********')
print()





print()
print('*****  start section 6 - using get and clear ********')
print()






print()
print('*****  end section 6 ********')
print()



print()
print('*****  start section 7 - using pop method ********')
print()






print()
print('*****  end section 7 ********')
print()



print()
print('*****  start section 8 - using popitem ********')
print()


a = phonebook.popitem()
print(a)
print(phonebook)



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
phone = phonebook[random_key]
print(phone)

print()
print('*****  end section 9 ********')
print()


'''





