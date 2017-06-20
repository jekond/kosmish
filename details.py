'''
Главный игровой файл, отвечающий за реализацию механики деталей и их функций. В классе Engine метод use_engine()
выполняет космические полеты корабля от одной планеты к другой

В классе Details создан метод repair, имеющий одинаковую схему для каждой из составляющей корабля. Однако материал для ремонта у всех разный,
потому у каждого объекта дочерних классов Details свои собственные ресурсы для ремонта.


'''
import ship
import random
import navigation
import math
#import grafon
#import pygame

global text_nav_message
global text_rep_message
global text_pzdc_message
text_rep_message=' '
text_nav_message=' '
text_pzdc_message=' '
class Details:
    def __init__(self,name,description,composition):
        self.name=name
        self.description=description#Описание
        self.composition=composition#Компановка или Уровень составляющей (на корпус первого уровня нельзя поставить деталь второго уровня и т.д.)
        self.rep_resource=0#имеющиеся ресурсы для ремонта
        self.rep_need=0#необходимое кол-во ресурсов для ремонта
        self.klei=''#Для определения типа детали. Будь это Двигатель, Генератор и т.д.
        self.repair_dictionary = {'engine':[0,self.rep_resource,self.rep_need,'Двигатель'],
                                  'oxi_station':[1,self.rep_resource,self.rep_need,'Кислородная станция'],
                                  'generator':[1,self.rep_resource,self.rep_need,'Генератор энергии'],
                                  'shell':[10,self.rep_resource,self.rep_need,'Обшивка']}
        #self.rep_quest=[]#список чисел для примеров пользователю
        #for i in range(50):
        #    self.rep_quest+=[random.randint(-999,999)]
        
    def repair_shit(self):
        #i=random.randint(0,47)
        #j=int(input(print('Необходимо подправить алгоритм ремонтного дрона:',self.rep_quest[i],'+',self.rep_quest[i+1],'-',self.rep_quest[i+2])))
        #if(j==(self.rep_quest[i] + self.rep_quest[i+1] - self.rep_quest[i+2])):
            klei=self.klei
            
            if(self.repair_dictionary[klei][0] == 0 and self.repair_dictionary[klei][1] >= self.repair_dictionary[klei][2]):
                self.repair_dictionary[klei][0] = 1
                self.rep_resource = self.rep_resource - self.repair_dictionary[klei][2]
                #print(self.repair_dictionary[klei][3],'теперь в отличном состоянии\nОсталось',self.rep_resource,'материала')
                text_rep_message=str(self.repair_dictionary[klei][3])+' теперь в отличном состоянии'
                global text_rep_message
            elif(self.repair_dictionary[klei][0] == 1 or self.repair_dictionary[klei][0] == 10):
                #print(self.repair_dictionary[klei][3],'и так в отличном состояние')
                text_rep_message=str(self.repair_dictionary[klei][3])+' и так в отличном состояние'
                global text_rep_message
            else:
                #print('У вас недостаточно ресурсов. Проверьте трюм')
                text_rep_message='У вас недостаточно ресурсов. Проверьте трюм'
                global text_rep_message
        #else:
        #    print("Неверная настройка дрона привела к ошибке в его работе.")#Нужно решить как наказывать за ошибку

    def display(self):#функция для проверки работы кода
        print ('Название',self.name,'Описание',self.description,'Комплекция',self.composition,'В наличие ресурсов',self.rep_resource,'Необходимо для ремонта',self.rep_need,'',self.klei)

