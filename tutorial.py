import os
here = os.getcwd()
if not os.path.exists("workdir_fam"):
    os.mkdir("workdir_fam")
if not os.path.exists("workdir_gpm"):
    os.mkdir("workdir_gpm")

from QDock.GridPointMatching.qdock import GPMDock
from QDock.FeatureAtomMatching.qdock import FAMDock
os.chdir("%s/workdir_fam"%(here))
fam = FAMDock()

#fam.make_receptor("./data/1y6r_protein.pdb", "./workdir_fam/")
fam.make_receptor("../data/1y6r_protein.pdb")

import shutil
ligand_li = [
  "1y6r_ligand.mol2",
  "2vkm_ligand.mol2",
  "3dxg_ligand.mol2",
  "2iwx_ligand.mol2",   
]

for i in ligand_li:
    shutil.copy("%s/%s"%("../data",i),"./%s"%(i))
#Well, it is a bug in AutoDockFR, that only ligand file at current dir could be processed.
    
fam.make_ligand(ligand_li)

# Create the docking box in either one of two ways below:

#Via original ligand
fam.make_box_ligand("data/1y6r_ligand.mol2",grid_length=1.0)

#Via manual input of docking box(coordinates of the center and length in x,y,z dimension)
#fam.make_box_input(x=56.217,y=73.499,z=20.476,dx=10,dy=10,dz=10,grid_length=1.0)

# Dock a single ligand, produces a numpy array
poses1 = fam.indiv_dock(ligand=fam.ligands[0], edge_cutoff=1.870, K_dist=2.261, K_mono=11.479, n_pos=30, 
                       save_qubo=True,sim_dock=True,save_match=True,save_pose=True)

# Or you can dock multiple ligands, produces a python list
poses2 = fam.dock(edge_cutoff=1.870, K_dist=2.261, K_mono=11.479, n_pos=30, 
                 save_qubo=True,sim_dock=True,save_match=True,save_pose=True)


# Now results are produced
# numpy array containing coordinates of sampled poses

print(type(poses1))
print(poses1.shape)
print(poses1[0])
print(type(poses2))
print(len(poses2))
print(poses2[1].shape)


# QUBO matrix saved in an npy file. 
import numpy as np
qubo = np.load("QUBOs/1y6r_ligand.npy",allow_pickle=True).item()
print(list(qubo.keys())[0:10])
print(qubo[list(qubo.keys())[0]])


# Now do this with the Grip Point Matching (GPM) method instead
os.chdir("%s/workdir_gpm"%(here))
import shutil

gpm = GPMDock()

print("Loading receptor and ligands...")
gpm.make_receptor("../data/1y6r_protein.pdb")

ligand_li = [
  "1y6r_ligand.mol2",
  "2vkm_ligand.mol2",
  "3dxg_ligand.mol2",
  "2iwx_ligand.mol2",   
]
for i in ligand_li:
    shutil.copy("%s/%s"%("../data",i),"./%s"%(i))
gpm.make_ligand(ligand_li)

print("Creating docking box...")
gpm.make_box_ligand("data/1y6r_ligand.mol2",grid_length=2.0)
#gpm.make_box_input(x=56.217,y=73.499,z=20.476,dx=10,dy=10,dz=10,grid_length=2.0)

print("Docking a single ligand...")
poses1 = gpm.indiv_dock(ligand=fam.ligands[0], edge_cutoff=2.162, K_dist=0.405, K_mono=25.090, n_pos=30, 
                       save_qubo=True,sim_dock=True,save_match=True,save_pose=True)
print("Docking all ligands...")
poses2 = gpm.dock(edge_cutoff=2.162, K_dist=0.405, K_mono=25.090, n_pos=30, 
                       save_qubo=True,sim_dock=True,save_match=True,save_pose=True)

print(type(poses1))
print(poses1.shape)
print(poses1[0])
print(type(poses2))
print(len(poses2))
print(poses2[1].shape)

import numpy as np
qubo = np.load("QUBOs/1y6r_ligand.npy",allow_pickle=True).item()
print(list(qubo.keys())[0:10])
print(qubo[list(qubo.keys())[0]])
