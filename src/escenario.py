import unittest
import pandas as pd
import numpy as np
from funcion import Calcular

#porcentaje = sys.argv[1]
#agrupa = sys.argv[2]
#tarea = sys.argv[3]
#try:
#    porcentaje=float(porcentaje)
#    agrupa=int(agrupa)
#    tarea=int(tarea)
#    print("Los datos ingresados para los escenarios son:",porcentaje,agrupa,tarea)

#with open("v1test.csv") as csvfile:
df = pd.read_csv('../src/v4test.csv')
#print(df)

#Escenario 1 Numero de visitas anual por empleado
df_new1=df.groupby(['PRIMERAPELLIDO_US','SEGUNDOAPELLIDO_US','PRIMERNOMBRE_US','SEGUNDONOMBRE_US'])['NUMEROCONTACTO_VST'].sum()
print(df_new1)
df_new1.to_csv('Escenario9.csv')

df.drop(['DESCRIPCION_CIC','PRIMERAPELLIDO_US','SEGUNDOAPELLIDO_US','PRIMERNOMBRE_US','SEGUNDONOMBRE_US','TIPO','NOMBRE',
                     'NOMBRE_LGV','NUMEROCONTACTO_VST','CODIGO_VST','FECHA_PLANIFICADA_VST','FECHA_CREACION_USW'], axis=1,inplace=True)

fecha=df['FECHA_VST']
fecha=pd.to_datetime(fecha)
df['FECHA_VST']=fecha
print (df['FECHA_VST'])

df=df[df.NOMBRE_ESV[:]=='REALIZADA']
print (df)

df['INTERPHARM']=df['NOMBRE_EMP']
df['SIEGFRIED']=df['NOMBRE_EMP']
df['NUTRICIONAL']=df['NOMBRE_EMP']
df.drop(['NOMBRE_EMP'],axis=1, inplace=True)
print (df)

df['NOMBRE_ESV']=1
df['INTERPHARM'].replace(to_replace=['INTERPHARM'],value=1,inplace=True)
df['SIEGFRIED'].replace(to_replace=['SIEGFRIED'],value=1,inplace=True)
df['NUTRICIONAL'].replace(to_replace=['NUTRICIONAL'],value=1,inplace=True)

df['INTERPHARM'].replace(to_replace=['SIEGFRIED','NUTRICIONAL'],value=0,inplace=True)
df['SIEGFRIED'].replace(to_replace=['INTERPHARM','NUTRICIONAL'],value=0,inplace=True)
df['NUTRICIONAL'].replace(to_replace=['SIEGFRIED','INTERPHARM'],value=0,inplace=True)
print (df)

porcentaje=0.30
prueba=df.sample(frac=porcentaje,random_state=1)
modelo=df.drop(prueba.index)

agrupa='60min'
pruebadf=prueba.resample(agrupa,on='FECHA_VST').sum()
pruebadf['Tiempo']=pruebadf.index.time
pruebadf=pruebadf.groupby('Tiempo').mean()
pruebadf.reset_index().to_csv('.././src/csv_escenarios/test.csv',header=True,index=False)

df=modelo.resample(agrupa,on='FECHA_VST').sum()
df['Tiempo']=df.index.time
df=df.groupby('Tiempo').mean()
print (df)
df.reset_index().to_csv('.././src/csv_escenarios/test1.csv',header=True,index=False)

tarea=4
tabla1=Calcular.escenario1(df,tarea)
print(tabla1)
tabla1.reset_index().to_csv('.././src/csv_escenarios/Escenario_1.csv',header=True,index=False)

tabla2=Calcular.escenario2(df,tarea,'INTERPHARM')
print(tabla2)
tabla2.reset_index().to_csv('.././src/csv_escenarios/Escenario_2.csv',header=True,index=False)

tabla3=Calcular.escenario2(df,tarea,'SIEGFRIED')
print(tabla3)
tabla3.reset_index().to_csv('.././src/csv_escenarios/Escenario_3.csv',header=True,index=False)

tabla4=Calcular.escenario2(df,tarea,'NUTRICIONAL')
print(tabla4)
tabla4.reset_index().to_csv('.././src/csv_escenarios/Escenario_4.csv',header=True,index=False)

tabla5=Calcular.escenario3(df,tarea,'INTERPHARM','SIEGFRIED')
print(tabla5)
tabla5.reset_index().to_csv('.././src/csv_escenarios/Escenario_5.csv',header=True,index=False)

tabla6=Calcular.escenario3(df,tarea,'INTERPHARM','NUTRICIONAL')
print(tabla6)
tabla6.reset_index().to_csv('.././src/csv_escenarios/Escenario_6.csv',header=True,index=False)

tabla7=Calcular.escenario3(df,tarea,'NUTRICIONAL','SIEGFRIED')
print(tabla7)
tabla7.reset_index().to_csv('.././src/csv_escenarios/Escenario_7.csv',header=True,index=False)

tabla8=Calcular.escenario4(df,tarea,'NUTRICIONAL','SIEGFRIED','INTERPHARM')
print(tabla8)
tabla8.reset_index().to_csv('.././src/csv_escenarios/Escenario_8.csv',header=True,index=False)