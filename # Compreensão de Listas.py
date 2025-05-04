# # Compreensão de Listas
# numeros = [1, 4, 7, 9, 10, 12, 21]
# quadrados = [num**2 for num in numeros]
# print(quadrados)
# Criar uma lista de numeros de 0 a 10
# pares = [num for num in range(1200) if num % 2 == 0]
# print(pares)
# frase = 'A lógica é apenas o principio da sabedoria'
# vogais = ['a','e','i','o','u']
# lista_vogais= [v for v in frase if v in vogais]
# print(f'A frase poussi {len(lista_vogais)} vogais:')
# print(lista_vogais)
# distribuitiva entre valores
distributiva = [k * m for k in [2,3,4] for m in [12,12,34]]
print(distributiva)