from time import sleep

# CORES PARA USAR NA FORMATAÇÃO
cor = {'verdeNeg': '\033[1;32m',
       'vermeNeg': '\033[1;31m',
       'laranNeg': '\033[1;33m',
       'negrito': '\033[1m',
       'fimCor': '\033[m'}

#IMPRESSÃO TITULO URNA ELETRÔNICA
print(f"{cor['negrito']}" '=' * 27)
print(' ' * 5, f"{cor['vermeNeg']} URNA ELETRÔNICA {cor['fimCor']}")
print(f"{cor['negrito']}" '=' * 27)

# MENU DE OPÇÕES
menu = (f'''
{cor['laranNeg']}===== MENU DE OPÇÕES ====={cor['fimCor']}
{cor['verdeNeg']}[0] Cadastrar um candidato
[1] Votar em um candidato
[2] Gerar relatório
[3] Finalizar votação{cor['fimCor']}
''')

#1ª IMPRESSÃO MENU DE OPÇÕES E ESCOLHA
print(menu)
escolhaMenu = int(input('Qual a opção escolhida?: '))
print('-' * 25)

########################################################################################
#DECLARAÇÃO DE VARIÁVEIS GLOBAIS
#Utilização Escolha 0
contagem = 0
listaNomeNumPart = []  #LISTA QUE RECEBERÁ A LISTA DE NOMES, PARTIDOS E NÚMEROS
listaNomes = []        #LISTA QUE RECEBERÁ O NOME DOS CANDIDATOS
listaPartidos = []     #LISTA QUE RECEBERÁ O PARTIDO DOS CANDIDATOS
listaNumeros = []      #LISTA QUE RECEBERÁ O NÚMERO DOS CANDITADOS
cadastroVoto = {}      #DICIONÁRIO QUE RECEBERÁ OS NÚMEROS e VOTOS        {13: 0}
cadastroNome = {}      #DICIONÁRIO QUE RECEBERÁ OS NOMES e PARTIDOS       {'José': 'Pt'}
cadastroPartido = {}   #DICIONÁRIO QUE RECEBERÁ OS PARTIDOS e NÚMEROS     {'Pt': 13}

#Utilização escolha 1
quantCandiCadastr = 0 #VARIÁVEL PARA GUARDAR A QUANTIDADE DE CANDIDATOS CADASTRADOS
contQtdCandi = 1      #CONTADOR PRA SER USADO NO FOR
votoValido = 0        #SOMANDO QUANTIDADE VOTO VALIDO
nulo = 0              #SOMANDO QUANTIDADE DE VOTOS NULOS
branco = 0            #SOMANDO QUANTIDADE DE VOTOS BRANCOS
formatacao = ''       #VARIÁVEL VAZIA APENAS PARA FORMATAÇÃO
maiorNumVotosCamp = 0 #VARIÁVEL PARA RECEBER O NÚMERO DE VOTOS DO CAMPEÃO, A MAIOR QUANTIDADE DE VOTOS
voto = 0              #VOTO ATUAL DE QUEM ESTÁ UTILIZANDO O PROGRAMA
quantVotosReal = 0    #RECEBE A QUANTIDADE DE VOTOS ATUAL E ACRESCENTA + 1 VOTO

#Utilização escolha 2
listaVoto = []        #LISTA PARA ARMAZENAR APENAS A QUANTIDADE DE VOTOS

#Utilização escolha 3
numeroVencedor = partidoVencedor = nomeVencedor = ''

########################################################################################
#==================================================
# ESCOLHA // CADASTRAR UM CANDIDATO//
while escolhaMenu == 0:
    nome = str(input('Nome: ')) #CADASTRANDO O NOME DO CANDIDATO
    partido = str(input('Partido: ')) #CADASTRANDO O PARTIDO
    numero = int(input('Número: ')) #CADASTRANDO O NÚMERO

    listaNomes.append(nome) #LISTA RECEBENDO O NOME DOS CANDIDATOS             ['José']
    listaPartidos.append(partido) #LISTA RECEBENDO O PARTIDO DOS CANDIDATOS    ['Pt']
    listaNumeros.append(numero) #LISTA RECEBENDO O NÚMERO DOS CANDITADOS       [13]
    listaNomeNumPart = listaNomes, listaPartidos, listaNumeros #LISTA RECEBENDO AS OUTRAS LISTAS (['José'], ['Pt'], [13])

    quantCandiCadastr += 1 #SOMA 1 A CADA NOVO CANDIDATO CADASTRADO

    cadastroNome.update({nome: partido}) #RECEBENDO OS NOMES e PARTIDOS {'José': 'Pt'}
    cadastroPartido.update({partido: numero}) #RECEBENDO OS PARTIDOS e NÚMEROS {'Pt': 13}
    cadastroVoto.update({numero: voto}) #RECEBENDO OS NÚMEROS e VOTOS {13: 0}

    # 2ª IMPRESSÃO MENU DE OPÇÕES E ESCOLHA 0
    print(menu)
    escolhaMenu = int(input('Qual a opção escolhida?: '))
    print('-' * 25)

