def select_with_o(members: list) -> list:
    return list(filter(lambda x: 'o' in x['name'], members))