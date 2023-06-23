import random
from math import sqrt
from tkinter import *


class Tag():

    def __init__(self, data, listcolors):   #Класс меток
        self.ID = str(data[0])
        self.colormas = ["green", "yellow", "black", "orange", "red", "blue", "grey"]   #Доступные цвета
        self.color = random.choice(self.colormas)   #Изначально задается случайный цвет из доступных цветов
        self.label = Label(text=self.ID, bg='white', font=("Arial", 7))   #Название метки сверху
        self.label.pack()
        self.label.place(x=1000000, y=1000000)   #Изначально пакуем и убираем далеко, чтобы не мешалось
        listcolors.insert('end', "Color: " + str(self.color))   #Табло с цветами меток
        self.x = float(data[1])+5   #Координата метки по оси OX
        self.y = float(data[2])+5   #Координата метки по оси OY
        self.maspathx = []   #Массив последних 5 точек по оси OX метки для прорисовки следа
        self.maspathy = []   #Массив последних 5 точек по оси OY метки для прорисовки следа

    def check(self, data):   #Проверка новая/старая метка
        if (data[0]) == (self.ID):
            return True
        else:
            return False

    def update(self, data, color, listcolors, tags):   #Обновление метки
        self.x = float(data[1])   #Обновление координаты по оси OX
        self.y = float(data[2])   #Обновление координаты по оси OY
        if len(self.maspathx) == 5:   #проверка длины пути метки (если больше 5, удаляем самую старую метки и добавляем новую)
            del self.maspathx[0]
            del self.maspathy[0]
        self.maspathx.append(self.x)
        self.maspathy.append(self.y)

        if color == " ":
            pass
        else:
            listcolors.delete(0, 'end')
            for tag in tags:
                listcolors.insert('end', "Color: " + str(tag.color))   #Обновление табло с цветами

    def drawme(self, canvas, listcoords, pxinX, pxinY, tags, startx, starty, stopx, stopy):   #Отрисовка меток
        canvas.delete('ID'+str(self.ID))   #Удаление старых меток
        canvas.create_oval(int((self.x-startx)*pxinX) - int(3*10/(stopx-startx)),
                           canvas.winfo_height()-int((self.y-starty)*pxinY) - int(3*10/(stopy-starty)),
                           int((self.x-startx)*pxinX) + int(3*10/(stopx-startx)),
                           canvas.winfo_height()-int((self.y-starty)*pxinY) + int(3*10/(stopy-starty)),
                           fill=self.color, tag='ID'+str(self.ID))

        self.label.update()   #Обновление названия метки сверху
        self.label.place(x=int((self.x-startx)*pxinX) + 150 - self.label.winfo_width() / 2,   #Изменение координаты названия метки
                         y=canvas.winfo_height()-int((self.y-starty)*pxinY) - self.label.winfo_height() - 10 + 55)

        canvas.delete('path')   #Удаление старого следа
        for j in range(len(self.maspathx)):   #Отрисока нового следа
            if j == 0:   #Первая точка
                canvas.create_oval(int((self.maspathx[j]-startx) * pxinX) - int(1*10/(stopx-startx)),
                                   canvas.winfo_height() - int((self.maspathy[j]-starty) * pxinY) - int(1*10/(stopy-starty)),
                                   int((self.maspathx[j]-startx) * pxinX) + int(1*10/(stopx-startx)),
                                   canvas.winfo_height() - int((self.maspathy[j]-starty) * pxinY) + int(1*10/(stopy-starty)),
                                   fill=self.color, tag='path')
            if j == 1:   #Вторая точка
                canvas.create_oval(int((self.maspathx[j]-startx) * pxinX) - int(1*10/(stopx-startx)),
                                   canvas.winfo_height() - int((self.maspathy[j]-starty) * pxinY) - int(1*10/(stopy-starty)),
                                   int((self.maspathx[j]-startx) * pxinX) + int(1*10/(stopx-startx)),
                                   canvas.winfo_height() - int((self.maspathy[j]-starty) * pxinY) + int(1*10/(stopy-starty)),
                                   fill=self.color, tag='path')
            if j == 2:   #Третья точка
                canvas.create_oval(int((self.maspathx[j]-startx) * pxinX) - int(2*10/(stopx-startx)),
                                   canvas.winfo_height() - int((self.maspathy[j]-starty) * pxinY) - int(2*10/(stopy-starty)),
                                   int((self.maspathx[j]-startx) * pxinX) + int(2*10/(stopx-startx)),
                                   canvas.winfo_height() - int((self.maspathy[j]-starty) * pxinY) + int(2*10/(stopy-starty)),
                                   fill=self.color, tag='path')
            if j == 3:   #Четвертая точка
                canvas.create_oval(int((self.maspathx[j]-startx) * pxinX) - int(2*10/(stopx-startx)),
                                   canvas.winfo_height() - int((self.maspathy[j]-starty) * pxinY) - int(2*10/(stopy-starty)),
                                   int((self.maspathx[j]-startx) * pxinX) + int(2*10/(stopx-startx)),
                                   canvas.winfo_height() - int((self.maspathy[j]-starty) * pxinY) + int(2*10/(stopy-starty)),
                                   fill=self.color, tag='path')
            if j == 4:   #Пятая точка
                canvas.create_oval(int((self.maspathx[j]-startx) * pxinX) - int(3*10/(stopx-startx)),
                                   canvas.winfo_height() - int((self.maspathy[j]-starty) * pxinY) - int(3*10/(stopy-starty)),
                                   int((self.maspathx[j]-startx) * pxinX) + int(3*10/(stopx-startx)),
                                   canvas.winfo_height() - int((self.maspathy[j]-starty) * pxinY) + int(3*10/(stopy-starty)),
                                   fill=self.color, tag='path')

        listcoords.delete(0, 'end')   #Удаление старых координат их табло
        for tag in tags:   #Запись новых координат в табло
            listcoords.insert('end', tag.ID + " X: " + str(round(tag.x, 2)) + " Y: " + str(round(tag.y, 2)))
