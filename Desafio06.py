# ler Nome e Sobrenome

n = str(input ('Digite o nome e o seu sobrenome : ')).strip()
nome = n.split()

print ('O seu nome é {} e o seu ultimo nome é {}.'.format(nome[0], nome[len(nome)-1]))
