###########
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)
###########

thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")  #['apple', 'cherry', 'banana', 'kiwi']
print(thislist)
###########

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)                          
print(thislist)  
#['apple', 'cherry']
###########

thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)  #in this case erase last
###########

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)
###########

thislist = ["apple", "banana", "cherry"]
del thislist  #del all list
###########

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)
###########