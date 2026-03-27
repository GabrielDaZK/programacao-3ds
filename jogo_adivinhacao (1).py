import random

# Exibe o menu de dificuldade e solicita ao usuário que escolha um nível.
print("Bem-vindo ao jogo de adivinhação!")
print("\nEscolha o nível de dificuldade:")
print("1. Fácil (números de 1 a 10)")
print("2. Médio (números de 1 a 50)")
print("3. Difícil (números de 1 a 100)")

# Solicita a escolha do jogador.
escolha = input("\nDigite 1, 2 ou 3 para escolher o nível: ")

# Define os parâmetros do jogo baseado na dificuldade escolhida.
if escolha == "1":
    nivel = "Fácil"
    limite_maximo = 10
    max_tentativas = 7
elif escolha == "2":
    nivel = "Médio"
    limite_maximo = 50
    max_tentativas = 8
elif escolha == "3":
    nivel = "Difícil"
    limite_maximo = 100
    max_tentativas = 10
else:
    # Se a escolha for inválida, define o nível médio como padrão.
    print("Escolha inválida! Modo Médio selecionado por padrão.")
    nivel = "Médio"
    limite_maximo = 50
    max_tentativas = 8

# Gera o número secreto baseado no limite máximo do nível escolhido.
# random.randint(a, b) retorna um número aleatório entre a e b (inclusive).
numero_secreto = random.randint(1, limite_maximo)

# Inicializa o contador de tentativas.
tentativas = 0

# Mensagens de introdução personalizadas.
print(f"\n--- Nível: {nivel} ---")
print(f"Tente adivinhar o número que estou pensando, entre 1 e {limite_maximo}.")
print(f"Você tem {max_tentativas} tentativas para acertar.\n")

# Loop principal do jogo.
while tentativas < max_tentativas:
    # Solicita um palpite ao usuário.
    try:
        palpite = int(input("Digite seu palpite: "))
        
        # Valida se o palpite está dentro do intervalo.
        if palpite < 1 or palpite > limite_maximo:
            print(f"Por favor, digite um número entre 1 e {limite_maximo}!")
            continue
    
    except ValueError:
        # Captura erros de entrada (não é um número).
        print("Erro! Digite um número válido.")
        continue
    
    # Conta esta tentativa como usada.
    tentativas += 1
    
    # Compara o palpite com o número secreto.
    if palpite == numero_secreto:
        # O jogador acertou!
        print(f"\n🎉 Parabéns! Você acertou o número {numero_secreto} em {tentativas} tentativa(s)!")
        print(f"Você jogou no nível {nivel}. Excelente trabalho!")
        break
    elif palpite < numero_secreto:
        # Palpite muito baixo.
        print(f"❌ Errado! O número é maior que {palpite}.")
    else:
        # Palpite muito alto.
        print(f"❌ Errado! O número é menor que {palpite}.")
    
    # Mostra quantas tentativas ainda restam.
    tentativas_restantes = max_tentativas - tentativas
    if tentativas_restantes > 0:
        print(f"Você tem {tentativas_restantes} tentativa(s) restante(s).\n")

# Se o loop terminar normalmente (sem acertar), mostra mensagem de derrota.
else:
    print(f"\n💀 Fim do jogo! O número secreto era {numero_secreto}.")
    print(f"Você não conseguiu adivinhar no nível {nivel}. Tente novamente!")
