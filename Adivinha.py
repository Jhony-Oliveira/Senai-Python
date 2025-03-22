import pygame
import random

# Inicializa o Pygame
pygame.init()

# Configurações da tela
LARGURA = 800
ALTURA = 600
TELA = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Jogo de Adivinhação")

# Cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
VERDE = (0, 255, 0)
VERMELHO = (255, 0, 0)

# Fonte
FONTE = pygame.font.Font(None, 48)

# Variáveis do jogo
numero_secreto = random.randint(0, 10)
tentativas_restantes = 6
palpite = ""
mensagem = "Tente adivinhar o número entre 0 e 10!"
jogando = True

def desenhar_texto(texto, x, y, cor):
    superficie_texto = FONTE.render(texto, True, cor)
    TELA.blit(superficie_texto, (x, y))

# Loop principal do jogo
clock = pygame.time.Clock()
while jogando:
    TELA.fill(BRANCO)

    # Exibe a mensagem e o palpite atual
    desenhar_texto(mensagem, 50, 50, PRETO)
    desenhar_texto(f"Palpite: {palpite}", 50, 150, PRETO)
    desenhar_texto(f"Tentativas restantes: {tentativas_restantes}", 50, 250, PRETO)

    # Verifica eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            jogando = False
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_RETURN:  # Quando o jogador pressiona Enter
                if palpite.isdigit():
                    palpite_int = int(palpite)
                    if palpite_int == numero_secreto:
                        mensagem = "Parabéns! Você acertou!"
                        numero_secreto = random.randint(0, 10)  # Sorteia um novo número
                        tentativas_restantes = 6  # Reseta as tentativas
                    else:
                        mensagem = "ERRRROUUUU"
                        tentativas_restantes -= 1
                        if tentativas_restantes == 0:
                            mensagem = f"Fim de jogo! O número era {numero_secreto}."
                            jogando = False
                    palpite = ""  # Limpa o palpite
                else:
                    mensagem = "Digite um número válido!"
            elif evento.key == pygame.K_BACKSPACE:  # Remove o último caractere
                palpite = palpite[:-1]
            else:
                if evento.unicode.isdigit():  # Aceita apenas números
                    palpite += evento.unicode

    # Atualiza a tela
    pygame.display.flip()
    clock.tick(30)

# Finaliza o Pygame
pygame.quit()