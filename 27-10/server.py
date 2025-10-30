import socket

PORT = 4444

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.bind(('10.3.40.21', PORT))
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True), True
    server.listen()

    conexao, endereco = server.accept()
    print(f'conexao fechada: {endereco}')

    while True:
        msg_cliente = conexao.recv(4096)
        print(f'Mensagem recebida: {msg_cliente.decode()}')

        resposta = input('> ').encode()
        conexao.sendall(resposta)