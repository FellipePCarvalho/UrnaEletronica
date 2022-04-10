from time import sleep

# CORES PARA USAR NA FORMATAÇÃO
cor = {'verdeNeg': '\033[1;32m',
       'vermeNeg': '\033[1;31m',
       'laranNeg': '\033[1;33m',
       'negrito': '\033[1m',
       'fimCor': '\033[m'}

# IMPRESSÃO TITULO URNA ELETRÔNICA
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

########################################################################################
# DECLARAÇÃO DE VARIÁVEIS GLOBAIS
# Utilização Escolha 0
contagem = 0
listaNomeNumPart = []  # LISTA QUE RECEBERÁ A LISTA DE NOMES, PARTIDOS E NÚMEROS
listaNomes = []  # LISTA QUE RECEBERÁ O NOME DOS CANDIDATOS
listaPartidos = []  # LISTA QUE RECEBERÁ O PARTIDO DOS CANDIDATOS
listaNumeros = []  # LISTA QUE RECEBERÁ O NÚMERO DOS CANDITADOS
cadastroVoto = {}  # DICIONÁRIO QUE RECEBERÁ OS NÚMEROS e VOTOS        {13: 0}
cadastroNome = {}  # DICIONÁRIO QUE RECEBERÁ OS NOMES e PARTIDOS       {'José': 'Pt'}
cadastroPartido = {}  # DICIONÁRIO QUE RECEBERÁ OS PARTIDOS e NÚMEROS     {'Pt': 13}

# Utilização escolha 1
quantCandiCadastr = 0  # VARIÁVEL PARA GUARDAR A QUANTIDADE DE CANDIDATOS CADASTRADOS
contQtdCandi = 1  # CONTADOR PRA SER USADO NO FOR
votoValido = 0  # SOMANDO QUANTIDADE VOTO VALIDO
nulo = 0  # SOMANDO QUANTIDADE DE VOTOS NULOS
branco = 0  # SOMANDO QUANTIDADE DE VOTOS BRANCOS
formatacao = ''  # VARIÁVEL VAZIA APENAS PARA FORMATAÇÃO
maiorNumVotosCamp = 0  # VARIÁVEL PARA RECEBER O NÚMERO DE VOTOS DO CAMPEÃO, A MAIOR QUANTIDADE DE VOTOS
voto = 0  # VOTO ATUAL DE QUEM ESTÁ UTILIZANDO O PROGRAMA
quantVotosReal = 0  # RECEBE A QUANTIDADE DE VOTOS ATUAL E ACRESCENTA + 1 VOTO

# Utilização escolha 2
listaVoto = []  # LISTA PARA ARMAZENAR APENAS A QUANTIDADE DE VOTOS

# Utilização escolha 3
numeroVencedor = partidoVencedor = nomeVencedor = ''
porcentagemNulo = porcentagemBranco = ''
contadorMaiorModa = 0

# 1ª IMPRESSÃO MENU DE OPÇÕES E ESCOLHA
print(menu)

# VALIDAÇÃO PARA QUE A ESCOLHA MENU ESTEJA DENTRO DO RANGE DE OPÇÕES
while True:
    try:
        escolhaMenu = int(input('Qual a opção escolhida?: '))
        if not escolhaMenu in range(0, 4):  # IDENTIFICANDO SE NUMERO ESTÁ NO RANGE
            raise ValueError()  # SE N ESTIVER NO RANGE, VAI IDENTIFICAR COMO ERRO
    except ValueError as num:  # SOLICITANDO ENTRADA DE NOVO DADO DEVIDO AO ERRO
        print('-' * 33)
        print('Por favor digite uma OPÇÃO válida ')
        print('-' * 33)
    else:
        break  # DIGITAÇÃO CORRETA SAI DO LOOP

# OBRIGATORIEDADE DE SE CADASTRAR UM CANDIDATO ANTES DE RODAR O PROGRAMA
while escolhaMenu != 0:
    try:
        print('-' * 30)
        print('CADASTRE um candidato primeiro!')
        print('-' * 30)
        escolhaMenu = int(input('Qual a opção escolhida?: '))

        #VERIFICANDO SE VARIAVEL ESTÁ NUMERO DENTRO DAS OPÇÕES
        if (type(escolhaMenu) != int): #Verifica se escolhaMenu é diferente de inteiro
            raise ValueError()
    except ValueError as num: #Manda digitar número
        print('-' * 33)
        print('Por Favor digite um NUMERO dentre as opções: ')
        print('-' * 33)

