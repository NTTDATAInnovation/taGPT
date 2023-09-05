from config import MODEL, TEMPERATURE, N
from apis.abstract import AbstractAPICaller

from openai import ChatCompletion


class OPENAICaller(AbstractAPICaller):
    @staticmethod
    def run_llm(sentence):
        return (
            ChatCompletion.create(
                model=MODEL,
                messages=[{"role": "user", "content": sentence}],
                temperature=TEMPERATURE,
                n=N,
            )
            .choices[0]
            .message["content"]
            .strip()
        )
