#Ainda falta loja grande, xp, lvl, armas, passivas, + classes...

from random import randint
from time import sleep
from math import trunc

tentar = 1
moedas = 0
namochila = []


while (tentar == 1):
    classe = int(input(
        '\033[1;32;40mEscolha a sua classe:\033[m\n\n \033[1;97;40m1.\033[1;97;40m Guerreiro\033[m\n  \033[1;31;40mHP: 15\033[m\n  \033['
        '1;31;40mDano '
        'físico: 8\033[m\n  \033[1;31;40mDano mágico: 0\033[m\n\n \033[1;97;40m2.Tank\033[m\n  \033[1;31;40mHP: 25\033[m\n  \033[1;31;40mDano físico: 5\033[m\n  '
        '\033[1;31;40mDano '
        'mágico: 0\033[m\n\n \033[1;97;40m3.Mago\033[m\n  \033[1;31;40mHP: 10\033[m\n  \033[1;31;40mDano físico: 0\033[m\n  \033[1;31;40mDano mágico: 12\033[m\n\n  \033[97;40m━━━━▶\033[m'
        ))
    #Apenas ações válidas
    while (classe < 1):
        classe = int(input('Selecione uma opção válida: '))
        while (classe > 3):
            classe = int(input('Selecione uma opção válida: '))
    while (classe > 3):
        classe = int(input('Selecione uma opção válida: '))
        while (classe < 1):
            classe = int(input('Selecione uma opção válida: '))

    #Guerreiro
    if classe == 1:
        hpbase = 15
        fdmg = 8
        mdmg = 0
        sleep(0.25)
        print('\033[1;30;107mVocê escolheu a classe\033[m\033[1;34;107m GUERREIRO\033[m\033[m\033[1;30;107m!\033[m')
        sleep(0.55)
    #Tank
    if classe == 2:
        hpbase = 25
        fdmg = 5
        mdmg = 0
        sleep(0.25)
        print('\033[1;30;107mVocê escolheu a classe\033[m\033[1;32;107m TANK\033[m\033[m\033[1;30;107m!\033[m')
        sleep(0.55)
    #Mago
    if classe == 3:
        hpbase = 10
        fdmg = 0
        mdmg = 12
        sleep(0.25)
        print('\033[1;30;107mVocê escolheu a classe\033[m\033[1;35;107m MAGO\033[m\033[m\033[1;30;107m!\033[m')
        sleep(0.55)

    hp = hpbase
    dmginimigo = 6

    #Atributos Inimigo DF
    hpinimigodf = 15
    dfinimigodf = 0
    dminimigodf = 3
    #Atributos Inimigo DM
    hpinimigodm = 15
    dfinimigodm = 0
    dminimigodm = 3
    #Atributos Inimigo HP
    hpinimigohp = 20
    dfinimigohp = 0
    dminimigohp = 0

    sleep(1)

    fase = 1
    print('Fase 1')
    #Aleatoriedade inimigo
    aleat = randint (1, 3)
    if aleat == 1:
        sleep(0.5)
        print('Seu inimigo será INIMIGO HP')
    if aleat == 2:
        sleep(0.5)
        print('Seu inimigo será INIMIGO DM')
    if aleat == 3:
        sleep(0.5)
        print('Seu inimigo será INIMIGO DF')

    #Recuperar vida dos inimigos ao passar de fase
    if aleat == 1:
        restohp = 20
    else:
        restohp = 15

    #Loja aleatória nao repetir itens
    while (hp > 0):
        randloja1 = randint(1, 5)
        randloja2 = randint(1, 5)
        while randloja2 == randloja1:
            randloja2 = randint(1, 5)
        randloja3 = randint(1, 5)
        while randloja3 == randloja1:
            randloja3 = randint(1, 5)
            while randloja3 == randloja2:
                randloja3 = randint(1, 5)
        while randloja3 == randloja2:
            randloja3 = randint(1, 5)
            while randloja3 == randloja1:
                randloja3 = randint(1, 5)
        #Aleatoriedade loja aleatória
        if randloja1 == 1:
            item1 = 'Poção de vida'
        elif randloja1 == 2:
            item1 = 'Escudo'
        elif randloja1 == 3:
            item1 = 'Poção de dano mágico'
        elif randloja1 == 4:
            item1 = 'Poção de dano físico'
        elif randloja1 == 5:
            item1 = 'Bomba'
        if randloja2 == 1:
            item2 = 'Poção de vida'
        elif randloja2 == 2:
            item2 = 'Escudo'
        elif randloja2 == 3:
            item2 = 'Poção de dano mágico'
        elif randloja2 == 4:
            item2 = 'Poção de dano físico'
        elif randloja2 == 5:
            item2 = 'Bomba'
        if randloja3 == 1:
            item3 = 'Poção de vida'
        elif randloja3 == 2:
            item3 = 'Escudo'
        elif randloja3 == 3:
            item3 = 'Poção de dano mágico'
        elif randloja3 == 4:
            item3 = 'Poção de dano físico'
        elif randloja3 == 5:
            item3 = 'Bomba'
        #Pós morte inimigo HP
        if aleat == 1:
            if restohp <= 0:
                print('\n\033[1;32;107mVocê derrotou INIMIGO HP!\033[m')
                #Vida recuperada e moedas ganhas depois de matar o inimigo
                hp = hp + 5
                moedas = moedas + 2
                print('\n\033[30;107mVocê ganhou \033[1;33m2 moedas\033[30;107m!\033[m\n\033[30;107mSuas moedas: \033[1;33m{}\033[30;107m moedas\033[m'.format(moedas))
                # Vida não passar do limite
                if classe == 1:
                    if hp > 15:
                        hp = 15
                if classe == 2:
                    if hp > 25:
                        hp = 25
                if classe == 3:
                    if hp > 10:
                        hp = 10
                print('\n\033[1;30;107mVocê restaurou \033[1;31;107m5 HP. \033[1;30;107mSua vida: \033[1;31;107m{}/10\033[m'.format(hp))
                print('\033[97m━\033[m' * 35)
                fase = fase + 1
                print('Fase {}'.format(fase))
                aleat = randint(1, 3)
                #Aleatoriedade próximo inimigo
                if aleat == 1:
                    restohp = 20
                    sleep(0.5)
                    dfinimigoa = 0
                    dminimigoa = 0
                    print('Seu inimigo será INIMIGO HP')
                elif aleat == 2:
                    restohp = 15
                    sleep(0.5)
                    dfinimigoa = 0
                    dminimigoa = 3
                    print('Seu inimigo será INIMIGO DM')
                elif aleat == 3:
                    restohp = 15
                    dfinimigoa = 3
                    dminimigoa = 0
                    print('Seu inimigo será INIMIGO DF')
        #Pós morte inimigo DM
        if aleat == 2:
            if restohp <= 0:
                print('\n\033[1;32;107mVocê derrotou INIMIGO DM!\033[m')
                #Vida recuperada e moedas ganhas depois de matar o inimigo
                hp = hp + 5
                moedas = moedas + 2
                print('\n\033[30;107mVocê ganhou \033[1;33m2 moedas\033[30;107m!\033[m\n\033[30;107mSuas moedas: \033[1;33m{}\033[30;107m moedas\033[m'.format(moedas))
                #Vida não passar do limite
                if classe == 1:
                    if hp > 15:
                        hp = 15
                if classe == 2:
                    if hp > 25:
                        hp = 25
                if classe == 3:
                    if hp > 10:
                        hp = 10
                print('\n\033[1;30;107mVocê restaurou \033[1;31;107m5 HP. \033[1;30;107mSua vida: \033[1;31;107m{}/10\033[m'.format(hp))
                print('\033[97m━\033[m' * 35)
                fase = fase + 1
                print('Fase {}'.format(fase))
                aleat = randint(1, 3)
                #Aleatoriedade próximo inimigo
                if aleat == 1:
                    restohp = 20
                    sleep(0.5)
                    dfinimigoa = 0
                    dminimigoa = 0
                    print('Seu inimigo será INIMIGO HP')
                elif aleat == 2:
                    restohp = 15
                    sleep(0.5)
                    dfinimigoa = 0
                    dminimigoa = 3
                    print('Seu inimigo será INIMIGO DM')
                elif aleat == 3:
                    restohp = 15
                    sleep(0.5)
                    dfinimigoa = 3
                    dminimigoa = 0
                    print('Seu inimigo será INIMIGO DF')
        #Pós morte inimigo DF
        if aleat == 3:
            if restohp <= 0:
                print('\n\033[1;32;107mVocê derrotou INIMIGO DF!\033[m')
                #Vida recuperada e moedas ganhas depois de matar o inimigo
                hp = hp + 5
                moedas = moedas + 2
                print('\n\033[30;107mVocê ganhou \033[1;33m2 moedas\033[30;107m!\033[m\n\033[30;107mSuas moedas: \033[1;33m{}\033[30;107m moedas\033[m'.format(moedas))
                #Vida não passar do limite
                if classe == 1:
                    if hp > 15:
                        hp = 15
                if classe == 2:
                    if hp > 25:
                        hp = 25
                if classe == 3:
                    if hp > 10:
                        hp = 10
                print('\n\033[1;30;107mVocê restaurou \033[1;31;107m5 HP. \033[1;30;107mSua vida: \033[1;31;107m{}/10\033[m'.format(hp))
                print('\033[97m━\033[m' * 35)
                fase = fase + 1
                print('Fase {}'.format(fase))
                aleat = randint(1, 3)
                #Aleatoriedade próximo inimigo
                if aleat == 1:
                    restohp = 20
                    sleep(0.5)
                    dfinimigoa = 0
                    dminimigoa = 0
                    print('Seu inimigo será INIMIGO HP')
                elif aleat == 2:
                    restohp = 15
                    sleep(0.5)
                    dfinimigoa = 0
                    dminimigoa = 3
                    print('Seu inimigo será INIMIGO DM')
                elif aleat == 3:
                    restohp = 15
                    sleep(0.5)
                    dfinimigoa = 3
                    dminimigoa = 0
                    print('Seu inimigo será INIMIGO DF')
        #Info inimigo
        if aleat == 1:
            sleep(1)
            print('\033[97m━\033[m' * 35)
            print('\nINIMIGO HP\nHP: {}/20\nDefesa física: 0\nDefesa mágica: 0'.format(restohp))
            sleep(1)
            print('\033[97m━\033[m' * 35)
        #Info inimigo
        if aleat == 2:
            sleep(1)
            print('\033[97m━\033[m' * 35)
            print('\nINIMIGO DM\nHP: {}/15\nDefesa física: 0\nDefesa mágica: 3'.format(restohp))
            sleep(1)
            print('\033[97m━\033[m' * 35)
        #Info inimigo
        if aleat == 3:
            sleep(1)
            print('\033[97m━\033[m' * 35)
            print('\nINIMIGO DF\nHP: {}/15\nDefesa física: 3\nDefesa mágica: 0'.format(restohp))
            print('\033[97m━\033[m' * 35)
            sleep(1)
        sleep(1)
        #Info pessoal
        print('\033[30;107mSeu HP: \033[1;31;107m{}/{}\033[m'.format(hp, hpbase))
        #Zerando escudo
        escudo = 0
        #Ações
        decisao = int(input('O que deseja fazer?\n1. Atacar\n2. Mochila\n3. Loja aleatória\n\033[97m━━━━▶\033[m '))
        #Apenas ações válidas
        while (decisao < 1):
            decisao = int(input('Selecione uma opção válida: '))
            while (decisao > 3):
                decisao = int(input('Selecione uma opção válida: '))
        while (decisao > 3):
            decisao = int(input('Selecione uma opção válida: '))
            while (decisao < 1):
                decisao = int(input('Selecione uma opção válida: '))
        #Loja aleatória
        while decisao == 3:
            comprar = int(input('Loja de consumíveis:\n1. {}\n2. {}\n3. {}\n4. Voltar\n\033[97m━━━━▶\033[m '.format(item1, item2, item3)))
            print ('Cada item custa 5 moedas')
            if comprar == 4:
                decisao = int(
                    input('O que deseja fazer?\n1. Atacar\n2. Mochila\n3. Loja aleatória\n\033[97m━━━━▶\033[m '))
                while (decisao < 1):
                    decisao = int(input('Selecione uma opção válida: '))
                    while (decisao > 3):
                        decisao = int(input('Selecione uma opção válida: '))
                while (decisao > 3):
                    decisao = int(input('Selecione uma opção válida: '))
                    while (decisao < 1):
                        decisao = int(input('Selecione uma opção válida: '))
            #Compras
            if comprar == 1:
                if moedas < 5:
                    print('Você não tem dinheiro suficiente')
                if moedas >= 5:
                    namochila = namochila + [item1]
                    moedas = moedas - 5
                    print ('Você comprou {}'.format(item1))
                    print('Agora você tem {} moedas'.format(moedas))
            if comprar == 2:
                if moedas < 5:
                    print('Você não tem dinheiro suficiente')
                if moedas >= 5:
                    namochila = [item2]
                    moedas = moedas - 5
                    print('Você comprou {}'.format(item2))
                    print('Agora você tem {} moedas'.format(moedas))
            if comprar == 3:
                if moedas < 5:
                    print('Você não tem dinheiro suficiente')
                if moedas >= 5:
                    namochila = [item3]
                    moedas = moedas - 5
                    print('Você comprou {}'.format(item3))
                    print('Agora você tem {} moedas'.format(moedas))
        #Mochila
        while decisao == 2:
            namochila = '-'.join(namochila)
            qtdpothp = namochila.find('Poção de vida') + 1
            qtdpotdm = namochila.find('Poção de dano mágico') + 1
            qtdbomba = namochila.find('Bomba') + 1
            qtdescudo = namochila.find('Escudo') + 1
            qtdpotdf = namochila.find('Poção de dano físico') + 1
            usar = int(input('Seus itens:\n 1. {}x Poções de vida (recupera 10HP)\n 2. {}x Poções de dano mágico (aumenta 6 de dano mágico)\n 3. {}x Poções de dano físico (aumenta 8 de dano físico)\n 4. {}x Bombas (Causa 15 de dano no inimigo)\n 5. {}x Escudos (você não toma dano nessa rodada)\n 9. Voltar\n\033[97m━━━━▶\033[m'.format(qtdpothp, qtdpotdm, qtdpotdf, qtdbomba, qtdescudo)))
            #Voltar
            if usar == 9:
                decisao = int(
                    input('O que deseja fazer?\n1. Atacar\n2. Mochila\n3. Loja aleatória\n\033[97m━━━━▶\033[m '))
                while (decisao < 1):
                    decisao = int(input('Selecione uma opção válida: '))
                    while (decisao > 3):
                        decisao = int(input('Selecione uma opção válida: '))
                while (decisao > 3):
                    decisao = int(input('Selecione uma opção válida: '))
                    while (decisao < 1):
                        decisao = int(input('Selecione uma opção válida: '))
            #Pot Vida
            if usar == 1:
                if qtdpothp <= 0:
                    print ('Você não tem poções de HP para usar.')
                elif qtdpothp > 0:
                    hp = hp + 10
                    qtdpothp = qtdpothp - 1
                    if hp > hpbase:
                        hp = hpbase
                    print('Você recuperou 10HP')
            #Pot dano mágico
            if usar == 2:
                if qtdpotdm <= 0:
                    print('Você não tem poções de dano mágico para usar.')
                elif qtdpotdm > 0:
                    mdmg = mdmg + 6
                    qtdpotdm = qtdpotdm - 1
                    if classe == 3:
                        print('Você dará {} de dano mágico'.format(mdmg+6))
                    else:
                        print ('Você dará {} de dano misto'.format(fdmg + trunc(mdmg/2)))
            #Pot dano físico
            if usar == 3:
                if qtdpotdm <= 0:
                    print('Você não tem poções de dano físico para usar.')
                elif qtdpotdm > 0:
                    fdmg = fdmg + 8
                    qtdpotdm = qtdpotdm - 1
                    if classe == 3:
                        print('Você dará {} de dano misto'.format(mdmg + trunc(fdmg/2)))
                    else:
                        print ('Você dará {} de dano físico'.format(fdmg + 8))
            #Bomba
            if usar == 4:
                if qtdbomba <= 0:
                    print('Você não tem bombas para usar.')
                if qtdbomba > 0:
                    restohp = restohp - 15
                    qtdbomba = qtdbomba - 1
                    print('Você causou 15 de dano ao inimigo')
                    break

            if usar == 5:
                if qtdescudo <= 0:
                    print('Você não tem escudos para usar.')
                if qtdescudo > 0:
                    qtdescudo = qtdescudo -1
                    escudo = dmginimigo
                    print ('Você está com escudo')
        while decisao == 3:
            comprar = int(input('Loja de consumíveis:\n1. {}\n2. {}\n3. {}\n4. Voltar\n\033[97m━━━━▶\033[m '.format(item1, item2, item3)))
            print('Cada item custa 5 moedas')
            if comprar == 4:
                decisao = int(
                    input('O que deseja fazer?\n1. Atacar\n2. Mochila\n3. Loja aleatória\n\033[97m━━━━▶\033[m '))
                while (decisao < 1):
                    decisao = int(input('Selecione uma opção válida: '))
                    while (decisao > 3):
                        decisao = int(input('Selecione uma opção válida: '))
                while (decisao > 3):
                    decisao = int(input('Selecione uma opção válida: '))
                    while (decisao < 1):
                        decisao = int(input('Selecione uma opção válida: '))
            #Compras
            if comprar == 1:
                if moedas < 5:
                    print('Você não tem dinheiro suficiente')
                if moedas >= 5:
                    namochila = namochila + [item1]
                    moedas = moedas - 5
                    print('Você comprou {}'.format(item1))
                    print('Agora você tem {} moedas'.format(moedas))
            if comprar == 2:
                if moedas < 5:
                    print('Você não tem dinheiro suficiente')
                if moedas >= 5:
                    namochila = [item2]
                    moedas = moedas - 5
                    print('Você comprou {}'.format(item2))
                    print('Agora você tem {} moedas'.format(moedas))
            if comprar == 3:
                if moedas < 5:
                    print('Você não tem dinheiro suficiente')
                if moedas >= 5:
                    namochila = [item3]
                    moedas = moedas - 5
                    print('Você comprou {}'.format(item3))
                    print('Agora você tem {} moedas'.format(moedas))

        #Atacar
        if decisao == 1:
            if aleat == 1:
                if classe != 3:
                    dano = ((fdmg + trunc((mdmg / 2))))
                    restohp = restohp - dano
                    print('\033[97m━\033[m' * 35)
                    sleep(1)
                    print('\033[1;30;107mVocê causou \033[m\033[1;31;107m{}\033[1;30;107m de dano.\033[m'.format(
                        fdmg + trunc((mdmg / 2))))
                    sleep(1)
            if aleat == 2:
                if classe != 3:
                    dano = ((fdmg + trunc((mdmg / 2)))-dminimigodm)
                    restohp = restohp - dano
                    print('\033[97m━\033[m' * 35)
                    sleep(1)
                    print('\033[1;30;107mVocê causou \033[m\033[1;31;107m{}\033[1;30;107m de dano.\033[m'.format(
                        fdmg + trunc((mdmg / 2))))
                    sleep(1)
            if aleat == 3 :
                if classe != 3:
                    dano = ((fdmg + trunc((mdmg / 2)))-dfinimigodf)
                    restohp = restohp - dano
                    print('\033[97m━\033[m' * 35)
                    sleep(1)
                    print('\033[1;30;107mVocê causou \033[m\033[1;31;107m{}\033[1;30;107m de dano.\033[m'.format(
                        fdmg + trunc((mdmg / 2))))
                    sleep(1)
            if aleat == 1:
                if classe == 3:
                    dano = (trunc(fdmg / 2) + mdmg)
                    restohp = restohp - dano
                    print('\033[97m━\033[m' * 35)
                    sleep(1)
                    print('\033[1;30;107mVocê causou \033[m\033[1;31;107m{}\033[1;30;107m de dano.\033[m'.format(dano))
                    sleep(1)
            if aleat == 2:
                if classe == 3:
                    dano = ((trunc(fdmg / 2) + mdmg)-dminimigodm)
                    restohp = restohp - dano
                    print('\033[97m━\033[m' * 35)
                    sleep(1)
                    print('\033[1;30;107mVocê causou \033[m\033[1;31;107m{}\033[1;30;107m de dano.\033[m'.format(dano))
                    sleep(1)
            if aleat == 3:
                if classe == 3:
                    dano = ((trunc(fdmg / 2) + mdmg)-dfinimigodf)
                    restohp = restohp - dano
                    print('\033[97m━\033[m' * 35)
                    sleep(1)
                    print('\033[1;30;107mVocê causou \033[m\033[1;31;107m{}\033[1;30;107m de dano.\033[m'.format(dano))
                    sleep(1)
        #Sofrendo dano caso o inimigo não morra
        if restohp > 0:
            hp = hp - (+ dmginimigo - escudo)
            print('\033[1;97;40mVocê sofreu \033[1;31;40m{}\033[1;97;40m de dano.\033[m'.format(+ dmginimigo - escudo))
    #Caso o jogador morra
    if hp < 0:
        print('Você morreu :(')
        tentar = int(input('Você deseja tentar de novo?\n1. Sim\n2.Não'))
        # Apenas ações válidas
        while (tentar < 1):
            tentar = int(input('Selecione uma opção válida: '))
            while (tentar > 2):
                tentar = int(input('Selecione uma opção válida: '))
        while (tentar > 2):
            tentar = int(input('Selecione uma opção válida: '))
            while (tentar < 1):
                tentar = int(input('Selecione uma opção válida: '))
        #Quit
        if tentar == 2:
            print('Muito obrigado, até mais! :)')