import urllib

def get_urls():
	with open("newrecipelinks.txt", "r") as myfile:
		suffix = 1
		for aline in myfile:
			print aline, "line"
			recipe_url = aline.strip()
			print recipe_url, ", in get_urls loop"
			recipe_name = "vegetarianrecipelist" + str(suffix)
			suffix +=1
			get_html(recipe_url, recipe_name)
				
def get_html(recipe_url, recipe_name):
	print recipe_url, ", in the get_html function"
	response = urllib.urlopen(recipe_url)
	html = response.read()
		# myfile = (value).encode('utf-8')
	myfile = (recipe_name + ".html").encode('utf-8')
	print myfile
	write_html(html, myfile)

def write_html(html, myfile):
	with open(myfile, "w") as newfile: 
		newfile.write(html)			


def main():
	get_urls()



if __name__ == "__main__":
    main()



