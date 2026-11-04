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
print(frota)
