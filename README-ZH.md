# FinRE

### 简介
FinRE是一个人工精标注的财经金融领域的数据集。给定句子和其中的头尾实体，要求模型预测头尾实体之间的关系。该数据集由新浪财经新闻语料标注得到，其中命名实体为商业公司，在关系上设计了除NA类之外的44个金融领域的关系类别（双向），包含拥有、持股、竞争、收购、交易、合作、减持等财经金融领域的特有关系类别。

### 论文
[Chinese Relation Extraction with Multi-Grained Information and External Linguistic Knowledge](https://www.aclweb.org/anthology/P19-1430.pdf). ACL 2019.

### 数据规模
训练集：7,454句；验证集：1,489句；测试集：3,727句。

### 数据格式描述
每条数据包含编号(id，以整数形式存储)，文本(text，以字符串形式存储)，关系标签序号(label，以整数形式存储)，关系标签内容(label_desc，以字符串形式存储)，头实体(head，以词典形式存储)以及尾实体(tail，以词典形式存储)。

### 数据样例
```json
{
  "id": 2, 
  "text": "东方航空AH股临时停牌传将与上航合并", 
  "label": 19, //若为负例，此处为0
  "label_desc": "合并", //若为负例，此处为"N/A"
  "head": {
    "mention": "东方航空", //实体提及内容
    "start": 0, //实体提及在句子中开始的字序号
    "end": 4  //实体提及在句子中结束的字序号
  }, 
  "tail": {
    "mention": "上航", 
    "start": 14, 
    "end": 16
  }
}
```

### 评测代码
预测代码需要和训练数据保持一样的格式。
正确提交文件名：FinRE.jsonl
```shell
python eval.py prediction_file test_private_file
```
评测指标为P, R, F1，输出结果为字典格式：
```she
return {"P":_, "R":_, "F1":_}
```

### 作者列表
李自然、丁宁、刘知远、郑海涛、沈颖

### 制作单位
清华大学

### 论文引用
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


