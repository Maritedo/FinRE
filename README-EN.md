# FinRE

### Introduction
FinRE is a manual-labeled financial news RE dataset. Given a sentence and its head and tail entities, the model needs to predict the relation between the head and tail entities. This dataset is annotated from the Sina Finance News corpus, in which the named entity is a commercial company, and the relation contains 44 financial relation categories (two-way) except for the NA category, including special relation categories in the financial and financial fields such as ownership, shareholding, competition, acquisition, transaction, cooperation, and shareholding.

### Paper
[Chinese Relation Extraction with Multi-Grained Information and External Linguistic Knowledge](https://www.aclweb.org/anthology/P19-1430.pdf). ACL 2019.

### Data Size
Training set: 7,454; Validation set: 1,489; Test set: 3,727.

### Data Format
Each instance is composed of id (id, an integer), text (text, a string), relation label (label, an integer), the description of relation label (label_desc, a string), a head entity (head, a dictionary), and a tail entity (tail, a dictionary).

### Example
```json
{
  "id": 2, 
  "text": "东方航空AH股临时停牌传将与上航合并", 
  "label": 19,
  "label_desc": "合并",
  "head": {
    "mention": "东方航空",
    "start": 0,
    "end": 4
  }, 
  "tail": {
    "mention": "上航", 
    "start": 14, 
    "end": 16
  }
}
```

### Evaluation Code
The prediction result needs to be consistent with the format of the training set.
The correct file name is FinRE.jsonl.
```shell
python eval.py prediction_file test_private_file
```
The evaluation metrics are P, R, F1, and the output is in dictionary format.
```she
return {"P":_, "R":_, "F1":_}
```

### Author List
Ziran Li, Ning Ding, Zhiyuan Liu, Haitao Zheng, Ying Shen

### Institutions
Tsinghua University

### Citation
```bibtex
@inproceedings{li-etal-2019-FinRE,
    title = "{C}hinese Relation Extraction with Multi-Grained Information and External Linguistic Knowledge",
    author = "Li, Ziran  and
      Ding, Ning  and
      Liu, Zhiyuan  and
      Zheng, Haitao  and
      Shen, Ying",
    booktitle = "Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics",
    year = "2019",
    pages = "4377--4386",
}
```


