# coiso = open('./teste.txt', 'a')
# coiso.write("bombardino crocodillo\n")
# coiso.close()

# arquivo = open('./teste.txt', 'r')
# linha = arquivo.readline()
# print(linha.strip())
# arquivo.seek(0)
# print(arquivo.readlines())
# arquivo.close()

lista = ['mario\n', 'dunha\n', 'maria\n', 'tiririca\n']
arquivo = open('nomes.txt', 'w')
arquivo.writelines(lista)

