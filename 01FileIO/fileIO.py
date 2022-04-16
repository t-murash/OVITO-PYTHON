from ovito.io import import_file
filename="N100M100.data"
pipeline=import_file(filename)

from ovito.io import export_file
outfilename="N100M100.out.data"
export_file(pipeline,outfilename,"lammps/data",atom_style="bond")
