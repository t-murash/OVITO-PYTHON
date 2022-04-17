# 05Anim
連番 png 画像を作ってから gif アニメを作る。
- anim.py: python script
- in.anim: LAMMPS インプットファイル
- anim.sh: bash script
- N100M100.data: 鎖長 N=100, 本数 M=100 のばねビーズモデル（Kremer-Grest モデル）のLAMMPS data

## 実行方法
```
$ mpirun ./lmp -in in.anim
$ conda activate ovito-python
$ bash anim.sh
```
**(注意)** lmp (LAMMPS)と convert (Imagemagick) が必要です。

## 実行結果
<img src=https://github.com/t-murash/OVITO-Tips/blob/master/05Anim/movie.gif width=400px>

## anim.py の簡単な説明
### trj.(番号).data を読み込んで、figure.(番号).png を出力する

```
frame=1
from ovito.io import import_file
filename="trj."+str(frame)+".data"
...
frame0=str(frame).zfill(4)
print(frame0)
vp.render_image(size=(1000,1000),filename="figure."+str(frame0)+".png",background=(0,0,0))
```

## in.anim の簡単な説明
100ステップおきにdataファイルを出力する
```
variable a loop 100
label loop
run 100
write_data trj.$a.data
next a
jump SELF loop
```

## anim.sh の簡単な説明
anim.py の一行目の数字を書き換えて、`python anim.py` を実行して、連番の figure.*.png を作成。
```
for((i=$INI;i<=$END;i++)); do
    sed -i "1c frame=$i" anim.py
    python anim.py
done
```

convert コマンドで gif アニメ movie.gif を作成。
```
convert -delay 5 -loop 0 figure.*.png movie.gif
```

