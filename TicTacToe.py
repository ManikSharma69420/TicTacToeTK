from tkinter import *
from tkinter import messagebox
from time import sleep

def splash():
    splashui=Tk()
    splashui.after(1, splashui.focus_force)
    splashui.overrideredirect(True)
    splashui.geometry("700x400+300+300")
    splashui.configure(bg="green")
    Game = Label(splashui, text="TicTacToe", font=("Cascadia Code", 100), fg="black", bg="green")
    Game.pack()
    loading = Label(splashui, text="Loading... Please be patient \n", font=("Cascadia Code", 25), fg="white", bg="green")
    loading.pack()
    credits = Label(splashui, text="\n \n Made by Manik Sharma", font=("Cascadia Code", 15), fg="white", bg="green")
    credits.pack()
    splashui.after(5000, splashui.destroy)
    mainloop()


splash()

def main_game():
    print(turn)

    global gamewon
    gamewon=False

    clicked_buttons = {}

    global b1_clicked_x
    global b2_clicked_x
    global b3_clicked_x
    global b4_clicked_x
    global b5_clicked_x
    global b6_clicked_x
    global b7_clicked_x
    global b8_clicked_x
    global b9_clicked_x
    global b1_clicked_o
    global b2_clicked_o
    global b3_clicked_o
    global b4_clicked_o
    global b5_clicked_o
    global b6_clicked_o
    global b7_clicked_o
    global b8_clicked_o
    global b9_clicked_o
    b1_clicked_x=False
    b2_clicked_x=False
    b3_clicked_x=False
    b4_clicked_x=False
    b5_clicked_x=False
    b6_clicked_x=False
    b7_clicked_x=False
    b8_clicked_x=False
    b9_clicked_x=False
    b1_clicked_o=False
    b2_clicked_o=False
    b3_clicked_o=False
    b4_clicked_o=False
    b5_clicked_o=False
    b6_clicked_o=False
    b7_clicked_o=False
    b8_clicked_o=False
    b9_clicked_o=False

    gui = Tk()
    gui.title("TicTacToe")
    gui.after(1, gui.focus_force)

    def win_conditions():
        global b1_clicked_x
        global b2_clicked_x
        global b3_clicked_x
        global b4_clicked_x
        global b5_clicked_x
        global b6_clicked_x
        global b7_clicked_x
        global b8_clicked_x
        global b9_clicked_x
        global b1_clicked_o
        global b2_clicked_o
        global b3_clicked_o
        global b4_clicked_o
        global b5_clicked_o
        global b6_clicked_o
        global b7_clicked_o
        global b8_clicked_o
        global b9_clicked_o
        global gamewon

        if b1_clicked_x==True and b4_clicked_x==True and b7_clicked_x==True:
            sleep(0.3)
            gui.destroy()
            messagebox.showinfo(title="TicTacToe - X WON", message="X WON")
            gamewon=True
        if b2_clicked_x==True and b5_clicked_x==True and b8_clicked_x==True:
            sleep(0.3)
            gui.destroy()
            messagebox.showinfo(title="TicTacToe - X WON", message="X WON")
            gamewon=True
        if b3_clicked_x==True and b6_clicked_x==True and b9_clicked_x==True:
            sleep(0.3)
            gui.destroy()
            messagebox.showinfo(title="TicTacToe - X WON", message="X WON")
            gamewon=True
        if b1_clicked_x==True and b2_clicked_x==True and b3_clicked_x==True:
            sleep(0.3)
            gui.destroy()
            messagebox.showinfo(title="TicTacToe - X WON", message="X WON")
            gamewon=True
        if b4_clicked_x==True and b5_clicked_x==True and b6_clicked_x==True:
            sleep(0.3)
            gui.destroy()
            messagebox.showinfo(title="TicTacToe - X WON", message="X WON")
            gamewon=True
        if b7_clicked_x==True and b8_clicked_x==True and b9_clicked_x==True:
            sleep(0.3)
            gui.destroy()
            messagebox.showinfo(title="TicTacToe - X WON", message="X WON")
            gamewon=True
        if b1_clicked_x==True and b5_clicked_x==True and b9_clicked_x==True:
            sleep(0.3)
            gui.destroy()
            messagebox.showinfo(title="TicTacToe - X WON", message="X WON")
            gamewon=True
        if b3_clicked_x==True and b5_clicked_x==True and b7_clicked_x==True:
            sleep(0.3)
            gui.destroy()
            messagebox.showinfo(title="TicTacToe - X WON", message="X WON")

        if b1_clicked_o==True and b4_clicked_o==True and b7_clicked_o==True:
            sleep(0.3)
            gui.destroy()
            messagebox.showinfo(title="TicTacToe - O WON", message="O WON")
            gamewon=True
        if b2_clicked_o==True and b5_clicked_o==True and b8_clicked_o==True:
            sleep(0.3)
            gui.destroy()
            messagebox.showinfo(title="TicTacToe - O WON", message="O WON")
            gamewon=True
        if b3_clicked_o==True and b6_clicked_o==True and b9_clicked_o==True:
            sleep(0.3)
            gui.destroy()
            messagebox.showinfo(title="TicTacToe - O WON", message="O WON")
            gamewon=True
        if b1_clicked_o==True and b2_clicked_o==True and b3_clicked_o==True:
            sleep(0.3)
            gui.destroy()
            messagebox.showinfo(title="TicTacToe - O WON", message="O WON")
            gamewon=True
        if b4_clicked_o==True and b5_clicked_o==True and b6_clicked_o==True:
            sleep(0.3)
            gui.destroy()
            messagebox.showinfo(title="TicTacToe - O WON", message="O WON")
            gamewon=True
        if b7_clicked_o==True and b8_clicked_o==True and b9_clicked_o==True:
            sleep(0.3)
            gui.destroy()
            messagebox.showinfo(title="TicTacToe - O WON", message="O WON")
            gamewon=True
        if b1_clicked_o==True and b5_clicked_o==True and b9_clicked_o==True:
            sleep(0.3)
            gui.destroy()
            messagebox.showinfo(title="TicTacToe - O WON", message="O WON")
            gamewon=True
        if b3_clicked_o==True and b5_clicked_o==True and b7_clicked_o==True:
            sleep(0.3)
            gui.destroy()
            messagebox.showinfo(title="TicTacToe - O WON", message="O WON")
            gamewon=True

        checkiftie = len(clicked_buttons)

        if checkiftie==9 and gamewon==False:
            sleep(0.3)
            gui.destroy()
            messagebox.showinfo(title="TicTacToe - Tied!", message="TIED")
            startgame()

        if gamewon == True:
            startgame()
            
    def cross_or_zero_b1():
        global turn
        global b1_clicked_x
        global b1_clicked_o
        print(turn)
        if turn == 0 and clicked_buttons.get("b1", False) == False:  # Check if b1 is not clicked
            print(turn)
            B1["text"] = '    O    '
            turn = 1
            clicked_buttons["b1"] = True  # Update clicked state
            print(turn)
            b1_clicked_o=True
        elif turn == 1 and clicked_buttons.get("b1", False) == False:
            print(turn)
            B1["text"] = '    X    '
            turn = 0
            clicked_buttons["b1"] = True
            print(turn)
            b1_clicked_x=True
    def cross_or_zero_b2():
        global turn
        global b2_clicked_x
        global b2_clicked_o
        print(turn)
        if turn == 0 and clicked_buttons.get("b2", False) == False:  # Check if b2 is not clicked
            print(turn)
            B2["text"] = '    O    '
            turn = 1
            clicked_buttons["b2"] = True  # Update clicked state
            print(turn)
            b2_clicked_o=True
        elif turn == 1 and clicked_buttons.get("b2", False) == False:
            print(turn)
            B2["text"] = '    X    '
            turn = 0
            clicked_buttons["b2"] = True
            print(turn)
            b2_clicked_x=True
    def cross_or_zero_b3():
        global turn
        global b3_clicked_x
        global b3_clicked_o
        print(turn)
        if turn == 0 and clicked_buttons.get("b3", False) == False:  # Check if b3 is not clicked
            print(turn)
            B3["text"] = '    O    '
            turn = 1
            clicked_buttons["b3"] = True  # Update clicked state
            print(turn)
            b3_clicked_o=True
        elif turn == 1 and clicked_buttons.get("b3", False) == False:
            print(turn)
            B3["text"] = '    X    '
            turn = 0
            clicked_buttons["b3"] = True
            print(turn)
            b3_clicked_x=True
    def cross_or_zero_b4():
        global turn
        global b4_clicked_x
        global b4_clicked_o
        print(turn)
        if turn == 0 and clicked_buttons.get("b4", False) == False:  # Check if b4 is not clicked
            print(turn)
            B4["text"] = '    O    '
            turn = 1
            clicked_buttons["b4"] = True  # Update clicked state
            print(turn)
            b4_clicked_o=True
        elif turn == 1 and clicked_buttons.get("b4", False) == False:
            print(turn)
            B4["text"] = '    X    '
            turn = 0
            clicked_buttons["b4"] = True
            print(turn)
            b4_clicked_x=True
    def cross_or_zero_b5():
        global turn
        global b5_clicked_x
        global b5_clicked_o
        print(turn)
        if turn == 0 and clicked_buttons.get("b5", False) == False:  # Check if b5 is not clicked
            print(turn)
            B5["text"] = '    O    '
            turn = 1
            clicked_buttons["b5"] = True  # Update clicked state
            print(turn)
            b5_clicked_o=True
        elif turn == 1 and clicked_buttons.get("b5", False) == False:
            print(turn)
            B5["text"] = '    X    '
            turn = 0
            clicked_buttons["b5"] = True
            print(turn)
            b5_clicked_x=True
    def cross_or_zero_b6():
        global turn
        global b6_clicked_x
        global b6_clicked_o
        print(turn)
        if turn == 0 and clicked_buttons.get("b6", False) == False:  # Check if b6 is not clicked
            print(turn)
            B6["text"] = '    O    '
            turn = 1
            clicked_buttons["b6"] = True  # Update clicked state
            print(turn)
            b6_clicked_o=True
        elif turn == 1 and clicked_buttons.get("b6", False) == False:
            print(turn)
            B6["text"] = '    X    '
            turn = 0
            clicked_buttons["b6"] = True
            print(turn)
            b6_clicked_x=True
    def cross_or_zero_b7():
        global turn
        global b7_clicked_x
        global b7_clicked_o
        print(turn)
        if turn == 0 and clicked_buttons.get("b7", False) == False:  # Check if b7 is not clicked
            print(turn)
            B7["text"] = '    O    '
            turn = 1
            clicked_buttons["b7"] = True  # Update clicked state
            print(turn)
            b7_clicked_o=True
        elif turn == 1 and clicked_buttons.get("b7", False) == False:
            print(turn)
            B7["text"] = '    X    '
            turn = 0
            clicked_buttons["b7"] = True
            print(turn)
            b7_clicked_x=True
    def cross_or_zero_b8():
        global turn
        global b8_clicked_x
        global b8_clicked_o
        print(turn)
        if turn == 0 and clicked_buttons.get("b8", False) == False:  # Check if b8 is not clicked
            print(turn)
            B8["text"] = '    O    '
            turn = 1
            clicked_buttons["b8"] = True  # Update clicked state
            print(turn)
            b8_clicked_o=True
        elif turn == 1 and clicked_buttons.get("b8", False) == False:
            print(turn)
            B8["text"] = '    X    '
            turn = 0
            clicked_buttons["b8"] = True
            print(turn)
            b8_clicked_x=True
    def cross_or_zero_b9():
        global turn
        global b9_clicked_x
        global b9_clicked_o
        print(turn)
        if turn == 0 and clicked_buttons.get("b9", False) == False:  # Check if b9 is not clicked
            print(turn)
            B9["text"] = '    O    '
            turn = 1
            clicked_buttons["b9"] = True  # Update clicked state
            print(turn)
            b9_clicked_o=True
        elif turn == 1 and clicked_buttons.get("b9", False) == False:
            print(turn)
            B9["text"] = '    X    '
            turn = 0
            clicked_buttons["b9"] = True
            print(turn)
            b9_clicked_x=True

    gui.resizable(False,False)

    Label2 = Label(gui, text="", font=("Cascadia Code", 10))
    Label2.grid(row=3,column=1)

    def turnlabel():
        if turn==0:
            Label2.config(text="O's Turn")
        if turn==1:
            Label2.config(text="X's Turn")

    turnlabel()

    B1 = Button(gui, bg="lightblue", text='         ',command=lambda: [cross_or_zero_b1(),win_conditions(), turnlabel()], width=6,height=2)
    B1.grid(row=0,column=0)
    B2 = Button(gui, bg="lightblue", text='         ',command=lambda: [cross_or_zero_b2(),win_conditions(), turnlabel()], width=6,height=2)
    B2.grid(row=0,column=1)
    B3 = Button(gui, bg="lightblue", text='         ',command=lambda: [cross_or_zero_b3(),win_conditions(), turnlabel()], width=6,height=2)
    B3.grid(row=0,column=2)
    B4 = Button(gui, bg="lightblue", text='         ',command=lambda: [cross_or_zero_b4(),win_conditions(), turnlabel()], width=6,height=2)
    B4.grid(row=1,column=0)
    B5 = Button(gui, bg="lightblue", text='         ',command=lambda: [cross_or_zero_b5(),win_conditions(), turnlabel()], width=6,height=2)
    B5.grid(row=1,column=1)
    B6 = Button(gui, bg="lightblue", text='         ',command=lambda: [cross_or_zero_b6(),win_conditions(), turnlabel()], width=6,height=2)
    B6.grid(row=1,column=2)
    B7 = Button(gui, bg="lightblue", text='         ',command=lambda: [cross_or_zero_b7(),win_conditions(), turnlabel()], width=6,height=2)
    B7.grid(row=2,column=0)
    B8 = Button(gui, bg="lightblue", text='         ',command=lambda: [cross_or_zero_b8(),win_conditions(), turnlabel()], width=6,height=2)
    B8.grid(row=2,column=1)
    B9 = Button(gui, bg="lightblue", text='         ',command=lambda: [cross_or_zero_b9(),win_conditions(), turnlabel()], width=6,height=2)
    B9.grid(row=2,column=2)
    gui.mainloop()

global turn
dropdownoption=""

def turn_number():
    global turn
    global dropdownoption
    turn = int(dropdownoption)
    print(dropdownoption)
    print("x")
    print(turn)
    print("x")

def startgame():
    startui = Tk()
    startui.after(1, startui.focus_force)
    startui.resizable(False,False)
    startui.title("TicTacToe")
    Label1 = Label(startui, text="Choose who moves first - 0 is O and 1 is X", font=("Cascadia Code", 10))
    Label1.pack()
    def dropdown():
        global dropdownoption
        dropdownoption = clicked.get()
    options = [ 
    "0",
    "1"
    ] 
    clicked = StringVar() 
    clicked.set("0") 
    drop = OptionMenu(startui , clicked , *options) 
    drop.pack()
    button = Button(startui , text = "Select" , font=("Cascadia Code", 10), command = lambda: [dropdown(), turn_number(), startui.destroy(), main_game()])
    button.pack()
    startui.mainloop()

startgame()