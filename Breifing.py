from bs4 import BeautifulSoup
import requests

if __name__ == '__main__':
    site = "https://www.whitehouse.gov/briefings-statements/"
    # Request to get contents of the Website
    result = requests.get(site)
    # Store the content in a variable
    src = result.content
    # Create a soup object
    soup = BeautifulSoup(src, "lxml")

    # Find all the content with H2 TAG
    urls = []
    for h2_tag in soup.find_all("h2"):
        # Find a TAG inside the h2_tag
        # Return 1st instance of a TAG inside H2_TAG
        a_tag = h2_tag.find("a")
        # Get value inside href attribute in a TAG
        if a_tag is not None:
            urls.append(a_tag.text + " : " + a_tag.attrs["href"])

    print(urls)
