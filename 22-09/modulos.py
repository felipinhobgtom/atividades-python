import random

aleatorio = random.randint(1, 10)
tentativas = 0
while tentativas < 10:
    tentativa = int(input("tente adivinhar o numero porra\nsua escolha: "))
    if tentativa == aleatorio:
        print("parabens seu merda")
        break
    else:
        print("voce errou seu imbecil")
        if tentativa < aleatorio:
            print("o numero eh maior")
        if tentativa > aleatorio:
            print("o numero eh menor")
        tentativas += 1

if tentativas == 10:
    print(f"perdeu seu {random.choice(["imbecil", "mongol", "jubarte", "burro"])}")