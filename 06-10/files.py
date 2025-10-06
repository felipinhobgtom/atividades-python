log = open('./log.txt', 'a')
user = input('usuario: ')
senha = input('senha: ')

logs = []

if senha == '123456':
    print('bem vindo')
    log.write(f'sucesso - {user} logou\n')
    # logs.append(f'sucesso - {user} logou\n')
else:
    print('houve uma falha na autenticacao')
    log.write(f'erro - {user} nao logou\n')
    # logs.append(f'erro - {user} nao logou\n')

# log.writelines(logs)
log.close()