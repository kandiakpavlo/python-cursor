def transform_uppercase_names(members: list) -> list:
	for m in members:
		m['name'] = m['name'].upper()
	return members




