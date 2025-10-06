# def encontrar_maior(lista):
#     maior = 0
#     for numero in lista:
#         if numero > maior:
#             maior = numero
#     return maior

# lista = [1,2,3,4,5,16,7,8]
# maior = encontrar_maior(lista)
# print(maior)

def encontrar_maior(lista):
    return max(lista)

def encontrar_minimo(lista):
    return min(lista)

lista = [1,2,3,4,5,6]

maior = encontrar_maior(lista)
menor = encontrar_minimo(lista)
soma = sum(lista)

print(maior)
print(menor)
print(soma)