else:
    ########################################################################################
    # ==================================================
    # ESCOLHA // CADASTRAR UM CANDIDATO//
    while escolhaMenu == 0:
        # VALIDANDO CARACTERES NOME
        while True:
            print('-' * 25)
            nome = input("Nome: ")

            # OBSERVAÇÃO: Ideologia -> Em prol da verificação de variavel nula
            if all(n.isalpha() or n.isspace() for n in
                   nome.split(' ')):  # identificando se foi digitado apenas letras e espaço

                break  # DIGITAÇÃO CORRETA SAI DO LOOP
            else:
                print('-' * 31)
                print('Por favor digite um NOME válido '
                      '\n(NÃO UTILIZE NÚMEROS)')
                print('-' * 31)

        # VALIDANDO CARACTERES PARTIDO
        while True:
            partido = input("Partido: ")
            # OBSERVAÇÃO:Ideologia -> Em prol da verificação de variavel nula
            if all(p.isalpha() or p.isspace() for p in
                   partido.split(' ')):  # identificando se foi digitado apenas letras e espaço
                break  # DIGITAÇÃO CORRETA SAI DO LOOP
            else:
                print('-' * 34)
                print('Por favor digite um PARTIDO válido '
                      '\n(NÃO UTILIZE NÚMEROS)')
                print('-' * 34)

        # VALIDANDO CARACTERES SE DENTRO DO RANGE MÁXIMO E SE NÚMERO
        while True:
            try:
                numero = int(input("Número: "))
                if not numero in range(0, 99999) or numero in listaNumeros:  # IDENTIFICANDO SE NUMERO ESTÁ NO RANGE
                    raise ValueError()  # SE N ESTIVER NO RANGE, VAI IDENTIFICAR COMO ERRO
            except ValueError as num:  # SOLICITANDO ENTRADA DE NOVO DADO DEVIDO AO ERRO
                print('-' * 33)
                print('Por favor digite um NÚMERO válido ')
                print('-' * 33)
            else:
                break  # DIGITAÇÃO CORRETA SAI DO LOOP

        # ÁREA DE ARMAZENAMENTO DOS NOMES, PARTIDOS, NÚMEROS E VOTOS
        listaNomes.append(nome)  # LISTA RECEBENDO O NOME DOS CANDIDATOS             ['José']
        listaPartidos.append(partido)  # LISTA RECEBENDO O PARTIDO DOS CANDIDATOS    ['Pt']
        listaNumeros.append(numero)  # LISTA RECEBENDO O NÚMERO DOS CANDITADOS       [13]
        listaNomeNumPart = listaNomes, listaPartidos, listaNumeros  # LISTA RECEBENDO AS OUTRAS LISTAS (['José'], ['Pt'], [13])

        quantCandiCadastr += 1  # SOMA 1 A CADA NOVO CANDIDATO CADASTRADO

        voto = 0
        cadastroNome.update({nome: partido})  # RECEBENDO OS NOMES e PARTIDOS {'José': 'Pt'}
        cadastroPartido.update({partido: numero})  # RECEBENDO OS PARTIDOS e NÚMEROS {'Pt': 13}
        cadastroVoto.update({numero: voto})  # RECEBENDO OS NÚMEROS e VOTOS {13: 0}

        # 2ª IMPRESSÃO MENU DE OPÇÕES E ESCOLHA 0

        print(menu)
        while True:
            try:
                escolhaMenu = int(input('Qual a opção escolhida?: '))
                if not escolhaMenu in range(0, 4):  # IDENTIFICANDO SE NUMERO ESTÁ NO RANGE
                    raise ValueError()  # SE N ESTIVER NO RANGE, VAI IDENTIFICAR COMO ERRO
            except ValueError as num:  # SOLICITANDO ENTRADA DE NOVO DADO DEVIDO AO ERRO
                print('-' * 33)
                print('Por favor digite uma OPÇÃO válida ')
                print('-' * 33)
            else:
                break  # DIGITAÇÃO CORRETA SAI DO LOOP

        ########################################################################################
        # ==================================================
        # ESCOLHA // VOTAR EM UM CANDIDATO //
        while escolhaMenu == 1:
            # CORES PARA USAR NA FORMATAÇÃO DO MENU
            cor = {'verdeNeg': '\033[1;32m',
                   'vermeNeg': '\033[1;31m',
                   'negrito': '\033[1m',
                   'fimCor': '\033[m', }

            # IMPRESSÃO MENU DE VOTAÇÃO
            print(f'''
            {cor['verdeNeg']}[0] VOTAR
            {cor['vermeNeg']}[1] ANULAR {cor['fimCor']}
            {cor['negrito']}[2] VOTAR EM BRANCO{cor['fimCor']}
            ''')

            # VALIDANDO ESCOLHA OPÇÃO SE DENTRO DO RANGE
            while True:
                try:
                    opcao = int(input('Digite a opção desejada: '))
                    if not opcao in range(0, 3):  # IDENTIFICANDO SE NUMERO ESTÁ NO RANGE
                        raise ValueError()  # SE N ESTIVER NO RANGE, VAI IDENTIFICAR COMO ERRO
                except ValueError as num:  # SOLICITANDO ENTRADA DE NOVO DADO DEVIDO AO ERRO
                    print('-' * 33)
                    print('Por favor digite uma OPÇÃO válida ')
                    print('-' * 33)
                else:
                    break  # DIGITAÇÃO CORRETA SAI DO LOOP
            print('-' * 25)

            # SE ESCOLHA VOTAR
            if opcao == 0:
                # CORES PARA USAR NA FORMATAÇÃO
                cor = {'negrito': '\033[1m',
                       'laranNeg': '\033[1;33m',
                       'fimCor': '\033[m', }

                # IMPRESSÃO LISTA DE CANDIDATOS
                print(' ' * 5, f"{cor['negrito']}" '=' * 40)
                print(' ' * 16, f"{cor['laranNeg']}" 'OS CANDIDATOS SÃO' f"{cor['fimCor']}")
                print(' ' * 5, f"{cor['negrito']}" '=' * 40)
                print(' ' * 5, 'CANDIDATO', ' ' * 6, 'PARTIDO', ' ' * 7, 'NÚMERO' f"{cor['fimCor']}")

                # PERCORRENDO A LISTA DE CANDIDATOS PARA IMPRIMIR
                for contQtdCandi in range(0, quantCandiCadastr):
                    print(f'\n{formatacao:6}{listaNomes[contQtdCandi]:16} {listaPartidos[contQtdCandi]:15} {listaNumeros[contQtdCandi]}', end=" ")
                    contQtdCandi += 1  # SOMANDO UM A QUANTIDADE DE CANDIDATOS CADASTRADOS

                # ÁREA DA COMPUTAÇÃO DOS VOTOS
                # 1ª VALIDAÇÃO VOTO, SE ESTÁ DENTRO DO RANGE MAXIMO E NÚMERO
                while True:
                    try:
                        voto = int(input('\nVoto Candidato (número): '))
                        if not voto in range(0, 99999):  # IDENTIFICANDO SE NUMERO ESTÁ NO RANGE
                            raise ValueError()  # SE N ESTIVER NO RANGE, VAI IDENTIFICAR COMO ERRO
                    except ValueError as num:  # SOLICITANDO ENTRADA DE NOVO DADO DEVIDO AO ERRO
                        print('-' * 32)
                        print('Por favor digite um VOTO válido ')
                        print('-' * 32)
                    else:
                        break  # DIGITAÇÃO CORRETA SAI DO LOOP

                # 2ª VALIDAÇÃO VOTO, SE NÚMERO JA CADASTRADO
                if voto in cadastroVoto:
                    quantVotosReal = cadastroVoto[voto]
                    totalDeVotosAtual = quantVotosReal + 1
                    cadastroVoto[voto] = totalDeVotosAtual
                    votoValido += 1

                    # SE O TOTAL DE VOTOS PRESENTE FOR MAIOR QUE O JA ARMAZENADO, ESSE SE TORNA O MAIOR
                    if totalDeVotosAtual > maiorNumVotosCamp:
                        maiorNumVotosCamp = totalDeVotosAtual
                else:
                    print('=' * 24)
                    print('Candidato não existente')
                    print('=' * 24)

            # SE ESCOLHA NULO
            elif opcao == 1:
                nulo += 1

            # SE ESCOLHA BRANCO
            else:
                branco += 1

            # 3ª IMPRESSÃO MENU DE OPÇÕES E ESCOLHA 1
            print(f'{menu}')
            while True:
                try:
                    escolhaMenu = int(input('Qual a opção escolhida?: '))
                    if not escolhaMenu in range(0, 4):  # IDENTIFICANDO SE NUMERO ESTÁ NO RANGE
                        raise ValueError()  # SE N ESTIVER NO RANGE, VAI IDENTIFICAR COMO ERRO
                except ValueError as num:  # SOLICITANDO ENTRADA DE NOVO DADO DEVIDO AO ERRO
                    print('-' * 33)
                    print('Por favor digite uma OPÇÃO válida ')
                    print('-' * 33)
                else:
                    break  # DIGITAÇÃO CORRETA SAI DO LOOP

            ########################################################################################
            # ==================================================
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

                # LISTA VAZIA PARA ZERAR OS VOTOS JA ARMAZENADOS E RECEBER NOVOS
                listaVoto = []

                # PERCORRENDO O DICIONARIO DE CADASTRO DOS VOTOS E PEGANDO OS VOTOS
                for quantidadeVotos in cadastroVoto:
                    guardandoVotos = cadastroVoto[quantidadeVotos]
                    listaVoto.append(guardandoVotos)

                # PERCORRENDO A LISTA DE CANDIDATOS E IMPRIMINDO NOME, PARTIDO, NÚMERO E VOTOS
                for contQtdCandi in range(0, quantCandiCadastr):
                    print(f'\n{formatacao:6}{listaNomes[contQtdCandi]:16} {listaPartidos[contQtdCandi]:15} {listaNumeros[contQtdCandi]} {listaVoto[contQtdCandi]:11}', end=" ")
                    contQtdCandi += 1  # SOMANDO UM A QUANTIDADE DE CANDIDATOS CADASTRADOS

                # 4ª IMPRESSÃO MENU DE OPÇÕES E ESCOLHA 2
                print(f'\n{menu}')
                while True:
                    try:
                        escolhaMenu = int(input('Qual a opção escolhida?: '))
                        if not escolhaMenu in range(0, 4):  # IDENTIFICANDO SE NUMERO ESTÁ NO RANGE
                            raise ValueError()  # SE N ESTIVER NO RANGE, VAI IDENTIFICAR COMO ERRO
                    except ValueError as num:  # SOLICITANDO ENTRADA DE NOVO DADO DEVIDO AO ERRO
                        print('-' * 33)
                        print('Por favor digite uma OPÇÃO válida ')
                        print('-' * 33)
                    else:
                        break  # DIGITAÇÃO CORRETA SAI DO LOOP

