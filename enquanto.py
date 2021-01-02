nome = input("diga seu nome :")
idade = input("Agora diga sua idade: ")
soma_idade = int(idade) + 2

print(nome + " tem " + str(idade) + " anos. Em 2 anos ele fará " + str(soma_idade))

print('-'* 80)

escreva = ''

while escreva != 'sair':

    print("Caso queira encerrar o programa, digite sair\n")
    escreva = input("Escreva algo: ")
    print(escreva)
    print("")

    print('-' * 80)

while True:
    print("Para encerrar digite sair: \n")
    cidade = input("Digite uma cidade: ")
    print("")

    if cidade == 'continuar':
        continue

    elif cidade == 'sair':
        break
    else:
        print("A cidade digitada foi " + cidade)

print('\nEstou fora do laço e encerrando')

