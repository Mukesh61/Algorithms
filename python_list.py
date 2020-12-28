class friend:
    def __init__(self, name, number):
        self.name = name
        self.number = number

list_friend =[]

friend1 = friend("Raj",21)
friend2 = friend("Jai",22)


list_friend.append(friend1)
list_friend.append(friend2)

print(list_friend[1].name)
