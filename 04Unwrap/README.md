# 04Unwrap
周期境界で折りたたまれた分子（wrapped 分子）を展開（unwrap）する。
- unwrap.py: python script
- N100M100.data: 鎖長 N=100, 本数 M=100 のばねビーズモデル（Kremer-Grest モデル）のLAMMPS data

## 実行方法
```
$ conda activate ovito-python
$ python unwrap.py
```

## 実行結果
<img src=https://github.com/t-murash/OVITO-Tips/blob/master/04Unwrap/figure.png width=400px>

## unwrap.py の簡単な説明
### PBC 番号の修正
分子中央粒子のPBC番号を引く。
```
def modify(frame,data):
    ...        
    pbc=data.particles_['Periodic Image_']
    pid=data.particles['Particle Identifier']
    mol_id_min=np.zeros((mol_max))
    mol_id_max=np.zeros((mol_max))
    mol_id_mid=np.zeros((mol_max))
    pbc_mid=np.zeros((mol_max,3))
    pbc_sort=np.zeros((num_particles,3))
    for i in range(mol_max):
        mol_id_min[i]=2*num_particles
        mol_id_max[i]=-1

    for i in range(num_particles):
        pid_i=pid[i]
        mol_i=mol[i]
        if pid_i < mol_id_min[mol_i-1]:
            mol_id_min[mol_i-1]=pid_i
        if pid_i > mol_id_max[mol_i-1]:
            mol_id_max[mol_i-1]=pid_i

    for i in range(num_particles):
        pid_i=pid[i]
        pbc_sort[pid_i-1,0]=pbc[i,0]
        pbc_sort[pid_i-1,1]=pbc[i,1]
        pbc_sort[pid_i-1,2]=pbc[i,2]

    for i in range(mol_max):
        min_id=mol_id_min[i]
        max_id=mol_id_max[i]
        mol_id_mid[i]=np.ceil((max_id-min_id+1)/2)+min_id
        pbc_mid[i,0]=pbc_sort[int(mol_id_mid[i])-1,0]
        pbc_mid[i,1]=pbc_sort[int(mol_id_mid[i])-1,1]
        pbc_mid[i,2]=pbc_sort[int(mol_id_mid[i])-1,2]

    for i in range(num_particles):
        pid_i=pid[i]
        mol_i=mol[i]
        pbc[i,0]-=pbc_mid[mol_i-1,0]
        pbc[i,1]-=pbc_mid[mol_i-1,1]
        pbc[i,2]-=pbc_mid[mol_i-1,2]
```

### Unwrap
Modifier (`UnwrapTrajectoriesModifier`) を使って Unwrap を実施する。
```
from ovito.modifiers import UnwrapTrajectoriesModifier
pipeline.modifiers.append(UnwrapTrajectoriesModifier())
```

## 詳細は
- [ovito.data](https://www.ovito.org/docs/current/python/modules/ovito_data.html)
- [ovito.modifiers](https://www.ovito.org/docs/current/python/modules/ovito_modifiers.html)
- [ovito.pipeline](https://www.ovito.org/docs/current/python/modules/ovito_pipeline.html)
- [ovito.vis](https://www.ovito.org/docs/current/python/modules/ovito_vis.html)