#Двигатель
class Engine(Details):
    def __init__ (self,name,descripron,composition,move_speed):
        Details.__init__(self,name,descripron,composition)
        self.move_speed=move_speed#Скорость. Преодоление расстояния за ход
        self.klei='engine'
        self.rep_resource=35*self.composition
        self.rep_need=self.rep_resource
        self.navigation_dict={'1':[navigation.Mercury.pl_data_coord,navigation.Mercury.coord_x,navigation.Mercury.coord_y,navigation.Mercury.sid_per],
                         '2':[navigation.Venus.pl_data_coord,navigation.Venus.coord_x,navigation.Venus.coord_y,navigation.Venus.sid_per],
                         '3':[navigation.Earth.pl_data_coord,navigation.Earth.coord_x,navigation.Earth.coord_y,navigation.Earth.sid_per],
                         '4':[navigation.Mars.pl_data_coord,navigation.Mars.coord_x,navigation.Mars.coord_y,navigation.Mars.sid_per],
                         '5':[navigation.Jupiter.pl_data_coord,navigation.Jupiter.coord_x,navigation.Jupiter.coord_y,navigation.Jupiter.sid_per],
                         '6':[navigation.Saturn.pl_data_coord,navigation.Saturn.coord_x,navigation.Saturn.coord_y,navigation.Saturn.sid_per],
                         '7':[navigation.Uranus.pl_data_coord,navigation.Uranus.coord_x,navigation.Uranus.coord_y,navigation.Uranus.sid_per],
                         '8':[navigation.Neptune.pl_data_coord,navigation.Neptune.coord_x,navigation.Neptune.coord_y,navigation.Neptune.sid_per]}
        self.day_on_trwl=[]
        self.pl_dist=[]

    
    def use_engine_calc(self,dest_point):#Полеты корабля
        print('calc')
        print(ship.Marvel.position)
        best_day_on_trwl=[9999999999999999999999999,0]
        #i=random.randint(0,45)
        #j=int(input(print('Необходимо подправить алгоритм автопилота:',self.rep_quest[i],'+',self.rep_quest[i+1],'+',self.rep_quest[i+2],'-',self.rep_quest[i+3],'+',self.rep_quest[i+4])))
        #if(j!=(self.rep_quest[i] + self.rep_quest[i+1] + self.rep_quest[i+2] - self.rep_quest[i+3] + self.rep_quest[i+4])):
            #print('Вы ошиблись в настройке. К счастью Первый закон робототехники не позволил вам разбиться в лепешку')
        if(ship.Marvel.fuel>=self.composition and self.repair_dictionary[self.klei][0]==1):              
            #dest_point=input(print('Выберите планету'))
            for j in range(self.navigation_dict[dest_point][3]):
                x=self.navigation_dict[dest_point][1][j]-ship.Marvel.position[0]
                y=self.navigation_dict[dest_point][2][j]-ship.Marvel.position[1]
                gip=math.sqrt(x*x+y*y)#гипатенуза Теорема Пифагора
                self.day_on_trwl+=[int(gip/self.move_speed)]#Дней на полет
                if(j>=self.navigation_dict[dest_point][0]):
                    self.pl_dist+=[j-self.navigation_dict[dest_point][0]]
                    #print(self.pl_dist[j],'pl_dist___','___day_on_trwl',self.day_on_trwl[j])
                else:
                    self.pl_dist+=[j+(self.navigation_dict[dest_point][3]-self.navigation_dict[dest_point][0])]
                    #print(self.pl_dist[j],'pl_dist___','___day_on_trwl',self.day_on_trwl[j])
            for i in range(self.navigation_dict[dest_point][3]):
                if(self.day_on_trwl[i]-self.pl_dist[i]==0):
                    if(best_day_on_trwl[0]>self.day_on_trwl[i]):
                        best_day_on_trwl=[self.day_on_trwl[i],i]
                    print(self.pl_dist[i],self.day_on_trwl[i])
                    print('Самый оптимальный путь найден. Он займет:',self.day_on_trwl[i])
            
            if(best_day_on_trwl[0]!=9999999999999999999999999):
                print(best_day_on_trwl[0],' дней. Это самый короткий путь')
            else:
                for ab in range(1,25):
                    for ij in range(self.navigation_dict[dest_point][3]):
                        if(self.day_on_trwl[ij]-self.pl_dist[ij]>=-ab and self.day_on_trwl[ij]-self.pl_dist[ij]<=ab):
                            if(best_day_on_trwl[0]>self.day_on_trwl[ij]):
                                best_day_on_trwl=[self.day_on_trwl[ij],ij]
                            print(self.pl_dist[ij],self.day_on_trwl[ij])
                            print('Найден путь с погрешностью в ',ab,' дней. Он займет:',self.day_on_trwl[ij])
                    if(best_day_on_trwl[0]!=9999999999999999999999999):
                        print(best_day_on_trwl[0],' дней. Это самый короткий путь, с погрешностью в ',ab,' дней.')
                        break
                    
            text_nav_message='Оптимальный путь найден. Он займет: '+str(best_day_on_trwl[0])+' дней'
            global text_nav_message
            text_pzdc_message=' '
            global text_pzdc_message
            print(text_nav_message)
            self.day_on_trwl=[]
            self.pl_dist=[]
        
        else:
            print("!!!ОТКАЗ! ПРОВЕРЬТЕ РАБОТОСПОСОБНОСТЬ ДВИГАТЕЛЯ И ЗАРЯД ЭНЕРГИИ!!!")
            text_pzdc_message="!!!ОТКАЗ! ПРОВЕРЬТЕ РАБОТОСПОСОБНОСТЬ ДВИГАТЕЛЯ И ЗАПАС ТОПЛИВА!!!"
            global text_pzdc_message

    def use_engine(self,dest_point):#Полеты корабля
        print('ne')
        print(ship.Marvel.position)
        best_day_on_trwl=[9999999999999999999999999,0]
        #i=random.randint(0,45)
        #j=int(input(print('Необходимо подправить алгоритм автопилота:',self.rep_quest[i],'+',self.rep_quest[i+1],'+',self.rep_quest[i+2],'-',self.rep_quest[i+3],'+',self.rep_quest[i+4])))
        #if(j!=(self.rep_quest[i] + self.rep_quest[i+1] + self.rep_quest[i+2] - self.rep_quest[i+3] + self.rep_quest[i+4])):
            #print('Вы ошиблись в настройке. К счастью Первый закон робототехники не позволил вам разбиться в лепешку')
        if(ship.Marvel.fuel>=self.composition and self.repair_dictionary[self.klei][0]==1):              
            #dest_point=input(print('Выберите планету'))
            for j in range(self.navigation_dict[dest_point][3]):
                x=self.navigation_dict[dest_point][1][j]-ship.Marvel.position[0]
                y=self.navigation_dict[dest_point][2][j]-ship.Marvel.position[1]
                gip=math.sqrt(x*x+y*y)#гипатенуза
                self.day_on_trwl+=[int(gip/self.move_speed)]#Дней на полет
                if(j>=self.navigation_dict[dest_point][0]):
                    self.pl_dist+=[j-self.navigation_dict[dest_point][0]]
                    #print(self.pl_dist[j],'pl_dist___','___day_on_trwl',self.day_on_trwl[j])
                else:
                    self.pl_dist+=[j+(self.navigation_dict[dest_point][3]-self.navigation_dict[dest_point][0])]
                    #print(self.pl_dist[j],'pl_dist___','___day_on_trwl',self.day_on_trwl[j])
            for i in range(self.navigation_dict[dest_point][3]):
                if(self.day_on_trwl[i]-self.pl_dist[i]==0):
                    if(best_day_on_trwl[0]>self.day_on_trwl[i]):
                        best_day_on_trwl=[self.day_on_trwl[i],i]
                    print(self.pl_dist[i],self.day_on_trwl[i])
                    print('Самый оптимальный путь найден. Он займет:',best_day_on_trwl[0])
            
            if(best_day_on_trwl[0]!=9999999999999999999999999):
                print(best_day_on_trwl[0],' дней. Это самый короткий путь')
            else:
                for ab in range(1,25):
                    for ij in range(self.navigation_dict[dest_point][3]):
                        if(self.day_on_trwl[ij]-self.pl_dist[ij]>=-ab and self.day_on_trwl[ij]-self.pl_dist[ij]<=ab):
                            if(best_day_on_trwl[0]>self.day_on_trwl[ij]):
                                best_day_on_trwl=[self.day_on_trwl[ij],ij]
                            print(self.pl_dist[ij],self.day_on_trwl[ij])
                            print('Найден путь с погрешностью в ',ab,' дней. Он займет:',self.day_on_trwl[ij])
                    if(best_day_on_trwl[0]!=9999999999999999999999999):
                        print(best_day_on_trwl[0],' дней. Это самый короткий путь, с погрешностью в ',ab,' дней.')
                        break   
                    
            ship.Marvel.position[0]=self.navigation_dict[dest_point][1][best_day_on_trwl[1]]
            ship.Marvel.position[1]=self.navigation_dict[dest_point][2][best_day_on_trwl[1]]
            
                   
            ship.Marvel.day+=best_day_on_trwl[0]
            navigation.Mercury.pl_fly(best_day_on_trwl[0])
            navigation.Venus.pl_fly(best_day_on_trwl[0])
            navigation.Earth.pl_fly(best_day_on_trwl[0])
            navigation.Mars.pl_fly(best_day_on_trwl[0])
            navigation.Jupiter.pl_fly(best_day_on_trwl[0])
            navigation.Saturn.pl_fly(best_day_on_trwl[0])
            navigation.Uranus.pl_fly(best_day_on_trwl[0])
            navigation.Neptune.pl_fly(best_day_on_trwl[0])

            self.navigation_dict={'1':[navigation.Mercury.pl_data_coord,navigation.Mercury.coord_x,navigation.Mercury.coord_y,navigation.Mercury.sid_per,],
                                  '2':[navigation.Venus.pl_data_coord,navigation.Venus.coord_x,navigation.Venus.coord_y,navigation.Venus.sid_per],
                                  '3':[navigation.Earth.pl_data_coord,navigation.Earth.coord_x,navigation.Earth.coord_y,navigation.Earth.sid_per],
                                  '4':[navigation.Mars.pl_data_coord,navigation.Mars.coord_x,navigation.Mars.coord_y,navigation.Mars.sid_per],
                                  '5':[navigation.Jupiter.pl_data_coord,navigation.Jupiter.coord_x,navigation.Jupiter.coord_y,navigation.Jupiter.sid_per],
                                  '6':[navigation.Saturn.pl_data_coord,navigation.Saturn.coord_x,navigation.Saturn.coord_y,navigation.Saturn.sid_per],
                                  '7':[navigation.Uranus.pl_data_coord,navigation.Uranus.coord_x,navigation.Uranus.coord_y,navigation.Uranus.sid_per],
                                  '8':[navigation.Neptune.pl_data_coord,navigation.Neptune.coord_x,navigation.Neptune.coord_y,navigation.Neptune.sid_per]}

            self.day_on_trwl=[]
            self.pl_dist=[]
            ship.Marvel.fuel-=self.composition
            text_pzdc_message=' '
            global text_pzdc_message
        else:
            print("!!!ОТКАЗ! ПРОВЕРЬТЕ РАБОТОСПОСОБНОСТЬ ДВИГАТЕЛЯ И ЗАРЯД ЭНЕРГИИ!!!")        
            text_pzdc_message="!!!ОТКАЗ! ПРОВЕРЬТЕ РАБОТОСПОСОБНОСТЬ ДВИГАТЕЛЯ И ЗАПАС ТОПЛИВА!!!"
            global text_pzdc_message

