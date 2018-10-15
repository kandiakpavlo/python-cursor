from functools import reduce


def sum_youngest_oldest(members: list):
    age_sum = reduce(lambda x, y: x + y, [x['age'] for x in members])
    youngest = min(members, key = lambda x: x['age'])
    oldest = max(members, key = lambda x: x['age'])
    return age_sum, youngest, oldest