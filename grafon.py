'''
Файл, отвечающий за картинку и выполняющий непосредственную связь между пользователем и игрой.
Кнопки определяются через координаты. При каждом клике берется расположение мышки по x и по y, после чего проходит
проверки и, в случае успеха одной из них, выполняется заданное действие.
'''

import pygame
import details
import persona
import ship
import navigation
pygame.init()


# Define some colors
black    = (   0,   0,   0)
white    = ( 255, 255, 255)
green    = (   0, 255,   0)
red      = ( 255,   0,   0)
spam     = ( 254, 252, 255)

#Чисор Пи, счетчитк дня и переменная для анимации судна
pi=3.141592653
day=1
ship_x = 0 #Test

#Разерность игрового окна
size=[1040,680]
screen=pygame.display.set_mode(size)

#Подгружаем фоновую картинку и изображение судна
background_image = pygame.image.load("0001.png").convert()
ship_image = pygame.image.load("07.png").convert()
ship_image.set_colorkey(white)#обрезаем белый фон изображения
dialog_wind_image = pygame.image.load("wind.png").convert()
dialog_wind_image.set_colorkey(white)#обрезаем белый фон изображения
status_wind_image = pygame.image.load("wind2.png").convert()
status_wind_image.set_colorkey(white)
console_show='_'


pygame.display.set_caption("Курсовая Кондратенко Е.А.")

pos = (0,0,)#координаты клика

button_fly = [[0,65],[0,85]]
for i in range(8):
    button_fly[0]+=[button_fly[0][-1]+25]
    button_fly[1]+=[button_fly[1][-1]+25]
    '''
    Заполнение коорднат кнопок, использующихся в меню навигации
    '''

#Вывод игрового текста
font = pygame.font.Font(None,20)


#Переменные текста для окна ремонта
text_rep = font.render("Окно ремонта:",True,black)
text_rep_eng = font.render("1. Починить двигатель",True,black)
text_rep_oxi = font.render("2. Починить Жизнеобеспечение",True,black)
text_rep_gen = font.render("3. Починить Генератор",True,black)

trm=''
text_rep_good = font.render(trm,True,black)

#Переменные текста для окна навигации
text_nav = font.render("Окно Навигации:",True,black)
text_nav_go = font.render("Полетели!",True,black)
text_nav_Mer = font.render("1. На Меркурий",True,black)
text_nav_Ven = font.render("2. На Венеру",True,black)
text_nav_Ear = font.render("3. На Землю",True,black)
text_nav_Mar = font.render("4. На Марс",True,black)
text_nav_Jup = font.render("5. На Юпитер",True,black)
text_nav_Sat = font.render("6. На Сатурн",True,black)
text_nav_Ura = font.render("7. На Уран",True,black)
text_nav_Nep = font.render("8. На Нептун",True,black)


tnm=''
text_nav_message=font.render(trm,True,black)

#Переменные для инфы
text_inf_V = font.render('',True,black)
text_inf_M = font.render('',True,black)
text_inf_R = font.render('',True,black)
text_inf_Pl = font.render('',True,black)
text_inf_Sid = font.render('',True,black)
text_inf_Sp = font.render('',True,black)
text_inf_hello = font.render('',True,black)

#Переменные для окна статуса
text_stat_name = font.render(ship.Marvel.name + ' - имя корабля',True,white)
text_stat_fuel = font.render("Запас топлива:" + str(ship.Marvel.fuel),True,white)
text_stat_pzdc = font.render(details.text_pzdc_message,True,black)

#Оставаться в цикле, пока пользователь не нажмёт на кнопку закрытия окна
done=False
 
# Используется для контроля частоты обновления экрана
clock=pygame.time.Clock()
 
# -------- Основной цикл программы -----------
while done==False:
    # ОБРАБОТКА ВСЕХ СОБЫТИЙ ДОЛЖНА БЫТЬ ПОД ЭТИМ КОММЕНТАРИЕМ
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done=True
        if event.type == pygame.MOUSEBUTTONDOWN:
            #print event.button
            print (pygame.mouse.get_pos())
            pos = pygame.mouse.get_pos()
            for i in range(1):
