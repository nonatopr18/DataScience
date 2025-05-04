# Forecasting: Média Móvel, Média Móvel Exponencial Simples e Média Móvel Exponeicial Dupla
# Importar Bibliotecas
import numpy as np
import pandas as pd
import scipy.stats as stats
from scipy.stats import norm
import matplotlib.pyplot as plt
# Gerar os primeiros modelos Média Móvel
Demand = []
Error = []
def moving_average(d, extra_periods=1, n=3):
    # Tamanho do período historico
    cols = len(d)
    d = np.append(d, [np.nan]*extra_periods)
    # Definindo a funçaõ de previsão
    f = np.full(cols+extra_periods, np.nan)

    # Criar o perido para t+1 previsões
    for t in range(n, cols):
        f[t] = np.mean(d[t-n:t])

    # Forecast para os periodos extras
    f[t+1:] = np.mean(d[t-n:t+1])

    # Data Frame com a previsão e o erro
    df = pd.DataFrame.from_dict({'Demand': d, 'Forecast1': f, 'Error': d-f})
    return df

# Gerando o modelo exponencial
def simple_exp_smooth(d1, extra_periods=1, alpha=0.4):
    # Período Histórico
    cols = len(d1)
    # Acrescentado os na aos períodos futuros
    d1 = np.append(d1, [np.nan]*extra_periods)

    # Forecast vetor
    f = np.full(cols+extra_periods, np.nan)
    # Inicializando as primeiras previsões
    f[1] = d1[0]

    # Criando os periodos de prvisão e o periodo historico
    for t in range(2, cols+1):
        f[t] = alpha*d1[t-1]+(1-alpha)*f[t-1]

     # Forecast para todos os periodos extras
    for t in range(cols+1, cols+extra_periods):
        # fazendo o update
        f[t] = f[t-1]
    df2 = pd.DataFrame.from_dict({'Demand': d1, 'Forecast': f, 'Error': d1-f})
    return df2
# Forescasting Exponeicial Duplo


def dupla_exponencial_suave(d2, extra_periods=1, alpha=0.4, beta=0.4):

    # Tamanho do Período Histórico
    cols = len(d2)
    # Gerando os nas para previsões futuras
    d2 = np.append(d2, [np.nan]*extra_periods)
    # Gerando a matriz de prvisão futura e os nas
    f,a,b = np.full((3,cols+extra_periods),np.nan)
    # Nivel e a Tendencia Iniciando
    a[0] = d2[0]
    b[0] = d2[1] - d2[0]
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
    df3 = pd.DataFrame.from_dict(
        {'Demand': d2, 'Forecast': f, 'Level': a, 'Trend': b, 'Error': d2-f})
    return df3
# Estimando os KPIS
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

# Fazendo as Previsões para o Modelo de Média Móvel
d = [28,19,18,13,19,16,19,18,13,16,16,11,18,15,13,15,13,11,13,10,12]
df = moving_average(d, extra_periods=4, n=5)
# Fazendo as previsões para a média móvel exponecial
d1 = [28,19,18,13,19,16,19,18,13,16,16,11,18,15,13,15,13,11,13,10,12]
df2 = simple_exp_smooth(d1, extra_periods=4)
# Fazendo as previsões para a média móvel exponecial Duplo
d2 = [28,19,18,13,19,16,19,18,13,16,16,11,18,15,13,15,13,11,13,10,12]
df3 = dupla_exponencial_suave(d, extra_periods=4)
df_final = pd.concat([df,df2,df3],axis=1)
df_final = df_final.replace(" ", 'sem registro')
# Gerando os arquivos csv
print(df_final)
kpi(df)
kpi(df2)
kpi(df3)
df_final.to_csv('C:\\Users\\nonat\\OneDrive\\Desktop\\Instituto Inteligência de Dados\\Ciencia de Dados\\HNT_Cientista de DAdos\\DataScience\\Resultados\\Forecasting_Otimizado.csv', index=True, decimal = ',')