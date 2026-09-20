import pandas as pd
import json
import os

print("current working directry", os.getcwd())

data_path = "./data/sales.csv"

df = pd.read_csv(data_path)
print("CSV Data")
print(df)
print(df.shape)
print(f"\nShape: {df.shape[0]} row, {df.shape[1]} columns")


df["total"] = df["Quantity"] + df["Price"]
print(df)


#creating folder (output) is folder is present then it will not return error becouse (exist_of=true)
os.makedirs("output", exist_ok=True)

#saving the output in diffrent format

# Save as Excel
df.to_excel("output/sales_data.xlsx", index=False)

# Save as JSON
df.to_json("output/sales_data.json", orient="records")

