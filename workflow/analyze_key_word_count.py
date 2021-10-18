import pandas as pd
import matplotlib.pyplot as plt
import sys

input_path = sys.argv[1]
output_path = sys.argv[2]

print("Start to load the data")
df = pd.read_csv(input_path)

print("Start to analyze the results")
counts = df.groupby('keyword')['tid'].nunique()
plt.bar(
    ['cat', 'dog'],
    [counts['cat'], counts['dog']]
)
plt.savefig(output_path, dpi=300)