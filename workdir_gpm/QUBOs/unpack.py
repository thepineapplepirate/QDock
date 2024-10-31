import numpy as np
from glob import glob
import json

all_qubos = []
for fname in glob('*.npy', recursive=True):
    all_qubos.append(fname)
print("Number of QUBO files: ", len(all_qubos))

for i in range(len(all_qubos)):
    matches = [x for x in all_qubos if "_ligand"+".npy" in x]
    #print(matches)
    # load .npy file
    with open("new_qubo_" + str(i), 'w') as outfile:
        data = np.load(all_qubos[i], allow_pickle=True)
        outfile.write(str(data))
        
    print(data)

