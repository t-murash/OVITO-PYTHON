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
<img src=https://github.com/t-murash/OVITO-Tips/blob/master/05Anim/movie.gif width=400px>

## anim.py の簡単な説明
trj.(番号).data を作成後、 ovito で figure.(番号).png を出力する。最後に convert で png をまとめて、gif アニメを作成する。

## in.anim の簡単な説明
1ステップ毎にdataファイルを出力する
```
variable a loop 100 pad
label loop
run 1
write_data N100M100.$a.data
next a
jump SELF loop
```

## anim.py の簡単な説明
<<<<<<< HEAD
unwrap.py の data 入力時と png 出力時に frame 番号を追加しただけ。
=======
>>>>>>> 2e10358 (05Anim)
```
frame=100
frame0=str(frame).zfill(3)
from ovito.io import import_file
filename="N100M100."+str(frame0)+".data"
...
vp.render_image(size=(1000,1000),filename="figure."+str(frame0)+".png",background=(0,0,0))
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

