from time import sleep

print('''========================
     URNA ELETRÔNICA 
========================''')

# menu de opções
menu = ('''
===== MENU DE OPÇÕES =====
[0] Cadastrar um candidato
[1] Votar em um candidato
[2] Gerar relatório
[3] Finalizar votação
''')
print(menu)
escolha = int(input('Qual a opção escolhida?: '))
print(escolha)

contagem = 0

# Escolha dentro dos padrões
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
        # print(candidato)
        # print(cadastro)
        print('=========')
        listaN = [nome]
        listaP = [partido]
        listaNu = [numero]
    else:
        print(contagem)
        # candidato.append(str(input('Nome: ')))
        # candidato.append(str(input('Partido: ')))
        nome = str(input('Nome: '))
        partido = str(input('Partido: '))
        numero = int(input('Número: '))
        candidato = [nome, partido]
        cadastro.update({numero: candidato})
        print('=========')
        # print(f'{cadastro}')
        print('=========')
        listaN.append(nome)
        listaP.append(partido)
        listaNu.append(numero)

    # VERIFICANDO SE JA EXISTE A CHAVE NO
    # DICIONÁRIO, CASO NÃO EXISTA, INSERIR
    cadastro.setdefault(numero, candidato)

    print(menu)
    escolha = int(input('Qual a opção escolhida?: '))

votos = nulo = branco = 0

# VOTAR EM UM CANDIDATO
while escolha == 1:
    print('''
    [0] VOTAR
    [1] ANULAR
    [2] VOTAR EM BRANCO''')
    opcao = int(input('Digite a opção desejada: '))
    if opcao == 0:
        print(f'''        =====================
          OS CANDIDATOS SÃO
        =====================
      Número    Candidato       Partido
''')

        print(listaN, listaP, listaNu)

        voto = int(input('\n\nVoto Candidato (número): '))
        votos += 1
    if opcao == 1:
        nulo += 1
    if opcao == 2:
        branco += 1

    # IMPRIMINDO MENU
    print(menu)
    escolha = int(input('Qual a opção escolhida?: '))

# GERAR RELATÓRIO
while escolha == 2:
    print(f'O candidato {voto} recebeu {votos} votos')
    print(f'Tiveram {branco} votos brancos')
    print(f'Tiveram {nulo} votos nulos')

    # IMPRIMINDO MENU
    print(menu)
    escolha = int(input('Qual a opção escolhida?: '))

# FINALIZAR VOTAÇÃO
if escolha == 3:
    print('O PROGRAMA SERÁ ENCERRADO')
    sleep(2)
    print('Obrigado por votar!')
