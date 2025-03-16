from qiskit.algorithms.minimum_eigensolvers import VQE
from qiskit.algorithms.optimizers import SLSQP
from qiskit.primitives import Estimator
from qiskit_nature.second_q.mappers import ParityMapper
from qiskit.circuit.library import TwoLocal
from qiskit.utils import QuantumInstance
from qiskit.providers.fake_provider import FakeManila

# Load Hamiltonian
with open('../data/hamiltonian.txt', 'r') as f:
    hamiltonian_str = f.read()
hamiltonian = eval(hamiltonian_str)

# Map Hamiltonian to qubits
mapper = ParityMapper()
qubit_op = mapper.map(hamiltonian)

# Define ansatz
num_qubits = qubit_op.num_qubits
ansatz = TwoLocal(num_qubits, 'ry', 'cz', entanglement='full', reps=3)

# Configure VQE
optimizer = SLSQP(maxiter=500)
estimator = Estimator()
backend = FakeManila()  # Simulate noise of real hardware
quantum_instance = QuantumInstance(backend, shots=1000)

vqe = VQE(
    estimator,
    ansatz,
    optimizer,
    quantum_instance=quantum_instance
)
result = vqe.compute_minimum_eigenvalue(qubit_op)

# Save results
with open('../data/results.csv', 'w') as f:
    f.write(f"VQE Energy: {result.eigenvalue}\n")
print("VQE Energy saved to data/results.csv")
