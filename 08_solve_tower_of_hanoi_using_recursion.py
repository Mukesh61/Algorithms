'''
if there is only one disk, then we will move it from source to target. this is base case.

if more than 1, then move n -1 to Auxiliary then from Auxiliary to target. once we moved n-1 to target only 1 is left. so move it from source to target.

'''
def tower_of_hanoi(num, source, target, aux):
    if num == 1:
        print(f"move disk {num} from {source} to {target}")
        return
    else:
        tower_of_hanoi(num-1, source, aux, target)
        print(f"move disk {num} from {source} to {target}")
        tower_of_hanoi(num-1, aux, target, source)


tower_of_hanoi(4, 'A', 'C','B')
