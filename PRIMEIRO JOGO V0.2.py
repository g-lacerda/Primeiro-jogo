#Ainda falta acabar a mochila, loja grande, xp, lvl, armas, passivas, + classes...

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
            if comprar == 2:
                if moedas < 5:
                    print('Você não tem dinheiro suficiente')
                if moedas >= 5:
                    namochila = [item2]
                    moedas = moedas - 5
            if comprar == 3:
                if moedas < 5:
                    print('Você não tem dinheiro suficiente')
                if moedas >= 5:
                    namochila = [item3]
                    moedas = moedas - 5
        #Mochila
        if decisao == 2:
            namochila = '-'.join(namochila)
            qtdpothp = namochila.find('Poção de vida') + 1
            qtdpotdm = namochila.find('Poção de dano mágico') + 1
            qtdbomba = namochila.find('Bomba') + 1
            qtdescudo = namochila.find('Escudo') + 1
            qtdpotdf = namochila.find('Poção de dano físico') + 1
            print ('Você tem {} Poções de vida, {} Poções de dano mágico, {} poções de dano físico, {} bombas, {} escudos'.format(qtdpothp, qtdpotdm, qtdpotdf, qtdbomba, qtdescudo))
        #Atacar
        if decisao == 1:
            if aleat == 1:
                if classe != 3:
                    dano = ((fdmg + (trunc((mdmg / 2)))))
                    restohp = restohp - dano
                    print('\033[97m━\033[m' * 35)
                    sleep(1)
                    print('\033[1;30;107mVocê causou \033[m\033[1;31;107m{}\033[1;30;107m de dano.\033[m'.format(
                        fdmg + (trunc((mdmg / 2)))))
                    sleep(1)
            if aleat == 2:
                if classe != 3:
                    dano = ((fdmg + (trunc((mdmg / 2))))-dminimigodm)
                    restohp = restohp - dano
                    print('\033[97m━\033[m' * 35)
                    sleep(1)
                    print('\033[1;30;107mVocê causou \033[m\033[1;31;107m{}\033[1;30;107m de dano.\033[m'.format(
                        fdmg + (trunc((mdmg / 2)))))
                    sleep(1)
            if aleat == 3 :
                if classe != 3:
                    dano = ((fdmg + (trunc((mdmg / 2))))-dfinimigodf)
                    restohp = restohp - dano
                    print('\033[97m━\033[m' * 35)
                    sleep(1)
                    print('\033[1;30;107mVocê causou \033[m\033[1;31;107m{}\033[1;30;107m de dano.\033[m'.format(
                        fdmg + (trunc((mdmg / 2)))))
                    sleep(1)
            if aleat == 1:
                if classe == 3:
                    dano = (((trunc(fdmg / 2)) + mdmg))
                    restohp = restohp - dano
                    print('\033[97m━\033[m' * 35)
                    sleep(1)
                    print('\033[1;30;107mVocê causou \033[m\033[1;31;107m{}\033[1;30;107m de dano.\033[m'.format(dano))
                    sleep(1)
            if aleat == 2:
                if classe == 3:
                    dano = (((trunc(fdmg / 2)) + mdmg)-dminimigodm)
                    restohp = restohp - dano
                    print('\033[97m━\033[m' * 35)
                    sleep(1)
                    print('\033[1;30;107mVocê causou \033[m\033[1;31;107m{}\033[1;30;107m de dano.\033[m'.format(dano))
                    sleep(1)
            if aleat == 3:
                if classe == 3:
                    dano = (((trunc(fdmg / 2)) + mdmg)-dfinimigodf)
                    restohp = restohp - dano
                    print('\033[97m━\033[m' * 35)
                    sleep(1)
                    print('\033[1;30;107mVocê causou \033[m\033[1;31;107m{}\033[1;30;107m de dano.\033[m'.format(dano))
                    sleep(1)
        #Sofrendo dano caso o inimigo não morra
        if restohp > 0:
            hp = hp - dmginimigo
            print('\033[1;97;40mVocê sofreu \033[1;31;40m{}\033[1;97;40m de dano.\033[m'.format(dmginimigo))
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