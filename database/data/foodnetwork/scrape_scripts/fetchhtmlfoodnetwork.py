from BeautifulSoup import BeautifulSoup
import urllib

files = []

recipe_urls = {}


def make_Soup(my_file):
	html = open(my_file).read()
	soup = BeautifulSoup(html)
	return soup

def get_urls(soup):
	print "I'm here"
	for each_div in soup.findAll('article', {'class':'recipe'}):
		for each in soup.findAll('div', {'class':"pull-right "}):
			for each in soup.findAll('h6'):
				recipe_item = soup.findAll('a')
				for item in recipe_item:
					recipe_name = item.text
					hrefs = item.get('href').split(',')
					for link in hrefs:
						if "/recipes/" in link:
								recipe_urls[recipe_name] = "http://www.foodnetwork.com/" + link
	get_html(recipe_urls)	
			
def get_html(recipe_urls):
	for key, value in recipe_urls.iteritems():
		url = value
		response = urllib.urlopen(url)
		html = response.read()
		# myfile = (value).encode('utf-8')
		myfile = (key + ".html").encode('utf-8')
		if myfile != ".html":
			print myfile
			write_html(html, myfile)

def write_html(html, myfile):
	with open(myfile, "w") as newfile: 
		newfile.write(html)

def make_list():
	for i in range(2,5):
		files.append("vegetarianrecipelist" + str(i) + ".html")
	
def main():
	make_list()
	for i in range(len(files)):
		my_file = files[i]
		soup = make_Soup(my_file)
		get_urls(soup)



if __name__ == "__main__":
    main()



