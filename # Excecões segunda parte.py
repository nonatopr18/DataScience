# Excecões segunda parte
from math import sqrt
class numeronegativoError(Exception):
    def __init__(self):
        pass

if __name__ == '__main__':
    try:
        num = int(input("Digite um nmeor positivo: "))
        if num < 0:
            raise numeronegativoError
    except numeronegativoError:
        print(f'Foi fornecido um numero negativo')
    else:
        print(f'A raiz quadrada de {num}  é {sqrt(num)}')
    finally:
        print(f'fim do calculo')
