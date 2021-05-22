from tkinter import *

# nastojki okna
window = Tk()
window.geometry('400x500')
window.title('Позиционирование виджетов')


frame1 = LabelFrame(text='Pack', width=300, height=100)
frame1.place(x=40, y=350)
frame2 = LabelFrame(text='Gird', width=300, height=100)
frame2.place(x=75, y=100)
frame3 = LabelFrame(text='Place', width=300, height=100)
frame3.place(x=40, y=0)

button10 = Button(frame1, text='Button 10', bg='black', fg='white', width=10)
button10.pack(pady=10, padx=10, side=LEFT)
button11 = Button(frame1, text='Button 11', bg='black', fg='white', width=10)
button11.pack(pady=10, padx=10, side=LEFT)
button12 = Button(frame1, text='Button 12', bg='black', fg='white', width=10)
button12.pack(pady=10, padx=10, side=LEFT)
esc = Button(text='Close program', width=20, command=quit)
esc.place(x=100, y=450)

button20 = Button(frame2, text='Button 20', bg='black', fg='white', width=28)
button20.grid(pady=10, padx=10, column=0, row=0, columnspan=2)
button21 = Button(frame2, text='Button 21', bg='black', fg='white', width=10)
button21.grid(pady=10, padx=10, column=0, row=1)
button22 = Button(frame2, text='Button 22', bg='black', fg='white', width=10,
                  height=10)
button22.grid(pady=10, padx=10, column=1, row=1, rowspan=3)
button23 = Button(frame2, text='Button 23', bg='black', fg='white', width=10)
button23.grid(pady=10, padx=10, column=0, row=2)
#button24 = Button(frame2, text='Button 11', bg='black', fg='white', width=10)
#button24.grid(pady=10, padx=10, column=1, row=2)
button25 = Button(frame2, text='Button 25', bg='black', fg='white', width=10)
button25.grid(pady=10, padx=10, column=0, row=3)

button30 = Button(frame3, text='Button 30', bg='black', fg='white', width=10)
button30.place(x=60, y=25)
button31 = Button(frame3, text='Button 31', bg='black', fg='white', width=10)
button31.place(x=150, y=25)


window.mainloop()
