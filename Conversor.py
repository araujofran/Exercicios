#Converter medidas
# ponto partida metros 
# régua (km,hm,dam,m,dm,cm,mm)

valor = float (input(' Digite o valor medido : '))

print ('O valor medido  foi de {} metros!'. format(valor))

km = valor/1000
hm = valor / 100
dam = valor /10
dm = valor*10
cm = valor *100
mm = valor *1000

print ('Convertendo fica :\n  {:.5f} kilometros \n {:.5f} hectometros \n {:.5f} decametros \n {:.5f} decimetros \n {:.5f} centimetros \n  {:.5f} milimetros'.format (km,hm,dam,dm,cm,mm))


