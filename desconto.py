print('Bem-vindo a loja do Kevin G. Porto')

valorProduto = float(input('Digite o valor desejado:'))
quantidadeProduto = int(input('Digite a quantidade desejada:'))
descontoProduto = 0

if quantidadeProduto < 200:
    descontoProduto = 0.00
elif 200 <= quantidadeProduto < 1000:
    descontoProduto = 0.05
elif 1000 <= quantidadeProduto < 2000:
    descontoProduto = 0.10
else:
    descontoProduto = 0.15

totalSemDesconto = valorProduto * quantidadeProduto
print('O valor total SEM desconto é de: R$ {:.2f}'.format(totalSemDesconto))

totalComDesconto = totalSemDesconto - totalSemDesconto * descontoProduto
print('O valor total COM desconto é de R$ {:.2f}'.format(totalComDesconto))
