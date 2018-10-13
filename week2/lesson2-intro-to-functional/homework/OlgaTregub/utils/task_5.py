from functools import reduce


def sum_youngest_oldest(members: list):
    age_sum = reduce(lambda x, y: x + y, [m['age'] for m in members])
    youngest = reduce(lambda x, y: x if x['age'] < y['age'] else y, members)
    oldest = reduce(lambda x, y: x if x['age'] > y['age'] else y, members)
    return age_sum, youngest, oldest
