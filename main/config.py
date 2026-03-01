#Configurações da tela
COLUNAS = 10
LINHAS = 20
TAMANHO_BLOCO = 30
LARGURA = COLUNAS * TAMANHO_BLOCO # 300px
ALTURA =LINHAS * TAMANHO_BLOCO # 600px
TELA_CHEIA = False

#Cores
PRETO = (0, 0, 0)
CINZA = (50, 50, 50)
BRANCO = (255, 255, 255)
VERMELHO = (255, 0, 0)
VERDE = (0, 240, 0)
# Formatos das peças (cada uma tem seus blocos em [linha, coluna])
PECAS = [
    [[0,0], [1,0], [2,0], [3,0]],  # I
    [[0,0], [0,1], [1,0], [1,1]],  # O
    [[0,1], [1,0], [1,1], [1,2]],  # T
    [[0,0], [1,0], [2,0], [2,1]],  # L
    [[0,1], [1,1], [2,0], [2,1]],  # J
    [[0,0], [0,1], [1,1], [1,2]],  # S
    [[0,1], [0,2], [1,0], [1,1]],  # Z
]

# Uma cor para cada peça
CORES = [
    (0, 240, 240),   # I - ciano
    (240, 240, 0),   # O - amarelo
    (160, 0, 240),   # T - roxo
    (240, 160, 0),   # L - laranja
    (0, 0, 240),     # J - azul
    (0, 240, 0),     # S - verde
    (240, 0, 0),     # Z - vermelho
]

