#-*- coding:utf-8 -*-
#Игра Виселица

import math #подключаем модуль math
import time #подключаем модуль для определения времени и работы со временем
import random
import data
from tkinter import * #подключаем графическую библиотеку tkinter
root = Tk()
canvas = Canvas(root, width = 800, height = 500) #инициализация холста 500х500
canvas.pack()#размещаем холст в нашем окне
# Объявление глобальных переменных
which_screen = ""  #флаг показывающий какой сейчас экран
sucses = 0 # переменная для отрисовывания фразы "есть такая буква"
mistake = 0 # переменная для отрисовывания фразы "нет такой буквы"
congr = 0 # переменная для отрисовывания фразы "поздравляем вы отгадали слово"
pos_let = 0 # позиция буквы в слове
s = 0  
abc = []  #алфавит
naz_buk = [] # названные буквы
s_list = []
z = 0
def random_word_and_calc():
    global i, otstup, x1, x2, y1, y2, wwh, answer_const, pos, abc
    abc = ["а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п",
       "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я"]
    pos = random.randint(0, 12)
    answer = data.answers[pos]
    answer = answer.lower()
    answer_const = answer
    i = len(answer)
    let = ""
    wwh = i * "*"
    width = 800
    midle = 800/2
    l = 70 #длина бОльшего квадрата она же ширина
    long = 70 * i #длина всей цепочки квадратов
    otstup = ((width - long)/2) - 100
    x1 = otstup
    x2 = otstup + 70
    y1 = 50
    y2 = y1 + 70
# функции для ленивых
#отрисовка текста
def text(x1, x2, string, fon, color):
    s = canvas.create_text(x1, x2, text = string, font = fon, fill = color)
    return s
#отрисовка линий
def line(x1, y1, x2, y2, w, color):
    canvas.create_line(x1, y1, x2, y2, width = w, fill = color)
#линии повешенного    
def hang_man(c):
    global z
    hang_list = [(600, 250, 700, 250, 5, "blue"),
                 (650, 250, 650, 50, 4, "blue"),
                 (650, 50, 700, 50, 4, "blue"),
                 (700, 50, 700, 70, 2, "blue"),                 
                 (650, 50, 700, 50, 4, "blue"),
                 (700, 120, 700, 180, 3, "blue"),
                 (700, 180, 675, 210, 3, "blue"),
                 (700, 180, 725, 210, 3, "blue"),
                 (675, 150, 725, 150, 3, "blue"),
                 (675, 150, 725, 150, 3, "blue")]
    s = hang_list[c]
    
    return s

#отрисовка прямоугольников    
def rect(x1, y1, x2, y2, color, outline, w):
    rec = canvas.create_rectangle(x1, y1, x2, y2, fill = color, outline = outline, width = w)
    return rec
#обработка и вывод названных букв
def nazv_bukvy(bukva):
    global abc, naz_buk, s
    if bukva in abc:
        canvas.delete(s)
        i = abc.index(bukva, 0, len(abc))
        abc.pop(i)
        naz_buk.append(bukva)
        text(300, 370, "названные буквы:", "Arial, 20", "blue")
        s = text(300, 450, naz_buk, "Arial, 16", "blue")
              
    else:
       pass

# основная функция    
def pole_chudes(let):
    global sucses, mistake, congr, wwh, z
    nazv_bukvy(let)
    wwh_list = list(wwh)
    wwh_list_1 = wwh_list
    count = 0
    for elem in answer_const:
        if elem != let:
            count = count + 1
            
        else:
            wwh_list[count] = let
            
            create_let_in_pos(count, wwh_list)
            root.update()
            count = count + 1
    
    if let in wwh_list_1:
        canvas.delete(mistake, sucses)
        sucses = text(300, 250, "есть такая буква", "Arial, 16", "blue")
        
    else:
        canvas.delete(sucses, mistake)
        mistake = text(300, 250, "нет такой буквы", "Arial, 16", "blue")
                
        if z != 4:
            s = hang_man(z)
            line(s[0], s[1], s[2], s[3], s[4], s[5])
            z = z + 1
        else:
            canvas.create_oval([675, 70], [725, 120], outline = "blue", width = 3)
            z = z + 1
        if z == 9:
            s = hang_man(z)
            line(s[0], s[1], s[2], s[3], s[4], s[5])
            root.update()
            time.sleep(1.5)
            game_over()  
        
    wwh = "".join(wwh_list)
    j = wwh.find("*", 0, len(wwh))
    if j == -1:
        time.sleep(1.5)
        victory()      
    return wwh
