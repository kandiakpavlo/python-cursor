def sort_by_name_length(members: list) -> list:
    return sorted(members, key = lambda x: (len (x['name']), x['age']))
