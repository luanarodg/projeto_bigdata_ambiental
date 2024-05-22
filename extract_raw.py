import pandas as pd

# Script básico para transformar os dados de csv para parquet.

df = pd.read_csv("temas_ambientais.csv", sep=";", encoding="utf-8")

df.to_parquet("temas_ambientais.parquet")