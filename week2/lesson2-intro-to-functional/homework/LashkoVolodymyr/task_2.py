from some_module import members

def upp_name(members: list):
    for i in members:
        i['name'] = i['name'].upper()
    return members
