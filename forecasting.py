# Importar Bibliotecas
import numpy as np
import pandas as pd
import scipy.stats as stats
from scipy.stats import norm
import matplotlib.pyplot as plt
# Gerar os primeiros modelos Média Móvel
def moving_average(d, extra_periods=1, n=3):
    # Tamanho do período historico
    cols = len(d)
    d=np.append(d,[np.nan]*extra_periods)
    # Definindo a funçaõ de previsão
    f = np.full(cols+extra_periods,np.nan)
    
    # Criar o perido para t+1 previsões 
    for t in range(n,cols):
        f[t]=np.mean(d[t-n:t])

    #Forecast para os periodos extras
    f[t+1:]=np.mean(d[t-n:t+1])
    
    # Data Frame com a previsão e o erro
    df=pd.DataFrame.from_dict({'Demand':d,'Forecast':f,'Error':d-f})
    return df
# Estimando o Bias e o MAPE , Erro médio relativo e o Erro Médio Quadrático
def kpi(df):
    dem_ave=df.loc[df['Error'].notnull(),'Demand'].mean()
    bias_abs=df['Error'].mean()
    bias_rel=bias_abs/dem_ave
    print('Bias:{:0.2f},{:.2%}'.format(bias_abs,bias_rel))
    MAPE=(df['Error'].abs()/df['Demand']).mean()
    print('MAPE:{:.2%}'.format(MAPE))
    MAE_abs=df['Error'].abs().mean()
    MAE_rela=MAE_abs/dem_ave
    print('MAE:{:0.2f}, {:.2%}'.format(MAE_abs,MAE_rela))
    RMSE_abs=np.sqrt((df['Error']**2)).mean()
    RMSE_rel=RMSE_abs/dem_ave
    print('RMSE:{0:.2f}, {0:.2%}'.format(RMSE_abs, RMSE_rel))

#Estimando o MAPE


d = [28,19,18,13,19,16,19,18,13,16,16,11,18,15,13,15,13,11,13,10,12]
df = moving_average(d, extra_periods=4, n=5)
#d = [28,19,18,13,19,16,19,18,13,16,16,11,18,15,13,15,13,11,13,10,12]
#df = moving_average(d, extra_periods=4)
kpi(df)
print(df)
#df[['Demand','Forecast']].plot()
#plt.plot(df[['Demand','Forecast']])
#plt.show() 
