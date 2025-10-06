log = open('./log.txt', 'a')
user = input('usuario: ')
senha = input('senha: ')

if senha == '123456':
    print('bem vindo')
    log.write(f'sucesso - {user} logou\n')
else:
    print('houve uma falha na autenticacao')
    log.write(f'erro - {user} nao logou\n')

log.close()