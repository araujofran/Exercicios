nome = (input ('Digite um  nome : '))

nome = nome.upper()

print (" O nome {} contem a palavra Silva?".format(nome))
print ('SILVA' in nome)

print (" O nome {} contem a palavra Silva?{}".format(nome,'SILVA' in nome))
