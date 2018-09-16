# sentiment classification


## 套件版本

*   pytho3.6
*   keras 2.0.8
*   tensorflow 1.7.0

## 下載 pre train 好的 word embedding

    wget -O Dict_3.npy https://www.dropbox.com/s/8txl5kmr3hyub89/Dict_3.npy?dl=0

這個檔案要確定放在跟 [main.py](./main.py) 同一個路徑底下
## 執行

    $ bash run.sh

## Demo

    $ bash run.sh
    Sentence:
    >> thank you !
    Score:  [[0.9891985]]

## 結束程式

    Sentence:
    >> exit
