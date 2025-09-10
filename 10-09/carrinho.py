import os
import time

carrinho = []

while True:
    os.system("clear")
    option = input(
        "o que ce quer disgraca\n1 - adicionar item\n2 - mostrar carrinho")

    if option == "1":
        item = input("o que ce quer colocar no carrinho disgraca")
        carrinho.append(item)
        os.system("clear")
    if option == "2":
        os.system("clear")
        print(carrinho)
        time.sleep(3)
    if option == "exit":
        break
