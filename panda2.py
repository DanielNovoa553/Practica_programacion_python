import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('panda.csv')  # read csv file
# print(df)  # print dataframe
#
# df_filtrado = df.dropna()  # Elimina las filas con valores nulos
# print("\n", df_filtrado)  # Imprime el nuevo DataFrame
#
# df_remove = df.fillna(0)  # Reemplaza los valores nulos por 0
# print("\n", df_remove)  # Imprime el nuevo DataFrame
#
# print("\n", df[["email", "name", "lastname"]])  # Imprime las columnas email y name
# df_iloc = df.iloc[0]  # Imprime la primera fila
# print("\n", df_iloc)  # Imprime la primera fila
#
# df_fillna = df.fillna({"email": 0, "password": -1})  # Reemplaza los valores nulos por 0 y -1
# print("\n", df_fillna)  # Imprime el nuevo DataFrame
#
# df_registro = df.loc[[1], ["id", "email", "name", "lastname", "user", "password"]]  #
# print("\n", df_registro)

grouped = df.groupby("name").agg(
     {"edad": "mean"}
)

grouped["edad"].plot(kind="bar", figsize=(10, 10), title="Edad promedio por nombre", color="green",  use_index=True, legend=True, scrollable=True )
plt.show()