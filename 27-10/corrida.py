import threading as t, time, random


def corrida(carro):
    distancia = 0
    while distancia <= 10:
        distancia += 1
        time.sleep(random.random())
        print(f'{carro} andou a distancia de {distancia}km')

t1 = t.Thread(target=corrida, args=('ferrari',))
t2 = t.Thread(target=corrida, args=('fusca',))

t1.start()
t2.start()