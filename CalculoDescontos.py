preco = float (input(' Digite o preço do produto : R$ '))

d = preco*0.05
valor2= preco-d
valor3= preco*0.95

print ('O preço do produto é R$ {:.2f} o desconto de 5% tira R$ {} e novo valor fica R$ {}'.format (preco,d,valor2))