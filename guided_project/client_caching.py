# a client that gets whatever url we specify
# but it will cache the webpage that's returned

import urllib.request
import datetime

class CacheEntry:
    def __init__(self, url, data):
        """[summary]

        Args:
            url ([type]): [description]
            data ([type]): [description]
        """
        self.url = url
        self.data = data
        self.time_fetched = datetime.datetime.now().timestamp()

cache = {}

url = 'https://www.google.com'


TIMEOUT = 10

def get_page(url):

    time_now = datetime.datetime.now().timestamp()
    if url in cache:
        # if less than 10 seconds since out last request
        if time_now - cache[url],
        #webpage = cache[url]
    else:
        print("Going out into the web to get the page.")
        resp = urllib.request.urlopen(url)
        data = resp.read()
        resp.close()

        cache[url] = CacheEntry(data)
    return cache[url]

# page = get_page(url)
# print("GET FROM CACHE")
# page = get_page(url)

# Review
# we are caching, like we want!
# but, assumes page never chanches.
# And cache will get really large.