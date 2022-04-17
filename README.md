# OVITO-Tips
ovito の python モジュール `ovito-python` を使って高分子の gif アニメを作る。

<img src=https://github.com/t-murash/OVITO-Tips/blob/master/05Anim/movie.gif width=400px>

## ovito 関連のリンク

- [ovito の HP](https://www.ovito.org/)
- [ovito (GUI版) のマニュアル](https://www.ovito.org/docs/current/)
- [ovito-python のマニュアル](https://www.ovito.org/docs/current/python/)


## ovito-python の準備

事前に Miniconda3 をいれておく。

- [Miniconda3](https://docs.conda.io/en/latest/miniconda.html)

```
$ conda create -n ovito-python
$ conda activate ovito-python
```

**(注意)** ovito を使う際は毎回必ず `conda activate ovito-python` を実行すること。

ovito の pythonモジュールをインストール。
```
$ conda activate ovito-python
$ conda install --strict-channel-priority -c https://conda.ovito.org -c conda-forge ovito
```
**(注意)** GUI版 ovito もインストールされるが、Pro版のため、試用期限が過ぎるとGUI版 ovito は使えなくなる。

# 内容
1. [01FileIO](./01FileIO)
2. [02Render](./02Render)
3. [03Color](./03Color)
4. [04Unwrap](./04Unwrap)
5. [05Anim](./05Anim)
