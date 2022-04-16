# OVITO-Tips
ovitoのpythonモジュールについてのメモを書きます。

## ovito 関連のリンク

- [ovito の HP](https://www.ovito.org/)
- [ovito のマニュアル](https://www.ovito.org/docs/current/)
- [ovito-python のマニュアル](https://www.ovito.org/docs/current/python/)


## ovito-python の準備

事前に Miniconda3 をいれておく。

- [Miniconda3](https://docs.conda.io/en/latest/miniconda.html)

```
$ conda create -n ovito
$ conda activate ovito
```

**(注意)** ovito を使う際は毎回必ず `conda activate ovito` を実行すること。

ovitoのpythonモジュールをインストール。
```
$ conda activate ovito
$ conda install --strict-channel-priority -c https://conda.ovito.org -c conda-forge ovito
```
