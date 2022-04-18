# 07OSPRay
連番 png 画像を作ってから gif アニメを作る。ここでは OSPRay renderer を使用する。
- in.anim: LAMMPS インプットファイル
- ospray.py: python script
- ospray.sh: bash script
- N100M100.data: 鎖長 N=100, 本数 M=100 のばねビーズモデル（Kremer-Grest モデル）のLAMMPS data

## 実行方法
```
$ mpirun ./lmp -in in.anim
$ conda activate ovito-python
$ bash ospray.sh
```

## 実行結果
<img src=https://github.com/t-murash/OVITO-Tips/blob/master/07OSPRay/movie.gif width=500px>

<img src=https://github.com/t-murash/OVITO-Tips/blob/master/07OSPRay/figure.001.png width=500px>

## 簡単な説明
06Tachy と内容はほぼ同じ。違いは下記。
```
from ovito.vis import OSPRayRenderer
vp.render_image(size=(500,500),filename="figure."+str(frame0)+".png",background=(0,0,0),renderer=renderer=OSPRayRenderer(dof_enabled=True,focal_length=80,aperture=5.))
```
注目したい場所にピントを合わせて、他はぼかした絵が描ける。focal_lengthでピントを合わせる位置を調節、aperture でぼかしの強さを設定する。


