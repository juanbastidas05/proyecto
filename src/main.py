import pandas as pd

datos = pd.read_csv('..\\data\\v2_BD_Ficheros_MEdicos1.csv', header=0, sep=';',engine = 'python')
print(datos)
v2_BD_Ficheros_MEdicos1 = pd.DataFrame (datos, columns=['NOMBRE_EMP','FECHA_VST'])
v2_BD_Ficheros_MEdicos1['NOMBRE_EMP'] = v2_BD_Ficheros_MEdicos1['NOMBRE_EMP'].astype('category',copy=False)
##v2_BD_Ficheros_MEdicos1['FECHA_VST'] = v2_BD_Ficheros_MEdicos1['FECHA_VST'].astype('category',copy=False)
print(v2_BD_Ficheros_MEdicos1.dtypes)
print(v2_BD_Ficheros_MEdicos1['NOMBRE_EMP'])

