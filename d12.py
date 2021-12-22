from tkinter import *
from tkinter import messagebox
import random


def func():
    output_field.delete(1.0, END)
    
    ed_izm = list(lis.curselection())
    ed_izm = spisok[ed_izm[0]]
    second_ed_izm = ''
    
    product = ''
    kol_vo = float(input_field.get(1.0,END))
    new_kol_vo = 0
    
    if ed_izm == 'Литры':
        second_ed_izm = 'кг'
        ed_izm = 'л'
        
        if var.get() == 0:
            product = 'Сметана 36%'
            new_kol_vo = kol_vo/0.994
        elif var.get() == 1:
            product = 'Сметана 20%'
            new_kol_vo = kol_vo/1.012
        elif var.get() == 2:
            product = 'Сметана 15%'
            new_kol_vo = kol_vo/1.02
        elif var.get() == 3:
            product = 'Кефир'
            new_kol_vo = kol_vo/0.97
        elif var.get() == 4:
            product = 'Ряженка'
            new_kol_vo = kol_vo/0.9984
        else:
            messagebox.showerror('Ошибка', 'Ошибка!')
    elif ed_izm == 'Килограммы':
        second_ed_izm = 'л'
        ed_izm = 'кг'
        
        if var.get() == 0:
            product = 'Сметана 36%'
            new_kol_vo = kol_vo*0.994
        elif var.get() == 1:
            product = 'Сметана 20%'
            new_kol_vo = kol_vo*1.012
        elif var.get() == 2:
            product = 'Сметана 15%'
            new_kol_vo = kol_vo*1.02
        elif var.get() == 3:
            product = 'Кефир'
            new_kol_vo = kol_vo*0.97
        elif var.get() == 4:
            product = 'Ряженка'
            new_kol_vo = kol_vo*0.9984
        else:
            messagebox.showerror('Ошибка', 'Ошибка!')
    else:
        messagebox.showerror('Ошибка', 'Ошибка!')
    
    new_kol_vo = round(new_kol_vo,4)
    output_field.insert(1.0, str(product)+'\n'+str(kol_vo)+' '+ed_izm+' = '+str(new_kol_vo)+' '+second_ed_izm)
    with open('Changelog.txt', 'a') as file:
        file.write(str(product)+'\n'+str(kol_vo)+' '+ed_izm+' = '+str(new_kol_vo)+' '+second_ed_izm+'\n\n')
    

#ИНТЕРФЕЙС
win = Tk()
win.title("Молочные продукты")
win.configure(background = 'light gray')
win.geometry("500x300")
win.resizable(height = 0, width = 0)

label = Label(win, text = 'Выберите продукт:',bg = "white")
label.grid(row = 0, column = 2, columnspan = 2)

var=IntVar()
var.set(3)
rad0 = Radiobutton(win, text="Сметана 36%", variable=var, value=0,bg = "white")
rad0.grid(row = 1, column = 2)

rad1 = Radiobutton(win, text="Сметана 20%", variable=var, value=1,bg = "white")
rad1.grid(row = 2, column = 2)

rad2 = Radiobutton(win, text="Сметана 15%", variable=var, value=2,bg = "white")
rad2.grid(row = 3, column = 2, pady = 5)

rad3 = Radiobutton(win, text="Кефир            ", variable=var, value=3,bg = "white")
rad3.grid(row = 1, column = 3, padx = 10)

rad4 = Radiobutton(win, text="Ряженка         ", variable=var, value=4,bg = "white")
rad4.grid(row = 2, column = 3, padx = 10)


label2 = Label(win, text = 'Выберите ед. измерения:',bg = "white")
label2.grid(row = 0, column = 0, padx = 5, pady = 5)

spisok = ['Килограммы','Литры']
lis = Listbox(win, selectmode=SINGLE, height=2)
for name in spisok:
   lis.insert(END, name)
lis.grid(row = 1, column = 0, padx = 5)


label3 = Label(win,text = 'Введите кол-во ↓',bg = "white")
label3.grid(row = 2, column = 0, padx = 5, pady = 5)

input_field = Text(win, height = 2, width = 25, font = "lucida 10",)
input_field.grid(row = 3, column = 0, padx = 10)

label4 = Label(win, text = 'Вывод ↓ ',bg = "white")
label4.grid(row = 4, column = 0, padx = 5, pady = 5)

output_field = Text(win, height = 2, width = 25, font = "lucida 10",)
output_field.grid(row = 5, column = 0, padx = 10)

button = Button(win,text = "Ввод",bg = "white",command = func)
button.grid(row = 6, column = 0, pady = 5, padx = 10)

win.mainloop()