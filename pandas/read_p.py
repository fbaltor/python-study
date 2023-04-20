import pandas as pd
import io

def f(n):
    return "./P" + str(n) + ".csv"

def r(n):
    return pd.read_csv(f(n), sep=";", encoding="latin_1").drop_duplicates()

df1 = r(1)
print(df1)

df2 = r(2)

dfs = [df1, df2]

df = pd.concat(dfs, axis=0, ignore_index=True).drop_duplicates()
