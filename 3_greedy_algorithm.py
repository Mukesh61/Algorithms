"""
we will learn greedy algorithm using coin change problem. 
525 = max currency which we can use is 500
25 = max 20
5 = max 5
525 = 500 + 20 + 5
at all the time it will give change with max possible currency like a greedy one. now think about below scenario

available currency = 2, 5 and make change of 8
8 = max currency 5
8-5 = 3 = max 2
3-2 = 1 and we don't have currency of 1 so it's not possible. 

possible solution without greedy will be 2, 2, 2 , 2
"""

def make_change(total_amount: int):
    change_item = []
    currency_nomination = [1, 5, 10, 20, 50, 100, 500]
    currency_nomination.sort(reverse=True)

    for item in currency_nomination:
        while total_amount - item >= 0:
            change_item.append(item)
            total_amount -= item

    print(change_item)

make_change(46)
make_change(16)
make_change(525)
