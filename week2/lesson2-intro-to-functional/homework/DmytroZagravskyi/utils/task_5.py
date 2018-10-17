def makeStats(p_list: list) -> set:
	sum_of_ages = sum(list(map(lambda p: p['age'], p_list)))
	min_age = min(p_list, key=lambda p: p['age'])
	max_age = max(p_list, key=lambda p: p['age'])
	return (sum_of_ages, min_age, max_age)
	
