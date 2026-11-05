import random

from funcoes import define_posicoes
from funcoes import preenche_frota
from funcoes import posicao_valida
frota = {}

embarcacoes = [['porta-aviões', 4, 1], ['navio-tanque', 3, 2], ['contratorpedeiro', 2, 3], ['submarino', 1, 4]]
for i in embarcacoes:
    c = 0
    while c < i[2]:
        print(f'Insira as informações referentes ao navio {i[0]} que possui tamanho {i[1]}')
        linha = int(input('linha: '))
        coluna = int(input('coluna: '))
        if i[0] != 'submarino':
            orientacao = int(input('[1] Vertical [2] Horizontal: '))
            if orientacao == 1:
                orientacao = 'vertical'
            elif orientacao == 2:
                orientacao = 'horizontal'
        else:
            orientacao = 'vertical'
        valida = posicao_valida(frota, linha, coluna, orientacao, i[1])
        if valida == True:
            preenche_frota(frota, i[0], linha, coluna, orientacao, i[1])
            c += 1
        else:
            print('Esta posição não está válida!')


from funcoes import posiciona_frota
from funcoes import afundados
from funcoes import faz_jogada

frota_oponente = {
    'porta-aviões': [
        [[9, 1], [9, 2], [9, 3], [9, 4]]
    ],
    'navio-tanque': [
        [[6, 0], [6, 1], [6, 2]],
        [[4, 3], [5, 3], [6, 3]]
    ],
    'contratorpedeiro': [
        [[1, 6], [1, 7]],
        [[0, 5], [1, 5]],
        [[3, 6], [3, 7]]
    ],
    'submarino': [
        [[2, 7]],
        [[0, 6]],
        [[9, 7]],
        [[7, 6]]
    ]
}

tabuleiro_oponente = posiciona_frota(frota_oponente)
tabuleiro_jogador = posiciona_frota(frota)

def monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente):
    texto = ''
    texto += '   0  1  2  3  4  5  6  7  8  9         0  1  2  3  4  5  6  7  8  9\n'
    texto += '_______________________________      _______________________________\n'

    for linha in range(len(tabuleiro_jogador)):
        jogador_info = '  '.join([str(item) for item in tabuleiro_jogador[linha]])
        oponente_info = '  '.join([info if str(info) in 'X-' else '0' for info in tabuleiro_oponente[linha]])
        texto += f'{linha}| {jogador_info}|     {linha}| {oponente_info}|\n'
    return texto

acertos = 0
tabuleiros = monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente)
print(tabuleiros)

jogadas_oponente = []
acertos_oponente = 0 
while acertos != 10 and acertos_oponente != 10:

    linhaj = int(input('Jogador, qual linha deseja atacar? '))
    while linhaj < 0 or linhaj > 9:
        print('Linha inválida!')
        linhaj = int(input('Jogador, qual linha deseja atacar? '))

    colunaj = int(input('Jogador, qual coluna deseja atacar? '))
    while colunaj < 0 or colunaj > 9:
            print('Coluna inválida!')
            colunaj = int(input('Jogador, qual coluna deseja atacar? '))
    if (tabuleiro_oponente[linhaj][colunaj]) == 'X' or (tabuleiro_oponente[linhaj][colunaj]) == '-':
        print(f'A posição linha {linhaj} e coluna {colunaj} já foi informada anteriormente!')
    else:
        faz_jogada(tabuleiro_oponente, linhaj, colunaj)
        acertos = afundados(frota_oponente, tabuleiro_oponente)
        if acertos != 10:
            linha_oponente = random.randint(0, 9)
            coluna_oponente = random.randint(0, 9)
            if [linha_oponente, coluna_oponente] in jogadas_oponente:
                while [linha_oponente, coluna_oponente] in jogadas_oponente:
                    linha_oponente = random.randint(0, 9)
                    coluna_oponente = random.randint(0, 9)
            jogadas_oponente.append([linha_oponente, coluna_oponente])
            print(f'Seu oponente está atacando na linha {linha_oponente} e coluna {coluna_oponente}')
            faz_jogada(tabuleiro_jogador, linha_oponente, coluna_oponente)
            acertos_oponente = afundados(frota, tabuleiro_jogador)

            tabuleiros = monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente)
            print(tabuleiros)
            if acertos_oponente == 10:
                print ('Xi! O oponente derrubou toda a sua frota =(')
            
            
if acertos_oponente != 10: 
    print ('Parabéns! Você derrubou todos os navios do seu oponente!')