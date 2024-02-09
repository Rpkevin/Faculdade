def cachorro_peso():
    while True:
        try:
            peso = float(input("Digite o peso do cachorro em kg: "))

            if peso < 3:
                return 40
            elif peso < 10:
                return 50
            elif peso < 30:
                return 60
            elif peso < 50:
                return 70
            else:
                print("Cachorros acima de 50 kg não é suportado.")
        except ValueError:
            print("Por favor, digite um valor numérico.") 


def cachorro_pelo():
    while True:

        tipo_pelo = input("Digite o tipo de pelo do cachorro Pelo curto (C), Pelo Médio(M), Pelo Longo (L) (c/m/l): ")
        if tipo_pelo == 'c':
            return 1
        elif tipo_pelo == 'm':
            return 1.5
        elif tipo_pelo == 'l':
            return 2
        else:
            print("Opção inválida. Escolha entre 'c', 'm' ou 'l'.")


def cachorro_extra():
    extras = {'1': 10, '2': 12, '3': 15, '0': 0}
    total_extra = 0

    while True:
        try:
            print('Corte de unhas: 10R$(1) | Escovar os dentes: R$12 (2) | Limpeza de orelhas R$15,00 (3) | Não desejo mais mais nada. (0)')
            adicional = input("Deseja Algum serviço adicional? Digite (1/2/3/0): ")

            if adicional in extras:
                total_extra += extras[adicional] 
                if adicional == '0':
                    return total_extra
            else:
                print("Opção inválida. Escolha entre '1', '2', '3' ou '0'.") 
        except ValueError:
            print("Por favor, digite um valor numérico.")


def main():
    try:
        print("Bem-vindo ao PetShop do Kevin G. Porto!") 

        nome = input("Digite seu nome: ")
        print(f"Olá, {nome}!")

        base = cachorro_peso()
        multiplicador = cachorro_pelo()
        total_extra = cachorro_extra()

        total = base * multiplicador + total_extra
        print(f"\nTotal a pagar: R${total:.2f}")

    except ValueError: 
        print("Ops, algo deu errado. Certifique-se de digitar números válidos.")

main()