Eng_1=Engine('Мотылек','Самый слабый и ненадежный двигатель из всех',1,1548000)
Eng_2=Engine('Гагарин','Теперь человечество может смело заявить, что еще не все потеряно',2,2700000)
Eng_3=Engine('GNB-11','Лучшее, что могут предложить корпорации',3,4000000)
Eng_4=Engine('Эксперементальный двигатель','Физика считает, что эта вещь незаконна',4,5645000)
Eng_5=Engine('Сквозь горизонт','Просто прими это как должное',6,12000000)
#Жизнеобеспечения
class Oxi_station(Details):
    def __init__ (self,name,descripron,composition):
        Details.__init__(self,name,descripron,composition)
        self.oxi_power=self.composition*25
        self.klei='oxi_station'
        self.rep_resource=20*self.composition
        self.rep_need=self.rep_resource

    def oxi_generate(self):
        if(self.repair_dictionary[self.klei][0]==1 and ship.Marvel.oxigen<self.composition*200 and ship.Marvel.energy<self.composition):
            ship.Marvel.oxigen=ship.Marvel.oxigen+self.oxi_power
        elif(ship.Marvel.oxigen>=self.composition*200):
            pass
        elif(ship.Marvel.energy<self.composition):
            print("Недостаточно энергии")
        else:
            print("!!!ВНИМАНИЕ! СИСТЕМА ЖИЗНЕОБЕСПЕЧЕНИЯ НЕИСПРАВНА!!!")

