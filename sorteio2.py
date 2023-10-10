import random

n1 = str (input('Digite um nome: '))
n2 = str (input('Digite um nome: '))
n3 = str (input('Digite um nome: '))

lista = [n1,n2,n3]

random.shuffle (lista)

print ("A ordem da lista reordenada foi  {} ".format(lista))