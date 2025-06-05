# Importar as bibliotecas
# Trabalhando com manipulação de Datas e horários
import pandas as pd
import numpy as np
from pytz import all_timezones
data_string = np.array(
    ['03-04-2005 11:35 PM', '23-05-2010 12:01 AM', '04-09-2009 09:09 PM'])
# Converter a date times
datas = [pd.to_datetime(date, format='%d-%m-%Y %I:%M %p',
                        errors="coerce") for date in data_string]
print(datas)
# Alterar ou adicionar fuso-horário
print(pd.Timestamp)
# Gerando uma data a um local especifico
data = pd.Timestamp('2025-06-04 06:00:00')
# Apontar para o local
data_londres = data.tz_localize('Europe/London')
# Converter para outra localidade
print(data_londres.tz_convert('Africa/Abidjan'))
# Aplicando para vários períodos
data_periodo = pd.Series(pd.date_range('5/6/2025', periods=5, freq='M'))
print(data_periodo)
# apontando o range de datas para outra localidade
print(data_periodo.dt.tz_localize('Africa/Abidjan'))
print(all_timezones[1:89])  # vendo as zonas
# Selecionando datas e períodos
dataframe = pd.DataFrame()
# Gerando as datas
dataframe['data'] = pd.date_range('1/1/2001', periods=100000, freq='H')
print(dataframe.head(10))
# Selecionando um períod
print(dataframe[(dataframe['data'] > '2002-1-1 01:00:00')
      & (dataframe['data'] <= '2002-1-1 23:00:00')])
# Gerando várias colunas de datas com periodos diferentes
#dataframe['data'] = pd.date_range('1/1/2001', periods=150, freq='W')
# Criando as features para ano, mês,dia, hora e minutos
dataframe['Ano']=dataframe['data'].dt.year
dataframe['Mês']=dataframe['data'].dt.month
dataframe['Dia']=dataframe['data'].dt.day
dataframe['Hora']=dataframe['data'].dt.hour
dataframe['Minuto']=dataframe['data'].dt.minute
print(dataframe.head(4))