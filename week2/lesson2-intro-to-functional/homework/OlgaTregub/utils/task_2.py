def transform_uppercase_names(members: list) -> list:
    return list({'age':m['age'], 'name':m['name'].upper()} for m in members)




