import requests

first_call = "http://api.yummly.com/v1/api/recipes?_app_id=b3046620&_app_key=8d80241c736a05dc77df52f886388210&q=peach&allowedAllergy[]=393^Gluten-Free&requirePictures=True"

newcall = ""

def get_json(call):
	resp = requests.get(url=call).json()
	return resp


def large_image(imageurl):
	last_four = imageurl[-4:]
	last_five = imageurl[-5:]
	if last_four == "=s90":
		newimageurl = imageurl[:-4] + '=l180'
	elif last_five == "s.jpg":
		newimageurl = imageurl[:-5] + 'l.jpg'
	elif last_five == "s.png":
		newimageurl = imageurl[:-5] + 'l.png'
	return newimageurl
# def write_recipe(object, my_file):
	

def search_json(json_object):
	match = json_object['matches']
	for i in match:
		print i
		for item in i:
			print item
			# recipe = match[i][item]['id']
			# print recipe
			# new_call = first_call + recipe
			# print newcall
	# new_resp = get_json(new_call)
	# for item in new_resp['matches']:
	# 	print item
	# 	recipeName = item['recipeName']
	# 	ingredients = item['ingredients']
	# 	image = large_image(item['smallImageUrls'][0])
		# print "The recipe %s contains these ingredients: %s; you can see the image here %s." % (recipeName, ingredients, image)
		 
	# new_resp = dict(new_resp)
	# my_file = recipe + ".py"
	# with open(my_file, "w") as new_file:
	# 	new_file.write(new_resp)


def main():
	json_object = get_json(first_call)
	search_json(json_object)

if __name__ == "__main__":
    main()