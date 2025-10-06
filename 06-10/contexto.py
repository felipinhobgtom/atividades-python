with open('log.txt') as cu, open('log.txt', 'a') as cu2:
    linhas = cu.read()
    cu2.write(linhas)
    print(linhas)