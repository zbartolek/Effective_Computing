"""
Imports the all_abundance csv file, finds the Fe stess flavodoxin  gene and plots it.
"""

import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pyplot as plt
import numpy as np

#importing table:
table = pd.read_csv (r'/Users/zinkabartolek/Desktop/CLASSES/Effective Computing /data/all_abundnace_TPM.csv')
print(table)

#finding flavodoxin gene in table:
flav = table.loc[table['Gene ID'] == 'THAPSDRAFT_28635']
print (flav)

#making one table with theis gene only and time and converting to long format:
flav = flav.T
print(flav)
