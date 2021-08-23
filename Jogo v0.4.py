from random import randint
from time import sleep
from math import trunc

fase = 1
recorde = 1
tentar = 1
moedas = 0
namochila = 'a '
fdpot = 0
mdpot = 0
tentativa = 1
tentativapontuacaomaisalta = 1

while (tentar == 1):
    classe = int(input(
        '\033[1;32;40mEscolha a sua classe:\033[m\n\n \033[1;97;40m1.\033[1;97;40m Guerreiro\033[m\n  \033[1;31;40mHP: 25\033[m\n  \033['
        '1;31;40mDano '
        'físico: 10\033[m\n  \033[1;31;40mDano mágico: 0\033[m\n\n \033[1;97;40m2.Tank\033[m\n  \033[1;31;40mHP: 30\033[m\n  \033[1;31;40mDano físico: 8\033[m\n  '
        '\033[1;31;40mDano '
        'mágico: 0\033[m\n\n \033[1;97;40m3.Mago\033[m\n  \033[1;31;40mHP: 14\033[m\n  \033[1;31;40mDano físico: 0\033[m\n  \033[1;31;40mDano mágico: 12\033[m\n\n  \033[97;40m━━━━▶\033[m'
        ))
    print('\033[97m━\033[m' * 35)
    #Apenas ações válidas
    while (classe < 1):
        classe = int(input('Selecione uma opção válida: '))
        while (classe > 3):
            classe = int(input('Selecione uma opção válida: '))
    while (classe > 3):
        classe = int(input('Selecione uma opção válida: '))
        while (classe < 1):
            classe = int(input('Selecione uma opção válida: '))

    #Classes
    if classe == 1:
        hpbase = 25
        dmbase = 0
        dfbase = 10
        print('\033[1;30;107mVocê escolheu a classe\033[m\033[1;34;107m GUERREIRO\033[m\033[m\033[1;30;107m!\033[m')
    if classe == 2:
        hpbase = 30
        dmbase = 0
        dfbase = 8
        print('\033[1;30;107mVocê escolheu a classe\033[m\033[1;32;107m TANK\033[m\033[m\033[1;30;107m!\033[m')
    if classe == 3:
        hpbase = 14
        dmbase = 12
        dfbase = 0
        print('\033[1;30;107mVocê escolheu a classe\033[m\033[1;35;107m MAGO\033[m\033[m\033[1;30;107m!\033[m')

    hp = hpbase
    danoinimigo = 6

    inimigo = randint(1, 3)

    #Inimigos
    #Inimigo HP
    if inimigo == 1:
        hpbaseinimigo = 20
        rfbaseinimigo = 0
        rmbaseinimigo = 0
        inimigostr = 'Inimigo HP'
    #Inimigo Resistência Mágica
    if inimigo == 2:
        hpbaseinimigo = 15
        rfbaseinimigo = 0
        rmbaseinimigo = 3
        inimigostr = 'Inimigo RM'
    #Inimigo Resistência Física
    if inimigo == 3:
        hpbaseinimigo = 15
        rfbaseinimigo = 3
        rmbaseinimigo = 0
        inimigostr = 'Inimigo RF'

    hpinimigo = hpbaseinimigo
    rfinimigo = rfbaseinimigo
    rminimigo = rmbaseinimigo

    print('\033[97m━\033[m' * 35)
    print ('\033[30;107mFase {}\033[m'.format(fase))
    print ('Seu inimigo será {}'.format(inimigostr))
    print('\n{}\nHP:{}/{}\nResistência mágica: {}\nResistência física: {}'.format(inimigostr, hpinimigo, hpbaseinimigo,
                                                                                  rminimigo, rfinimigo))
    print('\033[97m━\033[m' * 35)
    print('\033[30;107mSeu HP: \033[1;31;107m{}/{}\033[m'.format(hp, hpbase))

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
        # Aleatoriedade loja aleatória
        if randloja1 == 1:
            item1 = 'Poção de vida '
        elif randloja1 == 2:
            item1 = 'Escudo '
        elif randloja1 == 3:
            item1 = 'Poção de dano mágico '
        elif randloja1 == 4:
            item1 = 'Poção de dano físico '
        elif randloja1 == 5:
            item1 = 'Bomba '
        if randloja2 == 1:
            item2 = 'Poção de vida '
        elif randloja2 == 2:
            item2 = 'Escudo '
        elif randloja2 == 3:
            item2 = 'Poção de dano mágico '
        elif randloja2 == 4:
            item2 = 'Poção de dano físico '
        elif randloja2 == 5:
            item2 = 'Bomba '
        if randloja3 == 1:
            item3 = 'Poção de vida '
        elif randloja3 == 2:
            item3 = 'Escudo '
        elif randloja3 == 3:
            item3 = 'Poção de dano mágico '
        elif randloja3 == 4:
            item3 = 'Poção de dano físico '
        elif randloja3 == 5:
            item3 = 'Bomba '
        #Pós morte inimigo
        if hpinimigo <= 0:
            print('\n\033[1;32;107mVocê derrotou {}!\033[m'.format(inimigostr))
            hp = hp + 5
            if hp > hpbase:
                hp = hpbase
            moedas = moedas + 2
            fase = fase + 1
            if fase > recorde:
                recorde = fase
                tentativapontuacaomaisalta = tentativa
            #Moedas ganhas
            print(
                '\n\033[30;107mVocê ganhou \033[1;33m2 moedas\033[30;107m!\033[m\n\033[30;107mSuas moedas: \033[1;33m{}\033[30;107m moedas\033[m'.format(
                    moedas))
            #Vida recuperada
            print(
                '\n\033[1;30;107mVocê restaurou \033[1;31;107m5 HP. \033[1;30;107mSua vida: \033[1;31;107m{}/{}\033[m'.format(
                    hp, hpbase))
            print('\033[97m━\033[m' * 35)
            print('\033[30;107mFase {}\033[m'.format(fase))
            inimigo = randint(1, 3)
            # Inimigos
            # Inimigo HP
            if inimigo == 1:
                hpinimigo = 20
                rfinimigo = 0
                rminimigo = 0
                inimigostr = 'Inimigo HP'
                print('Seu inimigo será {}'.format(inimigostr))
            # Inimigo Resistência Mágica
            if inimigo == 2:
                hpinimigo = 15
                rfinimigo = 0
                rminimigo = 3
                inimigostr = 'Inimigo RM'
                print('Seu inimigo será {}'.format(inimigostr))
            # Inimigo Resistência Física
            if inimigo == 3:
                hpinimigo = 15
                rfinimigo = 3
                rminimigo = 0
                inimigostr = 'Inimigo RF'
                print('Seu inimigo será {}'.format(inimigostr))
            hpbaseinimigo = hpinimigo
            print('\033[97m━\033[m' * 35)
            print ('{}\nHP:{}/{}\nResistência mágica: {}\nResistência física: {}'.format(inimigostr, hpinimigo, hpbaseinimigo, rminimigo, rfinimigo))
            print('\033[97m━\033[m' * 35)
            print('\033[30;107mSeu HP: \033[1;31;107m{}/{}\033[m'.format(hp, hpbase))
        escudo = 0

        decisao = int(input('O que deseja fazer?\n1. Atacar\n2. Mochila\n3. Loja aleatória\n\033[97m━━━━▶\033[m '))
        while (decisao < 1):
            decisao = int(input('Selecione uma opção válida: '))
            while (decisao > 3):
                decisao = int(input('Selecione uma opção válida: '))
        while (decisao > 3):
            decisao = int(input('Selecione uma opção válida: '))
            while (decisao < 1):
                decisao = int(input('Selecione uma opção válida: '))
        while decisao == 3:
            print('Cada item custa 5 moedas')
            print('Você tem {} moedas'.format(moedas))
            comprar = int(input(
                'Loja de consumíveis:\n1. {}\n2. {}\n3. {}\n9. Voltar\n\033[97m━━━━▶\033[m '.format(item1, item2,
                                                                                                    item3)))
            if comprar == 9:
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
            # Compras
            if comprar == 1:
                if moedas < 5:
                    print('Você não tem dinheiro suficiente')
                if moedas >= 5:
                    namochila = namochila + item1
                    moedas = moedas - 5
                    print('Você comprou {}'.format(item1))
                    print('Agora você tem {} moedas'.format(moedas))
            if comprar == 2:
                if moedas < 5:
                    print('Você não tem dinheiro suficiente')
                if moedas >= 5:
                    namochila = namochila + item2
                    moedas = moedas - 5
                    print('Você comprou {}'.format(item2))
                    print('Agora você tem {} moedas'.format(moedas))
            if comprar == 3:
                if moedas < 5:
                    print('Você não tem dinheiro suficiente')
                if moedas >= 5:
                    namochila = namochila + item3
                    moedas = moedas - 5
                    print('Você comprou {}'.format(item3))
                    print('Agora você tem {} moedas'.format(moedas))
        while decisao == 2:
            #namochila = ' '.join(namochila)
            qtdpothp = namochila.count('Poção de vida ')
            qtdpotdm = namochila.count('Poção de dano mágico ')
            qtdbomba = namochila.count('Bomba ')
            qtdescudo = namochila.count('Escudo ')
            qtdpotdf = namochila.count('Poção de dano físico ')
            #namochila.split()
            usar = int(input(
                'Seus itens:\n 1. {}x Poções de vida (recupera 10HP)\n 2. {}x Poções de dano mágico (aumenta 6 de dano mágico)\n 3. {}x Poções de dano físico (aumenta 8 de dano físico)\n 4. {}x Bombas (Causa 15 de dano no inimigo)\n 5. {}x Escudos (você não toma dano nessa rodada)\n 9. Voltar\n\033[97m━━━━▶\033[m'.format(
                    qtdpothp, qtdpotdm, qtdpotdf, qtdbomba, qtdescudo)))
            # Voltar
            if usar == 9:
                decisao = int(
                    input(
                        'O que deseja fazer?\n1. Atacar\n2. Mochila\n3. Loja aleatória\n\033[97m━━━━▶\033[m '))
                while (decisao < 1):
                    decisao = int(input('Selecione uma opção válida: '))
                    while (decisao > 3):
                        decisao = int(input('Selecione uma opção válida: '))
                while (decisao > 3):
                    decisao = int(input('Selecione uma opção válida: '))
                    while (decisao < 1):
                        decisao = int(input('Selecione uma opção válida: '))
            if usar == 1:
                if qtdpothp <= 0:
                    print('Você não tem poções de HP para usar.')
                elif qtdpothp > 0:
                    hp = hp + 10
                    namochila = namochila.replace('Poção de vida ', '')
                    if hp > hpbase:
                        hp = hpbase
                    print('Você recuperou 10HP')
                    print('\033[30;107mSeu HP: \033[1;31;107m{}/{}\033[m'.format(hp, hpbase))
            # Pot dano mágico
            if usar == 2:
                if qtdpotdm <= 0:
                    print('Você não tem poções de dano mágico para usar.')
                elif qtdpotdm > 0:
                    mdpot = 6
                    namochila = namochila.replace('Poção de dano mágico ', '')
                    if classe == 3:
                        print('Você dará {} de dano mágico'.format(dmbase + 6))
                    else:
                        print('Você dará {} de dano misto'.format(dfbase + trunc((dmbase + mdpot) / 2)))
            # Pot dano físico
            if usar == 3:
                if qtdpotdf <= 0:
                    print('Você não tem poções de dano físico para usar.')
                elif qtdpotdf > 0:
                    fdpot = 8
                    namochila = namochila.replace('Poção de dano físico ', '')
                    if classe == 3:
                        print('Você dará {} de dano misto'.format(dmbase + trunc((dfbase + fdpot) / 2)))
                    else:
                        print('Você dará {} de dano físico'.format(dfbase + 8))
            # Bomba
            if usar == 4:
                if qtdbomba <= 0:
                    print('Você não tem bombas para usar.')
                if qtdbomba > 0:
                    hpinimigo = hpinimigo - 15
                    namochila = namochila.replace('Bomba ', '')
                    print('Você causou 15 de dano ao inimigo')
                    break

            if usar == 5:
                if qtdescudo <= 0:
                    print('Você não tem escudos para usar.')
                if qtdescudo > 0:
                    namochila = namochila.replace('Escudo ', '')
                    escudo = danoinimigo
                    print('Você está com escudo')
        while decisao == 3:
            print('Cada item custa 5 moedas')
            print('Você tem {} moedas'.format(moedas))
            comprar = int(input(
                'Loja de consumíveis:\n1. {}\n2. {}\n3. {}\n9. Voltar\n\033[97m━━━━▶\033[m '.format(item1,
                                                                                                    item2,
                                                                                                    item3)))
            if comprar == 9:
                decisao = int(
                    input(
                        'O que deseja fazer?\n1. Atacar\n2. Mochila\n3. Loja aleatória\n\033[97m━━━━▶\033[m '))
                while (decisao < 1):
                    decisao = int(input('Selecione uma opção válida: '))
                    while (decisao > 3):
                        decisao = int(input('Selecione uma opção válida: '))
                while (decisao > 3):
                    decisao = int(input('Selecione uma opção válida: '))
                    while (decisao < 1):
                        decisao = int(input('Selecione uma opção válida: '))
        if decisao == 1:
            if classe == 3:
                danomagico = dmbase + mdpot
                danofisico = trunc((dfbase + fdpot) / 2)
                danomagicototal = danomagico - rminimigo
                if danomagicototal < 0:
                    danomagicototal = 0
                danofisicototal = danofisico - rfinimigo
                if danofisicototal < 0:
                    danofisicototal = 0
                danototal = (danomagicototal) + (danofisicototal)
                if danototal < 0:
                    danototal = 0
                hpinimigo = hpinimigo - danototal
                print('\033[97m━\033[m' * 35)
                print(
                    '\033[1;30;107mVocê causou \033[m\033[1;31;107m{}\033[1;30;107m de dano, sendo \033[1;31;107m{}\033[1;30;107m dano mágico e \033[1;31;107m{}\033[1;30;107m dano físico.\033[m'.format(
                        danototal, danomagicototal, danofisicototal))
            else:
                danomagico = trunc((dmbase + mdpot) / 2)
                danofisico = dfbase + fdpot
                danofisicototal = danofisico - rfinimigo
                if danofisicototal < 0:
                    danofisicototal = 0
                danomagicototal = danomagico - rminimigo
                if danomagicototal < 0:
                    danomagicototal = 0
                danototal = (danomagicototal) + (danofisicototal)
                if danototal < 0:
                    danototal = 0
                hpinimigo = hpinimigo - danototal
                print('\033[97m━\033[m' * 35)
                print(
                    '\033[1;30;107mVocê causou \033[m\033[1;31;107m{}\033[1;30;107m de dano, sendo \033[1;31;107m{}\033[1;30;107m dano mágico e \033[1;31;107m{}\033[1;30;107m dano físico.\033[m'.format(
                        danototal, danomagicototal, danofisicototal))
        if hpinimigo > 0:
            print('\n{}\nHP: {}/{}\nDefesa física: {}\nDefesa mágica: {}'.format(inimigostr, hpinimigo, hpbaseinimigo,
                                                                                 rfinimigo, rminimigo))
        print('\033[97m━\033[m' * 35)
        if hpinimigo > 0:
            hp = hp - (danoinimigo - escudo)
            print('\033[1;97;40mVocê sofreu \033[1;31;40m{}\033[1;97;40m de dano.\033[m'.format(
                + danoinimigo - escudo))
            print('\033[30;107mSeu HP: \033[1;31;107m{}/{}\033[m'.format(hp, hpbase))
        fdpot = 0
        mdpot = 0
        if hp <= 0:
            fase = 1
            moedas = 0
            namochila = 'a '
            tentativa = tentativa + 1
            print('Você morreu :(\nSeu recorde foi: Fase {}, na tentativa {}'.format(recorde, tentativapontuacaomaisalta))
            tentar = int(input('Você deseja tentar de novo?\n1. Sim\n2. Não\n\033[97m━━━━▶\033[m '))
            # Apenas ações válidas
            while (tentar < 1):
                tentar = int(input('Selecione uma opção válida: '))
                while (tentar > 2):
                    tentar = int(input('Selecione uma opção válida: '))
            while (tentar > 2):
                tentar = int(input('Selecione uma opção válida: '))
                while (tentar < 1):
                    tentar = int(input('Selecione uma opção válida: '))
        # Quit
        if tentar == 2:
            print('Muito obrigado, até mais! :)')