from tkinter import *
from datetime import datetime as dt

window = Tk()
window.geometry("300x300")
window.title("Clock")
window.config(background="lavender")


def update_time():
    new_time=f"Time: {dt.now().hour}:{dt.now().minute}:{dt.now().second} \nDate:{dt.now().day}/{dt.now().month}/{dt.now().year}"
    lable.config(text=new_time)


lable = Label(
    master=window, 
    text=f"Time: {dt.now().hour}:{dt.now().minute}:{dt.now().second} \nDate:{dt.now().day}/{dt.now().month}/{dt.now().year}", 
    font="Calibri 30 bold", 
    foreground="brown", 
    background="lavender"
    )
lable.pack(pady=30, side="top")


button = Button(
    master=window, 
    text="Update", 
    background="black", 
    foreground="white", 
    font="Arial",
    command=update_time
)
button.pack()

window.mainloop()