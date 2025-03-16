from qiskit_nature.second_q.drivers import PySCFDriver
from qiskit_nature.second_q.problems import ElectronicStructureProblem

# Step 2: Generate Hamiltonian using PySCF
driver = PySCFDriver(
    atom='optimized_geometry.xyz',
    basis='sto3g',
    charge=0,
    spin=0,
    method='dft',
    xc='b3lyp',
)
problem = driver.run()

# Save Hamiltonian data
with open('../data/hamiltonian.txt', 'w') as f:
    f.write(str(problem.second_q_ops()[0]))
print("Hamiltonian saved to data/hamiltonian.txt")
