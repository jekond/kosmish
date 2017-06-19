import math
import ship
import details
import random
pi2=2*math.pi

class Planet:
    def __init__(self,name,af,per,x,y,sid_per,pl_inform):
        self.name=name
        self.af_per=[af,per]#Афелий и перигелий (дальняя и ближайшая точки от солнца)
        self.position=[x,y]# Стартовая позиция
        self.sid_per=sid_per#Сидерический период (кол-во дней на оборот вокруг Солнца)
        self.gravitation=0#пока никак не используется, но будет
        self.pl_day=pi2/self.sid_per
        self.pl_data_coord=0
        self.pl_inform=pl_inform#Объем, масса,Средний радиус, средняя плотность, период вращения, орбит. скорость 

        self.coord_x=[]
        self.coord_y=[]

    def display(self):
        print (self.name,self.af_per,self.position,self.sid_per,self.pl_data_coord,'позиция в списке координат')
    def pl_move(self):#Заполнение списков координат
        while(self.sid_per>self.pl_data_coord):
            self.coord_x+=[self.af_per[0]*(math.cos(self.pl_day))]
            self.coord_y+=[self.af_per[1]*(math.sin(self.pl_day))]
            self.pl_day+=pi2/self.sid_per
            self.pl_data_coord+=1

    def pl_fly(self,time_to_fly):#Движение планет
        ttf=time_to_fly+self.pl_data_coord
        if(ttf>self.sid_per):
            while(ttf>self.sid_per):
                ttf-=self.sid_per
        self.position[0]=self.coord_x[ttf]
        self.position[1]=self.coord_y[ttf]
        self.pl_data_coord=ttf
        
        
###Классы планет
Mercury = Planet('Меркурий',69817445,46001009,69817445,0,88,['0,056 земного','0,0552 земной','2439,7 км','5,427 г/см(куб)','88 земных дней','47,36 км/с'])
Venus = Planet('Венера',108942780,107476170,108942780,0,225,['0,857 земного','0,815 земной','6051,8 км','5,24 г/см(куб)','224 земных дней','35,02 км/с'])
Earth = Planet('Земля',152098233, 147098291,152098233,0,365,['10,83*10(в 11 степени) км(куб)','5,97*10(в 24 степени) кг','6371 км','5,5153 г/см(куб)','365 земных дней','29,78 км/с'])
Mars = Planet('Марс',249232432,206655215,249232432,0,687,['0,151 земного','0,107 земной','3389,5 км','3,933 г/см(куб)','687 земных дней','24,13 км/с'])
Jupiter = Planet('Юпитер',816001807,740679835,816001807,0,4333,['1320,4 земного','316,58 земных','69911 км','1,326 г/см(куб)','4332 земных дня','13,07 км/с'])
Saturn = Planet('Сатурн',1503509229,1349823615,1503509229,0,10759,['768,6 земного','95 земных','54364 км','0,687 г/см(куб)','10759 земных дня','9,69 км/с'])
Uranus = Planet('Уран',3006318143,2734998229,3006318143,0,30685,['63 земного','14,6 земных','25362 км','1,27 г/см(куб)','30685 земных дня','6,81 км/с'])
Neptune = Planet('Нептун',4537039826,4459753056,4537039826,0,60190,['57 земного','17,147 земных','24622 км','1,638 г/см(куб)','60190 земных дня','5,4349 км/с'])
###

##Заполнение списка позиций
Mercury.pl_move()
Venus.pl_move()
Earth.pl_move()
Mars.pl_move()
Jupiter.pl_move()
Saturn.pl_move()
Uranus.pl_move()
Neptune.pl_move()

start_data=random.randint(1,60190)
    
Mercury.pl_data_coord=start_data
Mercury.pl_fly(0)
Venus.pl_data_coord=start_data
Venus.pl_fly(0)
Earth.pl_data_coord=start_data
Earth.pl_fly(0)
Mars.pl_data_coord=start_data
Mars.pl_fly(0)
Jupiter.pl_data_coord=start_data
Jupiter.pl_fly(0)
Saturn.pl_data_coord=start_data
Saturn.pl_fly(0)
Uranus.pl_data_coord=start_data
Uranus.pl_fly(0)
Neptune.pl_data_coord=start_data    
Neptune.pl_fly(0)
