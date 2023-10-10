nome = str(input ('Digite seu nome completo : ')).strip()

# Mostrar o nome com todas as letras maiúsculas, minúsculas 

print (nome.upper())
print (nome.lower())

# quantas letras tem ao todo ( sem considerar os espaços)
print("Seu nome tem {} letras ".format(len(nome) - nome.count(' ')))


# quantas letras tem o primeiro nome
print("Seu primeiro nome tem {} letras ".format(nome.find(' ')))
