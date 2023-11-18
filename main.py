import random

def vitoria():
    print("PARABÉNS!!!")
    reinício = input('Tentar novamente(s/n): ')
    if(reinício == 's'):
        jogar()

def jogar():
    print("+++++++++++++++++++++++++++++++++")
    print("+++Bem vindo ao jogo da Forca!+++")
    print("+++++++++++++++++++++++++++++++++")
    
    lista_de_palavras = [
        "Abacaxi", "Borboleta", "Cachorro", "Diversidade", "Elefante",
        "Futebol", "Girassol", "Harmonia", "Inovação", "Jardim",
        "Ketchup", "Laranja", "Melodia", "Notável", "Ondulado",
        "Pintura", "Quimera", "Radiante", "Sombra", "Travesseiro",
        "Utopia", "Vinho", "Xadrez", "Zoológico","Verve"
        "Aventura", "Bambu", "Cachecol", "Diamante", "Elegância",
        "Fantasia", "Gargalhada", "Hortelã", "Ímpeto", "Jubiloso",
        "Límpido", "Mágico", "Nostalgia", "Orquídea", "Piquenique",
        "Quasar", "Rústico", "Sincero", "Tremor", "Uva","Vortex",
        "Aquarela", "Brilhante", "Céu", "Delicioso", "Estrela",
        "Frio", "Granizo", "Holograma", "Incrível", "Janela",
        "Kung Fu", "Luar", "Maravilha", "Nebulosa", "Oceano",
        "Perfume", "Querubim", "Riso", "Sabedoria", "Templo",
        "Universo", "Voo", "Wok", "Xícara", "Yacht",
        "Zumbido", "Afável", "Beleza", "Cachoeira", "Desejo",
        "Euforia", "Fulgor", "Gratidão", "Harmonia", "Inspiração",
        "Júbilo", "Luminoso", "Místico", "Oásis", "Pétala",
        "Querência", "Ressurreição", "Solene", "Transcendental", "Utopia"]

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
