from tkinter import *

root = Tk()
root.geometry("1350x750+0+0")
root.title("Tic Tac Toe")
root.iconbitmap('XO.ico')
root.configure(background='bisque1')

Tops = Frame(root, bg='darksalmon', pady=2, width=1350, height=100, relief=RIDGE)
Tops.grid(row=0, column=0)

title = Label(Tops, font=('Birch Std', 50, 'bold'), text="Tic Tac Toe Game", bd=21, bg='darksalmon', fg='Cornsilk',
              justify=CENTER, relief=SUNKEN)
title.grid(row=0, column=0)

MainFrame = Frame(root, bg='darksalmon', bd=20, width=1350, height=600, relief=SUNKEN)
MainFrame.grid(row=1, column=0)

LeftFrame = Frame(MainFrame, bd=10, width=750, height=500, pady=2, padx=10, bg="mistyrose1", relief=GROOVE)
LeftFrame.pack(side=RIGHT)

RightFrame = Frame(MainFrame, bd=10, width=560, height=500, pady=2, padx=10, bg="mistyrose2", relief=GROOVE)
RightFrame.pack(side=LEFT)

RightFrame1 = Frame(RightFrame, bd=10, width=560, height=200, pady=2, padx=10, bg="mistyrose1", relief=GROOVE)
RightFrame1.grid(row=0, column=0)

RightFrame2 = Frame(RightFrame, bd=10, width=560, height=200, pady=2, padx=10, bg="mistyrose1", relief=GROOVE)
RightFrame2.grid(row=1, column=0)

playerX = IntVar()
playerO = IntVar()
playerX.set(0)
playerO.set(0)

titleX = Label(RightFrame2, font=('Birch Std', 30, 'bold'), text="Player X:", padx=2, pady=2, bg="darksalmon")
titleX.grid(row=0, column=0, sticky=W)
textX = Entry(RightFrame2, font=('Birch Std', 30, 'bold'), bd=2, fg="black", textvariable=playerX, width=14,
              justify=LEFT)
textX.grid(row=0, column=1)

titleO = Label(RightFrame2, font=('Birch Std', 30, 'bold'), text="Player O:", padx=2, pady=2, bg="darksalmon")
titleO.grid(row=1, column=0, sticky=W)
textO = Entry(RightFrame2, font=('arial', 30, 'bold'), bd=2, fg="black", textvariable=playerO, width=14, justify=LEFT)
textO.grid(row=1, column=1)

newGameBtn = Button(RightFrame1, text="New Game", font='arial 26 italic bold', height=3, width=8, bg='bisque1',
                    command=lambda: new_game_function())
newGameBtn.grid(row=0, column=1, padx=6, pady=11)

resetBtn = Button(RightFrame1, text=" Reset", font='arial 26 italic bold', height=3, width=8, bg='bisque1',
                  command=lambda: reset())
resetBtn.grid(row=0, column=0, padx=6, pady=11)

btn1 = Button(LeftFrame, text=" ", font='Times 26 bold', height=3, width=8, bg='mistyrose1', image="",
              command=lambda: check_buttons(btn1))
btn1.grid(row=1, column=0, sticky=S + N + E + W)

btn2 = Button(LeftFrame, text=" ", font='Times 26 bold', height=3, width=8, bg='mistyrose1', image="",
              command=lambda: check_buttons(btn2))
btn2.grid(row=1, column=1, sticky=S + N + E + W)

btn3 = Button(LeftFrame, text=" ", font='Times 26 bold', height=3, width=8, bg='mistyrose1', image="",
              command=lambda: check_buttons(btn3))
btn3.grid(row=1, column=2, sticky=S + N + E + W)

btn4 = Button(LeftFrame, text=" ", font='Times 26 bold', height=3, width=8, bg='mistyrose1',
              command=lambda: check_buttons(btn4))
btn4.grid(row=2, column=0, sticky=S + N + E + W)

btn5 = Button(LeftFrame, text=" ", font='Times 26 bold', height=3, width=8, bg='mistyrose1',
              command=lambda: check_buttons(btn5))
btn5.grid(row=2, column=1, sticky=S + N + E + W)

btn6 = Button(LeftFrame, text=" ", font='Times 26 bold', height=3, width=8, bg='mistyrose1',
              command=lambda: check_buttons(btn6))
btn6.grid(row=2, column=2, sticky=S + N + E + W)

