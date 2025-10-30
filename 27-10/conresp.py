import socket as s, sys

if len(sys.argv ) < 2:
    print("ERRO! Uso incorreto\nUso: python rede.py <destino> <porta>")
    sys.exit(1)

ALVO = sys.argv[1]
PORTA = int(sys.argv[2])

try:
    con = s.socket(s.AF_INET,s.SOCK_STREAM)
    s.setdefaulttimeout(0.5)
    con.connect((ALVO,PORTA))

    while True:
        msg = input("> ")
        if msg.lower() == 'sair':
            break
        #encode() para bytes
        con.sendall((msg + '\n').encode())    
        
        #recuperando a mensagem enviada
        resp = con.recv(4096)
        if resp:
            print("Resp:", resp.decode(errors="ignore").rstrip(), flush=True)

    con.close()
except Exception as e:
    print(e)