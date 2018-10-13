def add_age_load(members: list) -> list:
    members = list({'age':m['age'], 'name':m['name'], 'load':m['age']*100/200} for m in members)
    return list(filter(lambda x: x['load'] < 100, members))