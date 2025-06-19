import os
from dotenv import load_dotenv
import sys
from Services.Summarizer.OpenAI.OpenAISummarizer import OpenAISUmmarizer

from Services.Scrapper.Scrapper import Scrapper

load_dotenv(override=True)
api_key = os.getenv('OPENAI_API_KEY')

if len(sys.argv) < 2:
    print("Por favor, proporciona una URL como argumento.")
    sys.exit(1)

url = sys.argv[1]

scrapper = Scrapper()
webpage = scrapper.scrape(url)

sumarizer = OpenAISUmmarizer(api_key)
summary = sumarizer.summarize(webpage)

print(summary)