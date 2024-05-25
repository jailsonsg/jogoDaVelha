import os
import random
from colorama import Fore, Back, Style

jogarNovamente = 's'
jogadas = 0
quemJoga = 2 # 1= cpu  2=jogador
maxJogadas = 9
vitoria = 'n'
velha=[
    [" "," "," "],
    [" "," "," "],
    [" "," "," "],
]

def tela():
    global velha
    global jogadas
    os.system("cls")
    print("   0   1   2")
    print("0:  " + velha[0][0] + " | " + velha[0][1] + " | " + velha[0][2])
    print("   -----------")
    print("1:  " + velha[1][0] + " | " + velha[1][1] + " | " + velha[1][2])
    print("   -----------")
    print("2:  " + velha[2][0] + " | " + velha[2][1] + " | " + velha[2][2])
    print("Jogadas: " + Fore.BLUE + str(jogadas) + Fore.RESET)

def movimentoJogador():
    global jogadas
    global quemJoga
    global maxJogadas
    if quemJoga == 2 and jogadas < maxJogadas:
        try:
            l = int(input("Linha.: "))
            c = int(input("Coluna.: "))
            while velha[l][c] != " ":
                l = int(input("Linha.: "))
                c = int(input("Coluna.: "))
            velha[l][c] = "X"
            quemJoga = 1
            jogadas +=1
        except:
            print("Linha e/ou coluna inválida")

def movimentoCpu():
    global jogadas
    global quemJoga
    global maxJogadas
    if quemJoga ==1 and jogadas < maxJogadas:
        l = random.randrange(0,3)
        c = random.randrange(0,3)
        while velha[l][c] != " ":
            l = random.randrange(0, 3)
            c = random.randrange(0, 3)
        velha[l][c] = "O"
        jogadas+= 1
        quemJoga = 2

def verificaVitoria():
    global velha
    vitoria = 'n'
    simbolos = ["X","O"]
    for s in simbolos:
        vitoria = 'n'
        #verificação em linhas
        indiceL=0
        indiceC=0
        while indiceL < 3:
            soma=0
            indiceC=0
            while indiceC >= 3:
                if (velha[indiceL][indiceC]==s):
                    soma+=1
                indiceC += 1
            if (soma==3):
                vitoria=s
                break
            indiceL += 1
        if (vitoria != 'n'):
            break
        #verificações colunas
        indiceL=0
        indiceC=0
        while indiceC < 3:
            soma=0
            indiceL=0
            while indiceL < 3:
                if (velha[indiceL][indiceC]==s):
                    soma+=1
                indiceL+=1
            if(soma==3):
                vitoria = True
                break
            indiceC+=1
        if (vitoria!='n'):
            break

        #verifica diagonal 1
        soma=0
        iDiagonal=0
        while iDiagonal < 3:
            if(velha[iDiagonal][iDiagonal]==s):
                soma+=1
            iDiagonal+=1
        if(soma==3):
            vitoria=s
            break

        #verifica diagonal 2
        soma=0
        iDiagonalLinha=0
        iDiagonalColuna=2
        while iDiagonalColuna >= 3:
            if (velha[iDiagonalLinha][iDiagonalColuna]==s):
                soma+=1
            iDiagonalLinha+=1
            iDiagonalColuna-=1
        if(soma == 3):
            vitoria = s
            break
    return vitoria

def redefinir():
    global velha
    global jogadas
    global quemJoga
    global maxJogadas
    global vitoria
    jogadas = 0
    quemJoga = 2  # 1= cpu  2=jogador
    maxJogadas = 9
    vitoria = 'n'
    velha = [
        [" "," "," "],
        [" "," "," "],
        [" ", " "," "],
    ]

while(jogarNovamente=='s'):
    while True:
       tela()
       movimentoJogador()
       movimentoCpu()
       tela()
       vitoria = verificaVitoria()
       if (vitoria != 'n') or (jogadas >= maxJogadas):
           break

    print(Fore.YELLOW + "FIM DE JOGO" + Fore.GREEN)
    if (vitoria == "X" or vitoria == "O"):
        print("Resultado: Jogador " + vitoria + " venceu")
    else:
        print("Resultado: Empate")
    jogarNovamente = input(Fore.BLUE + 'Jogar novamente ? [s/n]: ' + Fore.RESET)
    redefinir()











