def calcula_tabuada(numero):
    cont = 1
    while cont <= 10:
        print(f"{numero} x {cont} = {numero*cont}")
        cont = cont + 1


escolha = int(input("Quer tabuada de qual numero?"))
calcula_tabuada(escolha)
