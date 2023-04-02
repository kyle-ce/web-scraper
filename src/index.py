import asyncio
import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import os

# pretty print
from pprint import pprint

from fetch import fetch_all_requests

cwd = os.getcwd()
url1 = "http://manuals.gogenielift.com/Parts%20And%20Service%20Manuals/1MainPMIndex.htm"


# split text creates a tuple of the whole path and the extension
url_index, ext = os.path.splitext(os.path.basename(os.path.normpath(url1)))
parent_directory = f"{cwd}/{url_index}"
print(parent_directory)


soup = BeautifulSoup(requests.get(url1).text, "html.parser")
# find all links (a tags) and extract their URLs
ul = soup.find("ul", {"data-role": "listview"})
print(ul)
links = [urljoin(url1, link.get("href")) for link in ul.find_all("a")]
# print((soup.prettify()))
pprint(links)


hrefs = asyncio.run(fetch_all_requests(links))
soups = [BeautifulSoup(href, "html.parser") for href in hrefs]
for soup in soups:
    print(soup.prettify())
