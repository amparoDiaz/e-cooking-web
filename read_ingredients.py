def get_ingredients_from_model():
	return ['salt', 'oil', 'pepper', 'oliv']

def get_ingredients_model(filename):
	result='''<H1>Ingredientes</H1> <table style="border: 1px;"> <tr>'''
	ingredients=get_ingredients_from_model()
	for ingredient in ingredients:
		result= result + "<tr><td> "+ ingredient + '</td></tr>'
	return result + '</table><frameset cols="25%,50%"><frame src="frame_a.htm"></frameset> '

from keras.models import load_model


