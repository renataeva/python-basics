from tkinter import *

wiget_set = True

window = Tk()
window.geometry('400x300')
window.maxsize(400, 300)
window.minsize(400, 300)
window.title('Ввод-вывод данных')


def dark():
    window['bg'] = '#353535'
    passwordbox.config(fg='white', bg='#353535')
    label1.config(fg='white', bg='#353535')
    label2.config(bg='#353535')
    showbutton.config(fg='white', bg='#535353')
    themechange.config(fg='white', bg='#535353', state=DISABLED)


passwordbox = LabelFrame(text='Проверка пароля', width=170, height=180)
passwordbox.pack(pady=5, padx=10)

label1 = Label(passwordbox, text='Введите пароль')
label1.pack(pady=5, padx=10)

inputbox = Entry(passwordbox, bg='gray18', fg='lavender blush',
                 font='Helvetica12', justify=CENTER, relief=RAISED, width=15,
                 state=NORMAL, show='*')
inputbox.pack(pady=5, padx=10)


label2 = Label(passwordbox)
label2.pack(pady=5, padx=10)

label3 = Label(passwordbox)
label3.pack(pady=5, padx=10)


def symbols(pasword):
    print(pasword)
    ABCD = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n',
            'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    nums = list(range(10))

    # space check
    if ' ' in pasword:
        label3.config(text='space is not allowed', fg='red')
        wiget_set = False

        return

    # number check
    num_in_pass = False
    for i in nums:
        if str(i) in pasword:
            num_in_pass = True
            break
    if not num_in_pass:
        label3.config(text='must contain number', fg='red')
        wiget_set = False
        return

    # char check
    char_in_pass = False
    for i in ABCD:
        if str(i) in pasword:
            char_in_pass = True
            break
    if not char_in_pass:
        label3.config(text='must contain letter', fg='red')
        wiget_set = False
        return

    label3.config(text='', fg='green')
    wiget_set = True


def show():
    password = inputbox.get()

    symbols(password)
    if len(password) < 8:
        label2.config(text='Пароль слишком короткий!', fg='red')
    elif len(password) > 18:
        label2.config(text='Пароль слишком длинный!', fg='red')
    elif wiget_set == True:
        label2.config(text='Пароль подходит!', fg='green')


showbutton = Button(passwordbox, text='Проверить пароль', command=show)
showbutton.pack(pady=5, padx=10)

themechange = Button(text='Сменить тему', command=dark)
themechange.pack(pady=5, padx=10)
window.mainloop()
