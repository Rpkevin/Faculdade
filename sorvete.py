print('Bem-vindo à Sorveteria do Kevin G. Porto!')
print('-----------------------------------------CARDÁPIO------------------------------------')
print('| Nº DE BOLAS |   SABOR TRADICIONAL (tr) | SABOR PREMIUM (pr) | SABOR ESPECIAL (es) |')
print('|      1      |       R$6,00             |      R$ 7,00       |      R$ 8,00        |')
print('|      2      |       R$10,00            |      R$ 12,00      |      R$ 14,00       |')
print('|      3      |       R$14,00            |      R$ 17,00      |      R$ 20,00       |')
print('------------------------------------------------------------------------------------')
valorTotal = 0

while True:
    sabor =  input('Digite o sabor do sorvete (tr/pr/es): ').lower()
    quantidade = int(input('Digite a quantidade de bolas (1/2/3): '))

    if sabor not in ['tr', 'pr', 'es']:
        print('Sabor de Sorvete Inválido.Tente Novamente')
        continue

    if quantidade not in [1, 2, 3]:
        print('Quantidade de Bolas de Sorvete Inválida.Tente Novamente')
        continue

    if sabor == 'tr':
        if quantidade == 1:
            preco = 6
        elif quantidade == 2:
            preco = 10
        else:
            preco = 14

    elif sabor == 'pr':
        if quantidade == 1:
            preco = 7
        elif quantidade == 2:
            preco = 12
        else:
            preco = 17

    else:
        if quantidade == 1:
            preco = 8
        elif quantidade == 2:
            preco = 14
        else:
            preco = 20

    valorTotal += preco

    mais_pedidos = input('Deseja pedir mais alguma coisa? (s/n): ')
    if mais_pedidos.lower() != 's':
        break

print(f'Valor total: R$ {valorTotal:.2f}')