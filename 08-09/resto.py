dinheiro = int(input("quanto voce quer sacar desgraca\ntemos notas de R$10, R$20, R$50: "))

if dinheiro % 10 != 0:
    print("so multiplo de 10 filhada puta")
else:
    notas = [50, 20, 10]
    cont = 0
    for valor_nota in notas:
        qtd_notas = dinheiro // valor_nota

        if qtd_notas > 0:
            contagem_notas = valor_nota * qtd_notas
            dinheiro -= contagem_notas
            print(f"{qtd_notas} nota(s) de R${valor_nota}")