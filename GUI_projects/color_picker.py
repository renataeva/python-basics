from tkinter import *

window = Tk()
window.geometry('550x300')
window.resizable(False, False)
window.title('Color picker')
window.iconbitmap('color.ico')


def color_generate(value):
    red = red_scale.get()
    green = green_scale.get()
    blue = blue_scale.get()
    color = f'#{red:02x}{green:02x}{blue:02x}'
    color2 = f'#{255-red:02x}{255-green:02x}{255-blue:02x}'
    label_color.config(text=color)
    label_color.config(fg=color2)
    label_color.config(bg=color)


frame_RGB = LabelFrame(text='Выберте цвета', height=250, width=250)
frame_RGB.place(x=14.5, y=20)

frame_color = LabelFrame(text='Полученый цвет', height=250, width=250)
frame_color.place(x=279, y=20)

red_scale = Scale(frame_RGB, from_=0, to=255, orient=HORIZONTAL, label='Red',
                  width=20, length=200, activebackground='red', fg='red',
                  command=color_generate)
red_scale.place(x=10, y=10)

blue_scale = Scale(frame_RGB, from_=0, to=255, orient=HORIZONTAL, label='Blue',
                   width=20, length=200, activebackground='blue', fg='blue',
                   command=color_generate)
blue_scale.place(x=10, y=74)

green_scale = Scale(frame_RGB, from_=0, to=255, orient=HORIZONTAL,
        label='Green',
        width=20, length=200, activebackground='green',
        fg='green',
        command=color_generate)
green_scale.place(x=10, y=148)

label_color = Label(frame_color, justify=CENTER,
                    font=('Arial', 15, 'bold'), height=8,
                    width=17, bg='black')
label_color.place(x=15, y=10)

window.mainloop()
