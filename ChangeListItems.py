thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)
###########

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]  #
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)
###########

thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]  #['apple', 'blackcurrant', 'watermelon', 'cherry']
print(thislist)
###########

thislist = ["apple", "banana", "cherry"]    #['apple', 'watermelon']
thislist[1:3] = ["watermelon"]
print(thislist)
###########

thislist = ["apple", "banana", "cherry"]

thislist.insert(2, "watermelon")

print(thislist)      #['apple', 'banana', 'watermelon', 'cherry']
###########

