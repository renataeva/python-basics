from tkinter import *
import random

window = Tk()
window.geometry('250x350')
window.title('Будильник')
window.iconbitmap('alarm.ico')


def deletef():
    indexes = alarmbox.curselection()
    for i in reversed(indexes):
        alarmbox.delete(i)
    status.config(text=f'Всего будильников: {alarmbox.size()}')


def open_change_window():
    change = Toplevel()
    change.title('Изменить')
    change.geometry('300x125')
    change.iconbitmap('alarm.ico')

    label_change = Label(change, text='Введите новое значение будильника')
    label_change.pack(padx=10, pady=10)

    newalarm = Entry(change, justify=CENTER)
    newalarm.pack(padx=10, pady=10)
    a = alarmbox.curselection()[0]
    al = alarmbox.get(a)
    newalarm.insert(0, al)

    def update_alarm():
        na = newalarm.get()
        print(a)
        alarmbox.delete(a)
        alarmbox.insert(a, na)
        change.destroy()

    saveb = Button(change, text='Сохранить', command=update_alarm)
    saveb.pack(pady=5, padx=10)




def generate_alarms():
    alarms = []
    a = 0
    b = 5
    for _ in range(10):
        m = random.randint(a, b)
        if m >= 10:
            alarms.append(f'07:{m}')
        else:
            alarms.append(f'07:0{m}')
        a += 6
        b += 6
    alarmbox.insert(END, *alarms)
    status.config(text=f'Всего будильников: {alarmbox.size()}')


label1 = Label(text='Будилники')
label1.pack(pady=5, padx=10)

alarmbox = Listbox(width=30, height=10, justify=CENTER, selectmode=EXTENDED)

status = Label(text=f'Всего будильников: 0')
status.pack(pady=5, padx=10)

alarmbox.pack()

randomb = Button(text='Случайные будильники', command=generate_alarms)
randomb.pack(pady=5, padx=10)

deleteb = Button(text='Удалить будильник', command=deletef)
deleteb.pack(pady=5, padx=10)

config = Button(text='Изменить будильники', command=open_change_window)
config.pack(pady=5, padx=10)


window.mainloop()
