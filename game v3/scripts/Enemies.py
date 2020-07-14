class Enemy():
    
    def __init__(self, EnemyName, EnemyHP, EnemyDMG, EnemyLoot):
        self.EnemyName = EnemyName
        self.EnemyHP = EnemyHP
        self.EnemyDMG = EnemyDMG
        self.EnemyLoot = EnemyLoot
    
    def EnemyNutshell(self):
        print(f'O nome do inimigo é {self.EnemyName}\n')
        print(f'O dano do inimigo é {self.EnemyDMG}\n')
        print(f'Os pontos de vida do inimigo são {self.EnemyHP}\n')
        print(f'O inimigo tem chance de dropar {self.EnemyLoot}\n')

    

Slime = Enemy('Slime', 10, 5, 'uma Espada de Diamante +5 DMG')
