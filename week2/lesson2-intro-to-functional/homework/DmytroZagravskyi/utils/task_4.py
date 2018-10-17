def makeFilter(members: dict, f: str) -> dict:
	members = list(filter(lambda d: f in d['name'].lower(), members))
	return members
