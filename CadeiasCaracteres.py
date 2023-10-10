import random

frase = (       'Curso em Video Python'    )
print (frase[:13])


print(len(frase))
print (frase.count('o'))
print (frase.count('o',0,13))
print (frase.find('Vid'))

print ('Curso' in frase)
print (frase.replace('Curso', 'Abracadabra'))
print (frase.title())
print (frase.upper())
print (frase.lower())
print (frase.capitalize())
print(frase.strip())
print(frase.rstrip())

print(frase.split())
print ('-'.join(frase))

lista = frase.split()
random.shuffle (lista)
print (lista)
