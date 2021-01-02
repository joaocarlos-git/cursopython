#Crie um joguinho de par ou impar, o programa irá perguntar ao primeiro jogador se ele
#quer para ou ímpar e vai pedir um numero, logo pedirá ao segundo
#jogador outro número, fará a soma, utilizando o mesmo mòdulo do exercício anterior,
# e dirá se o resultado é par ou ímpar, exibindo uma mensagem de parabéns ao vencedor daquela partida.

import matematico

continuar = ""

while True:
    continuar = input("\nDeseja jogar par ou impar? S/N ")
    if continuar.lower() != "s" or continuar.lower() == "n":
        print("Digite s para jogar ou n para terminar o jogo")
        break

    else:
        jogador1 = input("\nDigite o nome do jogador: ")
        jogador2 = input("\nDigite o nome do segundo jogador: ")
        par_ou_impar = input(jogador1 + " Digite 1 para impar e 2 para par: ")

        if par_ou_impar != "1" and par_ou_impar != "2":
            print("Você digitou uma opção inválida")
            continue

        else:
            num_jog1 = int(input(jogador1 + " digite um número qualquer: "))
            num_jog2 = int(input(jogador2 + " digite um numero qualquer: "))
            resultado = matematico.par_impar(num_jog1, num_jog2)
            soma = matematico.soma(num_jog1, num_jog2)
            print("\nO " + jogador1 + " escolheu " + str(num_jog1) + " e o " + jogador2 + " escolheu " + str(num_jog2) )
            print("e a soma da " + str(soma) + " que é " + resultado)

            if resultado == "PAR":
                if par_ou_impar == "1":
                    print("\nParabéns " + jogador2 + " você é o vencedor! ")
                else:
                    print("\nParabens " + jogador1 + " você é o vencedor! ")
            else:
                if par_ou_impar == "1":
                    print("\nParabéns " + jogador1 + " você é o vencedor! ")
                else:
                    print("\nParabéns " + jogador2 + " você é o vencedor! ")

print("\nEspero que tenha se divertido, volte mais vezes ")
