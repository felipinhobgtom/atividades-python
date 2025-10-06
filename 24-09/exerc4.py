def verifica(lista, num):
    if num in lista:
        lista.remove(num)
        return lista
    else:
        return False


lista = [1, 2, 3]
print(verifica(lista, 2))
