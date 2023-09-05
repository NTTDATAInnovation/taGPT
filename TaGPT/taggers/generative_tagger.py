from tqdm import tqdm
import random
from langchain.prompts import PromptTemplate

from examples import EXAMPLES
from prompts import SYSTEM_PROMPT, INPUT_VARIABLES
from apis.api_openai import OPENAICaller
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
        response = OPENAICaller.run_llm(prompt)

        return {"tags": response} | msg

    @classmethod
    def tag_many(cls, data):
        return [cls.tag_one(msg) for msg in tqdm(data)]

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


# def generative_tagger(data_path, tag_path, api_key):


#     final_res = []
#     for ind, row in enumerate(tqdm.tqdm(df_exp.iterrows())):
#         data = row[1].to_dict()
#         example = examples[random.randint(0, 4)]
#         text = prompt.format(preference=preference, caption=data['caption'],
#                              category_name=data['category_name'], ocr=data['ocr'],
#                              asr=data['asr'], example=example)

#         try:
#             completion = openai.ChatCompletion.create(
#                 model="gpt-3.5-turbo",
#                 messages=[{"role": "user", "content": text}],
#                 temperature=1.5,
#                 n=5
#             )

#             res = []
#             for j in range(5):
#                 ans = completion.choices[j].message["content"].strip()
#                 ans = ans.replace("\n", "")
#                 ans = ans.replace("。", "")
#                 ans = ans.replace("，", "、")
#                 res += ans.split('、')

#             tag_count = Counter(res)
#             tag_count = sorted(tag_count.items(), key=lambda x: x[1], reverse=True)

#             candidate_tags = [_[0] for _ in tag_count]
#             candidate_tags_embed = encoder.encode(candidate_tags)
#             candidate_tags_dis = [np.sqrt(np.dot(_, _.T)) for _ in candidate_tags_embed]

#             scores = np.dot(candidate_tags_embed, tags_embed.T)

#             ans = []
#             for i in range(scores.shape[0]):
#                 for j in range(scores.shape[1]):
#                     score = scores[i][j] / (candidate_tags_dis[i] * tags_dis[j])
#                     if score > 0.9:
#                         ans.append(tags[j])

#             ans = Counter(ans)
#             ans = sorted(ans.items(), key=lambda x: x[1], reverse=True)

#             final_res.append(ans)
#         except:
#             print("api error")

#     return final_res
