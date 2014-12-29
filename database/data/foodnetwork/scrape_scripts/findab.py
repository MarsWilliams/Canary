import requests


def get_urls_ab():
    open_file = open('alton-brown.txt', 'w')
    for i in xrange(1,19):
        name = 'http://www.foodnetwork.com/chefs/alton-brown/recipes.mostpopular.page-'+str(i)+'.html'
        r = requests.get(name)
        open_file.write(r.text+"\n")


def main():
        get_urls_ab()

if __name__=="__main__":
    main()

