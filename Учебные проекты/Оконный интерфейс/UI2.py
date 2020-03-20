from tkinter import *
from tkinter.ttk import Combobox
from tkinter.ttk import Checkbutton
from tkinter.ttk import Radiobutton

def clicked():  
    res = "Привет {}".format(txt.get())
    lbl.configure(text=res)
    lbl2.configure(text="Я же просил...")  

window = Tk()
window.title("Пользовательский интерфейс") # Заголовок окна

lbl = Label(window, text="Привет") 
lbl.grid(column=0, row=0)

lbl2 = Label(window, text="Привет", font=("Arial Bold", 10))
lbl2.grid(column=0, row=1)

txt = Entry(window,width=10)  
txt.focus()
txt.grid(column=1, row=0)  

btn = Button(window, text="Не нажимать!")
btn.grid(column=0, row=2)

btn2 = Button(window, text="Не нажимать!", bg="black", fg="red", command=clicked)
btn2.grid(column=1, row=2)

combo = Combobox(window)  
combo['values'] = (1, 2, 3, 4, 5, "Текст")  
combo.current(1)  # установите вариант по умолчанию  
combo.grid(column=0, row=3)  

chk_state = BooleanVar()  
chk_state.set(True)  # задайте проверку состояния чекбокса  
chk = Checkbutton(window, text='Выбрать', var=chk_state)  
chk.grid(column=1, row=3)  

chk_state2 = IntVar()
chk_state2.set(0) # False
chk_state2.set(1) # True
chk2 = Checkbutton(window, text='Выбрать', var=chk_state2)  
chk2.grid(column=2, row=3)  

def clicked2():
    lbl2.configure(text="radiobutton1")  
rad1 = Radiobutton(window, text='Первый', value=1, command=clicked2)  
rad2 = Radiobutton(window, text='Второй', value=2)  
rad3 = Radiobutton(window, text='Третий', value=3)  
rad1.grid(column=0, row=4)  
rad2.grid(column=1, row=4)  
rad3.grid(column=2, row=4)  



window.geometry('400x250') # Размер окна
window.mainloop() # Бесконечный цикл, ожидающий взаимодействия

