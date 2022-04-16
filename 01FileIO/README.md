# 01FileIO
LAMMPS の data ファイルの読み込みと書き出しの例。
- fileIO.py: python script
- N100M100.data: 鎖長 N=100, 本数 M=100 のばねビーズモデル（Kremer-Grest モデル）のLAMMPS data

## 実行方法
```
$ conda activate ovito-python
$ python fileIO.py
```

## ファイル読み込み
```
from ovito.io import import_file
filename="N100M100.data"
pipeline=import_file(filename)
```

## ファイル書き出し
```
from ovito.io import export_file
outfilename="N100M100.out.data"
export_file(pipeline,outfilename,"lammps/data",atom_style="bond")
```

## 詳細が知りたい人は
- [ovito.io](https://www.ovito.org/docs/current/python/modules/ovito_io.html)
