"""
Jogo de Adivinhação
Autor: Eduardo José
Descrição:
  - O computador escolhe um número de 1 a 100.
  - O jogador tenta adivinhar.
  - O programa informa se o palpite é maior ou menor
    até que o jogador acerte.
"""


import random

def jogo_adivinhacao():
    print("=== JOGO DE ADIVINHAÇÃO ===")
    print("Digite 'exit' a qualquer momento para sair.")
    numero_secreto = random.randint(1, 100)
    tentativas = 0

    while True:
        entrada = input("Digite seu palpite (1‑100): ")

        if entrada.lower() == "exit":
            print("Você saiu do jogo. Até mais!")
            break

        try:
            chute = int(entrada)
        except ValueError:
            print("Digite um número inteiro válido ou 'exit' para sair.")
            continue

        tentativas += 1

        if chute < numero_secreto:
            print("Seu palpite foi MENOR que o número secreto.")
        elif chute > numero_secreto:
            print("Seu palpite foi MAIOR que o número secreto.")
        else:
            print(f"Parabéns! Você acertou em {tentativas} tentativas.")
            break

if __name__ == "__main__":
    jogo_adivinhacao()