### Функционал Осноных кнопок ###
                if(pos[0]>=370 and pos[0]<=700 and pos[1]>=540 and pos[1]<=size[1]):
                    console_show='eng_use'
                    
                
                    break

                elif(pos[0]>=800 and pos[0]<=1035 and pos[1]>=515 and pos[1]<=600):
                    console_show='rep'
                    
                    trm=''
                    text_rep_good = font.render(trm,True,black)
                    break
                    print('2')

                elif(pos[0]>=80 and pos[0]<=203 and pos[1]>=527 and pos[1]<=606):#кнопка вывода информации о планете
                    console_show='inf'
                    for i in range(len(navigation.button_list)):
                        if(ship.Marvel.position[0] in navigation.button_list[i].coord_x):
                            text_inf_V = font.render('Объем: ' + navigation.button_list[i].pl_inform[0],True,black)
                            text_inf_M = font.render("Масса: " + navigation.button_list[i].pl_inform[1],True,black)
                            text_inf_R = font.render("Средний радиус: " + navigation.button_list[i].pl_inform[2],True,black)
                            text_inf_Pl = font.render("Плотность планеты: " + navigation.button_list[i].pl_inform[3],True,black)
                            text_inf_Sid = font.render("Оборот вокруг солнца за: " + navigation.button_list[i].pl_inform[4],True,black)
                            text_inf_Sp = font.render("Орбитальная скорость: " + navigation.button_list[i].pl_inform[5],True,black)

                    break
                
                
### Функционал Кнопок ремонта ###
                elif(pos[0]>=25 and pos[0]<=285 and pos[1]>=380 and pos[1]<=400 and console_show=='rep'):
                    details.Shell_1.detail_dict['engine'].repair_shit()
                    trm=details.text_rep_message
                    text_rep_good = font.render(trm,True,black)

                elif(pos[0]>=25 and pos[0]<=285 and pos[1]>=405 and pos[1]<=425 and console_show=='rep'):
                    details.Shell_1.detail_dict['oxi_station'].repair_shit()
                    trm=details.text_rep_message
                    text_rep_good = font.render(trm,True,black)
                    
                elif(pos[0]>=25 and pos[0]<=285 and pos[1]>=430 and pos[1]<=450 and console_show=='rep'):
                    details.Shell_1.detail_dict['generator'].repair_shit()
                    trm=details.text_rep_message
                    text_rep_good = font.render(trm,True,black)

