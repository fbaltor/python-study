import pandas as pd
import io
import json

file_path = "./test.json"

f = io.open(file_path, "r", encoding="utf-8")

json = json.load(f)

data = json["data"]
headers = data.pop(0)

df = pd.DataFrame(data, columns=headers)
print(df)