btn7 = Button(LeftFrame, text=" ", font='Times 26 bold', height=3, width=8, bg='mistyrose1',
              command=lambda: check_buttons(btn7))
btn7.grid(row=3, column=0, sticky=S + N + E + W)

btn8 = Button(LeftFrame, text=" ", font='Times 26 bold', height=3, width=8, bg='mistyrose1',
              command=lambda: check_buttons(btn8))
btn8.grid(row=3, column=1, sticky=S + N + E + W)

btn9 = Button(LeftFrame, text=" ", font='Times 26 bold', height=3, width=8, bg='mistyrose1',
              command=lambda: check_buttons(btn9))
btn9.grid(row=3, column=2, sticky=S + N + E + W)

btn = StringVar()
click = True


def check_buttons(btn):
    global click
    if btn["text"] == " " and click:
        btn["text"] = "X"
        click = False
        play()
    elif btn["text"] == " " and not click:
        btn["text"] = "O"
        click = True
        play()
    elif not play():
        btn4.config(background="firebrick1")
        btn4.config(text='RE')
        btn5.config(background="firebrick1")
        btn5.config(text='MI')
        btn6.config(background="firebrick1")
        btn6.config(text='ZA')
        btn1["text"] = " "
        btn2["text"] = " "
        btn3["text"] = " "
        btn1.config(background="mistyrose1")
        btn2.config(background="mistyrose1")
        btn3.config(background="mistyrose1")
        btn7["text"] = " "
        btn8["text"] = " "
        btn9["text"] = " "
        btn7.config(background="mistyrose1")
        btn8.config(background="mistyrose1")
        btn9.config(background="mistyrose1")


def check_for_win_x(x, y, z):
    if x["text"] == "X" and y["text"] == "X" and z["text"] == "X":
        n = int(playerX.get())
        score = n + 1
        playerX.set(score)
        x.config(background="darkgoldenrod1")
        x.config(text='X')
        y.config(background="darkgoldenrod1")
        y.config(text='won')
        z.config(background="darkgoldenrod1")
        z.config(text='this')
    else:
        return 0


def check_for_win_o(x, y, z):
    if x["text"] == "O" and y["text"] == "O" and z["text"] == "O":
        n = int(playerO.get())
        score = n + 1
        playerO.set(score)
        x.config(background="darkgoldenrod1")
        x.config(text='O')
        y.config(background="darkgoldenrod1")
        y.config(text='won')
        z.config(background="darkgoldenrod1")
        z.config(text='this')
    else:
        return 0


def play():
    check_for_win_x(btn1, btn2, btn3)
    check_for_win_x(btn4, btn5, btn6)
    check_for_win_x(btn7, btn8, btn9)
    check_for_win_x(btn2, btn5, btn8)
    check_for_win_x(btn1, btn4, btn7)
    check_for_win_x(btn3, btn6, btn9)
    check_for_win_x(btn1, btn5, btn9)
    check_for_win_x(btn3, btn5, btn7)

    check_for_win_o(btn1, btn2, btn3)
    check_for_win_o(btn4, btn5, btn6)
    check_for_win_o(btn7, btn8, btn9)
    check_for_win_o(btn2, btn5, btn8)
    check_for_win_o(btn1, btn4, btn7)
    check_for_win_o(btn3, btn6, btn9)
    check_for_win_o(btn1, btn5, btn9)
    check_for_win_o(btn3, btn5, btn7)


def new_game_function():
    if btn1["text"] or btn2["text"] or btn3["text"] or btn4["text"] or btn5["text"] or btn6["text"] or btn7["text"] or \
            btn8["text"] or btn9["text"]:
        btn1["text"] = " "
        btn2["text"] = " "
        btn3["text"] = " "
        btn4["text"] = " "
        btn5["text"] = " "
        btn6["text"] = " "
        btn7["text"] = " "
        btn8["text"] = " "
        btn9["text"] = " "
        btn1.config(background="mistyrose1")
        btn2.config(background="mistyrose1")
        btn3.config(background="mistyrose1")
        btn4.config(background="mistyrose1")
        btn5.config(background="mistyrose1")
        btn6.config(background="mistyrose1")
        btn7.config(background="mistyrose1")
        btn8.config(background="mistyrose1")
        btn9.config(background="mistyrose1")


def reset():
    new_game_function()
    playerX.set(0)
    playerO.set(0)


root.mainloop()