### Функционал Кнопок полета ###
                for i in range(1,9):
                    if(pos[0]>=25 and pos[0]<=550 and pos[1]>=button_fly[0][i] and pos[1]<=button_fly[1][i] and console_show=='eng_use'):
                        if(pos[0]>=360 and pos[0]<=550):
                            details.Shell_1.detail_dict['engine'].use_engine(str(i))
                        
                        else:
                            details.Shell_1.detail_dict['engine'].use_engine_calc(str(i))
                        tnm=details.text_nav_message
                        text_nav_message = font.render(tnm,True,black)
            
            
           # Flag that we are done so we exit this loop
    # ОБРАБОТКА ВСЕХ СОБЫТИЙ ДОЛЖНА НАХОДИТЬСЯ НАД ЭТИМ КОММЕНТАРИЕМ
    
 
    # ВСЯ ИГРОВАЯ ЛОГИКА ДОЛЖНА НАХОДИТЬСЯ ПОД ЭТИМ КОММЕНТАРИЕМ

    
    # ВСЯ ИГРОВАЯ ЛОГИКА ДОЛЖНА НАХОДИТЬСЯ НАД ЭТИМ КОММЕНТАРИЕМ
 
 
    # ВЕСЬ КОД ДЛЯ РИСОВАНИЯ ДОЛЖЕН НАХОДИТЬСЯ ПОД ЭТИМ КОММЕНТАРИЕМ
    screen.fill(black)
    screen.blit(background_image, [0,0])
    screen.blit(ship_image, [0,0])
    screen.blit(dialog_wind_image,[0,0])
    screen.blit(status_wind_image,[size[0]-404,0])
    screen.blit(text_stat_name, [680,45])
    text_stat_fuel = font.render("Запас топлива:" + str(ship.Marvel.fuel),True,white)
    screen.blit(text_stat_fuel,[680,95])
    
    if(ship.Marvel.position[0] in navigation.Mercury.coord_x):
        text_inf_hello = font.render('Добро пожаловать на Меркурий',True,white)
        screen.blit(text_inf_hello,[680,70])
    elif(ship.Marvel.position[0] in navigation.Venus.coord_x):
        text_inf_hello = font.render('Добро пожаловать на Венеру',True,white)
        screen.blit(text_inf_hello,[680,70])
    elif(ship.Marvel.position[0] in navigation.Earth.coord_x):
        text_inf_hello = font.render('Добро пожаловать на Землю',True,white)
        screen.blit(text_inf_hello,[680,70])
    elif(ship.Marvel.position[0] in navigation.Mars.coord_x):
        text_inf_hello = font.render('Добро пожаловать на Марс',True,white)
        screen.blit(text_inf_hello,[680,70])
    elif(ship.Marvel.position[0] in navigation.Jupiter.coord_x):
        text_inf_hello = font.render('Добро пожаловать на Юпитер',True,white)
        screen.blit(text_inf_hello,[680,70])
    elif(ship.Marvel.position[0] in navigation.Saturn.coord_x):
        text_inf_hello = font.render('Добро пожаловать на Сатурн',True,white)
        screen.blit(text_inf_hello,[680,70])
    elif(ship.Marvel.position[0] in navigation.Uranus.coord_x):
        text_inf_hello = font.render('Добро пожаловать на Уран',True,white)
        screen.blit(text_inf_hello,[680,70])
    elif(ship.Marvel.position[0] in navigation.Neptune.coord_x):
        text_inf_hello = font.render('Добро пожаловать на Нептун',True,white)
        screen.blit(text_inf_hello,[680,70])
    
        
    if(console_show=='rep'):
        screen.blit(text_rep, [30,355])
        screen.blit(text_rep_eng, [40,380])
        screen.blit(text_rep_oxi, [40,405])
        screen.blit(text_rep_gen, [40,430])
        screen.blit(text_rep_good, [40,65])
    elif(console_show=='eng_use'):
        screen.blit(text_nav, [110,45])
        screen.blit(text_nav_Mer, [40,65])
        screen.blit(text_nav_Ven, [40,90])
        screen.blit(text_nav_Ear, [40,115])
        screen.blit(text_nav_Mar, [40,140])
        screen.blit(text_nav_Jup, [40,165])
        screen.blit(text_nav_Sat, [40,190])
        screen.blit(text_nav_Ura, [40,215])
        screen.blit(text_nav_Nep, [40,240])
        text_nav_message = font.render(str(details.text_nav_message),True,black)
        screen.blit(text_nav_message,[45,365])
        text_stat_pzdc = font.render(details.text_pzdc_message,True,black)
        screen.blit(text_stat_pzdc,[35,390])
        for i in range(8):
            screen.blit(text_nav_go, [360,65+(i*25)])
    elif(console_show=='inf'):
        screen.blit(text_inf_V, [40,65])
        screen.blit(text_inf_M, [40,90])
        screen.blit(text_inf_R, [40,115])
        screen.blit(text_inf_Pl, [40,140])
        screen.blit(text_inf_Sid, [40,165])
        screen.blit(text_inf_Sp, [40,190])
        
        
    pygame.display.flip()
    # ВЕСЬ КОД ДЛЯ РИСОВАНИЯ ДОЛЖЕН НАХОДИТЬСЯ НАД ЭТИМ КОММЕНТАРИЕМ

    # Ограничить до 20 кадров в секунду
    clock.tick(20)
pygame.quit ()
