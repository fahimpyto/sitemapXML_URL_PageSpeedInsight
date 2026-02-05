import requests
from bs4 import BeautifulSoup as bs
import json

url = "https://huntsvilleresidentialfencing.com/sitemap_index.xml"
output = "site_url.json"

res = requests.get(url)
soup = bs(res.text, "xml")

index_urls = [loc.text for loc in soup.find_all("loc")]
all_data = {}

for index_url in index_urls:
    resp = requests.get(index_url)
    soup_url = bs(resp.text, "xml")

    urls = []
    for url_tag in soup_url.find_all("url"):
        loc = url_tag.find("loc")
        if loc:
            urls.append(loc.text)

    sitemap_name = index_url.split("/")[-1]
    all_data[sitemap_name] = urls

with open(output, 'w', encoding="utf-8") as f:
    json.dump(all_data, f, indent=4, ensure_ascii=False)

print("work Done!")
