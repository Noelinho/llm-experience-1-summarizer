from openai import OpenAI

from Services.Summarizer.BadKeyException import BadKeyException


class OpenAISUmmarizer:
    def __init__(self, api_key: str):
        self.checkKey(api_key)

        self.client = OpenAI(api_key=api_key)


    def summarize(self, text: str, model: str = "gpt-3.5-turbo", max_tokens: int = 150) -> str:
        response = self.client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are a helpful assistant that summarizes text."},
                {"role": "user", "content": text}
            ],
            max_tokens=max_tokens
        )
        return response.choices[0].message['content'].strip()


    def checkKey(self, api_key):
        if not api_key:
            raise BadKeyException("No API key was found - please head over to the troubleshooting notebook in this folder to identify & fix!")

        elif not api_key.startswith("sk-proj-"):
            raise BadKeyException("An API key was found, but it doesn't start sk-proj-; please check you're using the right key - see troubleshooting notebook")
        elif api_key.strip() != api_key:
            raise BadKeyException("An API key was found, but it looks like it might have space or tab characters at the start or end - please remove them - see troubleshooting notebook")
