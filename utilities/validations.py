from enums import general_enums


def is_empty(item):
	return item in general_enums.empties


def not_empty(item):
	return not is_empty(item)


def is_empty_or_false(item):
	return item in general_enums.empties + ['false', False]


def not_empty_or_false(item):
	return not is_empty_or_false(item)