alien_0 = {'cor': 'verde', 'pontuacao': 5}

print(alien_0['cor'])

#trocando a cor do alien
alien_0['cor'] = 'azul'

print(alien_0['cor'])
print(alien_0['pontuacao'])

#trocando a pontuacao do alien

alien_0['pontuacao'] = 4

print("O alien agora tem " + str(alien_0['pontuacao']) + " pontos.")

print(alien_0)

#criando outro atributo dentro de alien_0

alien_0['posicao_x'] = 0
alien_0['posicao_y'] = 25

print(alien_0)