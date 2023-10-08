# Calculo da area da parede
#Levantamento do rendimento da tinta
# Quantidade de demãos
#Quantidade de paredes a ser pintada
# Fabricante anonimo 10m²/l


larg= float (input('Digite o valor da largura da parede:  '))
alt =float (input ('Digite o valor da altura da parede: '))
paredes = int (input('Digite a quantidade de paredes que serão pintadas: '))

rendimento = 10

area = larg * alt 

print ('O valor da area a ser pintada é de: {:.0f} metros' .format (area))

#rendimento : 1 litro pinta 10m2
# demão = litros necessarios

qdtdemaolitros = area / rendimento

tintaTotal = qdtdemaolitros * paredes

print ( 'A quantidade de demão  por parede é de : {:.1f} litros' .format (qdtdemaolitros))

print ('O numero de paredes a serem  pintadas são : {} x  quantidade de demão {:.1f} litros. Precisamos comprar {} litros de tinta'.format (paredes,qdtdemaolitros, tintaTotal))






