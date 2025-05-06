# Importar Bibliotecas
import numpy as np
import pandas as pd
import scipy.stats as stats
from scipy.stats import norm
import matplotlib.pyplot as plt


def simple_exp_smooth(d, extra_periods=1, alpha=0.4):
    # Período Histórico
    cols = len(d)
    # Acrescentado os na aos períodos futuros
    d = np.append(d, [np.nan]*extra_periods)

    # Forecast vetor
    f = np.full(cols+extra_periods, np.nan)
    # Inicializando as primeiras previsões
    f[1] = d[0]

    # Criando os periodos de prvisão e o periodo historico
    for t in range(2, cols+1):
        f[t] = alpha*d[t-1]+(1-alpha)*f[t-1]

     # Forecast para todos os periodos extras
    for t in range(cols+1, cols+extra_periods):
        # fazendo o update
        f[t] = f[t-1]
    df = pd.DataFrame.from_dict({'Demanda': d, 'Forecast': f, 'Erro': d-f})
    return df


# Alimentar o Modelo
# Plotando os dados
#df.index.name = 'Period0'
#df[['Demanda', 'Forecast']].plot(figsize=(8,3), title='Suavização Simples', ylim=(0,30), style=['-', '--'])
#plt.show()

# Estimando os KPIS
def kpi(df):
    dem_media=df.loc[df['Erro'].notnull(),'Demanda'].mean()
    bias_abs=df['Erro'].mean()
    bias_rel=bias_abs/dem_media
    print('Bias:{:0.2f},{:.2%}'.format(bias_abs,bias_rel))
    MAPE=(df['Erro'].abs()/df['Demanda']).mean()
    print('MAPE:{:.2%}'.format(MAPE))
    MAE_abs=df['Erro'].abs().mean()
    MAE_rela=MAE_abs/dem_media
    print('MAE:{:0.2f}, {:.2%}'.format(MAE_abs,MAE_rela))
    RMSE_abs=np.sqrt((df['Erro']**2)).mean()
    RMSE_rel=RMSE_abs/dem_media
    print('RMSE:{0:.2f}, {0:.2%}'.format(RMSE_abs, RMSE_rel))




d = [28,19,18,13,19,16,19,18,13,16,16,11,18,15,13,15,13,11,13,10,12]
df = simple_exp_smooth(d, extra_periods=4)
print(df)
kpi(df)
