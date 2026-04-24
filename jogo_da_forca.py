import random

# Lista de palavras possíveis
palavras = ["girafa", "elefante", "computador", "cachorro", "abacaxi"]

# Escolhe uma palavra aleatória
palavra_secreta = random.choice(palavras).lower()

# Inicializa variáveis
letras_acertadas = ["_"] * len(palavra_secreta)
tentativas = 6
letras_tentadas = set()

# Desenhos da forca (6 partes: cabeça, tronco, braço esq, braço dir, perna esq, perna dir)
forca = [
    """
     ------
     |    |
     |
     |
     |
     |
    _|_
    """,
    """
     ------
     |    |
     |    O
     |
     |
     |
    _|_
    """,
    """
     ------
     |    |
     |    O
     |    |
     |
     |
    _|_
    """,
    """
     ------
     |    |
     |    O
     |   /|
     |
     |
    _|_
    """,
    """
     ------
     |    |
     |    O
     |   /|\\
     |
     |
    _|_
    """,
    """
     ------
     |    |
     |    O
     |   /|\\
     |   /
     |
    _|_
    """,
    """
     ------
     |    |
     |    O
     |   /|\\
     |   / \\
     |
    _|_
    """
]

print("Bem-vindo ao jogo da Forca!")

while tentativas > 0 and "_" in letras_acertadas:
    print(forca[6 - tentativas])  # Mostra o desenho atual
    print("Palavra:", " ".join(letras_acertadas).upper())  # Usa upper()
    print("Letras já tentadas:", " ".join(sorted(letras_tentadas)).upper())

    palpite = input("Digite uma letra: ").lower().strip()

    # Usa count() para verificar se a letra aparece na palavra
    if palavra_secreta.count(palpite) > 0:
        for i, letra in enumerate(palavra_secreta):
            if letra == palpite:
                letras_acertadas[i] = letra
        print("Boa! Você acertou uma letra.")
    else:
        if palpite in letras_tentadas:
            print("Você já tentou essa letra antes.")
        else:
            tentativas -= 1
            print(f"Você errou! Restam {tentativas} tentativas.")
    letras_tentadas.add(palpite)

if "_" not in letras_acertadas:
    print("Parabéns, você ganhou! A palavra era:", palavra_secreta.upper())
else:
    print(forca[6])  # Mostra desenho final
    print("Que pena, você perdeu. A palavra era:", palavra_secreta.upper())
