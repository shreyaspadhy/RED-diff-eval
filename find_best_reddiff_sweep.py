import itertools
import os

lr_values = [0.05, 0.1, 0.25, 0.5, 1.0]
grad_term_weights = [0.05, 0.1, 0.25, 0.5, 1.0]

etas = [0.0, 0.2, 0.4, 0.5, 0.6, 0.8, 1.0]

# Generate all combinations of the argument values
combinations = list(itertools.product(etas, grad_term_weights))

# Open the output file in write mode
folder = "/home/sp2058/RED-diff/<root>/_exp/_exp"


for eta, weight in combinations:
    file_folder = os.path.join(folder, f"blur_dps_eta_{eta}_weight_{weight}")

    results = os.path.join(file_folder, "results.txt")

    with open(results, "r") as f:
        lines = f.readlines()
        psnr = float(lines[0].split()[1])
        print(eta, weight, psnr)

# os.makedirs(os.path.dirname(filename), exist_ok=True)
# with open(filename, "w") as f:
#     f.write("#!/bin/bash\n")
#     # Iterate over the combinations and write each version to a new line in the file
#     for lr, weight in combinations:
