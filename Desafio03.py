cidade = str(input ('Digite o nome de uma cidade: ')).strip()

print (" O nome da cidade {} contém palavra Santo? {} ".format(cidade,('Santo' in cidade))) # existe santo no nome da cidade

cidade.find('Santo') # Santo esta na posição zero?

print ('A cidade começa com a palavra Santo? {}'. format(cidade.find('Santo')==(0)))# Santo esta na posição zero?

# seu primeiro nome tem 

separa = cidade.split()
print(separa)

print ('A primeira palavra da cidade é {} '.format(separa[0]))
print ('A quantidade de letras nessa expressão é {} '. format(cidade.find (' ')))