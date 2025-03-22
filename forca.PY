import pygame
import random

# Inicializa o Pygame
pygame.init()

# Configuração da tela
WIDTH, HEIGHT = 1200, 900
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jogo da Forca")

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (200, 0, 0)
GREEN = (0, 200, 0)
GRAY = (180, 180, 180)
BLUE = (0, 100, 255)

# Fonte
font = pygame.font.Font(None, 36)

# Lista de palavras e dicas
palavras_e_dicas = [
    {"palavra": "PYTHON", "dica": "Linguagem de programação"},
    {"palavra": "JAVA", "dica": "Linguagem de programação orientada a objetos"},
    {"palavra": "GATO", "dica": "Animal doméstico"},
    {"palavra": "ABACAXI", "dica": "Fruta tropical"},
    {"palavra": "SOL", "dica": "Estrela central do sistema solar"},
    {"palavra": "LUA", "dica": "Satélite natural da Terra"},
    {"palavra": "CARRO", "dica": "Meio de transporte"},
    {"palavra": "COMPUTADOR", "dica": "Dispositivo eletrônico"},
    {"palavra": "CELULAR", "dica": "Aparelho de comunicação"},
    {"palavra": "BANANA", "dica": "Fruta amarela"},
    {"palavra": "ELEFANTE", "dica": "Animal de grande porte"},
    {"palavra": "ESCOLA", "dica": "Local de aprendizado"},
    {"palavra": "MONTANHA", "dica": "Formação geográfica"},
    {"palavra": "OCEANO", "dica": "Grande corpo de água"},
    {"palavra": "VIOLÃO", "dica": "Instrumento musical"},
    {"palavra": "CACHORRO", "dica": "Animal de estimação"},
    {"palavra": "BICICLETA", "dica": "Meio de transporte"},
    {"palavra": "AVIÃO", "dica": "Meio de transporte aéreo"},
    {"palavra": "TARTARUGA", "dica": "Animal de casco"},
    {"palavra": "BORBOLETA", "dica": "Inseto colorido"},
    {"palavra": "PYTHON", "dica": "Linguagem de programação"},
    {"palavra": "JAVA", "dica": "Linguagem de programação orientada a objetos"},
    {"palavra": "GATO", "dica": "Animal doméstico"},
    {"palavra": "ABACAXI", "dica": "Fruta tropical"},
    {"palavra": "SOL", "dica": "Estrela central do sistema solar"},
    {"palavra": "LUA", "dica": "Satélite natural da Terra"},
    {"palavra": "CARRO", "dica": "Meio de transporte"},
    {"palavra": "COMPUTADOR", "dica": "Dispositivo eletrônico"},
    {"palavra": "CELULAR", "dica": "Aparelho de comunicação"},
    {"palavra": "BANANA", "dica": "Fruta amarela"},
    {"palavra": "ELEFANTE", "dica": "Animal de grande porte"},
    {"palavra": "ESCOLA", "dica": "Local de aprendizado"},
    {"palavra": "MONTANHA", "dica": "Formação geográfica"},
    {"palavra": "OCEANO", "dica": "Grande corpo de água"},
    {"palavra": "VIOLÃO", "dica": "Instrumento musical"},
    {"palavra": "CACHORRO", "dica": "Animal de estimação"},
    {"palavra": "BICICLETA", "dica": "Meio de transporte"},
    {"palavra": "AVIÃO", "dica": "Meio de transporte aéreo"},
    {"palavra": "TARTARUGA", "dica": "Animal de casco"},
    {"palavra": "BORBOLETA", "dica": "Inseto colorido"},
    {"palavra": "FUTEBOL", "dica": "Esporte com bola"},
    {"palavra": "PRAIA", "dica": "Local de areia e mar"},
    {"palavra": "FLORESTA", "dica": "Área com muitas árvores"},
    {"palavra": "CACHOEIRA", "dica": "Queda d'água"},
    {"palavra": "ARCOIRIS", "dica": "Fenômeno óptico"},
    {"palavra": "ESTRELA", "dica": "Corpo celeste"},
    {"palavra": "PLANETA", "dica": "Corpo que orbita uma estrela"},
    {"palavra": "GALÁXIA", "dica": "Conjunto de estrelas"},
    {"palavra": "ASTRONAUTA", "dica": "Viajante espacial"},
    {"palavra": "FOGUETE", "dica": "Veículo espacial"},
    {"palavra": "SATÉLITE", "dica": "Objeto que orbita um planeta"},
    {"palavra": "TERRA", "dica": "Planeta que habitamos"},
    {"palavra": "MARTE", "dica": "Planeta vermelho"},
    {"palavra": "JÚPITER", "dica": "Maior planeta do sistema solar"},
    {"palavra": "SATURNO", "dica": "Planeta com anéis"},
    {"palavra": "URANO", "dica": "Planeta gelado"},
    {"palavra": "NETUNO", "dica": "Planeta azul"},
    {"palavra": "MERCÚRIO", "dica": "Planeta mais próximo do Sol"},
    {"palavra": "VENUS", "dica": "Planeta mais quente"},
    {"palavra": "LUA", "dica": "Satélite natural da Terra"},
    {"palavra": "COMETA", "dica": "Corpo celeste com cauda"},
    {"palavra": "METEORO", "dica": "Estrela cadente"},
    {"palavra": "ASTEROIDE", "dica": "Corpo rochoso no espaço"},
    {"palavra": "NEBULOSA", "dica": "Nuvem de gás e poeira"},
    {"palavra": "BURACO NEGRO", "dica": "Região do espaço com gravidade extrema"},
    {"palavra": "VIA LÁCTEA", "dica": "Nossa galáxia"},
    {"palavra": "ANDROMEDA", "dica": "Galáxia vizinha"},
    {"palavra": "QUASAR", "dica": "Objeto celeste brilhante"},
    {"palavra": "PULSAR", "dica": "Estrela de nêutrons"},
    {"palavra": "SUPERNOVA", "dica": "Explosão estelar"},
    {"palavra": "BIG BANG", "dica": "Teoria da origem do universo"},
    {"palavra": "UNIVERSO", "dica": "Tudo que existe"},
    {"palavra": "GRAVIDADE", "dica": "Força que atrai corpos"},
    {"palavra": "RELATIVIDADE", "dica": "Teoria de Einstein"},
    {"palavra": "QUÂNTICA", "dica": "Física das partículas"},
    {"palavra": "ÁTOMO", "dica": "Unidade básica da matéria"},
    {"palavra": "MOLÉCULA", "dica": "Conjunto de átomos"},
    {"palavra": "ELÉTRON", "dica": "Partícula subatômica"},
    {"palavra": "PRÓTON", "dica": "Partícula subatômica"},
    {"palavra": "NÊUTRON", "dica": "Partícula subatômica"},
    {"palavra": "ENERGIA", "dica": "Capacidade de realizar trabalho"},
    {"palavra": "MATÉRIA", "dica": "Tudo que ocupa espaço"},
    {"palavra": "FORÇA", "dica": "Interação entre corpos"},
    {"palavra": "VELOCIDADE", "dica": "Rapidez de movimento"},
    {"palavra": "ACELERAÇÃO", "dica": "Variação da velocidade"},
    {"palavra": "INÉRCIA", "dica": "Resistência à mudança de movimento"},
    {"palavra": "MOMENTO", "dica": "Produto da massa pela velocidade"},
    {"palavra": "TRABALHO", "dica": "Força vezes distância"},
    {"palavra": "POTÊNCIA", "dica": "Trabalho por unidade de tempo"},
    {"palavra": "ENERGIA CINÉTICA", "dica": "Energia do movimento"},
    {"palavra": "ENERGIA POTENCIAL", "dica": "Energia armazenada"},
    {"palavra": "CALOR", "dica": "Transferência de energia térmica"},
    {"palavra": "TEMPERATURA", "dica": "Medida de calor"},
    {"palavra": "PRESSAO", "dica": "Força por unidade de área"},
    {"palavra": "VOLUME", "dica": "Espaço ocupado por um corpo"},
    {"palavra": "DENSIDADE", "dica": "Massa por unidade de volume"},
    {"palavra": "MASSA", "dica": "Quantidade de matéria"},
    {"palavra": "PESO", "dica": "Força da gravidade sobre um corpo"},
    {"palavra": "ATRITO", "dica": "Força que se opõe ao movimento"},
    {"palavra": "ELASTICIDADE", "dica": "Propriedade de voltar à forma original"},
    {"palavra": "DILATAÇÃO", "dica": "Aumento de volume com o calor"},
    {"palavra": "CONDUÇÃO", "dica": "Transferência de calor"},
    {"palavra": "CONVECÇÃO", "dica": "Transferência de calor por fluidos"},
    {"palavra": "RADIAÇÃO", "dica": "Transferência de calor por ondas"},
    {"palavra": "ONDAS", "dica": "Perturbação que se propaga"},
    {"palavra": "SONIDO", "dica": "Onda mecânica"},
    {"palavra": "LUZ", "dica": "Onda eletromagnética"},
    {"palavra": "ESPECTRO", "dica": "Distribuição de cores"},
    {"palavra": "REFLEXÃO", "dica": "Mudança de direção da luz"},
    {"palavra": "REFRACÃO", "dica": "Mudança de direção da luz ao mudar de meio"},
    {"palavra": "DIFRAÇÃO", "dica": "Espalhamento de ondas"},
    {"palavra": "INTERFERÊNCIA", "dica": "Sobreposição de ondas"},
    {"palavra": "POLARIZAÇÃO", "dica": "Orientação das ondas"},
    {"palavra": "QUANTUM", "dica": "Quantidade mínima de energia"},
    {"palavra": "ELETROMAGNETISMO", "dica": "Interação entre cargas elétricas"},
    {"palavra": "CORRENTE", "dica": "Fluxo de elétrons"},
    {"palavra": "TENSÃO", "dica": "Diferença de potencial"},
    {"palavra": "RESISTÊNCIA", "dica": "Oposição à passagem de corrente"},
    {"palavra": "CAPACITÂNCIA", "dica": "Capacidade de armazenar carga"},
    {"palavra": "INDUÇÃO", "dica": "Geração de corrente por campo magnético"},
    {"palavra": "CAMPO", "dica": "Região de influência"},
    {"palavra": "FORÇA ELETROMAGNÉTICA", "dica": "Interação entre cargas"},
    {"palavra": "FORÇA NUCLEAR", "dica": "Interação no núcleo atômico"},
    {"palavra": "FORÇA GRAVITACIONAL", "dica": "Interação entre massas"},
    {"palavra": "FORÇA FRACA", "dica": "Interação nuclear"},
    {"palavra": "FORÇA FORTE", "dica": "Interação nuclear"},
    {"palavra": "PARTÍCULA", "dica": "Componente da matéria"},
    {"palavra": "ANTIMATÉRIA", "dica": "Matéria com carga oposta"},
    {"palavra": "BÓSON", "dica": "Partícula de força"},
    {"palavra": "FÉRMION", "dica": "Partícula de matéria"},
    {"palavra": "QUARK", "dica": "Partícula fundamental"},
    {"palavra": "LÉPTON", "dica": "Partícula fundamental"},
    {"palavra": "HÁDROM", "dica": "Partícula composta"},
    {"palavra": "MÉSON", "dica": "Partícula composta"},
    {"palavra": "BÁRION", "dica": "Partícula composta"},
    {"palavra": "GLÚON", "dica": "Partícula de força forte"},
    {"palavra": "FÓTON", "dica": "Partícula de luz"},
    {"palavra": "GRAVITON", "dica": "Partícula hipotética da gravidade"},
    {"palavra": "NEUTRINO", "dica": "Partícula sem carga"},
    {"palavra": "ANTINEUTRINO", "dica": "Antipartícula do neutrino"},
    {"palavra": "MATÉRIA ESCURA", "dica": "Matéria invisível no universo"},
    {"palavra": "ENERGIA ESCURA", "dica": "Energia que acelera a expansão do universo"},
    {"palavra": "COSMOLOGIA", "dica": "Estudo do universo"},
    {"palavra": "ASTROFÍSICA", "dica": "Física aplicada ao espaço"},
    {"palavra": "ASTRONOMIA", "dica": "Ciência que estuda o espaço"},
    {"palavra": "GEOLOGIA", "dica": "Ciência que estuda a Terra"},
    {"palavra": "BIOLOGIA", "dica": "Ciência que estuda a vida"},
    {"palavra": "QUÍMICA", "dica": "Ciência que estuda a matéria"},
    {"palavra": "FÍSICA", "dica": "Ciência que estuda a natureza"},
    {"palavra": "MATEMÁTICA", "dica": "Ciência dos números"},
    {"palavra": "HISTÓRIA", "dica": "Estudo do passado"},
    {"palavra": "GEOGRAFIA", "dica": "Estudo da Terra"},
    {"palavra": "FILOSOFIA", "dica": "Estudo do pensamento"},
    {"palavra": "SOCIOLOGIA", "dica": "Estudo da sociedade"},
    {"palavra": "PSICOLOGIA", "dica": "Estudo da mente"},
    {"palavra": "ECONOMIA", "dica": "Estudo da produção e consumo"},
    {"palavra": "POLÍTICA", "dica": "Estudo do poder"},
    {"palavra": "DIREITO", "dica": "Estudo das leis"},
    {"palavra": "MEDICINA", "dica": "Ciência da saúde"},
    {"palavra": "ENGENHARIA", "dica": "Aplicação da ciência e matemática"},
    {"palavra": "ARQUITETURA", "dica": "Arte de projetar edifícios"},
    {"palavra": "ARTE", "dica": "Expressão criativa"},
    {"palavra": "MÚSICA", "dica": "Arte dos sons"},
    {"palavra": "TEATRO", "dica": "Arte dramática"},
    {"palavra": "CINEMA", "dica": "Arte cinematográfica"},
    {"palavra": "LITERATURA", "dica": "Arte da escrita"},
    {"palavra": "PINTURA", "dica": "Arte de pintar"},
    {"palavra": "ESCULTURA", "dica": "Arte de esculpir"},
    {"palavra": "DANÇA", "dica": "Arte do movimento"},
    {"palavra": "FOTOGRAFIA", "dica": "Arte de capturar imagens"},
    {"palavra": "DESIGN", "dica": "Arte de projetar"},
    {"palavra": "MODA", "dica": "Arte do vestuário"},
    {"palavra": "GASTRONOMIA", "dica": "Arte da culinária"},
    {"palavra": "ESPORTE", "dica": "Atividade física competitiva"},
    {"palavra": "JOGO", "dica": "Atividade lúdica"},
    {"palavra": "BRINCADEIRA", "dica": "Atividade divertida"},
    {"palavra": "DIVERSÃO", "dica": "Atividade prazerosa"},
    {"palavra": "LAZER", "dica": "Tempo livre"},
    {"palavra": "VIAGEM", "dica": "Deslocamento para outro lugar"},
    {"palavra": "TURISMO", "dica": "Atividade de viajar"},
    {"palavra": "HOTEL", "dica": "Local de hospedagem"},
    {"palavra": "RESTAURANTE", "dica": "Local para refeições"},
    {"palavra": "BAR", "dica": "Local para bebidas"},
    {"palavra": "CAFÉ", "dica": "Bebida quente"},
   

]

