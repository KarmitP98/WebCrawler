from bs4 import BeautifulSoup
import requests

if __name__ == '__main__':
    site = "https://www.amazon.ca/s?k=ssd&ref=nb_sb_noss_1"
    # Request to get contents of the Website
    result = requests.get(site).content
    # Create a soup object
    soup = BeautifulSoup(result, "lxml")

    for path_tag in soup.find_all("img"):
        print(path_tag)

    # Prints the first occurence of div
    # print(soup.div)
    # for div_tag in soup.find_all("div"):
    #     # if div_tag is not None:
    #     attrs = div_tag.attrs
    #     # print(div_tag, "\n", div_tag.attrs, "\n\n")
    #
    #     if "class" in attrs:
    #         print(div_tag["class"])
    # if div_tag.tag["class"] == "cXedhc":
    #     print(div_tag)
