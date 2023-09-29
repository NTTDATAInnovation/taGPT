# NDBS TAGPT
NDBS TAGPT is a WIP auto-label solution for NDBS, to be used as a sample project in the IBM AI CoE.


## 🔧 Dependencies
See Req.txt for required packages.

```bash
# after setting up a virtual environment
pip install -r Req.txt
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
