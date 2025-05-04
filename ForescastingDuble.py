# Importar Bibliotecas
import numpy as np
import pandas as pd
import scipy.stats as stats
from scipy.stats import norm
import matplotlib.pyplot as plt

# Forescasting Exponeicial Duplo


def dupla_exponencial_suave(d, extra_periods=1, alpha=0.4, beta=0.4):

    # Tamanho do Período Histórico
    cols = len(d)
    # Gerando os nas para previsões futuras
    d = np.append(d, [np.nan]*extra_periods)
    # Gerando a matriz de prvisão futura e os nas
    f,a,b = np.full((3,cols+extra_periods),np.nan)
    # Nivel e a Tendencia Iniciando
    a[0] = d[0]
    b[0] = d[1] - d[0]
    # Gerando o Forecasting para t+1
    for t in range(1, cols):
        f[t] = a[t-1] + b[t-1]
        a[t] = alpha*d[t] + (1-alpha)*(a[t-1]+b[t-1])
        b[t] = beta*(a[t] - a[t-1]) + (1-beta)*b[t-1]
    # Forecasting para períodos extras
    for t in range(cols, cols+extra_periods):
        f[t] = a[t-1] + b[t-1]
        a[t] = f[t]
        b[t] = b[t-1]
    df = pd.DataFrame.from_dict(
        {'Demand': d, 'Forecast': f, 'Level': a, 'Trend': b, 'Error': d-f})
    return df


def kpi(df):
    dem_media = df.loc[df['Error'].notnull(), 'Demand'].mean()
    bias_abs = df['Error'].mean()
    bias_rel = bias_abs/dem_media
    print('Bias:{:0.2f},{:.2%}'.format(bias_abs, bias_rel))
    MAPE = (df['Error'].abs()/df['Demand']).mean()
    print('MAPE:{:.2%}'.format(MAPE))
    MAE_abs = df['Error'].abs().mean()
    MAE_rela = MAE_abs/dem_media
    print('MAE:{:0.2f}, {:.2%}'.format(MAE_abs, MAE_rela))
    RMSE_abs = np.sqrt((df['Error'] ** 2).mean())
    RMSE_rel= RMSE_abs / dem_media
    print('RMSE:{0:.2f}, {0:.2%}'.format(RMSE_abs, RMSE_rel))


d = [28,19,18,13,19,16,19,18,13,16,16,11,18,15,13,15,13,11,13,10,12]
df = dupla_exponencial_suave(d, extra_periods=4)
print(df)
kpi(df)
print(kpi)

#f.index.name = 'Periodo'
#df[['Demand', 'Forecast']].plot(
#    figsize=(15, 3), title='Suavizaçaõ Dupla', ylim=(10, 30), style=['-', '.'])
#plt.show()
