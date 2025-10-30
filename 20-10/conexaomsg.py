import sys
import socket

args = sys.argv
if len(args) <= 2:
    print('not enough args')
    sys.exit()

ALVO = args[1]
PORTA = int(args[2])

conexao = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 10.3.40.120 - 4444
print(ALVO, PORTA)
conexao.connect((ALVO, PORTA))

while True:
    msg = input('> ')
    conexao.sendall((msg + '\n').encode())
    if(msg.lower() == 'sair'):
        break
    
conexao.close()