###########
myset = {"apple", "banana", "cherry"}
###########

thisset = {"apple", "banana", "cherry"}
print(thisset)
###########

thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)
###########  dubli is ignored 

thisset = {"apple", "banana", "cherry", True, 1, 2}

print(thisset)
########### true=1 false=0 {True, 2, 'banana', 'cherry', 'apple'}

thisset = {"apple", "banana", "cherry"}

print(len(thisset))
###########

set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}
###########

set1 = {"abc", 34, True, 40, "male"}
###########

myset = {"apple", "banana", "cherry"}
print(type(myset))
########### <class 'set'>

thisset = set(("apple", "banana", "cherry")) # note the double round-brackets set in set
print(thisset) 

