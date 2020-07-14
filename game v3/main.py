from scripts import Player, Enemies

NewPlayer = Player.Player('a', 10, 10, 'Espada de madeira')
NewPlayer.PlayerNutshell()

Slime = Enemies.Enemy('Slime', 10, 10, 'uma Espada de Diamante +100 DMG')
Slime.EnemyNutshell()



'''
while True:
    i = input('Qual ataque (A, B, C)')
    if i.lower() in aceppted_atk:
        if i.lower() == 'a':
            DoDMG(Slime, ataque_fraco)
            print(f'Você ataca o slime, causando {round(ataque_fraco)} de dano, o inimigo está com {round(Slime.EnemyHP)} pontos de vida')
            IsEnemyDead(Slime)
            if Slime.EnemyHP <= 0:
                EnemyLoot(Slime)
                break
            else:
                TakeDMG(Slime)
                if character.PlayerHP <= 0:
                    GameOver(character)
                    break
        if i.lower() == 'b':
            DoDMG(Slime, ataque_normal)
            print(f'Você ataca o slime, causando {ataque_normal} de dano, o inimigo está com {Slime.EnemyHP} pontos de vida')
            IsEnemyDead(Slime)
            if Slime.EnemyHP <= 0:
                EnemyLoot(Slime)
                break
        if i.lower() == 'c':
        #if JogarD20()
            DoDMG(Slime, ataque_forte)
            print(f'Você ataca o slime, causando {ataque_forte} de dano, o inimigo está com {Slime.EnemyHP} pontos de vida')
            IsEnemyDead(Slime)
            if Slime.EnemyHP <= 0:
                EnemyLoot(Slime)
                break
    else:
        print('Insira um ataque válido!')
'''

#Mecanica de receber dano


#Checa se o player morreu


'''

while True:
    
    #print('Jogo feito INTEIRAMENTE EM PYTHON! (sem o pygame)')
    
    #time.sleep(3)

    print(f'{character.PlayerName.title()}? Hum que nome bonito')
    
    continuar = print('Digite "sair" a qualquer momento para sair')

    IntroArco1 = print(
        f'____________________________________________________________________________________________________________\n\n'
        'Você saí de manhã da sua casa no interior e vai em direção ao rancho onde estão suas ovelhas você percebe que\n' 
        'elas estão acordadas, porém estão completamente cansadas, completamente fora do convencional como se eles\n' 
        'estivessem acordadas desde de o dia anterior, ou pior como se algo as impedisse de dormir durante toda aquela\n' 
        'noite, algo que lhe soa estranho levando em consideração o pesadelo que você teve, que agora você não se lembra\n'
        'de muita coisa, apenas de um homem com uma aura negra conspirando contra o mundo e pragejando com a sua boca\n' 
        'além disso de súbto lhe veio uma memória desse sonho você olha para cima e o céu azul de repente está\n' 
        'completamente negro não é visto nenhuma estrela nem a lua e nem mesmo o sol.\n'
        '____________________________________________________________________________________________________________\n\n'

    )
    time.sleep(5)
    IntroArco1_2 = input(
        f'____________________________________________________________________________________________________________\n\n'
        'Ao lembrar disso um arrepio lhe corre pela espinha e ao mesmo tempo uma das ovelhas berra "Beeeeeeeee" o que\n'
        'lhe assustou bastante, mas vida que segue "Deve ser apenas um sonho, um sonho muito ruim" você repete para sí\n' 
        'mesmo, depois de encher o lugar de alimento delas de comida (o que levou várias idas e vindas do silo até\n' 
        'o rancho) e também supri-las de àgua já que eles estavam exautas não seria uma boa ideia leva-las as campinas\n'
        'você decide o que fazer agora:\n' 
        'A - Voltar para casa\n'
        'B - Ir para as campinas e relaxar na árvore perto do lago\n'
        'C - Ficar no rancho e supervisionar as ovelhas\n'
        '____________________________________________________________________________________________________________\n\n'
    )
    if IntroArco1_2.lower() == 'sair':
        break 
    if IntroArco1_2.lower() == 'a':
        print(
        f'____________________________________________________________________________________________________________\n\n'
        'Saíndo do rancho você repara que há marcas estranhas na parte inferior da porta do rancho, ao se aproximar\n'
        'você nota que é algo como se fosse uma escrita runica, uma escrita que você já havia visto seu avô discutir\n' 
        'sobre com o mago da capital o Sr. Gilgamesh, como você não sabe do que se trata já que diferente do seu avô\n' 
        'você nunca se interessou por nada do tipo Arcano, simplismente anota as formas runicas num papel e decide\n' 
        'que quando for a capital vai perguntar ao Sr. Gilgamesh sobre essa runa e sobre o paradeiro do seu avô.\n'
        '____________________________________________________________________________________________________________\n\n'
        )
        msg1 = input(
        f'_____________________________________________________________________________________________________\n\n'
        'Ao abrir a porta de sua casa você vê de relançe um vulto o qual salta para fora de sua vista\n' 
        'então o que você faz?\n'
        'A - Vou sileciosamente ao encontro do vulto para ter o elemento surpresa (D20 envolvido > 10)\n'
        'B - Corro na direção dele\n'
        'C - Fujo em direção as campinas onde posso ver se alguem se aproxima de mim\n'
        )
        if msg1.upper() == 'A':
            Combate(Slime)
            break
            
            
            while True:
                    if JogarD20() > 10:
                        print('Você se aproxima silenciosamente e vê um slime como chegou furtivamente começa atacando')
                        DoDMGE(Slime)
                        print(f'O slime recebe {character.PlayerDMG} de dano ficando com {Slime.EnemyHP}')
                        time.sleep(1)
                        print('Agora é a vez do Slime!')
                        DoDMGP(Slime)
                        print(f'O slime lhe ataca causando {Slime.EnemyDMG} você fica com {character.PlayerHP} de vida')
                        print('Sua vez!')
                        DoDMGE(Slime)
                        print(f'O slime recebe {character.PlayerDMG} de dano ficando com {Slime.EnemyHP}')
                        print('Agora é a vez do Slime!')
                        DoDMGP(Slime)
                        print(f'O slime lhe ataca causando {Slime.EnemyDMG} você fica com {character.PlayerHP} de vida')
                        Dead()
                        EnemyDeadAndLoot(Slime)
                        break
                    else:
                        print('Sua tentativa de aproximar-se dele daria certo se você não fosse tao atrapalhado')
                        print('O Slime ataca primeiro')
                        DoDMGP(Slime)
                        print(f'O slime lhe ataca causando {Slime.EnemyDMG} você fica com {character.PlayerHP} de vida')
                        print('Sua vez!')
                        DoDMGE(Slime)
                        print(f'O slime recebe {character.PlayerDMG} de dano ficando com {Slime.EnemyHP}')
                        print('Agora é a vez do Slime!')
                        DoDMGP(Slime)
                        Dead()
                        EnemyDeadAndLoot(Slime)
                        break
    break
'''
    
'''
if finalr > finalb and finalr > finalm:
    print('Ao pisar nela uma driade furiosa lhe pisa e lhe causa 30 de dano')
    #HP - 30 if HP == 0 gameover!
if finalb > finalr and finalb > finalm:
    print('Ao regala você encontra uma poção de cura!')
    #HP += algum valor
if finalm > finalr and finalm > finalb:
    print('Você segue o seu caminho!')
'''
