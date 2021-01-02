# Crie uma calculadora com quatro operações, div, sub, som, mult, que pergunte ao usuario
#qual operação ele deseja fazer e peça os numeros que serão calculados, em seguida
#mostre o resultado da operação na tela, sendo que as funções utilizadas no programa
#estejam em um módulo separado do arquivo principal.
import matematico

continuar = ""

while True:
    continuar = input("\nDeseja calcular? S/N: ")

    if continuar.lower() == "n" or continuar != "s":
        break
    else:
        try:

            operacao = input("Qual operação deseja fazer? Digite\n1 para soma\n2 para subtraçao"
                             "\n3 para multiplicaçao\n4 para divisão\n")

            if operacao == "1":
                num1 = int(input("Digite um numero: "))
                num2 = int(input("Digite o segundo numero: "))
                print("Seu resultado é: " + str(matematico.soma(num1,num2)))
                print("")

            elif operacao == "2":
                num1 = int(input("Digite um numero: "))
                num2 = int(input("Digite o segundo numero: "))
                print("Seu resultado e: " + str(matematico.sub(num1,num2)))
                print("")

            elif operacao == "3":
                num1 = int(input("Digite um numero: "))
                num2 = int(input("Digite o segundo numero: "))
                print("Seu resultado e: " + str(matematico.mult(num1,num2)))
                print("")

            elif operacao == "4":
                num1 = int(input("Digite um numero: "))
                num2 = int(input("Digite o segundo numero: "))
                print("Seu resultado e: " + str(matematico.div(num1,num2)))
                print("")

            else:
                print("\nVocê digitou uma opção inválida, tente novamente.\n")

        except:
            print("\nOcorreu algum erro, verifique a sua operação, como por exemplo, \nse houve tentativa"
                  " de divisão por zero, pois não é possível dividir por zero. ")


print("\nObrigado por usar a calculadora de João Carlos!")