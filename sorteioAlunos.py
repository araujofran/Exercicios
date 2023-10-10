import random

num = random.randint (0,3)


print (num)

if num == 0:
    print ('Fran')
elif num == 1:
    print ('Pedrinho')
elif num == 2:
    print ('Marcos')
else :
    print ('Fábio')

print (8*"*********")

n1= str(input ('Digite o nome do primeiro aluno : '))
n2= str(input ('Digite o nome do segundo aluno: '))
n3= str(input ('Digite o nome do terceiro aluno: '))
n4= str(input ('Digite o nome do quarto aluno: '))

lista = [n1,n2,n3,n4]

escolhido = random.choice (lista)

print ('O nome escolhido foi {}'.format(escolhido))