Oxi_1=Oxi_station('Модена','Твой единственный друг в космосе, обеспечивает судно кислородом',1)
Oxi_2=Oxi_station('Церцея','Отличный выбор для дюженного экипажа',2)
Oxi_3=Oxi_station('Гидеон','С этим можно основывать коллонию',4)
    
#Генератор энергии
class Power_generator(Details):#Генератор энергии
    def __init__ (self,name,descripron,composition):
        Details.__init__(self,name,descripron,composition)
        self.klei='generator'
        self.rep_resource=40*self.composition
        self.rep_need=self.rep_resource

    def energe_generate(self):
        if(self.repair_dictionary[self.klei][0]==1 and ship.Marvel.energy<10*self.composition):
            ship.Marvel.energy+=self.composition*2
        elif(ship.Marvel.energy>=10*self.composition):
            print("Аккамулятор полон")
        else:
            print("!!!ВНИМАНИЕ! ГЕНЕРАТОР НЕИСПРАВЕН!!!")        

Gen_1=Power_generator('T-1000','С этим генератором ты сможешь поставить дедов трактор на ход',1)
Gen_2=Power_generator('FTL','Популярен среди торговцев и контрабандистов',3)
Gen_3=Power_generator('HLD-Py','Это очень запутанная система, включающая в себя энергию мертвых звезд',5)

