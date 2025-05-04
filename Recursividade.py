# Recursividade
# Formula Geral para o Fatorial
def fatorial(numero):
    if numero == 0 or numero == 1:
        return 1
    else:
        return numero * fatorial(numero-1)
if __name__ == '__main__':
    x = int(input('digite um numero: '))
    try:
        res = fatorial(x)
    except RecursionError:
        print (f'o numero fornecido é muito grande')
    else:
        print(f'o fatutorial de {x} é {res}')