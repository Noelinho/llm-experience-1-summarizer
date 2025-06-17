import os
from dotenv import load_dotenv

from IPython.display import Markdown, display

from Services.Scrapper.Scrapper import Scrapper

load_dotenv(override=True)
api_key = os.getenv('OPENAI_API_KEY')

scrapper = Scrapper()
webpage = scrapper.scrape("https://www.emagister.com/grado-comunicacion-digital-periodismo-cursos-3805765.htm")

print(webpage.title)
print(webpage.content)