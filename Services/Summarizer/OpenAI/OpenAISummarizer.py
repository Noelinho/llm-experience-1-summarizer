from openai import OpenAI

from Dtos.Webpage import Webpage
from Services.Summarizer.BadKeyException import BadKeyException


class OpenAISUmmarizer:
    def __init__(self, api_key: str):
        self.checkKey(api_key)

        self.client = OpenAI(api_key=api_key)


    def summarize(self, webpage: Webpage, model: str = "gpt-3.5-turbo", max_tokens: int = 150) -> str:
        response = self.client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": self.generateSystemPrompt()},
                {"role": "user", "content": self.generatePrompt(webpage)}
            ],
            max_tokens=max_tokens
        )
        return response.choices[0].message.content.strip()

    def generateSystemPrompt(self) -> str:
        return "Eres un asistente que analiza el contenido de una página web y retorna un resumen del contenido, ignorando el texto que puede estar relacionado con la navegación. Responde con markdown."

    def generatePrompt(self, webpage: Webpage) -> str:
        user_prompt = f"Estás analizando una página web con el título {webpage.title}"
        user_prompt += "\nEl contenido de la página es el siguiente; \
        por favor, devuélveme un resumen (como mínimo de 100 palabras y máximo 200) con markdown. \
        Si incluye noticias o anuncios, tenlas en cuenta para el resumen.\n\n"
        user_prompt += webpage.content

        return user_prompt

    def checkKey(self, api_key):
        if not api_key:
            raise BadKeyException("No API key was found - please head over to the troubleshooting notebook in this folder to identify & fix!")

        elif not api_key.startswith("sk-proj-"):
            raise BadKeyException("An API key was found, but it doesn't start sk-proj-; please check you're using the right key - see troubleshooting notebook")
        elif api_key.strip() != api_key:
            raise BadKeyException("An API key was found, but it looks like it might have space or tab characters at the start or end - please remove them - see troubleshooting notebook")
