from time import sleep
c = {'vd':'\033[32m',
     'vdN':'\033[1;32m', #não tava dando as cores pq esqueci de colocar o 'm'
     'vm':'\033[31m',
     'vmN':'\033[1;31m',
     'sc':'\033[m',
     'n':'\033[1m',
     'a':'\033[1;33m'}

print('''========================
     URNA ELETRÔNICA 
========================''')

#menu de opções
menu = (f'''
===== MENU DE OPÇÕES =====
{c['vdN']}[0] Cadastrar um candidato
[1] Votar em um candidato
[2] Gerar relatório
[3] Finalizar votação{c['sc']}
''')
print(menu)
escolha = int(input('Qual a opção escolhida?: '))
print(escolha)

contagem = 0
c = 1
#Escolha dentro dos padrões
while escolha == 0:
    contagem += 1
    # CADASTRO CANDIDATO
    if contagem == 1:
        print(contagem)
        nome = str(input('Nome: '))
        partido = str(input('Partido: '))
        numero = int(input('Número: '))

    # GUARDANDO VALORES DENTRO DA CHAVE
        candidato = [nome, partido]
        cadastro = {numero: candidato}
        print('=========')
        #print(candidato)
        #print(cadastro)
        print('=========')
        listaN = [nome]
        listaP = [partido]
        listaNu = [numero]
        lista = [listaN, listaP, listaNu]
    else:
        print(contagem)
        #candidato.append(str(input('Nome: ')))
        #candidato.append(str(input('Partido: ')))
        nome = str(input('Nome: '))
        partido = str(input('Partido: '))
        numero = int(input('Número: '))
        candidato = [nome, partido]
        cadastro.update({numero: candidato})
        print('=========')
        print(f'{cadastro}')
        print('=========')
        listaN.append(nome)
        listaP.append(partido)
        listaNu.append(numero)
        lista = listaN, listaP, listaNu

    # VERIFICANDO SE JA EXISTE A CHAVE NO
    # DICIONÁRIO, CASO NÃO EXISTA, INSERIR
    cadastro.setdefault(numero, candidato)


    print(menu)
    escolha = int(input('Qual a opção escolhida?: '))

{'''votos = nulo = branco = 0

formatacao = ''
# VOTAR EM UM CANDIDATO
while escolha == 1:
    print(
    [0] VOTAR
    [1] ANULAR
    [2] VOTAR EM BRANCO)
    opcao = int(input('Digite a opção desejada: '))
    if opcao == 0:
        print(' ' * 5, '=' * 40)
        print(' ' * 16, 'OS CANDIDATOS SÃO')
        print(' ' * 5, '=' * 40)
        print(' ' * 5, 'CANDIDATO', ' ' * 6, 'PARTIDO', ' ' * 7, 'NÚMERO')
        for c in range(0, len(lista)):
            print(f'\n{formatacao:6}{listaN[c]:16} {listaP[c]:15} {listaNu[c]}', end=" ")
            c += 1

        voto = int(input('\n\nVoto Candidato (número): '))
        votos += 1'''}

nulo = branco = 0
votos = 0
# CRIAÇÃO DO DICIONÁRIO
diciVotos = {numero: votos}
soma = 0

formatacao = ''
#VOTAR EM UM CANDIDATO
while escolha == 1:
    print('''
    [0] VOTAR
    [1] ANULAR
    [2] VOTAR EM BRANCO''')
    opcao = int(input('Digite a opção desejada: '))
    if opcao == 0:
        print(' ' * 5, '=' * 40)
        print(' ' * 16, 'OS CANDIDATOS SÃO')
        print(' ' * 5, '=' * 40)
        print(' ' * 5, 'CANDIDATO', ' ' * 6, 'PARTIDO', ' ' * 7, 'NÚMERO')
        for c in range(0, len(lista)):
            print(f'\n{formatacao:6}{listaN[c]:16} {listaP[c]:15} {listaNu[c]}', end=" ")
            c += 1
        if contagem == 1:
            voto = int(input('Voto Candidato (número): '))
            for varredura in cadastro:
                if voto == varredura:
                    soma += 1
                    numero = voto
                    # SOMA DOS VOTOS
                    diciVotos[varredura] = soma
                    print(diciVotos)
                    soma = 0
        else:
            voto = int(input('\nVoto Candidato (número): '))
            for varredura in cadastro:
                if voto == varredura:
                    soma += 1
                    numero = voto
                    # SOMA DOS VOTOS
                    diciVotos[varredura] = soma
                    print(diciVotos)
                    soma = 0

    if opcao == 1:
        nulo += 1
    if opcao == 2:
        branco += 1

    #IMPRIMINDO MENU
    print(menu)
    escolha = int(input('Qual a opção escolhida?: '))

#GERAR RELATÓRIO
while escolha == 2:
    print(' ' * 5, '=' * 52)
    print(' ' * 28, 'VOTOS')
    print(' ' * 5, '=' * 52)
    print(' ' * 5, 'CANDIDATO', ' ' * 6, 'PARTIDO', ' ' * 7, 'NÚMERO', ' ' * 5, 'VOTOS')
    print(f'O candidato {voto} recebeu {votos} votos')
    print(f'Tiveram {branco} votos brancos')
    print(f'Tiveram {nulo} votos nulos')

    # IMPRIMINDO MENU
    print(menu)
    escolha = int(input('Qual a opção escolhida?: '))

#FINALIZAR VOTAÇÃO
if escolha == 3:
    print('O PROGRAMA SERÁ ENCERRADO')
    sleep(2)
    print('Obrigado por votar!')
