from configparser import ConfigParser
from argparse import ArgumentParser
from datetime import datetime

####################
# Argument parsing
####################

parser = ArgumentParser()
parser.add_argument(
    "--data_path", type=str, help="data_path", default="data/test_data.xlsx"
)
parser.add_argument("--tag_path", type=str, help="tag_path", default="")
parser.add_argument(
    "--domain",
    type=str,
    help="domain of the data, e.g., manufacturing, education, etc.",
    default="manufacturing",
)
parser.add_argument(
    "--n_examples", type=int, help="number of examples to show", default=10
)
parser.add_argument(
    "--save_path",
    type=str,
    help="path to save the results",
    default=f"results/tagpt-{datetime.now().strftime('%Y-%m-%d-%H-%M')}.csv",
)

args = parser.parse_args()

DATA_PATH = args.data_path
SAVE_PATH = args.save_path
TAG_PATH = args.tag_path
DOMAIN = args.domain
N_EXAMPLES = args.n_examples


####################
# Secrets config
####################

config = ConfigParser()
config.read("config.cfg")
if not config["LLM"].get("API_KEY"):
    raise ValueError("Please set API_KEY in config.cfg")


API_KEY = config["LLM"]["API_KEY"]
MODEL = config["LLM"]["MODEL"]
TEMPERATURE = float(config["LLM"]["TEMPERATURE"])
N = int(config["LLM"]["N"])
