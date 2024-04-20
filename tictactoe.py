from tkinter import *
import time

window = Tk()
window.geometry("350x360")
window.title("Tic Tac Toe")

click_count = 0

# def combo_checker():
#     for btn in combo:
#         symbol = btn.cget("text")
#         if symbol == "":
#             continue
#         i = combo.index(btn)
        # if (combo[i-1].cget("text") == symbol) and (combo[i+1].cget("text") == symbol):
        #     if symbol == "0":
        #         label.config(text="Congraatulations!! Player 1 WON!!!")
        #     else:
        #         label.config(text="Congraatulations!! Player 2 WON!!!")

def combo_checker():
    got_winner = False
    if (combo[0].cget("text") == combo[1].cget("text")) and (combo[1].cget("text") == combo[2].cget("text")):
        symbol = combo[0].cget("text")
        got_winner = True
    elif (combo[3].cget("text") == combo[4].cget("text")) and (combo[4].cget("text") == combo[5].cget("text")):
        symbol = combo[3].cget("text")
        got_winner = True
    elif (combo[6].cget("text") == combo[7].cget("text")) and (combo[7].cget("text") == combo[8].cget("text")):
        symbol = combo[6].cget("text")
        got_winner = True
    elif (combo[0].cget("text") == combo[3].cget("text")) and (combo[3].cget("text") == combo[6].cget("text")):
        symbol = combo[0].cget("text")
        got_winner = True
    elif (combo[1].cget("text") == combo[4].cget("text")) and (combo[4].cget("text") == combo[7].cget("text")):
        symbol = combo[1].cget("text")
        got_winner = True
    elif (combo[3].cget("text") == combo[5].cget("text")) and (combo[5].cget("text") == combo[8].cget("text")):
        symbol = combo[3].cget("text")
        got_winner = True
    elif (combo[0].cget("text") == combo[4].cget("text")) and (combo[4].cget("text") == combo[8].cget("text")):
        symbol = combo[0].cget("text")
        got_winner = True
    elif (combo[2].cget("text") == combo[4].cget("text")) and (combo[4].cget("text") == combo[6].cget("text")):
        symbol = combo[2].cget("text")
        got_winner = True
    
    if got_winner:
        if symbol == "0":
            label.config(text="Congraatulations!! Player 1 WON!!! \nGame will be distroyed in 5 seconds!")
        else:
            label.config(text="Congraatulations!! Player 2 WON!!! \nGame will be distroyed in 5 seconds")
        # time.sleep(5)
        # window.destroy()
        # window.quit()
        


def play(btn):
    global click_count
    # This is to ensure that the button in only one time clickable
    if (btn.cget("text") != ""):
        return
    click_count += 1
    # this is to check the combination for winning
    if click_count >= 5:
        combo_checker()
    # this is to change the button text after click
    if click_count % 2== 0:
        btn.config(text = "X")
    else:
        btn.config(text = "0")

#Craeting Buttons and lables
label = Label(master=window, text="Keep Playing the game is going great!")
button_1 = Button(master=window, text="", font="Calibri 30 bold", command= lambda: play(button_1))
button_2 = Button(master=window, text="", font="Calibri 30 bold", command= lambda: play(button_2))
button_3 = Button(master=window, text="", font="Calibri 30 bold", command= lambda: play(button_3))
button_4 = Button(master=window, text="", font="Calibri 30 bold", command= lambda: play(button_4))
button_5 = Button(master=window, text="", font="Calibri 30 bold", command= lambda: play(button_5))
button_6 = Button(master=window, text="", font="Calibri 30 bold", command= lambda: play(button_6))
button_7 = Button(master=window, text="", font="Calibri 30 bold", command= lambda: play(button_7))
button_8 = Button(master=window, text="", font="Calibri 30 bold", command= lambda: play(button_8))
button_9 = Button(master=window, text="", font="Calibri 30 bold", command= lambda: play(button_9))

combo = [button_1, button_2, button_3, button_4, button_5, button_6, button_7, button_8, button_9]

#define a grid
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)
window.columnconfigure(2, weight=1)
window.rowconfigure(0, weight=1)
window.rowconfigure(1, weight=1)
window.rowconfigure(2, weight=1)
window.rowconfigure(3, weight=1)


#griding(row, column)
button_1.grid(row=0,column=0, sticky="nsew")
button_2.grid(row=0,column=1, sticky="nsew")
button_3.grid(row=0,column=2, sticky="nsew")
button_4.grid(row=1,column=0, sticky="nsew")
button_5.grid(row=1,column=1, sticky="nsew")
button_6.grid(row=1,column=2, sticky="nsew")
button_7.grid(row=2,column=0, sticky="nsew")
button_8.grid(row=2,column=1, sticky="nsew")
button_9.grid(row=2,column=2, sticky="nsew")
label.grid(row=3, columnspan=3)



window.mainloop()