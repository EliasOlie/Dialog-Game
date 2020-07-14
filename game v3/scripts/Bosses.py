class Boss():
    
    def __init__(self, BossName, BossHP, BossDMG, BossMultiplier, BossLoot):
        self.BossName = BossName
        self.BossHP = BossHP
        self.BossDMG = BossDMG
        self.BossLoot = BossLoot
        self.BossMultiplier = BossMultiplier
    
    def BossNutshell(self):
        print(f'O nome do Chefão inimigo é {self.BossName}\n')
        print(f'O dano do Chefão inimigo é {self.BossDMG}\n')
        print(f'Os pontos de vida do Chefão inimigo são {self.BossHP}\n')
        print(f'O Chefão inimigo tem chance de dropar {self.BossLoot}\n')

Lesser_Zombie = Boss('Lesser Zombie', 100, 15, 1, 'Poção da vida abundante (Aumenta permanentemente sua vida em 50!)')