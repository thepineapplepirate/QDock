from qiskit_algorithms.utils import algorithm_globals
from qiskit_algorithms import QAOA, NumPyMinimumEigensolver
from qiskit_algorithms.optimizers import COBYLA
from qiskit.primitives import Sampler
from qiskit_optimization.algorithms import (
    MinimumEigenOptimizer,
    RecursiveMinimumEigenOptimizer,
    SolutionSample,
    OptimizationResultStatus,
)
from qiskit_optimization import QuadraticProgram
from qiskit_optimization.converters import QuadraticProgramToQubo
from qiskit.visualization import plot_histogram
from typing import List, Tuple
import numpy as np

import ast

# Load the .txt file
with open('new_qubo_0', 'r') as file:
    content = file.read()

# Convert the content to a dictionary
data_dict = ast.literal_eval(content)

# Initialize the lists
linear_terms = []
qubit_names = []
quadratic_dict = {}

keys = list(data_dict.keys())

# Populate the lists based on the keys
for key in keys:
    if key[0] == key[1]:
        linear_terms.append(data_dict[key])
        qubit_names.append(key[0])
        print(key[0])
    else:
        quadratic_dict[key] = data_dict[key]

num_qubits = len(qubit_names)
print('Number of qubits:', num_qubits)

qubo = QuadraticProgram()
for qb_name in qubit_names:
    qubo.binary_var(qb_name)
qubo.minimize(linear=linear_terms, quadratic=quadratic_dict)
#qubo = QuadraticProgramToQubo().convert(qubo) #convert to QUBO
print(qubo.prettyprint())
print(qubo.export_as_lp_string())
# print('Number of qubits:', num_qubits)
print("the linear terms are:", linear_terms[0:10])
print("the qubit names are:", qubit_names[0:10])
print("the quadratic terms are:", list(quadratic_dict.keys())[0:10])
# #print(quadratic_dict)

qubit_op, offset = qubo.to_ising()

print(qubit_op)


