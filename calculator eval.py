import tkinter as tk #Импортируем библиотеку tkinter
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
    calc.delete(0, 'end')
    calc.insert(0, value+oper)
def calculate(): #Функция производит подсчет
    value = calc.get()
    if '^' in value:  #Чтобы возводить в степень надо поменять ^ на **
        value = value.replace("^", "**")
    if 'mod' in value:  #Чтобы брать остаток надо поменять mod на %
        value = value.replace("mod", "%")
    if value [-1] in '+-/*%**': #Повзоляет провести операцию вида "36*=" будет выведено 36 ^ 2
        value = value + value[:-1]
    calc.delete(0, 'end')  #Очищает enrty, но у нас все в value хранится
    try: #Пытается провести операцию
        calc.insert(0, eval(value))  #Через функцию eval считаем данные которые в value
    except (NameError, SyntaxError):    #Если у нас ошибки такого вида, всплывает окно(это нам дает сделать messagebox_
        messagebox.showinfo("ОШИБКА","Неправильный ввод. Можно вводить только цифры и операции!!")
        calc.insert(0,0)  #Вставляем нули, чтобы как в настоящем калькуляторе все начиналось с 0
    except ZeroDivisionError: #(это всё нам дает сделать messagebox)
        messagebox.showinfo("ВНИМАНИЕ!","На ноль делить нельзя!!!!")
        calc.insert(0,0)  #Вставляем нули, чтобы как в настоящем калькуляторе все начиналось с 0
def clear():  #Чистит ввод
    calc.delete(0, 'end')
    calc.insert(0,0) #Вставляем нули, чтобы как в настоящем калькуляторе все начиналось с 0
def clearlast():  #Убирает последний символ ввода
    calc.delete(len(calc.get()) - 1,len(calc.get()))#Обращаемся к предпоследнему и последнему символу в воде
    if len(calc.get()) == 0:
        calc.insert(0,0)

def make_digit(digit): #Фукнция создает кнопку, используем только на цифры
    return tk.Button(text=digit,bd=5, font=('Times New Roman',16,'bold'), bg = 'black', fg = 'white',
                     command=lambda: add_digit(digit))
def make_oper(oper): #Фукнция создает кнопку, используем только на операции
    return tk.Button(text=oper, bd=5, font=('Times New Roman', 16,'bold'),bg = 'black', fg = '#66ff99',
                     command=lambda: add_oper(oper))
def make_result(result): #Фукнция создает кнопку, используем только на знак равно
    return tk.Button(text=result, bd=5, font=('Times New Roman', 16,'bold'),bg = 'black', fg = '#66ff99',
                     command=calculate)
def make_clear_butt(cc): #Фукнция создает кнопку, используем только на C
    return tk.Button(text=cc, bd=5, font=('Times New Roman', 16,'bold'),bg = 'black', fg = '#66ff99',
                     command=clear)
def make_clearlast_butt(symb): #Фукнция создает кнопку, используем только на <=, удаляет последний символ
    return tk.Button(text=symb, bd=5, font=('Times New Roman', 16,'bold'),bg = 'black', fg = '#66ff99',
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