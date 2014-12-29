import simplejson

def main():
	myfile = open("Jordanas-Baked-Spaghetti-Squash-with-Tomato-and-Ricotta-571720.json").read()
	write_pretty(myfile)

def write_pretty(myfile):
	with open("prettyjson.txt", "w") as newfile: 
		newfile.write(simplejson.dumps(simplejson.loads(myfile), indent=4, sort_keys=True))

if __name__ == "__main__":
	main()