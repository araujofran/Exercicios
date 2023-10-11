frase = str(input(' Digite uma frase : ')).strip().upper()

print (frase)

print("A letra A  aparece {}  vez(es) na frase ! ".format(frase.count ('A')))

# em que posição ela aparece a primeira vez 

print ("A letra A aparece pela primeira vez na posição {}  da frase ! ".format(frase.find('A')+1))

# em que posição ela aparece a ultima vez?

print ("A letra A aparece pela ultima vez na posição {}  da frase ! ".format(frase.rfind('A')+1))



