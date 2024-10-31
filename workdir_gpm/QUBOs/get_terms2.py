

import numpy as np
ising = np.load("1y6r_ligand.npy",allow_pickle=True)

linear_terms = list(ising[0].values())
qubit_names = list(ising[0].keys())
offset = ising[2]
num_qubits = len(qubit_names)

quadratic_dict = ising[1]

quadratic_terms = []

for i in qubit_names:
    # i is the label for qubit i
    temp = []
    for j in qubit_names:
        # j is the label for qubit j
        try:
            temp.append(quadratic_dict[(i,j)])
        except:
            temp.append(0)
    quadratic_terms.append(temp)

# print("Linear terms: ", linear_terms)
# print("Quadratic terms: ", quadratic_terms)
# print("Offset: ", offset)
# print("Number of qubits: ", num_qubits)
# print("Qubit names: ", qubit_names)
print("First Quadratic list: ", quadratic_terms[0])

# make sure that the quadratic terms is a a square matrix
print("Quadratic terms is a square matrix: ", len(quadratic_terms) == len(quadratic_terms[0]))