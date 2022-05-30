import tkinter as tk #Импортируем библиотеку tkinter
from math import *
from tkinter import messagebox #Библиотека позволяет
def add_digit(digit): #Функция позволяет добавлять цифры в entry
    value=calc.get() #Берет значение из entry
    if value[0]=='0' and len(value) == 1:
            value = value[1:]
    calc.delete(0,tk.END)
    calc.insert(0,value+digit) #конкатенация
def add_oper(oper):  #Функция позволяет добавлять операции в entry
    value = calc.get()
    if value[-1] in '*^/+-':
        value = value[:-1] #Срезаем знак операции если он повторяется, чтобы нельзя было написать */-
    elif value[-1] in 'mod':
        value = value[:-3] #срезаем слово мод отдельно, тк в нем три символа
    elif '+' in value or '-' in value or '*' in value or '/' in value or 'mod' in value or '^' in value: #Чтобы считать больше одной операции
        calculate()
        value = calc.get()
    calc.delete(0, 'end')
    calc.insert(0, value+oper)
def calculate(): #Функция производит подсчет
    value = calc.get() #Сохраняем значение из виджета entry
    operations = ['+', '-', '/', 'mod', '^', '*'] # Наши операции
    result1 = 0 #Создаем переменную результат
    #Следующие 6 строк написаны для работы фунцкии 6*=
    if value[-1] == 'd':
        calc.delete(0, 'end')
        calc.insert(0, 1)
        return
    if value[-1] in operations:
        value = value + value[:-1]
    for i in range(6): #Цикл для проверки операций
        promres = operations[i] #Cохраняем операцию
        entry1 = value.split(promres) #Используем сплит чтобы получить массив вида ['1','21']
        if len(entry1) == 2:    #Проверяем длинну массива
            if promres == '+': #Проверяем знак
                result1 = float(entry1[0]) + float(entry1[1])
            elif promres == '/':
                if entry1[1] == '0': #Проверка на ноль
                    messagebox.showinfo("ВНИМАНИЕ!", "На ноль делить нельзя!!!!")
                    calc.delete(0, 'end')
                    calc.insert(0, 0)  # Вставляем нули, чтобы как в настоящем калькуляторе все начиналось с 0
                    return
                else:
                     result1 = float(entry1[0]) / float(entry1[1])
            elif promres == '-':#Проверяем знак
                result1 = float(entry1[0]) - float(entry1[1])
            elif promres == 'mod':#Проверяем знак
                result1 = float(entry1[0]) % int(entry1[1])
            elif promres == '*':#Проверяем знак
                result1 = float(entry1[0]) * float(entry1[1])
            elif promres == '^':#Проверяем знак
                result1 = float(entry1[0]) ** float(entry1[1])
    calc.delete(0, 'end')  #Очищает enrty, но у нас все в value хранится
    if result1 - 0.0000001 < floor(result1):
        calc.insert(0, int(result1))
    else:
        calc.insert(0, result1)


def clear():  #Чистит ввод
    calc.delete(0, 'end')
    calc.insert(0,0) #Вставляем нули, чтобы как в настоящем калькуляторе все начиналось с 0
def clearlast():  #Убирает последний символ ввода
    calc.delete(len(calc.get()) - 1,len(calc.get()))#Обращаемся к предпоследнему и последнему символу в воде
    if len(calc.get()) == 0:
        calc.insert(0,0)

def make_digit(digit): #Фукнция создает кнопку, используем только на цифры
    return tk.Button(text=digit, font=('Times New Roman',16,'bold'), bg = 'black', fg = 'white',
                     command=lambda: add_digit(digit))
def make_oper(oper): #Фукнция создает кнопку, используем только на операции
    return tk.Button(text=oper, font=('Times New Roman', 16,'bold'),bg = 'black', fg = '#66ff99',
                     command=lambda: add_oper(oper))
def make_result(result): #Фукнция создает кнопку, используем только на знак равно
    return tk.Button(text=result, font=('Times New Roman', 16,'bold'),bg = 'black', fg = '#66ff99',
                     command=calculate)
