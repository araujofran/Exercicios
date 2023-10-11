cidade = str(input ('Digite o nome de uma cidade: ')).strip()

print ('A cidade contem SANTO no inicio?')
print (cidade[:5].upper()== 'SANTO')


print (" O nome da cidade {} contém palavra Santo? {} ".format(cidade,('SANTO' in cidade.upper()))) # existe santo no nome da cidade

cidade.find('SANTO') # Santo esta na posição zero?

cidade = cidade.upper()

print ('A cidade começa com a palavra Santo? {}'. format(cidade.find('SANTO')==(0)))# Santo esta na posição zero?

# seu primeiro nome tem 

separa = cidade.split()
print(separa)

print ('A primeira palavra da cidade é {} '.format(separa[0]))
print ('A quantidade de letras nessa expressão é {} '. format(cidade.find (' ')))