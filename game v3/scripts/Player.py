from random import randint
import Dices

class Player():
    
    def __init__(self, PlayerName, PlayerHP, PlayerDMG, PlayerItems, PlayerMaxHP):
        self.PlayerName = PlayerName
        self.PlayerHP = PlayerHP
        self.PlayerDMG = PlayerDMG
        self.PlayerItems = PlayerItems
        self.PlayerMaxHP = PlayerMaxHP

    def PlayerNutshell(self): #Exibe os atributos do player
        print(f'O nome do player é {self.PlayerName}\n')
        print(f'O dano do player é {self.PlayerDMG}\n')
        print(f'Os pontos de vida do player são {self.PlayerHP}\n')
        print(f'O player está equipado com {self.PlayerItems}\n')
    
    def AtaqueFraco(self): #Da um ataque fraco que vai da metade do dano de ataque até o ataque todo
        dano = randint(self.PlayerDMG/2, self.PlayerDMG)
        return dano
    
    def AtaqueNormal(self): #Da um ataque normal que vai do dano de ataque +1 até +5
        if Dices.JogarD6() > 3:
            dano = randint(self.PlayerDMG +1, self.PlayerDMG +2)
            return dano
        else:
            dano = randint(self.PlayerDMG, self.PlayerDMG +1)
            return dano
    
    def AtaqueForte(self): #Da um ataque forte, que varia entre dano crítico(2x) e +2 até +6 do dano do personagem
        if Dices.JogarD20() == 20:
            dano = self.PlayerDMG * 2
            return dano
        elif Dices.JogarD20() >= 7:
            dano = randint(self.PlayerDMG +5, self.PlayerDMG +6)
            return dano
        else:
            dano = randint(self.PlayerDMG +2, self.PlayerDMG +3)
            return dano


NewPlayer = Player('a', 50, 10, 'Espada de madeira', 50)
