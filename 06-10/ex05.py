with open('access_log') as access_log:
    # EX05A
    leitura = access_log.readline()
    # print(leitura)

    #EX05B
    lista = []
    lista.append(leitura)
    # print(lista)

    #EX05C
    ip = leitura.split(' ')[0] # usando o espaco como separador de string
    # print(ip)

    #EX05D
    ips = []
    for line in access_log.readlines():
        ip_dois = line.split(' ')[0]
        if not ip_dois in ips:
            ips.append(ip_dois)
    # print(ips)

    ips_dois = {}
    #EX05E
    for linha in access_log.readlines():
        ip_tres = linha.split(' ')[0]
        if ip_tres in ips_dois:
            ips_dois[ip_tres] += 1
        else:
            ips_dois[ip_tres] = 1
    print(ips_dois)