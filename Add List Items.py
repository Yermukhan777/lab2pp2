###########
thislist = ["apple", "banana", "cherry"]  #['apple', 'banana', 'cherry', 'orange']
thislist.append("orange")
print(thislist)
###########

thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)
###########

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]  #['apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya']

thislist.extend(tropical)

print(thislist)
###########

thislist = ["apple", "banana", "cherry"]  #['apple', 'banana', 'cherry', 'kiwi', 'orange']
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)
###########

