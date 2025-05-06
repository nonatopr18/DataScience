# Forecasting: Média Móvel, Média Móvel Exponencial Simples e Média Móvel Exponeicial Dupla
# Importar Bibliotecas
import numpy as np
import pandas as pd
import scipy.stats as stats
from scipy.stats import norm
import matplotlib.pyplot as plt
# Gerar os primeiros modelos Média Móvel
# Gerando o modelo exponencial


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
    df2 = pd.DataFrame.from_dict({'Demanda': d, 'Forecast': f, 'Error': d-f})
    return df2
# Forescasting Exponeicial Duplo


def dupla_exponencial_suave(d, extra_periods=1, alpha=0.4, beta=0.4):
    # Tamanho do Período Histórico
    cols = len(d)
# Gerando os nas para previsões futuras
    d = np.append(d, [np.nan]*extra_periods)
# Gerando a matriz de prvisão futura e os nas
    f, a, b = np.full((3, cols+extra_periods), np.nan)
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
    df3 = pd.DataFrame.from_dict(
        {'Demanda': d, 'Forecast': f, 'Level': a, 'Trend': b, 'Error': d-f})
    return df3
# df_final.to_csv('C:\\Users\\nonat\\OneDrive\\Desktop\\Instituto Inteligência de Dados\\Ciencia de Dados\\HNT_Cientista de DAdos\\DataScience\\Resultados\\Forecasting_Otimizado.csv', index=True, decimal = ',')
# Otimizando o Modelo de Forecasting


def exp_smooth_opti(d, extra_periods=2):
    params = []  # contem os diferentes parametros do conjunto de dados
    KPIs = []  # contem os resultados encontrados para o modelo
    dfs = []  # contem todos os dataframes retornados pelos diferentes modelos
    for alpha in [0.05, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6]:
        df = simple_exp_smooth(d, extra_periods=extra_periods, alpha=alpha)
        params.append(f'simple Smoothing, alpha: {alpha}')
        dfs.append(df)
        MAE = df['Error'].abs().mean()
        KPIs.append(MAE)
        for beta in [0.05, 0.1, 0.2, 0.3, 0.4]:
            df = dupla_exponencial_suave(
                d, extra_periods=extra_periods, alpha=alpha, beta=beta)
            params.append(f'Double Smoothing, alpha:{alpha},beta: {beta}')
            dfs.append(df)
            MAE = df['Error'].abs().mean()
            KPIs.append(MAE)
    mini = np.argmin(KPIs)
    print(f'Solução Otima para {params[mini]} MAE of', round(KPIs[mini], 2))
    return dfs[mini]


# Minimizando os kpis
d = [28, 19, 18, 13, 19, 16, 19, 18, 13, 16,
     16, 11, 18, 15, 13, 15, 13, 11, 13, 10, 12]
df = exp_smooth_opti(d)
df[['Demanda', 'Forecast']].plot(
    figsize=(8, 3), title='Melhor Amortecimento', ylim=(0, 30), style=['-', '--'])
plt.show()  # Mostra o gráfico do Foercasting
