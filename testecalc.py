def menu():
    print("Selecione a operação:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Sair")

def calculadora():
    while True:
        menu()
        escolha = input("Digite sua escolha (1/2/3/4/5): ")

        if escolha == '5':
            print("Encerrando a calculadora. Até mais!")
            break

        if escolha in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))
            except ValueError:
                print("Entrada inválida! Por favor, insira números válidos.")
                continue

            if escolha == '1':
                print(f"Resultado: {num1} + {num2} = {num1 + num2}")
            elif escolha == '2':
                print(f"Resultado: {num1} - {num2} = {num1 - num2}")
            elif escolha == '3':
                print(f"Resultado: {num1} * {num2} = {num1 * num2}")
            elif escolha == '4':
                if num2 != 0:
                    print(f"Resultado: {num1} / {num2} = {num1 / num2}")
                else:
                    print("Erro: Divisão por zero não é permitida.")
        else:
            print("Opção inválida! Tente novamente.")

# Executar a calculadora
if __name__ == "__main__":
    calculadora()