#Корпус
class Ship_Shell(Details):
    def __init__ (self,name,descripron,composition,crew):
        Details.__init__(self,name,descripron,composition)
        self.crew=crew#максимальное кол-во экипажа на судне
        self.klei='shell'
        self.rep_resource=25*self.composition
        self.rep_need=self.rep_resource/5
        self.detail_dict={'engine':Eng_1,'oxi_station':Oxi_1,'generator':Gen_1}
    def gasp(self):
        self.Oxi.oxi_generate()
        ship.Marvel.oxigen-=self.crew*20
        if(ship.Marvel.oxigen<=0):
            self.crew=0
            
    def add_detail(self,detail):
        if(self.composition<detail.composition):
            print('Эта конструкция не предназначенна для вашего судна')
        else:
            self.detail_dict[detail.klei]=detail
            print('Установка прошла успешно. Теперь у вас стоит',detail.name)
            

Shell_1=Ship_Shell('Виктор','Одноместный космический корабль. Идеальный выбор для самостоятельного и малоимущего социофоба',1,1)
Shell_2=Ship_Shell('Герцог Уильям','Отличная компановка этого корпуса делает его универсальным выбором для космических приключений слаженной команды',3,5)
Shell_3=Ship_Shell('Фрегат','При должном старание на этом судне можно совершать перелеты между звездными системами',5,8)


#Тестовый код полетов
'''
for i in range(len(day_on_trwl)):
                if(self.navigation_dict[dest_point][0]>i):
                    if((day_on_trwl[i]-(i+(self.navigation_dict[dest_point][3]-self.navigation_dict[dest_point][0]))<best_day_on_trwl)):
                        print('x',self.navigation_dict[dest_point][1][i],'y',self.navigation_dict[dest_point][2][i],'за сколько долетит корабль',day_on_trwl[i],'за сколько долетт плнета',i+(self.navigation_dict[dest_point][3]-self.navigation_dict[dest_point][0]))
                        if(best_day_on_trwl>day_on_trwl[i]):
                            best_day_on_trwl=day_on_trwl[i]
                            pref_coord=i
                        
                else:
                    if((day_on_trwl[i]-(i+self.navigation_dict[dest_point][0]))<best_day_on_trwl):
                        print('x',self.navigation_dict[dest_point][1][i],'y',self.navigation_dict[dest_point][2][i],'за сколько долетит корабль',day_on_trwl[i],'за сколько долетт плнета',i+self.navigation_dict[dest_point][0])
                        if(best_day_on_trwl>day_on_trwl[i]):
                            best_day_on_trwl=day_on_trwl[i]
                            pref_coord=i

            print('Самый короткий путь займет',best_day_on_trwl)
            ship.Marvel.position[0]=self.navigation_dict[dest_point][1][pref_coord]
            ship.Marvel.position[1]=self.navigation_dict[dest_point][2][pref_coord]
            '''

