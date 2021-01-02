#Para percorrer a lista de carros do primeiro até o ultimo
#carros = ['ferrari','mustang','BMW','corvet','civic', 'corola']


#for carro in carros:
#    print("Eu quero um carro do modelo " + carro)
#print("Legal, Obrigado")

#Criando uma lista de 1 a 100 na horizontal
#numeros = list(range(1,101,4))
#print(numeros)

#Criando uma lista na vertical
#numeros = list(range(1,101))
#
#for n in numeros:
 #   print(n)

 #Criando uma lista direto no for mas atenção na identação
#for n in range(1,101):
 #   print(n)

 #Outro tipo de lista
#numeros = []
#for n in range(1,101):
 #   numeros.append(n)

#print(numeros)
#Tabuada
#num = int(input("Digite um numero para ver sua tabuada:"))
#print('-' * 12)
#print('{} X {:2} = {}'.format(num, 1, num*1))
#print('{} X {:2} = {}'.format(num, 2, num*2))
#print('{} X {:2} = {}'.format(num, 3 ,num*3))
#print('{} X {:2} = {}'.format(num, 4, num*4))
#print('{} X {:2} = {}'.format(num, 5, num*5))
#print('{} X {:2} = {}'.format(num, 6, num*6))
#print('{} X {:2} + {}'.format(num, 7, num*7))
#print('{} X {:2} = {}'.format(num, 8, num*8))
#print('{} X {:2} = {}'.format(num, 9, num*9))
#print('{} X {:2} = {}'.format(num, 10, num*10))
#print('-' * 12)

#Tabuada usando o For
n = int(input('Digite uma tabuada: '))
for c in range(1,11):
    print('{} X {:2} = {}'.format(n, c, n*c))
print("Fim")
