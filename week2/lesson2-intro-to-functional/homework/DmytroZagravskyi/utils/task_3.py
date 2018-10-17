def makeLoad(members: dict) -> dict:
	for dic in members: dic['load'] = str(format(dic['age']/200*100, '.2f'))
	members = list(filter(lambda d: float(d['load']) < 100, members))
	return members
