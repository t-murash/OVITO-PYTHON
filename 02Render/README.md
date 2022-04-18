# 02Render
LAMMPS の data ファイルを読み込んで、PNG 画像として出力
- render.py: python script
- N100M100.data: 鎖長 N=100, 本数 M=100 のばねビーズモデル（Kremer-Grest モデル）のLAMMPS data

## 実行方法
```
$ conda activate ovito-python
$ python render.py
```

## 実行結果
<img src=https://github.com/t-murash/OVITO-Tips/blob/master/02Render/figure.png width=500px>

## render.py の簡単な説明
### ファイル読み込み
```
from ovito.io import import_file
filename="N100M100.data"
pipeline=import_file(filename,atom_style="bond")

pipeline.add_to_scene()
```
data ファイルを読み込み後の `pipeline.add_to_scene()` が大事。

### 見栄えの調整
```
from ovito.vis import ParticlesVis
particle_vis=pipeline.source.data.particles.vis
particle_vis.radius=0.4

from ovito.vis import BondsVis
bond_vis=pipeline.source.data.particles.bonds.vis
bond_vis.width=0.6

cell_vis=pipeline.source.data.cell.vis
cell_vis.rendering_color=(1.0,1.0,1.0)

from ovito.vis import CoordinateTripodOverlay
tripod = CoordinateTripodOverlay()
tripod.size = 0.07
tripod.offset_x = 0.02
tripod.offset_y = 0.02
```
粒子半径、ボンド（シリンダ）幅、ユニットセルの色、座標軸表示の設定

### PNG ファイル出力
```
import math
from ovito.vis import Viewport
vp = Viewport(type=Viewport.Type.Perspective, camera_dir=(1,2,-1))
vp.zoom_all()
vp.overlays.append(tripod)
vp.render_image(size=(500,500),filename="figure.png",background=(0,0,0))
```

## 詳細は
- [ovito.data](https://www.ovito.org/docs/current/python/modules/ovito_data.html)
- [ovito.pipeline](https://www.ovito.org/docs/current/python/modules/ovito_pipeline.html)
- [ovito.vis](https://www.ovito.org/docs/current/python/modules/ovito_vis.html)
