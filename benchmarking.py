from pyscf import fci

# Load VQE results
with open('../data/results.csv', 'r') as f:
    vqe_energy = float(f.readline().split(": ")[1])

# Compare with FCI
mf = dft.RKS(molecule('C2H4'))
mf.xc = 'b3lyp'
mf.kernel()
cisolver = fci.FCI(mf)
fci_energy = cisolver.kernel()[0]

print(f"VQE Energy: {vqe_energy:.4f} Hartree")
print(f"FCI Energy: {fci_energy:.4f} Hartree")
