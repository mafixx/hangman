# Jogo da Forca por mafixx

# Importações
import random
from os import system, name

# Função para limpar a tela a cada execução, independente do sistema operacional utilizado pelo usuário.
def limpa_tela():
    
    # Windows
    if name == 'nt':
        _ = system('cls')
    
    # Mac ou Linux
    else:
        _ = system('clear')
        
# Desenhando a "forca" na tela
def mostrar_forca(chances):
    estagios = [ # estágio 1 a 10
        """
           -----
           |   |
          [O]  |
          /|\\  |
         _/ \\_ |
               |
        """,
        """
           -----
           |   |
          [O]  |
          /|\\  |
         _/ \\  |
               |
        """,
        """
           -----
           |   |
          [O]  |
          /|\\  |
          / \\  |
               |
        """,
        """
           -----
           |   |
          [O   |
          /|\\  |
          / \\  |
               |
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          /    |
               |
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
               |
               |
        """,
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
        """,
        """
           -----
           |   |
           O   |
           |   |
               |
               |
        """,
        """
           -----
           |   |
           O   |
               |
               |
               |
        """,
        """
           -----
           |   |
               |
               |
               |
               |
        """
    ]
    return estagios[chances]

# Função
def game():
    limpa_tela()
    print("\nBem vindo(a) ao jogo da forca!")
    print("Adivinhe a palavra abaixo:\n")
    
    # Lista das palavras
    palavras = ["Paradoxo","Quórum","Xilogravura","Zênite","Dáctilo","Efêmero","Frívolo","Gnose","Heresia","Iconoclasta","Jactância","Kafkiano",
    "Lúgubre","Mórbido","Néscio","Óbice","Pusilânime","Quimera","Reticente","Sagaz","Taciturno","Usura","Vexame","Xenofobia","Zombar","Ápice",
    "Bucólico","Conciso","Dúbio","Eloquente","Fútil","Gélido","Híbrido","Ímpeto","Júbilo","Kitsch","Lacônico","Móvel","Nadir","Ócio","Pacato","Querela",
    "Rancor","Sutil","Tacanho","Urbano","Voraz","Xadrez","Zelo","Astuto","Bravata"]

    # Escolhe aleatóriamente uma palavra
    palavra_original = random.choice(palavras)
    
    # Mapeamento de vogais acentuadas para não acentuadas
    vogais_acentuadas = {'á':'a', 'é':'e', 'í':'i',
                         'ó':'o', 'ú':'u', 'â':'a', 
                         'ê':'e', 'î':'i', 'ô':'o', 
                         'û':'u', 'ã':'a', 'õ':'o', 
                         'à':'a', 'è':'e', 'ì':'i', 'ò':'o', 'ù':'u'}
    
    # Substitui as vogais acentuadas na palavra escolhida
    palavra = ''.join([vogais_acentuadas[i] if i in vogais_acentuadas else i for i in palavra_original.lower()])
    
    # List Comprehension
    letras_descobertas = ['_' if letra.isalpha() else letra for letra in palavra]

    # Número de chances
    chances = 10

    # Lista para as letras erradas
    letras_erradas = []

    # Loop enquanto o número de chances for maior que zero
    while chances > 0:
        
        print(mostrar_forca(chances))# Print
        print(" ".join(letras_descobertas))
        print("\nChances restantes:", chances)
        print("Letras erradas:", " ".join(letras_erradas))
        
        # Tentativa
        tentativa = input("\nDigite uma letra: ").lower()
        
        # Condicional de verificação de letra repetida
        if tentativa in letras_erradas:
            print("Você já tentou essa letra. Escolha outra.")
            continue
        
        # Condicional
        if tentativa in palavra:
            index = 0
            for letra in palavra:
                if tentativa == letra:
                    letras_descobertas[index] = palavra_original[index]
                index+=1
        else:
            chances -= 1
            letras_erradas.append(tentativa)
            
        # Verificação se todas as letras foram descobertas (condicional)
        if "_" not in letras_descobertas:
            print("\nParabéns! Você ganhou! A  palavra era: ", palavra_original)
            break
    
    #  Se as chances acabarem, mostrar mensagem de derrota e sair do loop
    if chances == 0:
        print("\nVocê perdeu. A palavra era:", palavra_original)

# Bloco main
if __name__ == "__main__":
    game()
    print("\nPrograma elaborado por mafixx.")