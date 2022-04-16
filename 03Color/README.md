# 03Color
分子番号毎に色を変える
- color.py: python script
- N100M100.data: 鎖長 N=100, 本数 M=100 のばねビーズモデル（Kremer-Grest モデル）のLAMMPS data

## 実行方法
```
$ conda activate ovito-python
$ python color.py
```

## 実行結果
<img src=https://github.com/t-murash/OVITO-Tips/blob/master/03Color/figure.png width=400px>

## color.py の簡単な説明
### 分子番号の取得
```
mol=data.particles['Molecule Identifier']
import numpy as np
num_particles=mol.size
mol_max=np.max(mol)
```
num_particles=(粒子数)、mol_max=(分子番号の最大値)

### 分子番号 1 -- mol_max に対応する色を作る関数の定義
```
def color_rgb(i,max):
    f=float(i)/float(max)
    ...
    return [r,g,b]
```
f の値域を4つの区間に分けて、rgb値の値を線形に変化させる。

### Color を追加
```
def modify(frame,data):
    color=data.particles_.create_property('Color')
    for i in range(num_particles):
        mol_i=mol[i]
        color[i]=color_rgb(mol_i,mol_max)

pipeline.modifiers.append(modify)
```

## 詳細は
- [ovito.data](https://www.ovito.org/docs/current/python/modules/ovito_data.html)
- [ovito.pipeline](https://www.ovito.org/docs/current/python/modules/ovito_pipeline.html)

