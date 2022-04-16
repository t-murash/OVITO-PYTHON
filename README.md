# OVITO-Tips
ovito の python モジュール `ovito-python` についてのメモ

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
1. [File/IO 01FileIO](./01FileIO)
2. [Render 02Render](./02Render)
