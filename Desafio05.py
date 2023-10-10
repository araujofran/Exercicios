frase = (input(' Digite uma frase : '))

print (frase)

print("A letra A maiúscula aparece {}  vez(es) na frase ! ".format(frase.count ('A')))
print("A letra a minúscula aparece {}  vez(es) na frase ! ".format(frase.count ('a')))

# em que posição ela aparece a primeira vez 


print ("A letra A maiúscula aparece na posição {}  da frase ! ".format(frase.find('A')))
print ("A letra a minúscula aparece na posição {}  da frase ! ".format(frase.find('a')))

# em que posição ela aparece a ultima vez?

print (frase.find('a',0,10))



