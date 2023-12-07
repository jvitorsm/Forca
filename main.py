import random
from Lista_de_palavras import lista_de_palavras

def vitoria():
    print("PARABÉNS!!!")
    reinício = input('Tentar novamente(s/n): ')
    if(reinício == 's'):
        jogar()

def jogar():
    print("+++++++++++++++++++++++++++++++++")
    print("+++Bem vindo ao jogo da Forca!+++")
    print("+++++++++++++++++++++++++++++++++")
    
    

    palavra = random.choice(lista_de_palavras).lower()
    letras_corretas = '_'*len(palavra)
    letras_corretas = list(letras_corretas)
    print(letras_corretas)

    perdeu = False
    ganhou = False
    erros = 0

    while(not perdeu and not ganhou ):
        
        tentativa = input('Escolha uma letra: ').strip().lower()

        if(tentativa == palavra):
            vitoria()
        if (tentativa in palavra):
            index = 0
            for letra in palavra:
                if (tentativa == letra):
                    letras_corretas[index] = letra
                index += 1
        else:
            erros +=1
            print('ERRROOOOU!!! Tente novamente.''\n''{} tentativas restantes...'.format(6-erros))
        ganhou = '_' not in letras_corretas
        perdeu = erros == 6
        
        print(letras_corretas)
    
    if (ganhou):
        print("PARABÉNS!!!")
        reinício = input('Tentar novamente(s/n): ')
        if(reinício == 's'):
            jogar()
    if (perdeu):
        print('VOCÊ PERDEU!!! A palara certa éra: {}'.format(palavra.upper()))
        reinício = input('Tentar novamente(s/n): ')
        if(reinício == 's'):
            jogar()
    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()
