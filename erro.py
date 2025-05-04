# Exceção é um objeto que representa um erro ao executar um programa
# Blocos try ... except
# n1 = int(input('Digite um número: '))
# n2 = int(input('Digite outro número: '))

# try:
#     r = round(n1 / n2,2)
# except ZeroDivisionError:
#     print(f'não é possivel dividir por zero')
# else:
#     print(f'Resultado : {r}')
def div(k, j):
    return round( k / j,2)

if __name__ == '__main__':
    while True:
       try:
        n1 = int(input('Digite um número: '))
        n2 = int(input('Digite outro número: '))
        break 
       except ValueError:
          print(f'ocorreu um erro de digitação')
    try:
      r = div(n1,n2)
    except ZeroDivisionError:
      print(f'não é possivel dividir por zero')
    except:
      print(f'ocorreu um erro desconhecido')
    else:
      print(f'resultado: {r}')
    finally:
      print(f'\nfim do caldulo')
   
