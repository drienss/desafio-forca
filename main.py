import random
import time

palavras = ["GATO", "LUNAR", "ANEL", "CANJICA", "PEDRINHA", "POLVO", "JORNADA", "ADVOGADO", "GELADEIRA", "CANETA"]

escolha = palavras[random.randint(0, 9)]
tamanho = len(escolha)
descobre = ["_"] * tamanho
tentativas = tamanho + 5
tentados = tentativas
acertos = 0
ganha = 0
existe = 0


for i in range(0, tentativas):

    print(f"Tentativas restantes: {tentados}")
    tentados -= 1
    erro = 0
    existe = 0
    print(*descobre)
    letra = input("Digite uma letra: ").capitalize()
    for j in range(0, tamanho):
        if letra == escolha[j]:
            descobre[j] = escolha[j]
            acertos += 1
            existe += 1
        elif len(letra) > 1:
            erro = 1
    if erro == 1:
        print("digite apenas uma letra")
    if existe < 1 and erro == 0:
        print("Essa letra não existe")
        time.sleep(1)
    if acertos == tamanho:
        ganha = 1
        break

if ganha == 1:
    print("Você Ganhou!")
    print(f"A palavra era: {escolha}")
else:
    print("Você Perdeu! ")
