from some_module import members


sort_age = sorted(members, key= lambda x: x['age'])
members_sort = sorted(sort_age, key = lambda x: len(x['name']))


