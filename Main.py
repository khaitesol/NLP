import requests
from io import StringIO
import pandas as pd

file_id = '1J8IzaZVBp7AgbPcuJ2O2hTdiWjVJPwbN'
download_url = f'https://drive.google.com/uc?export=download&id={file_id}'

response = requests.get(download_url).text
df = pd.read_csv(StringIO(response))

print(df.head())
# Calculate the mean of the second column (named "Age")
mean_age = df["Age"].mean()
print("Mean Age of Patients:", mean_age)    
# Find the highest and lowest values in Age column
max_age = df["Age"].max()
min_age = df["Age"].min()   
print("Highest Age:", max_age)
print("Lowest Age:", min_age)       