def make_clear_butt(cc): #Фукнция создает кнопку, используем только на C
    return tk.Button(text=cc, font=('Times New Roman', 16,'bold'),bg = 'black', fg = '#66ff99',
                     command=clear)
def make_clearlast_butt(symb): #Фукнция создает кнопку, используем только на <=, удаляет последний символ
    return tk.Button(text=symb, font=('Times New Roman', 16,'bold'),bg = 'black', fg = '#66ff99',
                     command=clearlast)

def presskey(event): #Функция для контроля ввода с клавиатуры
    if event.char.isdigit():   #С клавиатуры можно вводить только цифры
        add_digit(event.char) #Добавляем в entry
    elif event.char in '+-*/^mod': #Добавляем проверку чтобы можно было вводить знаки операций
        add_oper(event.char)  #Добавляем в entry
    elif event.char == '\r': #Позволяет использовать enter, как знак равно
        calculate() #Вызываем функцию для подсчета



win=tk.Tk() #Создаем окно
win.geometry(f'300x350+500+400') #Размеры окна
win['bg']='black' #Бэкграунд черный
win.title('Калькулятор')  #Название окна
win.resizable(False,False)

win.bind('<Key>', presskey)  #Задаем для клавиш действия, их мы описываем в нашей функции presskey

calc=tk.Entry(win,justify=tk.RIGHT, bd = 0, font=('Times New Roman',21),width=20, bg = 'black',fg ='#ff99ff') #Создаем виджет entry и задаем ему параметры
calc.insert(0,'0') #Вставляем нули, чтобы как в настоящем калькуляторе все начиналось с 0
calc.grid(row=0,column=0,columnspan=4,stick='we')  #Располагаем entry на окне и выравниваем

make_digit('1').grid(row=2, column=0, stick='wens') #Вызываем функцию создания цифры и располагаем на окне
make_digit('2').grid(row=2, column=1, stick='wens')
make_digit('3').grid(row=2, column=2, stick='wens')
make_digit('4').grid(row=3, column=0, stick='wens')
make_digit('5').grid(row=3, column=1, stick='wens')
make_digit('6').grid(row=3, column=2, stick='wens')
make_digit('7').grid(row=4, column=0, stick='wens')
make_digit('8').grid(row=4, column=1, stick='wens')
make_digit('9').grid(row=4, column=2, stick='wens')
make_digit('0').grid(row=5, column=1, stick='wens')

make_oper('+').grid(row = 1, column = 3, stick = 'wens')#Вызываем функцию создания операции и располагаем на окне
make_oper('-').grid(row = 2, column = 3, stick = 'wens')
make_oper('*').grid(row = 3, column = 3, stick = 'wens')
make_oper('/').grid(row = 4, column = 3, stick = 'wens')
make_oper('^').grid(row = 1, column = 1, stick = 'wens')
make_oper('mod').grid(row = 1, column = 0, stick = 'wens')

make_result('=').grid(row = 5, column = 2, stick = 'wens',columnspan = 2) #Cоздаем и располагаем равно

make_clear_butt('C').grid(row = 5, column = 0, stick = 'wens') #Cоздаем и распологаем кнопку для чистки ввода

make_clearlast_butt('<=').grid(row = 1, column = 2, stick = 'wens')#Cоздаем и распологаем кнопку для удаления последнего символа

win.grid_columnconfigure(0,minsize=70) #Конфигурируем кнопки, а именно их размер
win.grid_columnconfigure(1,minsize=70)
win.grid_columnconfigure(2,minsize=70)
win.grid_columnconfigure(3,minsize=70)
win.grid_rowconfigure(1,minsize=60)
win.grid_rowconfigure(2,minsize=60)
win.grid_rowconfigure(3,minsize=60)
win.grid_rowconfigure(4,minsize=60)
win.grid_rowconfigure(5,minsize=60)
win.mainloop() #Главный цикл, без него окно не откроется