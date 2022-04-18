from ovito.io import import_file
filename="N100M100.data"
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
    for i in range(num_particles):
        mol_i=mol[i]
        color[i]=color_rgb(mol_i,mol_max)

pipeline.modifiers.append(modify)
pipeline.add_to_scene()

from ovito.vis import ParticlesVis
particle_vis=pipeline.source.data.particles.vis
particle_vis.radius=0.3

from ovito.vis import BondsVis
bond_vis=pipeline.source.data.particles.bonds.vis
bond_vis.width=0.2

cell_vis=pipeline.source.data.cell.vis
cell_vis.rendering_color=(1.0,1.0,1.0)

from ovito.vis import CoordinateTripodOverlay
tripod = CoordinateTripodOverlay()
tripod.size = 0.07
tripod.offset_x = 0.02
tripod.offset_y = 0.02


import math
from ovito.vis import Viewport
vp = Viewport(type=Viewport.Type.Perspective, camera_dir=(1,2,-1))
vp.zoom_all()
vp.overlays.append(tripod)
vp.render_image(size=(500,500),filename="figure.png",background=(0,0,0))

