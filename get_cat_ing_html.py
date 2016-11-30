from classify import classify
from flask import  redirect, url_for
from read_ingredients import get_ingredients_model

def getIngredients(filename):
	return '''<div style="float:left; margin-right: 30px;">''' + get_ingredients_model(filename) + '''</div><div style="float:rigth; margin-	right: 10px;">''' +   '''</p></div>
'''

def getCategory(filename):
	return '''<div style="float:left; margin-right: 30px;">''' +classify('static/' +filename) + '''</div><div style="float:rigth; margin-	right: 10px;">''' +   '''</p></div>
'''

