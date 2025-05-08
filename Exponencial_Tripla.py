# Suavização Exponencial Tripla
# Importar Bibliotecas
import numpy as np
import pandas as pd
import scipy.stats as stats
from scipy.stats import norm
import matplotlib.pyplot as plt
# Gerar os fatores sazonais iniciais


def seasonal_factors_mul(s, d, slen, cols):
    for i in range(slen):
        s[i] = np.mean(d[i:cols:slen])  # Sessão de Meéidas
    s /= np.mean(s[:slen])  # Calcula todos os fatores sazonais
    return s
# Gerar a Função Exponencial Tripla


def triple_exp_smooth_mul(d, slen=12, extra_periods=1, alpha=0.4, beta=0.4, phi=0.9, gamma=0.3):
    cols = len(d)  # Tamanho do período Histórico
    # Adicionando os nans no vetor de demanda
    d = np.append(d, [np.nan]*extra_periods)
    # Componentes de inicialização
    f, a, b, s = np.full((4, cols+extra_periods), np.nan)
    s = seasonal_factors_mul(s, d, slen, cols)
    a[0] = d[0]/s[0]
    b[0] = d[1]/s[1] - d[0]/s[0]
    # Gerando o Forecast para as primeiras sessões
    for t in range(slen, cols):
        f[t] = (a[t-1] + phi*b[t-1])*s[t-slen]
        a[t] = alpha*d[t]/s[t-slen] + (1-alpha)*(a[t-1]+phi*b[t-1])
        b[t] = beta*(a[t]-a[t-1]) + (1-beta)*phi*b[t-1]
        s[t] = gamma*d[t]/a[t] + (1-gamma)*s[t-slen]
    # Forecast para todos os períodos extras
        for t in range(cols, cols+extra_periods):
            f[t] = (a[t-1] + phi*b[t-1])*s[t-slen]
            a[t] = f[t]/s[t-slen]
            b[t] = phi*b[t-1]
            s[t] = s[t-slen]
    df = pd.DataFrame.from_dict(
        {'Demanda': d, 'Forecast': f, 'Nível': a, 'Tendencia': b, 'Sasonalidade': s, 'Erro': d - f})
    return df


d = [14, 10, 6, 2, 18, 8, 4, 1, 16, 9, 5, 3, 18, 11, 4, 2, 17, 9, 5, 1]
df = triple_exp_smooth_mul(d, slen=12, extra_periods=4,
                           alpha=0.3, beta=0.2, phi=0.9, gamma=0.2)
print(df)
df[['Nível', 'Tendencia', 'Sasonalidade']].plot(secondary_y=['Sasonalidade'])
df.plot(subplots=True)
plt.show()
