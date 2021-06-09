def process(tag):
	
	cols = ['type','ord','dorms','area']
	attrs = tag.split('-')
	
	for i in range(len(attrs)):
		print(cols[i],attrs[i])
	print("------------------")
