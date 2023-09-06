import openai

from taggers import GenTagger
from config import API_KEY, DATA_PATH, SAVE_PATH
from i_o import load_data, save_data
from utils.logger import logger, log_pipeline


openai.api_key = API_KEY


@log_pipeline
def main():
    _data = load_data(DATA_PATH)
    results = GenTagger.tag_many(_data)
    save_data(results, SAVE_PATH)
    logger.info("COMPLETED GENERATIVE TAGGING")


if __name__ == "__main__":
    main()
