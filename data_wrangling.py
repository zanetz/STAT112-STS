import json
import pandas as pd
import numpy as np

# load json
with open('2020-09-30-21-09#1031.json') as f:
    data = json.load(f)

# create dataframe
df = pd.DataFrame(data)

# take all objects in the event column and make them other columns
df = pd.concat([df.drop(['event'], axis=1), df['event'].apply(pd.Series)], axis=1)

# save as csv
df.to_csv('2020-09-30-21-09#1031.csv', index=False)