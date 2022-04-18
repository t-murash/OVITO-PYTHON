# 06Tachy
連番 png 画像を作ってから gif アニメを作る。05Anim はOpenGL renderer を使っていたが、ここではTachyon renderer を使用する。
- in.anim: LAMMPS インプットファイル
- tachy.py: python script
- tachy.sh: bash script
- N100M100.data: 鎖長 N=100, 本数 M=100 のばねビーズモデル（Kremer-Grest モデル）のLAMMPS data

## 実行方法
```
$ mpirun ./lmp -in in.anim
$ conda activate ovito-python
$ bash tachy.sh
```
**(注意)** 05Anim の時と比べると少し時間がかかります。

## 実行結果
<img src=https://github.com/t-murash/OVITO-Tips/blob/master/06Tachy/movie.gif width=500px>

<img src=https://github.com/t-murash/OVITO-Tips/blob/master/06Tachy/figure.001.png width=500px>

## 簡単な説明
05Anim と内容はほぼ同じ。違いは下記。
```
from ovito.vis import TachyonRenderer
vp.render_image(size=(500,500),filename="figure."+str(frame0)+".png",background=(0,0,0),renderer=renderer=TachyonRenderer())
```
05Anim の時と異なり影が付いている。Tachyon renderer を使うと立体的に見える絵が描ける。


