import requests
from io import StringIO
import pandas as pd

file_id = '1J8IzaZVBp7AgbPcuJ2O2hTdiWjVJPwbN'
download_url = f'https://drive.google.com/uc?export=download&id={file_id}'

response = requests.get(download_url).text
df = pd.read_csv(StringIO(response))

print(df.head())
# Calculate and print the mean of Age column
mean_age = df['Age'].mean()
print(f'Mean Age: {mean_age}')     
# Print the Highest and Lowest Values in the Age Column
max_age = df['Age'].max()
min_age = df['Age'].min()   
print(f'Highest Age: {max_age}')
print(f'Lowest Age: {min_age}')
