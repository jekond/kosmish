import persona
import details
import navigation
import math
class SpaseShip:
    def __init__(self, name):
        self.name = name
        self.position=[0,0] # Стартовая позиция
        self.energy=10
        self.oxigen = 100
        self.fuel=100
        self.day=0
        self.s_shel=0

    def start(self):
        self.position[0]=navigation.Earth.position[0]
        self.position[1]=navigation.Earth.position[1]
        #self.s_shel=details.Shell_1
        '''
        Идея была в том, что начинать игру можно будет на любой планете. По факту же вышел костыль, который помогает найти Землю
        после выполнения стартовых функций файла navigation
        '''

    def change_shell(self,xyz):
        if(xyz=='x' and self.s_shel!=details.Shell_1):
            self.s_shel=details.Shell_1
        elif(xyz=='y' and self.s_shel!=details.Shell_2):
            self.s_shel=details.Shell_2
        elif(xyz=='z' and self.s_shel!=details.Shell_3):
            self.s_shel=details.Shell_3


Marvel=SpaseShip("Валерий Иванович Космич")
Marvel.start()

