# NDBS TaGPT
NDBS TagGPT is a WIP auto-label solution for NDBS. It is based on the paper [TagGPT: Large Language Models are Zero-shot Multimodal Taggers](https://arxiv.org/abs/2304.03022) and the related TagGPT source code - Although 95% have changed.


## 🔧 Dependencies
See requirements.txt for details.

```bash
# after setting up a virtual environment
conda install --file requirements.txt
```

### Help
Run the following command to get help on arguments:
```bash
python main.py --help
```

### Config
Make sure to add your own config.cfg file (based on the structure in example-config.fg). Add your OpenAI key here.

### Step 0: Data preparation
Place the data (test_data.xlsx - ATT: Thor Hauberg if you haven't recieved it).

### Step 1: Run the script
```bash
python TaGPT/main.py
```

### Step 2: Evaluate the results in the 'results' folder
```bash
ls results
```

## TODO
- [ ] Add relevant examples (See TaGPT/examples.py)
- [ ] Implement improved preprocessing to reduce errors
- [ ] Virtually everything else

<br>
<br>

# 📜 Citation for original paper
```

@article{li2023taggpt,
  title={TagGPT: Large Language Models are Zero-shot Multimodal Taggers},
  author={Li, Chen and Ge, Yixiao and Mao, Jiayong and Li, Dian and Shan, Ying},
  journal={arXiv preprint arXiv:2304.03022},
  year={2023}
}
```