# Configuração inicial do jogo
game_active = False  # Começa desativado até clicar em "Iniciar"
game_over = False  # Indica se o jogo terminou
palavra_secreta = ""
dica = ""
letras_adivinhadas = []
tentativas = 6
mensagem = ""

# Botões de Iniciar e Reiniciar
btn_start = pygame.Rect(500, 400, 200, 60)
btn_restart = pygame.Rect(500, 500, 200, 60)

# Função para iniciar o jogo
def iniciar_jogo():
    global game_active, game_over, palavra_secreta, dica, letras_adivinhadas, tentativas, mensagem
    game_active = True
    game_over = False
    palavra_info = random.choice(palavras_e_dicas)
    palavra_secreta = palavra_info["palavra"]
    dica = palavra_info["dica"]
    letras_adivinhadas = ["_" for _ in palavra_secreta]
    tentativas = 6
    mensagem = ""

# Função para desenhar a forca
def desenhar_forca():
    if tentativas < 6:
        pygame.draw.line(screen, BLACK, (100, 800), (300, 800), 5)  # Base
    if tentativas < 5:
        pygame.draw.line(screen, BLACK, (200, 800), (200, 400), 5)  # Poste
    if tentativas < 4:
        pygame.draw.line(screen, BLACK, (200, 400), (400, 400), 5)  # Topo
    if tentativas < 3:
        pygame.draw.line(screen, BLACK, (400, 400), (400, 450), 5)  # Corda
    if tentativas < 2:
        pygame.draw.circle(screen, BLACK, (400, 480), 30, 5)  # Cabeça
    if tentativas < 1:
        pygame.draw.line(screen, BLACK, (400, 510), (400, 650), 5)  # Corpo
        pygame.draw.line(screen, BLACK, (400, 550), (350, 500), 5)  # Braço esquerdo
        pygame.draw.line(screen, BLACK, (400, 550), (450, 500), 5)  # Braço direito
        pygame.draw.line(screen, BLACK, (400, 650), (350, 700), 5)  # Perna esquerda
        pygame.draw.line(screen, BLACK, (400, 650), (450, 700), 5)  # Perna direita

