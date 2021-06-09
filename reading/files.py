def get_dfxs(names_path):
	f = open(names_path, 'r')
	dfxs_names = f.read().split('\n')
	return dfxs_names