#создаем квадраты как в поле чудес по колличеству букв в слове
def create_sq(i, x1, x2, y1, y2):
    while i > 0:
        i = i - 1
        question = text(300, 200, data.questions[pos], "Arial, 16", "blue")
        rec1 = rect(x1, y1, x2, y2, "white", "blue", "4")
        rec2 = rect(x1 + 5, y1 + 5, x2 - 5, y2 - 5, "blue", "white", "1")
        x1 = x1 + 70
        x2 = x2 + 70
    return rec1, rec2
#в нужном квадрате прописываем отгаданную букву
def create_let_in_pos(index, our_list):
    k = index
    if i % 2 == 0:
        x1 = otstup
        x2 = x1 + 70
        x1 = x1 + 70 * k
        x2 = x2 + 70 * k
        rec3 = rect(x1 + 5, y1 + 5, x2 - 5, y2 - 5, "white", "white", "1")
        lit = text(x1 + 35, y1 + 30, our_list[index], "Arial, 40", "blue")
        
        return rec3   
    else:
        x1 = otstup - 35/2
        x2 = x1 + 70
        x1 = x1 + 70 * k
        x2 = x2 + 70 * k
        rec3 = rect(x1 + 5, y1 + 5, x2 - 5, y2 - 5, "white", "white", "1")
        lit = text(x1 + 35, y1 + 30, our_list[index], "Arial, 40", "blue")
        return rec3

        
    
def start_(event):
    global which_screen, s
    if which_screen == "":
        canvas.delete("all")
        random_word_and_calc()
        s = 0
        which_screen = "game_start"
        if i % 2 == 0: 
            x1 = otstup
            x2 = x1 + 70
            create_sq(i, x1, x2, y1, y2)
    
        else:
        
            x1 = otstup - 35/2
            x2 = x1 + 70
            create_sq(i, x1, x2, y1, y2)
    else:
        pass
#выводит надпись игра окончена    
def game_over():
    global which_screen, naz_buk, z
    naz_buk = []
    z = 0
    canvas.delete("all")
    which_screen = ""
    game_ov = text(400, 200, "Вы проиграли", "Arial, 48", "blue")
    game_stert = text(400, 400, "нажмите пробел чтобы начать новую игру", "Arial, 16", "blue")
# выводит надпись вы выиграли    
def victory():
    global which_screen, naz_buk, z
    z = 0
    naz_buk = []
    canvas.delete("all")
    which_screen = ""
    game_ov = text(400, 200, "Вы выиграли", "Arial, 48", "blue")
    game_stert = text(400, 400, "нажмите пробел чтобы начать новую игру", "Arial, 16", "blue")

#ожидаем нажатия клавиши с буквами для отгадывания слова        
def onKeyPress(event):
    global which_screen
    if which_screen == "game_start":
        let = event.char
        pole_chudes(let)
        
    if which_screen == "game_over":
        pass
    if which_screen == "victory":
        pass
    
    else:
        pass
    

#Заставка
text_title = text(400, 100, "ВИСЕЛИЦА", "Arial, 64", "blue")
text_instr = text(400, 400, "нажмите пробел и игра начнется", "Arial, 16", "blue")
canvas.focus_set()
canvas.bind("<space>", start_)

canvas.bind("<KeyPress>", onKeyPress)

    
root.update()
root.mainloop()
