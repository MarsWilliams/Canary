import json
with open('/Users/marswilliams/src/canary/elasticsearch/elasticresult.py') as myfile:
	results = json.loads(myfile.read())
	hits = results['hits']['hits']
	recipes = []
	for i in range(len(hits)):
		recipe = {}
		hit = hits[i]['_source']
		recipe['name'] = hit['name']
		ingredients = hit['ingredients']
		ingredientList = []
		for item in ingredients:
			print ingredients[item].keys()
			ingredient = {}
			print ingredients[item]['gluten']
			print ingredients[item]['quantity']
			print ingredients[item]['unit']
	
			ingredient['name'] = item
			ingredient['gluten'] = ingredients[item]['gluten']
			ingredient['quantity'] = ingredients[item]['quantity']
			ingredient['unit'] = ingredients[item]['unit']
			# if 'flour_ratio' in ingredient[item].keys():
				# print ingredient[item]['flour_ratio']
	
			
			ingredientList.append(ingredient)

