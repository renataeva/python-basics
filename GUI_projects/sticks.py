from tkinter import *

window = Tk()
window.geometry('400x300')
window.resizable(False, False)
window.title('Палочки')

sticks = 20

def player():
    global sticks
    delete_sticks = int(entry_sticks.get())
    if delete_sticks <= 3 and delete_sticks < sticks:
        sticks-=delete_sticks
        label_sticks.config()


label_move = Label(font=('Arial', 15, 'bold'), text = 'Введите число от 1 до 3')
label_move.pack(pady=10, padx=10)

entry_sticks = Entry(font=('Arial', 15, 'bold'))
entry_sticks.pack(pady=10, padx=10)

label_sticks = Label(font=('Arial', 30, 'bold'), text = sticks*'|')
label_sticks.pack(pady=10, padx=10)

status = Label(font=('Arial', 30, 'bold'), text=20)
status.pack(pady=10, padx=10)

button_take = Button(font=('Arial', 15, 'bold'), text='Взять палочки')
button_take.pack(pady=10, padx=10)

window.mainloop()
