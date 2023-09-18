# NDBS TAGPT
NDBS TAGPT is a WIP auto-label solution for NDBS, to be used as a sample project in the IBM AI CoE.


## 🔧 Dependencies
See requirements.txt for details.


```bash

virtualenv venv -p python3.10
source venv/bin/activate

# after setting up a virtual environment
pip install python-dotenv
pip install "ibm-watson-machine-learning>=1.0.320" | tail -n 1
pip install "pydantic>=1.10.0" | tail -n 1
pip install langchain | tail -n 1


pip install rich
pip install pandas
pip install openpyxl --upgrade

# pip install ibm-generative-ai
# pip install "ibm-generative-ai[langchain]"
# pip install pypdf
# pip install InstructorEmbedding
# pip install 'transformers[torch]'
# pip install sentence-transformers
# pip install Flask flask-restful flask_httpauth
# pip install cachetools
# pip install unstructured
# pip install from-root
# pip install chromadb
# pip install chroma-migrate
# pip install text-extensions-for-pandas
# pip install --upgrade ibm-watson
# pip install jupyterlab

# pip install matplotlib
# pip install ibm-watson-machine-learning
```

## Help
Run the following command to get help on arguments:
```bash
python main.py --help
```

## Config
Make sure to add your own config.cfg file (based on the structure in example-config.fg). Add your OpenAI key here.

## Usage

#### Step 0/2: Data preparation
Place the data (test_data.xlsx - ATT: Thor Hauberg if you haven't recieved it).

#### Step 1/2: Run the script
```bash
python tagpt/main.py
```

#### Step 2/2: Evaluate the results in the 'results' folder
By default, the output .csv. file is saved as `tagpt-\<datetime>.csv`
```bash
ls results
```

## TODO

- [ ] Change to langchain
- [ ] Virtually everything else (this is a PoC)



## Inspiration
The original idea is based on the paper [TagGPT: Large Language Models are Zero-shot Multimodal Taggers](https://arxiv.org/abs/2304.03022) - Although 99% have changed.
```

@article{li2023taggpt,
  title={TagGPT: Large Language Models are Zero-shot Multimodal Taggers},
  author={Li, Chen and Ge, Yixiao and Mao, Jiayong and Li, Dian and Shan, Ying},
  journal={arXiv preprint arXiv:2304.03022},
  year={2023}
}
```
