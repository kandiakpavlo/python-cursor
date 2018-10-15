from some_module import members


def load(members: dict)->list:

    for x in members:
        x["load"]=x["age"]/2
    for i in members:
        if i["age"] >= 200:
            del i["age"], i["name"], i["load"]

    return members
