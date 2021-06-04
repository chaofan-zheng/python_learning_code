from pprint import pprint
from sklearn.datasets import load_boston
import pandas as pd
import numpy as np

boston = load_boston()
# pprint(boston)
# array01 = pd.array(np.arange(0,9,1).reshape((3,3)))
df1 = pd.DataFrame(np.arange(0,9,1).reshape((3,3)))
print(df1)
df1.astype()