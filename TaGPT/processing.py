import re
from inspect import stack

from utils.logger import logger

list_finder = re.compile(r"[\*'\"]?[\{\[](.*?)[\{\]][\*'\"]?")


def _preprocess(data):
    return data


def _postprocess(data: dict) -> dict:
    logger.info(data)
    try:
        if lists := list_finder.findall(data["tags"]):
            cleaned_tags = [
                (e.strip().strip('"').strip("'")) for e in lists[-1].split(",")
            ]

            logger.info(cleaned_tags)
            data["tags"] = cleaned_tags

    except Exception as e:
        logger.info(
            f"FAILED in '{stack()[0][3]}' | "
            + f"{e.__class__.__name__} | "
            + f"Input: {data}\n"
            + f"{e.with_traceback()}"
        )
        data["tags"] = []
    return data


# def posterior_process(data_path):
#     f = open(data_path, 'r')
#     out = ""
#     tag_all = []
#     for line in f.readlines():
#         line = line.replace(".", "")
#         line = line.replace("。", "")
#         line = line.replace(",", "、")
#         line = line.replace("，", "、")
#         line = line.replace("'", "")
#         line = line.replace("\n", "")
#         line = line.replace("\"", "")
#         tmp = line.strip().split('||')
#         out += str(tmp) + "\n"
#         for t in tmp:
#             if '、' in t:
#                 tags = t.split('、')
#                 tag_all += tags
#     f.close()

#     ans = Counter(tag_all)
#     ans = sorted(ans.items(), key=lambda x: x[1], reverse=True)

#     tags = []
#     for tmp in ans:
#         if tmp[1] > 2:
#             tags.append(tmp[0].replace(' ', ''))

#     f = open('../data/tags.txt', 'w')
#     f.write('\n'.join(tags))
#     f.close()

#     encoder = SentenceTransformer('hfl/chinese-roberta-wwm-ext-large')
#     tags_embed = encoder.encode(tags)
#     tags_dis = [np.sqrt(np.dot(_, _.T)) for _ in tags_embed]
#     mark = [0 for _ in range(len(tags))]
#     include = [[] for _ in range(len(tags))]

#     for i in tqdm.trange(len(tags)):
#         if mark[i] == 0:
#             score = np.dot(tags_embed[i], tags_embed[i:].T)
#             for j in range(i, len(tags)):
#                 if i != j:
#                     score[j - i] = score[j - i] / (tags_dis[i] * tags_dis[j])
#                     if score[j - i] > 0.95:
#                         mark[j] = 1
#                         include[i].append(tags[j])

#     out = ""
#     for i in range(len(tags)):
#         if mark[i] == 0:
#             out += tags[i] + "||" + str(include[i]) + "\n"

#     f = open('../data/final_tags.csv', 'w')
#     f.write(out)
#     f.close()
