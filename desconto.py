print('Bem-vindo a loja do Kevin G. Porto') #Cabeçalho!

# entrada para inserir o valor do produto e quantidade
valorProduto = float(input('Digite o valor desejado:'))
quantidadeProduto = int(input('Digite a quantidade desejada:'))
descontoProduto = 0

#desconto c baseado na quantidade
if quantidadeProduto < 200:
    descontoProduto = 0.00
elif 200 <= quantidadeProduto < 1000:
    descontoProduto = 0.05
elif 1000 <= quantidadeProduto < 2000:
    descontoProduto = 0.10
else:
    descontoProduto = 0.15

# calculo do preço total SEM desconto
totalSemDesconto = valorProduto * quantidadeProduto
print('O valor total SEM desconto é de: R$ {:.2f}'.format(totalSemDesconto))

# calculo preço total COM desconto
totalComDesconto = totalSemDesconto - totalSemDesconto * descontoProduto
print('O valor total COM desconto é de R$ {:.2f}'.format(totalComDesconto))
