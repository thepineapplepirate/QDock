# # Importing standard Qiskit libraries and configuring account
# from qiskit import QuantumCircuit, IBMQ
# from qiskit.compiler import transpile, assemble
# from qiskit.tools.jupyter import *
# from qiskit.visualization import *
#quadratic optimization
from qiskit_optimization import QuadraticProgram
from qiskit_optimization.converters import QuadraticProgramToQubo

# Prepare QUBO task

#prepare quadratic binary optimization task
task = QuadraticProgram(name = 'QUBO on QC')
task.binary_var(name = 'x')
task.binary_var(name = 'y')
task.binary_var(name = 'z')
task.minimize(linear = [1,-2,3], quadratic = [[0,0.5,-0.5],[0.5,0,1],[-0.5,1,0]])
qubo = QuadraticProgramToQubo().convert(task) #convert to QUBO
print(qubo.export_as_lp_string())

#converting QUBO task to Ising Hamiltonian for simulation on quantum computer
qubit_op, offset = qubo.to_ising()

#operator - unitary operator representing the simulated Hamiltonian
#offset - used after solution on QC to convert objective function value to the proper one

print(qubit_op)
# print(task)
# print(qubo)
# print(qubo.to_ising())

# qp = QuadraticProgram()
# qp.from_ising(qubit_op, offset, linear = True) #linear=True => x^2 is shown as x since x^2=x for x in {0,1}
# print(qp.export_as_lp_string())