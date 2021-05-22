from tkinter import *

window = Tk()
window.geometry('400x250')
window.title('Виджеты и их аргументы')

text = '''Lorem ipsum dolor sit amet, consectetur
 adipiscing elit. Sed sit amet ipsum
  sit amet eros auctor interdum.'''

frame1 = Frame(bg='#7a249c', relief=GROOVE, bd=1)
frame1.pack()
frame2 = Frame(bg='#7a249c')
frame2.pack(pady=10)

label1 = Label(frame1, text=text, relief=RAISED, bd=2, bg='#7a249c',
                    fg='white', font='arial 10 underline', width=40,
                    height=5)
label1.grid(columnspan=2)

button10 = Button(frame2, text='Запуск', bg='green', fg='black', width=10,
                  activebackground='DarkSeaGreen1')
button10.grid(pady=10, padx=20, row=1, column=0)
button11 = Button(frame2, text='Выход', bg='red', fg='black', width=10,
                  activebackground='DarkSeaGreen1')
button11.grid(pady=10, padx=20, row=1, column=1)


window.mainloop()
