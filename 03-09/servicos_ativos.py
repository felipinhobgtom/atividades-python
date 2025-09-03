servicos = []
servicos.append("http")
servicos.append("ssh")
servicos.remove("http")
servicos[-1] = "SFTP"

print(servicos)
