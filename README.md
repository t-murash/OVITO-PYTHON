# OVITO-Tips
ovito の python モジュール `ovito-python` を使って高分子の gif アニメを作る。

<img src=https://github.com/t-murash/OVITO-Tips/blob/master/06Tachy/movie.gif width=500px>

## ovito 関連のリンク

- [ovito の HP](https://www.ovito.org/)
- [ovito (GUI版) のマニュアル](https://www.ovito.org/docs/current/)
- [ovito-python のマニュアル](https://www.ovito.org/docs/current/python/)


## ovito-python の準備

Miniconda をいれる。

- [Miniconda](https://docs.conda.io/en/latest/miniconda.html)
```
$ wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
$ bash ./Miniconda3-latest-Linux-x86_64.sh
```

ovito-python の実行環境を作る。

```
$ conda create -n ovito-python
$ conda activate ovito-python
```

**(注意)** ovito-python を使う際は `conda activate ovito-python` を実行して、ovito-python 環境にする。

ovito の python モジュールをインストール。
```
$ conda activate ovito-python
$ conda install --strict-channel-priority -c https://conda.ovito.org -c conda-forge ovito
```
**(注意)** GUI 版 ovito もインストールされるが、有償のため、試用期限が過ぎると GUI 版 ovito は使えなくなる。細かい調整には GUI 版が便利です。

# 内容
1. [01FileIO](./01FileIO)
2. [02Render](./02Render)
3. [03Color](./03Color)
4. [04Unwrap](./04Unwrap)
5. [05Anim](./05Anim)
6. [06Tachy](./06Tachy)
7. [07OSPRay](./07OSPRay)
