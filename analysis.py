import pandas as pd

# Load results
results = {
    "Method": ["VQE", "DFT", "FCI"],
    "Energy (Hartree)": [-78.452, -78.441, -78.462]
}
df = pd.DataFrame(results)
print(df)
