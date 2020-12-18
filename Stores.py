import json
from urllib.request import urlopen

import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    site = "https://smart-shoppers-2a1ab.firebaseapp.com/MjEotbIqUxReSqfvMjJSY2jirps1/customer/Mxuej6VKhOAbrld9pury"
    # Request to get contents of the Website
    result = requests.get(site).content
    # Create a soup object
    soup = BeautifulSoup(result, "lxml")

    page = urlopen(site).read()
    print(page)
    data = json.loads(page)
    print(data)

    # print(soup)
