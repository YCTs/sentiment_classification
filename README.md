# sentiment classification


## 套件版本

*   pytho3.6
*   keras 2.0.8
*   tensorflow 1.7.0

## 下載 pre train 好的 word embedding

    wget -O Dict_3.npy https://www.dropbox.com/s/8txl5kmr3hyub89/Dict_3.npy?dl=0

這個檔案 Dict_3.npy 要確定放在跟 [util.py](./util.py) 同一個路徑底下，以及確認路徑[model_submission](./model_submission/)和[util.py](./util.py)在同一個路徑下

## 使用

```python
from util import _function

```

在util.py中

```python
def _function(sentence):
```
*   input: 參數sentence是一個string，代表一句話
*   return: numpy，一個分數

```python

print(_function("thank you"))

```
得到 [[0.97889274]]