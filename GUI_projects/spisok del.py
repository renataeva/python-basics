from tkinter import *
from tkinter import filedialog

# nastojki okna
window = Tk()
window.geometry('300x600')
window.title('Spisok del')
window.maxsize(300, 600)
window.minsize(300, 600)
window.config(bg='#c2ffea')

numeration = 0

def save():
    text = todolist.get(0.0, END)
    file = filedialog.asksaveasfile(
        title='Save file',
        filetypes=(('txt files', '*.txt'), ('all files', '*.*')))
    if file:
        file.write(text)


def load():
    todolist.delete(0.0, END)
    file = filedialog.askopenfile(title='Select file',
                                  filetypes=(('txt '
                                  'files', '*.txt'), ('all files', '*.*')))
    text = file.read()
    todolist.insert(END, text)


def delete_f():
    global numeration
    todolist.delete(0.0, END)
    numeration = 0


def clear(what_l, when_l):
    what_l.delete(0, END)
    when_l.delete(0, END)


def add():
    global numeration
    numeration += 1
    text = str(numeration) + '.' + what.get() + "\t" + when.get()+'\n'
    todolist.insert(END, text)
    clear(what, when)


frame = LabelFrame(text='Записать важное дело', width=300, height=150,
                   bg='pale turquoise')
frame.pack(pady=5, padx=10)


label1 = Label(frame, text='Какое дело?', relief=GROOVE, border=3,  fg='black',
               bg='bisque')
label1.grid(pady=5, padx=10, column=0, row=0)

what = Entry(frame, bg='white', fg='black', font='Arial8',
             justify=CENTER, relief=RAISED, width=9, state=NORMAL)
what.grid(column=0, row=1, pady=10, padx=10)

label2 = Label(frame, text='Когда?', relief=GROOVE, border=3,  fg='black',
               bg='PeachPuff2')
label2.grid(pady=5, padx=10, column=1, row=0)

when = Entry(frame, bg='white', fg='black', font='Arial8',
             justify=CENTER, relief=RAISED, width=9, state=NORMAL)
when.grid(pady=10, padx=10, column=1, row=1)


todolist = Text(width=30, height=18)
todolist.pack()


addbutton = Button(frame, text='Добавить важное дело', command=add,
                   relief=GROOVE, border=3, bg='LightSteelBlue1')
addbutton.grid(pady=10, padx=10, column=0, row=2, columnspan=2)


deleteb = Button(text='Удалить все', command=delete_f,
                 relief=RAISED,
                 border=5, bg='VioletRed1')
deleteb.pack(pady=10, padx=10)

saveb = Button(text='Save', command=save, relief=RAISED, border=5, bg='medium spring green')
saveb.pack(pady=10, padx=10)

loadb = Button(text='Load', command=load, relief=RAISED, border=5, bg='plum1')
loadb.pack(pady=10, padx=10)


window.mainloop()
