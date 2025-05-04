# #Funções lmabda(anomina)
# quadrado = lambda x: x**2
# for i in range(1,11):
#     print(quadrado(i))

# par = lambda x: x %2 == 0
# print(par(8))

# f_c= lambda f:(f-32)*5/9
# print(f_c(4))

# num = [2,4,5,1,6,8]
# dobro = list(map(lambda x: x*2,num))
# print(dobro)

# palavras = ['python', 'é', 'linguagem', 'de', 'programação']
# maiuscula = list(map(str.upper,palavras))
# print(maiuscula)

# def numeros_pares(n):
#     return n % 2 == 0

# numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13]

# num_par = list(filter(numeros_pares,numeros))
# print(num_par)

# numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13]
# num_impar = list(filter(lambda x: x % 2 != 0,numeros))
# print(num_impar)

from functools import reduce

# def multi(x,y):
#     return x * y
numeros = [1,2,3]
# total = reduce(multi, numeros)
# print(total)
total = reduce(lambda x,y: x**2 + y**2,numeros)
print(total)
