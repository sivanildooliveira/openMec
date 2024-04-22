import pandas as pd


df = pd.read_excel('servico.xlsx')

for c in df['Código da OS']:
    print(c)