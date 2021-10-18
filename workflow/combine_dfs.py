import pandas as pd
import sys

input_paths = sys.argv[1:-1]
output_path = sys.argv[-1]

print("Start to load dfs")
dfs = []
for input_path in input_paths:
    temp_df = pd.read_csv(input_path)
    dfs.append(temp_df)

df = pd.concat(dfs)
df.to_csv(output_path, index=None)