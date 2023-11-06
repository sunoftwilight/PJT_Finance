# import matplotlib.pyplot as plt
import csv
import numpy as np
import pandas as pd

csv_path = 'data/test_data.csv'

df = pd.read_csv(csv_path, encoding='cp949', usecols=['이름', '나이'])
df['나이'].fillna('null', inplace=True)
data = df.to_dict('records')
print(df)