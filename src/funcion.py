import pandas as pd
import numpy as np
class Calcular():
    def escenario1(df,tarea):
        tamano=len(df.index)
        escenario=pd.DataFrame(index=df.index[tarea:tamano],columns=range(0,tarea+1))
        for i in range(0,tamano-tarea):
            x1=df.ix[df.index[i:i+tarea],'NOMBRE_ESV'].values
            x1=np.append(x1,['0'])
            x2=np.transpose(x1)
            escenario.ix[escenario.index[i]]=x2
        escenario.ix[escenario.index[0:tamano-tarea],tarea]=df.ix[df.index[tarea:tamano],'NOMBRE_ESV']
        return escenario

    def escenario2(df,tarea,empresa1):
        tamano=len(df.index)
        escenario=pd.DataFrame(index=df.index[tarea:tamano],columns=range(0,tarea+2))
        for i in range(0,tamano-tarea):
            x1=df.ix[df.index[i:i+tarea],empresa1].values
            x1=np.append(x1,['0','0'])
            x2=np.transpose(x1)
            escenario.ix[escenario.index[i]]=x2
        escenario.ix[escenario.index[0:tamano-tarea],tarea]=df.ix[df.index[tarea:tamano],empresa1]
        escenario.ix[escenario.index[0:tamano-tarea],tarea+1]=df.ix[df.index[tarea:tamano],'NOMBRE_ESV']
        return escenario

    def escenario3(df,tarea,empresa1,empresa2):
        tamano=len(df.index)
        escenario=pd.DataFrame(index=df.index[tarea:tamano],columns=range(0,2*tarea+3))
        for i in range(0,tamano-tarea):
            x1=df.ix[df.index[i:i+tarea],empresa1].values
            x11=df.ix[df.index[i:i+tarea],empresa2].values
            xx=np.ravel(np.column_stack((x1,x11)))
            xx=np.append(xx,['0','0','0'])
            x2=np.transpose(xx)
            escenario.ix[escenario.index[i]]=x2
        escenario.ix[escenario.index[0:tamano-tarea],2*tarea]=df.ix[df.index[tarea:tamano],empresa1]
        escenario.ix[escenario.index[0:tamano-tarea],2*tarea+1]=df.ix[df.index[tarea:tamano],empresa2]
        escenario.ix[escenario.index[0:tamano-tarea],2*tarea+2]=df.ix[df.index[tarea:tamano],'NOMBRE_ESV']
        return escenario

    def escenario4(df, tarea, empresa1, empresa2, empresa3):
        tamano = len(df.index)
        escenario = pd.DataFrame(index=df.index[tarea:tamano], columns=range(0, 3 * tarea + 4))
        for i in range(0, tamano - tarea):
            x1 = df.ix[df.index[i:i + tarea], empresa1].values
            x11 = df.ix[df.index[i:i + tarea], empresa2].values
            x111 = df.ix[df.index[i:i + tarea], empresa3].values
            xx = np.ravel(np.column_stack((x1, x11,x111)))
            xx = np.append(xx, ['0', '0', '0','0'])
            x2 = np.transpose(xx)
            escenario.ix[escenario.index[i]] = x2
        escenario.ix[escenario.index[0:tamano - tarea], 3 * tarea] = df.ix[df.index[tarea:tamano], empresa1]
        escenario.ix[escenario.index[0:tamano - tarea], 3 * tarea+1] = df.ix[df.index[tarea:tamano], empresa2]
        escenario.ix[escenario.index[0:tamano - tarea], 3 * tarea+2] = df.ix[df.index[tarea:tamano], empresa3]
        escenario.ix[escenario.index[0:tamano - tarea], 3 * tarea+3] = df.ix[df.index[tarea:tamano], 'NOMBRE_ESV']
        return escenario