import urllib2

urls = []

for i in range(1, 18):
	urls.append("http://www.bonappetit.com/sitemap/recipes/page"+str(i))

print urls

for i in range(len(urls)):
	url = urls[i]
	print url
	response = urllib2.urlopen(url)
	html = response.read()
	myfile = "html" + str(i) + ".html"
	myfile = open(myfile, "w")
	myfile.write(html)