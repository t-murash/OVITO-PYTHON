# 05Anim
連番 png 画像を作ってから gif アニメを作る。
- in.anim: LAMMPS インプットファイル
- anim.py: python script
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
<img src=https://github.com/t-murash/OVITO-Tips/blob/master/05Anim/movie.gif width=500px>

## 簡単な説明
N100M100.(番号).data を作成後、 ovito で figure.(番号).png を出力する。最後に convert で png をまとめて、gif アニメを作成する。

## in.anim の説明
10ステップ毎に N100M100.(番号).dataファイルを出力するのを100回繰り返す。
```
variable a loop 100 pad
label loop
run 10
write_data N100M100.$a.data
next a
jump SELF loop
```


## anim.py の説明
unwrap.py の data 入力時と png 出力時に frame 番号を追加しただけ。
```
frame=100
frame0=str(frame).zfill(3)
print(frame0)
from ovito.io import import_file
filename="N100M100."+str(frame0)+".data"
...
vp.render_image(size=(500,500),filename="figure."+str(frame0)+".png",background=(0,0,0))
```


## anim.sh の説明
anim.py の一行目の数字を書き換えて、`python anim.py` を実行、figure.(番号).png を作成。
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

