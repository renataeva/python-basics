from tkinter import *

# nastojki okna
window = Tk()
window.geometry('400x300')
window.title('First')
window.maxsize(1000, 800)
window.minsize(300, 200)

# osnovnoj kod
esc = Button(text='Close program', width=20, command=quit)
esc.pack(expand=True)

# konec programmi
window.mainloop()