########################################################################################
# ==================================================
# ESCOLHA // FINALIZAR VOTAÇÃO //
if escolhaMenu == 3:
    # CORES PARA USAR NA FORMATAÇÃO
    cor = {'vermeNeg': '\033[1;31m',
           'laranNeg': '\033[1;33m',
           'negrito': '\033[1m',
           'fimCor': '\033[m'}

    print(f"{cor['vermeNeg']}"'O PROGRAMA SERÁ ENCERRADO' f"{cor['fimCor']}")
    sleep(2)

    # IMPRESSÃO LISTA DE CANDIDATOS, VOTOS e PORCENTAGEM
    print(' ' * 5, f"{cor['negrito']}" '=' * 80)
    print(' ' * 32, f"{cor['laranNeg']}"'VOTOS / PORCENTAGEM (TOTAL)' f"{cor['fimCor']}")
    print(' ' * 5, f"{cor['negrito']}" '=' * 80)
    print(' ' * 5, 'CANDIDATO', ' ' * 6, 'PARTIDO', ' ' * 7,
          'NÚMERO', ' ' * 5, 'VOTOS', ' ' * 5, '% Validos', ' ' * 4, '% Total' f"{cor['fimCor']}")

###############################################################
    # PERCORRENDO A LISTA DE CANDIDATOS
    for contQtdCandi in range(0, quantCandiCadastr):
        valido = listaVoto[contQtdCandi]

        if votoValido > 0:
            porcentagemValidos = (100 * valido) / (votoValido)
            porcentagemTotal = (100 * valido) / (votoValido + branco + nulo)
            porcentagemNulo = (100 * nulo) / (votoValido + branco + nulo)
            porcentagemBranco = (100 * branco) / (votoValido + branco + nulo)

            # IMPRIMINDO VOTOS E PORCENTAGENS
            print(f'\n{formatacao:6}{listaNomes[contQtdCandi]:16} {listaPartidos[contQtdCandi]:15} {listaNumeros[contQtdCandi]} {listaVoto[contQtdCandi]:11}'
                f' {porcentagemValidos:16.2f} {porcentagemTotal:14.2f}', end=" ")
            contQtdCandi += 1  # SOMANDO UM A QUANTIDADE DE CANDIDATOS CADASTRADOS

        else:
            porcentagemNulo = (100 * nulo) / (branco + nulo)
            porcentagemBranco = (100 * branco) / (branco + nulo)

    print(f"\n{formatacao:6}{'Nulos':17}{'--':16}{'--'}{nulo:12}{'--':>14}{porcentagemNulo:18.2f}")
    print(f"{formatacao:6}{'Brancos':17}{'--':16}{'--'}{branco:12}{'--':>14}{porcentagemBranco:18.2f}")
    print('\n')

    #IDENTIFICANDO O MAIOR VOTO E SOMANDO AO CONTADOR
    maiorVoto = maiorNumVotosCamp
    for contQtdCandi in range(0, quantCandiCadastr):
        valido = listaVoto[contQtdCandi]
        if valido == maiorVoto:
            contadorMaiorModa += 1

    if contadorMaiorModa > 1:
        # IMPRESSÃO TITULO EMPATE
        print(' ' * 5, f"{cor['negrito']}" '=' * 51)
        print(' ' * 28, f"{cor['laranNeg']}"'EMPATE' f"{cor['fimCor']}")
        print(' ' * 5, f"{cor['negrito']}" '=' * 51)
        print(f"{formatacao:18}HOUVE EMPATE, {cor['vermeNeg']} SEM GANHADOR {cor['fimCor']}", end=" ")

    else:
        # CAMPEÃO
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
