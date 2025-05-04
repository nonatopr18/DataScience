# Importar Bibliotecas
import numpy as np
import pandas as pd
import scipy.stats as stats
from scipy.stats import norm
import matplotlib.pyplot as plt
from forecasting import moving_average 
from ForescastingDuble import dupla_exponencial_suave 
# Gerando a funão para minizar os pârametros
def exp_suave_opti(d,extra_periodo=6):
    params = [] # Conjunto de parâmetros
    KPIs = [] # contem a performace do modelo
    dfs = [] # Dataframes retornado pelo diferentes modelos
    for alpha in [0.005,0.1,0.2,0.3,0.4,0.5,0.6]:
        df = moving_average(d, extra_periods=extra_periods, alpha=alpha)
        params.append(f'Simple Smoothing, alpha:{alpha}')
        dfs.append(df)
        MAE = df['Error'].abs().mean()
        KPIs.append(MAE)
        for beta in [0.05,0.1,0.2,0.3,0.4]:
            df = dupla_exponencial_suave(d, extra_periods=extra_periods, alpha=alpha, beta=beta)
            params.append(f'Double Smoothing, alpha: {alpha},beta:{beta}')
            dfs.append(df)
            MAE = df['Error'].abs().mean()
            KPIs.append(MAE)
        mini = np.argmin(KPIs)
        print(f'Solução Otima para os {params[mini]} MAE of',round(KPIs[mini],2))
        return dfs[mini]
    d = [28,19,18,13,19,16,19,18,13,16,16,11,18,15,13,15,13,11,13,10,12]
    df1 = exp_smooth_opti(d)
    print(df1)
    