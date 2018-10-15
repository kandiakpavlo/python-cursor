from some_module import members
from functools import reduce

members_young = min (members, key = lambda x: x['age'])
members_oldest = max(members, key = lambda x: x['age'])

def sum_min_max(members: list):
    list_1 = []
    for i in members:
        list_1.append(i["age"])
    global sum_age
    sum_age=(reduce(lambda x, y: x+y, list_1))

sum_min_max(members)



