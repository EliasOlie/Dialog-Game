import Player, Enemies, Dices, Bosses
from random import randint

jogador = Player.NewPlayer

slime = Enemies.Slime

lesserz = Bosses.Lesser_Zombie

def GameOver(): #Exibe uma mensagem de Game over se o jogador estiver sem pontos de vida
    if jogador.PlayerHP <= 0:
        print('Game Over!')
        return jogador.PlayerHP
    else:
        pass

def TakeDamage(mob): #Leva dano de alguma fonte (mob)
    damage = randint(mob.EnemyDMG/mob.EnemyDMG, mob.EnemyDMG +3)
    jogador.PlayerHP -= damage
    print(f'\nO jogador {jogador.PlayerName} foi atacado pelo {mob.EnemyName} perdendo {damage} pontos de vida! Agora ele tem {jogador.PlayerHP} pontos de vida')
    GameOver()
    return jogador.PlayerHP

def EnemyLoot(target): #Devolve ao jogador os espolios da vitoria | Falta checar se o player já tem o drop, para nao somar os atributos e desbalancear o jogo!
    if target.EnemyName == 'Slime':
        print(f'\nVasculhando a área que o Slime morreu você encontra {target.EnemyLoot}')
        jogador.PlayerDMG += 5
        print(f'O seu novo dano de ataque é: {jogador.PlayerDMG}!') 
        return jogador.PlayerDMG

def DoDMG(target): #Da dano em algum alvo
    ataque = input('\nQual ataque? \nA - Ataque fraco\nB - Ataque normal\nC - Ataque forte\n')
    if ataque.lower() == 'a':
        dano = jogador.AtaqueFraco()
        target.EnemyHP -= dano
    elif ataque.lower() == 'b':
        dano = jogador.AtaqueNormal()
        target.EnemyHP -= dano
    elif ataque.lower() == 'c':
        dano = jogador.AtaqueForte()
        target.EnemyHP -= dano
    print(f'\nO jogador ataca o {target.EnemyName}, causando {dano} de dano, o {target.EnemyName} agora tem {target.EnemyHP} pontos de vida')
    if target.EnemyHP <= 0:
        print('\nO inimigo se dissolve na sua frente, será que dropou alguma coisa?')
        if Dices.JogarD6() >= 5:
            EnemyLoot(slime)
        else:
            print(f'\nO {target.EnemyName} não dropu nada! Mais sorte na próxima')

    return target.EnemyHP


def Lutar(mob):
    print(f'Quem ataca primeiro? Você ou {mob.EnemyName}? Que a sorte seja lançada!')
    if JogarD6() >= 3:
        print('Você sai atacando!')
        while True:
            DoDMG(mob)
            if mob.EnemyHP <= 0:
                break
            else:
                TakeDamage(mob)
                if jogador.PlayerHP <= 0:
                    GameOver()
                    break
    else:
        print(f'O {mob.EnemyName} sai atacando!')
        while True:
            TakeDamage(mob)
            if jogador.PlayerHP <= 0:
                GameOver()
                break
            else:
                DoDMG(mob)
                if mob.EnemyHP <= 0:
                    break

Lutar(slime)

#DoDMG(slime)

print(jogador.PlayerDMG)