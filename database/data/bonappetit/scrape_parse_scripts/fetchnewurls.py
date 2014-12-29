from BeautifulSoup import BeautifulSoup
import urllib

files = ['recipes1.html', 'recipes2.html', 'recipes3.html', 'recipes4.html',  'recipes5.html', 'recipes6.html', 'recipes7.html', 'recipes8.html', 'recipes9.html', 'recipes10.html', 'recipes11.html', 'recipes12.html', 'recipes13.html', 'recipes14.html', 'recipes15.html', 'recipes16.html']

recipe_urls = {}


def make_Soup(myfile):
	html = open(myfile).read()
	soup = BeautifulSoup(html)
	return soup

def get_urls(soup):
	recipe_item = soup.findAll('a')
	counter = 1
	for item in recipe_item:
		recipe_name = "recipecorpus" + str(counter)
		counter +=1
		print recipe_name
		hrefs = item.get('href').split(',')
		for link in hrefs:
			if "http://www.bonappetit.com/recipe/" in link:
				recipe_urls[recipe_name] = link
	get_html(recipe_urls)	
			
def get_html(recipe_urls):
	print recipe_urls
	for key, value in recipe_urls.iteritems():
		url = value
		response = urllib.urlopen(url)
		html = response.read()
		# myfile = (value).encode('utf-8')
		myfile = (key + ".html").encode('utf-8')
		write_html(html, myfile)

def write_html(html, myfile):
	with open(myfile, "w") as newfile: 
		newfile.write(html)

def main():
	for myfile in files:
		soup = make_Soup(myfile)
		get_urls(soup)



if __name__ == "__main__":
    main()



