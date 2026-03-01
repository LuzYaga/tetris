# Imitação de Tetris

Um jogo inspirado em Tetris feito em Python com a biblioteca Pygame.

## Requisitos
- Python 3.10 ou superior
- Pygame
- Git
## Como executar

## Download
Baixe a última versão em [Releases](https://github.com/LuzYaga/tetris/releases)
> **Atenção:** O Windows pode exibir um aviso de segurança ao executar. Clique em "Mais informações" e depois "Executar assim mesmo".
### 1. Clone o repositório
```
git clone https://github.com/LuzYaga/tetris.git
```

### 2. Entre na pasta do projeto
```
cd tetris
```

### 3. Instale as dependências
```
pip install -r requirements.txt
```

### 4. Execute o jogo
```
cd main
python main.py
```

## Como jogar
- **Seta esquerda / A** — mover para esquerda
- **Seta direita / D** — mover para direita
- **Seta baixo / S** — acelerar queda
- **Seta cima / W** — girar peça
- **R** — reiniciar após game over
- **F11** — tela cheia

## Pontuação
- 1 linha = 100 pontos
- 2 linhas = 300 pontos
- 3 linhas = 500 pontos
- 4 linhas = 800 pontos

## Estrutura do projeto
- `main.py` — loop principal do jogo
- `funcoes.py` — funções do jogo
- `config.py` — configurações e constantes
- `assets/` — imagens e músicas
