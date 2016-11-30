import random, os

def getImage(folder):
	path = "static/UECFOOD100/" + folder
	random_filename = random.choice([
    	x for x in os.listdir(path)
    	if os.path.isfile(os.path.join(path, x))
	])
	return random_filename

