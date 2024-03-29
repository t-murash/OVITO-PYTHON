frame=100
frame0=str(frame).zfill(3)
print(frame0)
from ovito.io import import_file
filename="N100M100."+str(frame0)+".data"
pipeline=import_file(filename,atom_style="bond")

data=pipeline.compute()
mol=data.particles['Molecule Identifier']
import numpy as np
num_particles=mol.size
mol_max=np.max(mol)

def color_rgb(i,max):
    f=float(i)/float(max)
    r=0
    g=0
    b=0
    if f < 0.25:
        r=1.0
        g=4*f
        b=0.0
    elif f < 0.5:   
        r=1.0-4*(f-0.25)
        g=1.0
        b=0.0
    elif f < 0.75:
        r=0.0
        g=1.0
        b=4*(f-0.5)
    else:
        r=0.0
        g=1.0-4*(f-0.75)
        b=1.0
    return [r,g,b]

def modify(frame,data):
    color=data.particles_.create_property('Color')
    #trans=data.particles_.create_property('Transparency')
    for i in range(num_particles):
        mol_i=mol[i]
        #if mol_i == 1:
        #    trans[i]=0.0
        #else:
        #    trans[i]=0.9
        color[i]=color_rgb(mol_i,mol_max)
        
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

pipeline.modifiers.append(modify)

from ovito.modifiers import UnwrapTrajectoriesModifier
pipeline.modifiers.append(UnwrapTrajectoriesModifier())
pipeline.add_to_scene()

from ovito.vis import ParticlesVis
particle_vis=pipeline.source.data.particles.vis
particle_vis.radius=0.4

from ovito.vis import BondsVis
bond_vis=pipeline.source.data.particles.bonds.vis
bond_vis.width=0.6
bond_vis.enabled=True

cell_vis=pipeline.source.data.cell.vis
cell_vis.rendering_color=(1.0,1.0,1.0)

from ovito.vis import CoordinateTripodOverlay
tripod = CoordinateTripodOverlay()
tripod.size = 0.07
tripod.offset_x = 0.02
tripod.offset_y = 0.02
lx=data.cell[0,0]
ly=data.cell[1,1]
lz=data.cell[2,2]

import math
from ovito.vis import Viewport
vp = Viewport(type=Viewport.Type.Perspective, camera_dir=(1,1,-1),camera_pos=(-lx,-ly,2*lz))
vp.overlays.append(tripod)
from ovito.vis import OSPRayRenderer
vp.render_image(size=(500,500),filename="figure."+str(frame0)+".png",background=(0,0,0),renderer=OSPRayRenderer(dof_enabled=True,focal_length=40,aperture=0.8))

