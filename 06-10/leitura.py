ler_log = open('log.txt')
# linhas = ler_log.readline()
# print(linhas)
# linhas = ler_log.readline()
# print(linhas)
linhas = ler_log.readline ()
print(linhas)

ler_log.seek(0) # volta o ponteiro
linhas = ler_log.readline()
print(linhas)