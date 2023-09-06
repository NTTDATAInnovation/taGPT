from config import MODEL, TEMPERATURE, N
from apis.abstract import AbstractAPICaller

from openai import ChatCompletion


class OPENAICaller(AbstractAPICaller):
    @staticmethod
    def query(msg):
        return (
            ChatCompletion.create(
                model=MODEL,
                messages=[{"role": "user", "content": msg}],
                temperature=TEMPERATURE,
                n=N,
            )
            .choices[0]
            .message["content"]
            .strip()
        )
