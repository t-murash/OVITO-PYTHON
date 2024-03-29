from ovito.io import import_file
filename="N100M100.data"
pipeline=import_file(filename,atom_style="bond")

pipeline.add_to_scene()

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


import math
from ovito.vis import Viewport
vp = Viewport(type=Viewport.Type.Perspective, camera_dir=(1,2,-1))
vp.zoom_all()
vp.overlays.append(tripod)
vp.render_image(size=(500,500),filename="figure.png",background=(0,0,0))

