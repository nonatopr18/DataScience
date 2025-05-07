# Função de Suavização com salto amortecido
# Importar Bibliotecas
import numpy as np
import pandas as pd
import scipy.stats as stats
from scipy.stats import norm
import matplotlib.pyplot as plt
def dupla_exponencial_amortecida_suavizada(d, extra_periods=1, alpha=0.4, beta=0.4, phi=0.9):
    cols = len(d) #Histórico do periódo
    # acrescentando os nas ao vetor de demanda e previsões
    d = np.append(d,[np.nan]*extra_periods)
    # Criando o vetor de nivel, tendência e forecasting
    f, a, b = np.full((3, cols+extra_periods), np.nan)
    # Iniciando o nivel e a tendencia
    a[0] = d[0]
    b[0] = d[1] - d[0]
    # Criando o Forecasting para todo o periodo t+1
    for t in range(1, cols):
        f[t] = a[t-1] - phi*b[t-1]
        a[t] = alpha*d[t] + (1-alpha)*(a[t-1] + phi*b[t-1])
        b[t] = beta*(a[t] - a[t-1]) + (1-beta)*phi*b[t-1]
    # Forecasting para todos os periodos
    for t in range(cols, cols+extra_periods):
        f[t] = a[t-1] - phi*b[t-1]
        a[t] = f[t]
        b[t] = phi*b[t-1]
    df = pd.DataFrame.from_dict(
        {'Demand': d, 'Forecast': f, 'Level': a, 'Trend': b, 'Error': d-f})
    return (df)
def kpi(df0):
    dem_ave=df.loc[df0['Error'].notnull(),'Demand'].mean()
    bias_abs=df0['Error'].mean()
    bias_rel=bias_abs/dem_ave
    print('Bias:{:0.2f},{:.2%}'.format(bias_abs,bias_rel))
    MAPE=(df0['Error'].abs()/df0['Demand']).mean()
    print('MAPE:{:.2%}'.format(MAPE))
    MAE_abs=df['Error'].abs().mean()
    MAE_rela=MAE_abs/dem_ave
    print('MAE:{:0.2f}, {:.2%}'.format(MAE_abs,MAE_rela))
    RMSE_abs=np.sqrt((df0['Error']**2)).mean()
    RMSE_rel=RMSE_abs/dem_ave
    print('RMSE:{0:.2f}, {0:.2%}'.format(RMSE_abs, RMSE_rel))
d = [28,19,18,13,19,16,19,18,13,16,16,11,18,15,13,15,13,11,13,10,12]
df = dupla_exponencial_amortecida_suavizada(d, extra_periods=4)
#print(df)
kpi(df)