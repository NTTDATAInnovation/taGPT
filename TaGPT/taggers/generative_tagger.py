from tqdm import tqdm
import random
from langchain.prompts import PromptTemplate

from examples import EXAMPLES
from prompts import SYSTEM_PROMPT, INPUT_VARIABLES
from apis import OPENAICaller
from config import DOMAIN, N_EXAMPLES
from processing import _preprocess, _postprocess
from utils import log_pipeline


class GenTagger:
    @staticmethod
    @log_pipeline
    def predict(msg):
        examples = random.sample(
            EXAMPLES[DOMAIN], k=min(N_EXAMPLES, len(EXAMPLES[DOMAIN]))
        )

        template = PromptTemplate(
            input_variables=INPUT_VARIABLES, template=SYSTEM_PROMPT
        )

        prompt = template.format(
            domain=DOMAIN,
            examples=examples,
            material_description=msg[
                "Material description"
            ],  # TODO: Make dynamic
            industry_std_description=msg[
                "Industry Std Desc."
            ],  # TODO: Make dynamic
        )
        response = OPENAICaller.query(prompt)

        return {"tags": response} | msg

    @classmethod
    def preprocess(cls, msg):
        return _preprocess(msg)

    @classmethod
    def postprocess(cls, result):
        return _postprocess(result)

    @classmethod
    def tag_one(cls, msg):
        _msg = cls.preprocess(msg)
        result = cls.predict(_msg)
        return cls.postprocess(result)

    @classmethod
    def tag_many(cls, data):
        return [cls.tag_one(msg) for msg in tqdm(data)]
