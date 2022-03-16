import requests
from bs4 import BeautifulSoup

def get_artists(url):
    ret = []
    r = requests.get(url) # Get the URL
    body = r.content  
    soup = BeautifulSoup(body, features="html.parser") # Create soup
    tracklist = soup.find("table", {"class": "tracklist"}) # Find the tracklist table
    links = tracklist.find_all("a") # Find all links in the tracklist table
    for i in links:  
        ret.append((i.text, i['href'])) # Get all the text and URLs in the list of links and add them to ret
    return ret # ret will be the list of artists
    
def crawl():
    artists = get_artists("https://www.songlyrics.com/a/")
    for name, link in artists:
        print (name, "     :      ", link)

if __name__ == "__main__":
    crawl()




