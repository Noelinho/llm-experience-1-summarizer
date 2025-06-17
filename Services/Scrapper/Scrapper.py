from bs4 import BeautifulSoup
import requests

from Dtos.Webpage import Webpage

headers = {
 "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
}

irrelevantElements = ["script", "style", "img", "input"]

class Scrapper:
    def __init__(self):
        pass

    def scrape(self, url: str) -> Webpage:
        title = ""
        body = ""

        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        title = soup.title.string if soup.title else "No title found"

        for irrelevant in soup.body(irrelevantElements):
            irrelevant.decompose()

        body = soup.body.get_text(separator="\n", strip=True)

        return Webpage(url=url, title=title, content=body)



