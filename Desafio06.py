# ler Nome e Sobrenome

nome = str(input ('Digite o nome e o seu sobrenome : ')).strip()
separa = nome.split()
separasobrenome = nome.rsplit()
print(separasobrenome)

print ('O seu nome é {} e o seu sobrenome é {}.'.format(separa[0],separasobrenome[2]))
print ('A quantidade de letras que contem seu nome são {} .'
       .format(nome.find(' ')))