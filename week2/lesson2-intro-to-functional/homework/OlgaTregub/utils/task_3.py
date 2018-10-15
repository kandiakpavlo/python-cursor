def add_age_load(members: list) -> list:
	for m in members:
		m['load'] = m['age']*100/200
	return list(filter((lambda x: x['load'] < 100), members))