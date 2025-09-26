###########
mytuple = ("apple", "banana", "cherry")
###########  A tuple is a collection which is ordered and unchangeable.

thistuple = ("apple", "banana", "cherry")
print(thistuple)
###########

thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)
########### okay with dubli

thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

## 3

thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))
###########       <class 'tuple'> comma is power
###########       <class 'str'>

tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)
###########
tuple1 = ("abc", 34, True, 40, "male")

###########
mytuple = ("apple", "banana", "cherry")
print(type(mytuple))
###########  <class 'tuple'>

thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)  
########### tuple in tuple
