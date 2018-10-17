def makeUppercase(s: dict, i: str) -> dict:
	for dic in s: dic[i] = dic[i].upper()
	return s
