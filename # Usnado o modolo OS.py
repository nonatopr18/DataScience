# Usnado o modolo OS
# iremos montar um sistema os
import os

os.chdir('C:\\Users\\nonat\\OneDrive\\Desktop\\Instituto Inteligência de Dados\\Ciencia de Dados\\HNT_Cientista de DAdos\\Data_Science\\Teste')
print(f'Diretorio Atual: {os.getcwd()}')

padrao_nome = input('Qual o padrão de nome sem extensão ')

for contador, arq in enumerate(os.listdir()):
    if os.path.isfile(arq):
        nome_arq, exten_arq = os.path.splitext(arq)
        nome_arq = padrao_nome + ' ' + str(contador)

        nome_novo = f'{nome_arq}{exten_arq}'
        os.rename(arq,nome_arq)
print(f'\nArquivos renomeados')