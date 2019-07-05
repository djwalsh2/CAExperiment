import CA
import hashlib
import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd
from random import choice
import sys
import seaborn as sns
"""
Experiment Name: Rule 30
Date: 7/4/2019
Prepared by: David Walsh
"""

def get_redundant_pairs(df):
    '''Get diagonal and lower triangular pairs of correlation matrix'''
    pairs_to_drop = set()
    cols = df.columns
    for i in range(0, df.shape[1]):
        for j in range(0, i+1):
            pairs_to_drop.add((cols[i], cols[j]))
    return pairs_to_drop


def get_top_abs_correlations(df, n=1001):
    au_corr = df.corr().abs().unstack()
    labels_to_drop = get_redundant_pairs(df)
    au_corr = au_corr.drop(labels=labels_to_drop).sort_values(
        ascending=False).dropna()
    return au_corr[0:n]

"""
CA Parameters
"""
ca_rule = 30
ca_radius = 1
ca_config_num = 1
ca_config_len = 19
ca_generations = 100
ca_df = pd.DataFrame()
ca_df_headers = list()
pd.set_option('display.max_columns', 1001)
pd.set_option('display.max_rows', 1001)
file = os.path.basename(__file__) + "_results.txt"
sys.stdout = open(file, 'wt')

"""
Question:
    Does the CA rule 30 generate high correlation coefficients for 1000 
    randomly generated bit strings of length 19 for 100 generations?
"""

"""
Process
"""
# Step 1) Randomly generate n bit strings of length l
l = 19
n = 100
print()
print("Step 1\n====")
print("Generating " + str(n) + " bit strings of length " + str(l))
print("Result:")

bit_list = []
for i in range(0, n):
    b = ''.join(choice(['0', '1']) for _ in range(l))
    print(b)
    bit_list.append(b)

for bs in bit_list:
    print(bs, end='\n')
print()

# Step 2) For each bit string, evolve over g generations]
print("Step 2\n===")
print("Evolving each bit strings over " + str(ca_generations) + " generations")
print("Result: ")
results = []
for bs in bit_list:
    bs = CA.bin_to_dec(bs)
    r = CA.evolve(ca_rule, ca_radius, bs, ca_config_len,
                  ca_generations)
    r = [y for x in r for y in x]
    results.append(r)
    print(r, end='\n\n')

# Step 3) Create data frame from results
print("Step 3\n===")
print("Data Frame of Results")

for i in range(0, l):
    for j in range(0, ca_generations+1):
        s = ("x" + str(j) + "t" + str(i))
        ca_df_headers.append(s)
ca_df = pd.DataFrame(results, columns=ca_df_headers, index=bit_list)
print(ca_df)
print()

# Step 4) Generate Correlation Matrix
# corr = ca_df.corr()
# mask = np.zeros_like(corr, dtype=np.bool)
# mask[np.triu_indices_from(mask)] = True
# f, ax = plt.subplots(figsize=(11, 9))
# sns.heatmap(corr, mask=mask, cmap="Purples", vmax=.3, center=0,
#             square=True, linewidths=.5, cbar_kws={"shrink": .5})
# plt.show()

# Step 5) Sort correlation coefficients
print("Top Absolute Correlations")
print(get_top_abs_correlations(ca_df, 100))
print()

"""
Results
"""

"""
Conclusions
"""

"""
Conjectures
"""

"""
Documentation
"""
print("Documentation\n====")
# get current file name
script = os.path.basename(__file__)

# calculate script md5 hash
script_hash = hashlib.md5(open(script, 'rb').read()).hexdigest()
print("Script hash=" + script_hash)

# calculate results md5 hash
csv_hash = hashlib.md5(open('rule30.csv', 'rb').read()).hexdigest()
print("CSV hash=" + csv_hash)
