import gzip
import json
import sys
import pandas as pd

input_path = sys.argv[1]
output_path = sys.argv[-1]

print("Start to load the tweets")
with gzip.open(input_path) as f:
    tweets = json.load(f)

print("Start to process tweets")
counts = []
for tweet in tweets:
    text = tweet['text'].lower()
    tid = tweet['id']
    if 'dog' in text:
        counts.append([tid, 'dog'])

    if 'cat' in text:
        counts.append([tid, 'cat'])

df = pd.DataFrame(counts, columns=['tid', 'keyword'])
df.to_csv(output_path, index=None)