from tkinter import *

container = Tk()
container.geometry('350x400')
container.title("Digital Tasbih")
container.configure(background= 'lavender')


count = 0
def increase():
    global count 
    count += 1
    lable_counter.config(text=str(count))

def decrease():
    global count
    count -= 1
    lable_counter.config(text= str(count))

def reset():
    global count
    count = 0
    lable_counter.config(text= str(count))

lable_counter = Label(master= container, text=str(count), font= 'Calibri 100 bold', background= 'lavender')
lable_counter.pack()

increase_button = Button(master= container, text= "Increase", command=increase, height=2, width=10, background='black', foreground='yellow', font='Arial 11 bold')
increase_button.pack(side='left', padx = 20, pady= 30)

decrease_button = Button(master= container, text='Decrease', command=decrease, height=2, width=10, background='black', foreground='yellow', font='Arial 11 bold')
decrease_button.pack(side='right', padx=20, pady= 30)

reset_button = Button(master= container, text= "Reset", command= reset, height=1, width=5, background='red', foreground='black', font='Arial 12 bold')
reset_button.pack(side='bottom', pady= 40)

container.mainloop()