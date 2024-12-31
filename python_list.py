"""
We will create a class called Friend with name and number attribute then added friends objects to list.
"""
class Friend:
    def __init__(self, name, number):
        self._name = name
        self._number = number

friend_list =[]

friend1 = Friend("Raj Kumar", 21)
friend2 = Friend("Jai Kumar", 22)


friend_list.append(friend1)
friend_list.append(friend2)

print(list_friend[1].name)