########################################################################################
#==================================================
# ESCOLHA // VOTAR EM UM CANDIDATO //
while escolhaMenu == 1:
    # CORES PARA USAR NA FORMATAÇÃO DO MENU
    cor = {'verdeNeg': '\033[1;32m',
         'vermeNeg': '\033[1;31m',
         'negrito': '\033[1m',
         'fimCor': '\033[m', }

    #IMPRESSÃO MENU DE VOTAÇÃO
    print(f'''
    {cor['verdeNeg']}[0] VOTAR
    {cor['vermeNeg']}[1] ANULAR {cor['fimCor']}
    {cor['negrito']}[2] VOTAR EM BRANCO{cor['fimCor']}
    ''')
    opcao = int(input('Digite a opção desejada: ')) #OPÇÃO ENTRE VOTAR, BRANCO OU NULO

    #SE ESCOLHA VOTAR
    if opcao == 0:
        # CORES PARA USAR NA FORMATAÇÃO
        cor = {'negrito': '\033[1m',
               'laranNeg': '\033[1;33m',
               'fimCor': '\033[m', }

        #IMPRESSÃO LISTA DE CANDIDATOS
        print(' ' * 5, f"{cor['negrito']}" '=' * 40)
        print(' ' * 16, f"{cor['laranNeg']}" 'OS CANDIDATOS SÃO' f"{cor['fimCor']}")
        print(' ' * 5, f"{cor['negrito']}" '=' * 40)
        print(' ' * 5, 'CANDIDATO', ' ' * 6, 'PARTIDO', ' ' * 7, 'NÚMERO' f"{cor['fimCor']}")

        #PERCORRENDO A LISTA DE CANDIDATOS PARA IMPRIMIR
        for contQtdCandi in range(0, quantCandiCadastr):
            print(f'\n{formatacao:6}{listaNomes[contQtdCandi]:16} {listaPartidos[contQtdCandi]:15} {listaNumeros[contQtdCandi]}', end=" ")
            contQtdCandi += 1 #SOMANDO UM A QUANTIDADE DE CANDIDATOS CADASTRADOS

        # ÁREA DA COMPUTAÇÃO DOS VOTOS
        voto = int(input('\nVoto Candidato (número): '))
        quantVotosReal = cadastroVoto[voto]
        totalDeVotosAtual = quantVotosReal + 1
        cadastroVoto[voto] = totalDeVotosAtual
        votoValido += 1

        #SE O TOTAL DE VOTOS PRESENTE FOR MAIOR QUE O JA ARMAZENADO, ESSE SE TORNA O MAIOR
        if totalDeVotosAtual > maiorNumVotosCamp:
            maiorNumVotosCamp = totalDeVotosAtual

    # SE ESCOLHA NULO
    elif opcao == 1:
        nulo += 1

    # SE ESCOLHA BRANCO
    else:
        branco += 1

    # 3ª IMPRESSÃO MENU DE OPÇÕES E ESCOLHA 1
    print(f'\n{menu}')
    escolhaMenu = int(input('Qual a opção escolhida?: '))
    print('-' * 25)

########################################################################################
#==================================================
# ESCOLHA // GERAR RELATÓRIO //
while escolhaMenu == 2:
    # CORES PARA USAR NA FORMATAÇÃO
    cor = {'negrito': '\033[1m',
           'laranNeg': '\033[1;33m',
           'fimCor': '\033[m', }

    # IMPRESSÃO LISTA DE CANDIDATOS E VOTOS
    print(' ' * 5, f"{cor['negrito']}" '=' * 51)
    print(' ' * 28, f"{cor['laranNeg']}"'VOTOS' f"{cor['fimCor']}")
    print(' ' * 5, f"{cor['negrito']}" '=' * 51)
    print(' ' * 5, 'CANDIDATO', ' ' * 6, 'PARTIDO', ' ' * 7, 'NÚMERO', ' ' * 5, 'VOTOS' f"{cor['fimCor']}")

    #PERCORRENDO O DICIONARIO DE CADASTRO DOS VOTOS E PEGANDO OS VOTOS
    for quantidadeVotos in cadastroVoto:
        guardandoVotos = cadastroVoto[quantidadeVotos]
        listaVoto.append(guardandoVotos)

    # PERCORRENDO A LISTA DE CANDIDATOS E IMPRIMINDO NOME, PARTIDO, NÚMERO E VOTOS
    for contQtdCandi in range(0, quantCandiCadastr):
        print(f'\n{formatacao:6}{listaNomes[contQtdCandi]:16} {listaPartidos[contQtdCandi]:15} {listaNumeros[contQtdCandi]} {listaVoto[contQtdCandi]:11}', end=" ")
        contQtdCandi += 1 #SOMANDO UM A QUANTIDADE DE CANDIDATOS CADASTRADOS

    # 4ª IMPRESSÃO MENU DE OPÇÕES E ESCOLHA 2
    print(f'\n{menu}')
    escolhaMenu = int(input('Qual a opção escolhida?: '))
    print('-' * 25)

