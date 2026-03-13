# Importa o módulo random para poder gerar números aleatórios.
# `random` é parte da biblioteca padrão do Python e fornece funções
# úteis para gerar valores pseudo-aleatórios.
import random

# Gera um número aleatório entre 1 e 10 (inclusive) e guarda na variável `numero_secreto`.
# Esse é o número que o jogador terá que adivinhar.
numero_secreto = random.randint(1, 10)

# Contador de tentativas já feitas pelo jogador.
tentativas = 0

# Número máximo de tentativas que o jogador terá para acertar.
max_tentativas = 5

# Mensagens de introdução para o jogador.
print("Bem-vindo ao jogo de adivinhação!")
print("Tente adivinhar o número que estou pensando, entre 1 e 10.")

# Loop principal do jogo: continua enquanto o jogador ainda tiver tentativas.
while tentativas < max_tentativas:
    # Solicita um palpite ao usuário e converte o texto digitado para inteiro.
    # (Se o usuário digitar algo que não seja número, o programa levantará um erro.)
    palpite = int(input("Digite seu palpite: "))

    # Conta esta tentativa como usada.
    tentativas += 1

    # Compara o palpite com o número secreto.
    if palpite == numero_secreto:
        # O jogador acertou, encerra o loop usando `break`.
        print(f"Parabéns! Você acertou o número em {tentativas} tentativas.")
        break
    elif palpite < numero_secreto:
        # Palpite muito baixo.
        print("Quase lá! Tente um número maior.")
    else:
        # Palpite muito alto.
        print("Quase lá! Tente um número menor.")

    # Mostra ao jogador quantas tentativas ainda restam.
    if tentativas < max_tentativas:
        print(f"Você tem {max_tentativas - tentativas} tentativas restantes.")

# O bloco `else` do while só é executado se o loop terminar normalmente
# (sem passar pelo `break`), ou seja, quando o jogador usa todas as tentativas.
else:
    print("Infelizmente, você não acertou. O número era", numero_secreto)
    print("Fim do jogo!")
