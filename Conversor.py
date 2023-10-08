#Converter medidas
# ponto partida metros 
# régua (km,hm,dam,m,dm,cm,mm)

valor = int (input(' Digite o valor medido : '))

print ('O valor medido  foi de {:.0f} metros!'. format(valor))

km = valor/1000
hm = valor / 100
dam = valor /10
dm = valor*10
cm = valor *100
mm = valor *1000

print ('Convertendo fica :\n  {:.0f} kilometros \n {:.0f} hectometros \n {:.0f} decametros \n {:.0f} decimetros \n {:.0f} centimetros \n  {:.0f} milimetros'.format (km,hm,dam,dm,cm,mm))


