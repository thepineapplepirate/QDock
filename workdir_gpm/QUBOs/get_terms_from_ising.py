

import numpy as np

from qiskit.quantum_info import Pauli, SparsePauliOp



def get_linear_op(num_qubits: int, linear_terms_list: list) -> SparsePauliOp:
    pauli_list = []
    for i in range(num_qubits):
        z = np.zeros(num_qubits, dtype=bool)
        z[i] = True
        pauli_list.append(Pauli((z, np.zeros(num_qubits, dtype=bool))))
    return SparsePauliOp(pauli_list, coeffs=linear_terms_list)


def get_quadratic_op(
    qubit_names: list, quadratic_terms_dict: dict
) -> SparsePauliOp:
    pauli_list = []
    coeffs = []
    for i, qb_i in enumerate(qubit_names):
        for j, qb_j in enumerate(qubit_names):
            try:
                coeffs.append(quadratic_terms_dict[(qb_i, qb_j)])
            except:
                coeffs.append(0) # if we dont have a term, we add a 0
            z = np.zeros(num_qubits, dtype=bool) # list of pauli Z operators
            z[i] = True
            z[j] = True
            pauli_list.append(Pauli((z, np.zeros(num_qubits, dtype=bool))))
    return SparsePauliOp(pauli_list, coeffs=coeffs)

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

print("Linear terms: ", linear_terms)
print("Quadratic terms: ", quadratic_terms)
print("Offset: ", offset)
print("Number of qubits: ", num_qubits)
print("Qubit names: ", qubit_names)

# make sure that the quadratic terms is a a square matrix
print("Quadratic terms is a square matrix: ", len(quadratic_terms) == len(quadratic_terms[0]))
# make sure that the number of terms in the linear terms is equal to the number of qubits
print("Number of terms in the linear terms is equal to the number of qubits: ", len(linear_terms) == num_qubits)
# make sure that the number of terms in the quadratic terms is equal to the number of qubits
print("Number of terms in the quadratic terms is equal to the number of qubits: ", len(quadratic_terms) == num_qubits)

print(get_linear_op(num_qubits, linear_terms))
print(get_quadratic_op(qubit_names, quadratic_dict))

op = get_linear_op(num_qubits, linear_terms) + get_quadratic_op(qubit_names, quadratic_dict)

qp = QuadraticProgram()
qp.from_ising(op, offset, linear=True)
print(qp.prettyprint())