# Função para desenhar as letras adivinhadas
def desenhar_palavra():
    palavra_exibida = " ".join(letras_adivinhadas)
    palavra_text = font.render(palavra_exibida, True, BLACK)
    screen.blit(palavra_text, (100, 50))

# Função para desenhar a dica
def desenhar_dica():
    dica_text = font.render(f"Dica: {dica}", True, BLACK)
    screen.blit(dica_text, (100, 100))

# Função para desenhar os botões de letras
def desenhar_botoes_letras():
    letras = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i, letra in enumerate(letras):
        btn_x = 50 + (i % 7) * 100  # Organiza em colunas
        btn_y = 200 + (i // 7) * 60
        btn_rect = pygame.Rect(btn_x, btn_y, 50, 50)
        pygame.draw.rect(screen, GRAY, btn_rect)
        text = font.render(letra, True, BLACK)
        screen.blit(text, (btn_x + 15, btn_y + 10))

# Loop principal
running = True
while running:
    screen.fill(WHITE)
    
    if game_active:
        # Exibir tentativas restantes
        tentativas_text = font.render(f"Tentativas: {tentativas}", True, BLACK)
        screen.blit(tentativas_text, (600, 20))

        # Exibir mensagem
        mensagem_text = font.render(mensagem, True, RED if "ERRRROUUUU" in mensagem else GREEN)
        screen.blit(mensagem_text, (600, 60))

        # Desenhar a forca
        desenhar_forca()

        # Desenhar a palavra oculta
        desenhar_palavra()

        # Desenhar a dica
        desenhar_dica()

        if not game_over:
            # Desenhar botões de letras apenas se o jogo não terminou
            desenhar_botoes_letras()

        # Se o jogador perder, mostrar botão de reiniciar
        if game_over:
            pygame.draw.rect(screen, BLUE, btn_restart)
            restart_text = font.render("Reiniciar", True, WHITE)
            screen.blit(restart_text, (btn_restart.x + 50, btn_restart.y + 15))

    else:
        # Tela inicial com botão de iniciar
        pygame.draw.rect(screen, GREEN, btn_start)
        start_text = font.render("Iniciar", True, WHITE)
        screen.blit(start_text, (btn_start.x + 70, btn_start.y + 15))

    pygame.display.flip()

    # Evento de entrada do jogador
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if not game_active and btn_start.collidepoint(event.pos):
                iniciar_jogo()  # Inicia o jogo ao clicar em "Iniciar"

            if game_active and not game_over:
                # Verifica se clicou em uma letra
                letras = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
                for i, letra in enumerate(letras):
                    btn_x = 50 + (i % 7) * 100
                    btn_y = 200 + (i // 7) * 60
                    btn_rect = pygame.Rect(btn_x, btn_y, 50, 50)
                    if btn_rect.collidepoint(event.pos):
                        if letra in palavra_secreta:
                            for j, char in enumerate(palavra_secreta):
                                if char == letra:
                                    letras_adivinhadas[j] = letra
                            if "_" not in letras_adivinhadas:
                                mensagem = "🎉 Parabéns! Você venceu!"
                                game_over = True
                        else:
                            mensagem = "ERRRROUUUU!"
                            tentativas -= 1
                            if tentativas == 0:
                                mensagem = f"💀 Fim de jogo! A palavra era {palavra_secreta}."
                                game_over = True  # Ativa o estado de game over

            # Se clicou no botão de reiniciar
            if game_over and btn_restart.collidepoint(event.pos):
                iniciar_jogo()

pygame.quit()