# Função para calcular o valor base com base no peso do cachorro
def cachorro_peso():
    while True:
        try:
            #pede ao usuário para inserir o peso do cachorro
            peso = float(input("Digite o peso do cachorro em kg: "))
            #Determina o valor c base no peso informado
            if peso < 3:
                return 40
            elif peso < 10:
                return 50
            elif peso < 30:
                return 60
            elif peso < 50:
                return 70
            else:
                print("Cachorros acima de 50 kg não é suportado.")#msg se o peso for acima de 50kg
        except ValueError:
            print("Por favor, digite um valor numérico.") #qnd um valor inválido for inserido


# função p/ calcular o multiplicador c base no tipo de pelo do cachorro.
def cachorro_pelo():
    while True:
        #!pergunta sobre o tipo de pelo do cachorro.
        tipo_pelo = input("Digite o tipo de pelo do cachorro Pelo curto (C), Pelo Médio(M), Pelo Longo (L) (c/m/l): ")
        if tipo_pelo == 'c':
            return 1
        elif tipo_pelo == 'm':
            return 1.5
        elif tipo_pelo == 'l':
            return 2
        else:
            #msg caso escreva uma opção inválida.
            print("Opção inválida. Escolha entre 'c', 'm' ou 'l'.")


# !!!unção para calcular o valor extra com base nos serviços adicionais escolhidos!
def cachorro_extra():
    extras = {'1': 10, '2': 12, '3': 15, '0': 0}
    total_extra = 0

    while True:
        try: #pergunta se deseja um adicional.
            print('Corte de unhas: 10R$(1) | Escovar os dentes: R$12 (2) | Limpeza de orelhas R$15,00 (3) | Não desejo mais mais nada. (0)')
            adicional = input("Deseja Algum serviço adicional? Digite (1/2/3/0): ")

            if adicional in extras:
                total_extra += extras[adicional] #aq adc o valor adicional caso escolhido
                if adicional == '0':
                    return total_extra
            else:
                print("Opção inválida. Escolha entre '1', '2', '3' ou '0'.") #+1 msg caso uma msg escrita for inválida.
        except ValueError:
            print("Por favor, digite um valor numérico.")


# Função principal!
def main():
    try:
        print("Bem-vindo ao PetShop do Kevin G. Porto!") #cabeçalho
        #1 pergunta. Nome do usuario.
        nome = input("Digite seu nome: ")
        print(f"Olá, {nome}!")

        base = cachorro_peso()
        multiplicador = cachorro_pelo()
        total_extra = cachorro_extra()

        #!calculo do valor total q é exibido no final.
        total = base * multiplicador + total_extra
        print(f"\nTotal a pagar: R${total:.2f}")

    except ValueError: #pegar exceções caso entradas sejam inválidas.
        print("Ops, algo deu errado. Certifique-se de digitar números válidos.")

# chamada da função principal sem uma frunção main especifica.
main()
