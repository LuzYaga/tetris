import sys

import pygame

from funcoes import *
import funcoes
#Inicializa jogo
pygame.init()

#Muda o ícone do jogo
icone = pygame.image.load("../assets/tetris.png")
pygame.display.set_icon(icone)

#Adiciona a música ao jogo
pygame.mixer.init()
pygame.mixer.music.load("../assets/tetrisTheme.mp3")
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play(-1)

#Cria a janela
tela = pygame.display.set_mode((LARGURA,ALTURA))
tela_cheia = False
LARGURA_TELA = LARGURA
ALTURA_TELA = ALTURA

# Calcula o offset para centralizar o tabuleiro
offset_x = 0
offset_y = 0
pygame.display.set_caption("Tetris")

#Controlar a velocidade
relogio = pygame.time.Clock()
fonte = pygame.font.SysFont("comicsansms", 24)

#Cria a primeira peça

peca_atual = nova_peca()

#Controle do tempo de queda
tempo_queda = 0
velocidade_queda = 500 # milissegundos

tempo_baixo = 0 # para quando segurar a tecla de abaixar
# é um cronômetro que acumula tempo a cada frame
# só executa a ação quando esse cronômetro passa do limite definido em velocidade_baixo

velocidade_baixo = 50  # ms entre cada descida (ajuste esse valor ao seu gosto)
tempo_esquerda = 0
tempo_direita = 0
velocidade_lateral = 80  # ajuste ao seu gosto
#Loop principal do jogo
while True:
    tempo_queda += relogio.tick(60) #60 frames por segundo
    for evento in pygame.event.get():
        if evento.type  == pygame.QUIT:
            pygame.quit()
            sys.exit()
        #DETECTA TECLA PRESSIONADA
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_F11:
                tela_cheia = not tela_cheia
                if tela_cheia:
                    tela = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
                    LARGURA_TELA = tela.get_width()
                    ALTURA_TELA = tela.get_height()
                    offset_x = (LARGURA_TELA - LARGURA) // 2
                    offset_y = (ALTURA_TELA - ALTURA) // 2
                else:
                    tela = pygame.display.set_mode((LARGURA, ALTURA))
                    offset_x = 0
                    offset_y = 0
            if evento.key == pygame.K_ESCAPE:
                if tela_cheia:
                    tela_cheia = False
                    tela = pygame.display.set_mode((LARGURA, ALTURA))
                    offset_x = 0
                    offset_y = 0

            if not game_over:
                if evento.key == pygame.K_UP or evento.key == pygame.K_w:
                    girar_peca(peca_atual)
                if evento.key == pygame.K_LEFT or evento.key == pygame.K_a:
                    if peca_pode_mover(peca_atual, colunas_extra=-1):
                        peca_atual["coluna"] -= 1
                if evento.key == pygame.K_RIGHT or evento.key == pygame.K_d:
                    if peca_pode_mover(peca_atual, colunas_extra=1):
                        peca_atual["coluna"] += 1
            else:
                if evento.key == pygame.K_r:
                    game_over = reiniciar()
                    peca_atual = nova_peca()


    #Move as peças quando a tecla determinada é pressionada
    teclas = pygame.key.get_pressed()
    if not game_over:
        if teclas[pygame.K_LEFT] or teclas[pygame.K_a]:
            tempo_esquerda += relogio.tick(60)
            if tempo_esquerda >= velocidade_lateral:
                if peca_pode_mover(peca_atual, colunas_extra=-1):
                    peca_atual["coluna"] -= 1
                tempo_esquerda = 0
        else:
            tempo_esquerda = 0

        if teclas[pygame.K_RIGHT] or teclas[pygame.K_d]:
            tempo_direita += relogio.tick(60)
            if tempo_direita >= velocidade_lateral:
                if peca_pode_mover(peca_atual, colunas_extra=1):
                    peca_atual["coluna"] += 1
                tempo_direita = 0
        else:
            tempo_direita = 0
        if teclas[pygame.K_DOWN] or teclas[pygame.K_s]:
            tempo_baixo += relogio.tick(60)
            if tempo_baixo >= velocidade_baixo:
                if peca_pode_mover(peca_atual, linhas_extra=1):
                    peca_atual["linha"] += 1
                tempo_baixo = 0
        else:
            tempo_baixo = 0

    #Faz a peça cair automaticamente
    if not game_over:
        if tempo_queda >= velocidade_queda:
            if peca_pode_mover(peca_atual, linhas_extra=1):
                peca_atual["linha"] += 1
            else:
                #Chegou ao fundo, cria outra peça
                fixar_peca(peca_atual)
                limpar_linhas()
                try:
                    peca_atual = nova_peca()
                except:
                    print("Erro ao criar nova peça!")
                    pygame.quit()
                    sys.exit()
                if verificar_game_over(peca_atual):
                    game_over = True
            tempo_queda = 0

    velocidade_queda = max(100, 500 // funcoes.nivel)
    #Pinta o fundo de preto
    tela.fill(PRETO)

    desenhar_tabuleiro(tela, offset_x, offset_y)

    if game_over:
        desenhar_game_over(tela, fonte, offset_x, offset_y)
    else:
        desenhar_peca(tela, peca_atual, offset_x, offset_y)
    #Atualiza a tela
    desenhar_pontuacao(tela, fonte, offset_x, offset_y)
    pygame.display.flip()