########################################################################################
#==================================================
# ESCOLHA // FINALIZAR VOTAÇÃO //
if escolhaMenu == 3:
    # CORES PARA USAR NA FORMATAÇÃO
    cor = {'vermeNeg': '\033[1;31m',
           'laranNeg': '\033[1;33m',
           'negrito': '\033[1m',
           'fimCor': '\033[m'}

    print(f"{cor['vermeNeg']}"'O PROGRAMA SERÁ ENCERRADO' f"{cor['fimCor']}")
    sleep(2)

    porcentagemValidos = (100 * votoValido) / (votoValido + branco + nulo)

    # IMPRESSÃO LISTA DE CANDIDATOS, VOTOS e PORCENTAGEM
    print(' ' * 5, f"{cor['negrito']}" '=' * 60)
    print(' ' * 21, f"{cor['laranNeg']}"'VOTOS / PORCENTAGEM (TOTAL)' f"{cor['fimCor']}")
    print(' ' * 5, f"{cor['negrito']}" '=' * 60)
    print(' ' * 5, 'CANDIDATO', ' ' * 6, 'PARTIDO', ' ' * 7,
          'NÚMERO', ' ' * 5, 'VOTOS', ' ' * 4, '%' f"{cor['fimCor']}")

    # PERCORRENDO A LISTA DE CANDIDATOS
    for contQtdCandi in range(0, quantCandiCadastr):
        valido = listaVoto[contQtdCandi]
        print(f'\n{formatacao:6}{listaNomes[contQtdCandi]:16} {listaPartidos[contQtdCandi]:15} {listaNumeros[contQtdCandi]} {listaVoto[contQtdCandi]:11}'
              f' {(100 * valido) / (votoValido + branco + nulo):12.2f}', end=" ")
        contQtdCandi += 1 #SOMANDO UM A QUANTIDADE DE CANDIDATOS CADASTRADOS

    print(f'''\n{' ' * 6}Nulos {' ' * 40}{nulo} {' ' * 7}{(100 * nulo) / (votoValido + branco + nulo):.2f}
    {' ' * 2}Brancos {' ' * 38}{branco} {' ' * 7}{(100 * branco) / (votoValido + branco + nulo):.2f}
    ''')

    #CAMPEÃO
    # IMPRESSÃO TITULO CAMPEÃO
    print(' ' * 5, f"{cor['negrito']}" '=' * 51)
    print(' ' * 28, f"{cor['laranNeg']}"'CAMPEÃO' f"{cor['fimCor']}")
    print(' ' * 5, f"{cor['negrito']}" '=' * 51)
    print(' ' * 5, 'CANDIDATO', ' ' * 6, 'PARTIDO', ' ' * 7, 'NÚMERO', ' ' * 5, 'VOTOS' f"{cor['fimCor']}")

    # IDENTIFICANDO NÚMERO COM MAIOR NÚMERO DE VOTOS
    for numero, voto in cadastroVoto.items():
        if voto == maiorNumVotosCamp:
            numeroVencedor = numero

    # IDENTIFICANDO PARTIDO COM MAIOR NÚMERO DE VOTOS ATRAVÉS DO NÚMERO VENCEDOR
    for partido, numero in cadastroPartido.items():
        if numero == numeroVencedor:
            partidoVencedor = partido

    # IDENTIFICANDO CANDIDATO COM MAIOR NÚMERO DE VOTOS ATRAVÉS DO PARTIDO VENCEDOR
    for nome, partido in cadastroNome.items():
        if partido == partidoVencedor:
            nomeVencedor = nome

    # IMPRIMINDO CAMPEÃO
    print(f'{formatacao:6}{nomeVencedor:16} {partidoVencedor:15} {numeroVencedor} {maiorNumVotosCamp:11}', end=" ")

    sleep(2)
    print(f"\n\n{cor['negrito']}"'Obrigado por votar!')
