import random
from colorama import Fore
from os import system, name

class Hangman:
    def __init__(self):
        self.palavras = ["Paradoxo","Quórum","Xilogravura","Zênite","Dáctilo","Efêmero","Frívolo","Gnose","Heresia","Iconoclasta","Jactância","Kafkiano",
        "Lúgubre","Mórbido","Néscio","Óbice","Pusilânime","Quimera","Reticente","Sagaz","Taciturno","Usura","Vexame","Xenofobia","Zombar","Ápice",
        "Bucólico","Conciso","Dúbio","Eloquente","Fútil","Gélido","Híbrido","Ímpeto","Júbilo","Kitsch","Lacônico","Móvel","Nadir","Ócio","Pacato","Querela",
        "Rancor","Sutil","Tacanho","Urbano","Voraz","Xadrez","Zelo","Astuto","Bravata"]
        self.vogais_acentuadas = {'á':'a', 'é':'e', 'í':'i', 'ó':'o', 'ú':'u', 'â':'a', 'ê':'e', 'î':'i', 'ô':'o', 'û':'u', 'ã':'a', 'õ':'o', 'à':'a', 'è':'e', 'ì':'i', 'ò':'o', 'ù':'u'}
        self.estagios = [ # estágio 1 a 10
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
        self.chances = 10
        self.letras_erradas = []
        self.palavra_original = random.choice(self.palavras)
        self.palavra = ''.join([self.vogais_acentuadas[i] if i in self.vogais_acentuadas else i for i in self.palavra_original.lower()])
        self.letras_descobertas = ['_' if letra.isalpha() else letra for letra in self.palavra]

    def limpa_tela(self):
        if name == 'nt':
            _ = system('cls')
        else:
            _ = system('clear')

    def mostrar_forca(self):
        return self.estagios[self.chances]

    def game(self):
        self.limpa_tela()
        print(f"{Fore.RED}ʭʭʭʭʭʭʭʭʭʭʭʭʭʭʭʭʭʭʭʭʭʭʭʭʭʭʭʭʭ")
        print(f"ʭʭʭʭʭʭʭʭʭʭ {Fore.WHITE}HANGMAN{Fore.RED} ʭʭʭʭʭʭʭʭʭʭ")
        print(f"ʭʭʭʭʭʭʭʭʭʭʭʭʭʭʭʭʭʭʭʭʭʭʭʭʭʭʭʭʭ{Fore.WHITE}")
        print("\nBem vindo(a) ao jogo da forca!")
        print(f"Adivinhe a palavra abaixo:\n{Fore.GREEN}")

        while self.chances > 0:
            self.limpa_tela()
            print(f"{Fore.RED}ʭʭʭʭʭʭʭʭʭʭʭʭʭʭʭʭʭʭʭʭʭʭʭʭʭʭʭʭʭ")
            print(f"ʭʭʭʭʭʭʭʭʭʭ {Fore.WHITE}HANGMAN{Fore.RED} ʭʭʭʭʭʭʭʭʭʭ")
            print(f"ʭʭʭʭʭʭʭʭʭʭʭʭʭʭʭʭʭʭʭʭʭʭʭʭʭʭʭʭʭ{Fore.WHITE}")
            print("\nBem vindo(a) ao jogo da forca!")
            print(f"Adivinhe a palavra abaixo:\n{Fore.GREEN}")
            print(self.mostrar_forca())# Print
            print(" ".join(self.letras_descobertas))
            print("\nChances restantes:", self.chances)
            print("Letras erradas:", " ".join(self.letras_erradas))
            
            # Tentativa
            tentativa = input("\nDigite uma letra: ").lower()
            
            # Condicional de verificação de letra repetida
            if tentativa in self.letras_erradas:
                print("Você já tentou essa letra.")
                continue
            
            if tentativa in self.palavra:
                index = 0
                for letra in self.palavra:
                    if tentativa == letra:
                        self.letras_descobertas[index] = self.palavra_original[index]
                    index += 1
            else:
                self.chances -= 1
                self.letras_erradas.append(tentativa)
            
            # Verificação se todas as letras foram descobertas (condicional)
            if "_" not in self.letras_descobertas:
                print("\nParabéns! Você ganhou! A palavra era: ", self.palavra_original)
                break
        
        #  Se as chances acabarem, mostrar mensagem de derrota e sair do loop
        if self.chances == 0:
            print("\nVocê perdeu. A palavra era:", self.palavra_original)

if __name__ == "__main__":
    jogo = Hangman()
    jogo.game()
    print("\nObrigado por jogar! By mafixx\n")