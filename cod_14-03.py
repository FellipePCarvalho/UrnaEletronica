from time import sleep

# CORES PARA USAR NA FORMATAÇÃO
cor = {'verde': '\033[32m',
     'verdeNeg': '\033[1;32m',
     'vermelho': '\033[31m',
     'vermeNeg': '\033[1;31m',
     'negrito': '\033[1m',
     'laranNeg': '\033[1;33m',
     'fimCor': '\033[m'}

#IMPRESSÃO TITULO
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
escolha = int(input('Qual a opção escolhida?: '))
print('-' * 25)

#DECLARAÇÃO DE VARIÁVEIS GLOBAIS
#Utilização Escolha 0
contagem = 0
lista = []
listaN = []
listaP = []
listaNu = []
cadastroVoto = {}
cadastroNome = {}
cadastroPartido = {}

#Utilização escolha 1
c = 1
soma = 0
votos = 0
formatacao = ''
contIm = 0
voto = 0
votoValido = 0
nulo = 0
branco = 0
campeaoVotos = 0

#Utilização escolha 2
listaVoto = []

#==================================================
# ESCOLHA // CADASTRAR UM CANDIDATO//
while escolha == 0:
    nome = str(input('Nome: '))
    partido = str(input('Partido: '))
    numero = int(input('Número: '))

    listaN.append(nome)
    listaP.append(partido)
    listaNu.append(numero)
    lista = listaN, listaP, listaNu
    contIm += 1

    cadastroNome.update({nome: partido})
    cadastroPartido.update({partido: numero})
    cadastroVoto.update({numero: voto})

    # 2ª IMPRESSÃO MENU DE OPÇÕES E ESCOLHA 0
    print(menu)
    escolha = int(input('Qual a opção escolhida?: '))
    print('-' * 25)

#==================================================
# ESCOLHA // VOTAR EM UM CANDIDATO //
while escolha == 1:
    # CORES PARA USAR NA FORMATAÇÃO
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
    opcao = int(input('Digite a opção desejada: '))

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

        #PERCORRENDO A LISTA DE CANDIDATOS
        for c in range(0, contIm):
            print(f'\n{formatacao:6}{listaN[c]:16} {listaP[c]:15} {listaNu[c]}', end=" ")
            c += 1

        # ÁREA DE VOTAÇÃO
        voto = int(input('\nVoto Candidato (número): '))
        votos = cadastroVoto[voto]
        votoTotal = votos + 1
        cadastroVoto[voto] = votoTotal
        votoValido += 1

        if votoTotal > campeaoVotos:
            campeaoVotos = votoTotal

    # SE ESCOLHA NULO
    elif opcao == 1:
        nulo += 1

    # SE ESCOLHA BRANCO
    else:
        branco += 1

    # 3ª IMPRESSÃO MENU DE OPÇÕES E ESCOLHA 1
    print(f'\n{menu}')
    escolha = int(input('Qual a opção escolhida?: '))
    print('-' * 25)

#==================================================
# ESCOLHA // GERAR RELATÓRIO //
while escolha == 2:
    # CORES PARA USAR NA FORMATAÇÃO
    cor = {'negrito': '\033[1m',
           'laranNeg': '\033[1;33m',
           'fimCor': '\033[m', }
    # IMPRESSÃO LISTA DE CANDIDATOS E VOTOS

    print(' ' * 5, f"{cor['negrito']}" '=' * 51)
    print(' ' * 28, f"{cor['laranNeg']}"'VOTOS' f"{cor['fimCor']}")
    print(' ' * 5, f"{cor['negrito']}" '=' * 51)
    print(' ' * 5, 'CANDIDATO', ' ' * 6, 'PARTIDO', ' ' * 7, 'NÚMERO', ' ' * 5, 'VOTOS' f"{cor['fimCor']}")

    #PERCORRENDO A LISTA DE CADASTRO E PEGANDO OS VOTOS
    for key in cadastroVoto:
        pegandoVotosDici = cadastroVoto[key]
        listaVoto.append(pegandoVotosDici)

    # PERCORRENDO A LISTA DE CANDIDATOS
    for c in range(0, contIm):
        print(f'\n{formatacao:6}{listaN[c]:16} {listaP[c]:15} {listaNu[c]} {listaVoto[c]:11}', end=" ")
        c += 1

    # 4ª IMPRESSÃO MENU DE OPÇÕES E ESCOLHA 2
    print(f'\n{menu}')
    escolha = int(input('Qual a opção escolhida?: '))
    print('-' * 25)

#==================================================
# ESCOLHA // FINALIZAR VOTAÇÃO //
if escolha == 3:
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
    for c in range(0, contIm):
        valido = listaVoto[c]
        print(f'\n{formatacao:6}{listaN[c]:16} {listaP[c]:15} {listaNu[c]} {listaVoto[c]:11}'
              f' {(100 * valido) / (votoValido + branco + nulo):12.2f}', end=" ")
        c += 1

    print(f'''\n{' ' * 6}Nulos {' ' * 40}{nulo} {' ' * 7}{(100 * nulo) / (votoValido + branco + nulo):.2f}
    {' ' * 2}Brancos {' ' * 38}{branco} {' ' * 8}{(100 * branco) / (votoValido + branco + nulo):.2f}''')

    #CAMPEÃO
    # IMPRESSÃO CAMPEÃO
    print(' ' * 5, f"{cor['negrito']}" '=' * 51)
    print(' ' * 28, f"{cor['laranNeg']}"'CAMPEÃO' f"{cor['fimCor']}")
    print(' ' * 5, f"{cor['negrito']}" '=' * 51)
    print(' ' * 5, 'CANDIDATO', ' ' * 6, 'PARTIDO', ' ' * 7, 'NÚMERO', ' ' * 5, 'VOTOS' f"{cor['fimCor']}")

    # Identificando número com maior número de votos
    for numero, voto in cadastroVoto.items():
        if voto == campeaoVotos:
            numeroVencedor = numero

    # Identificando partido com maior número de votos
    for partido, numero in cadastroPartido.items():
        if numero == numeroVencedor:
            partidoVencedor = partido

    # Identificando candidato com maior número de votos
    for nome, partido in cadastroNome.items():
        if partido == partidoVencedor:
            nomeVencedor = nome

    # IMPRIMINDO CAMPEÃO
    print(f'\n{formatacao:6}{nomeVencedor:16} {partidoVencedor:15} {numeroVencedor} {campeaoVotos:11}', end=" ")

    sleep(2)
    print(f"\n\n{cor['negrito']}"'Obrigado por votar!')
