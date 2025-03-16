
]
]
from ase.build import molecule
from pyscf import dft

# Step 1: Geometry optimization with DFT
ethylene = molecule('C2H4')
ethylene.set_cell((10, 10, 10))  # Simulation box
ethylene.center()

# PySCF DFT calculation
mf = dft.RKS(ethylene)
mf.xc = 'b3lyp'
mf.kernel()

# Save optimized geometry
ethylene.write('optimized_geometry.xyz')
print("Optimized geometry saved to optimized_geometry.xyz")
