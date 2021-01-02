# Crie um dicionário, você irá inserir palavras e significados para estas palavras,
# ao executar o programa, o ususario será perguntado qual palavra ele quer saber o
# significado. Caso a palavra esteja no dicionário, ele apresentará o significado desta
# palavra na tela, caso não esteja, ele irá exibiruma mensagem, dizendo que não possui
# a palavra em seu dicionário.

dicio = {}

dicio["violao"] = "\nVIOLÂO\nsubstantivo masculino\n1.\nMÚSICA\n" \
                "instrumento de coradas dedilháveis, com caixa de ressonancia em\n" \
                "formato semelhante a um oito, com seis coradas, de diferentes materiais." \
                "POR METONÍMIA*MŚICA\nm.q. VIOLONISTA (SUBST.).\n3.\nPOR ANALOGIA\n" \
                "(da acp. 1) b infrm.mulher de formas arredondadas, ancas largas e cintura fina"

dicio["tecnologia"] = "\nTECNOLOGIA\nsubstantivo feminino\n1.\nteoria" \
                    "geral e/ou estudo sistematico sobre técnicas, " \
                    "processos, métodos, meios e \ninstrumentos de um" \
                    "ou mais ofícios ou dominios da atividade humana\n" \
                    "(p.ex., industria, ciência etc.).\n2.\nPOR METONÍMIA\n" \
                    "tecnica ou conjunto de tecnicas de um dominio particular. \n" \
                    "a t. nutricional\n3.\nPOR EXTENSÃO\nqualquer técnica moderna e complexa"

continuar = ""

while True:
    continuar = input("\nDeseja saber o significado de alguma palavra? S/N: ")
    if continuar.lower() == "n":
        break
    else:
        palavra = input("Digite uma palavra: ")
        if palavra.lower() in dicio:
            print(dicio[palavra.lower()])
        else:
            print("\nA palavra " + palavra + " não existe em nosso banco de dados, tente novamente.\n")

print("\nObrigado por ter utilizado o dicionário do João Carlos!\n")

