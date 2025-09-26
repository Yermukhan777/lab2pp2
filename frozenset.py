###########
"""
Python frozenset
frozenset is an immutable version of a set.

Like sets, it contains unique, unordered, unchangeable elements.

Unlike sets, elements cannot be added or removed from a frozenset.
"""

x = frozenset({"apple", "banana", "cherry"})

#display x:
print(x)

#display the data type of x:
print(type(x)) 
 ###########  frozenset({'banana', 'cherry', 'apple'})
###########  <class 'frozenset'>

"""
Frozenset Methods
Being immutable means you cannot add or remove elements. However, frozensets support all non-mutating operations of sets.

Method	Shortcut	Description	Try it
copy()	 	Returns a shallow copy	
difference()	-	Returns a new frozenset with the difference	
intersection()	&	Returns a new frozenset with the intersection	
isdisjoint()	 	Returns whether two frozensets have an intersection	
issubset()	<= / <	Returns True if this frozenset is a (proper) subset of another	
issuperset()	>= / >	Returns True if this frozenset is a (proper) superset of another	
symmetric_difference()	^	Returns a new frozenset with the symmetric differences	
union()	|	Returns a new frozenset containing the union
"""

