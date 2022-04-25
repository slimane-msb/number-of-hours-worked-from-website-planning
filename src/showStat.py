import pandas as pd

df = pd.read_csv("20222523062524.csv", encoding = "ISO-8859-1")

with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
    print(df)