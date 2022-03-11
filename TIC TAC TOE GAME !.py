"""
Code by  Abdelrhman Reda Mohamed a Student in FCAI-CU !
Descripe : 
The game Has a  2 players, each player should pick 2 numbers from a list [1,20]
the 2 number convert into a string character if these characters are , same then the player take a point, and we make a screen clear 
if these characters are not  the same then we make screen clear then the other player play

"""
from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
import tkinter.messagebox
arr = []
screen = Tk()
screen.title("Tic Tac Toe BY ABDELRHMAN ")

clicked = True
count = 0

# PLAYER 1 ,2 OPTIONS
def b_click(b):
    global clicked , count
    #check button !
    if b["text"] == "" and clicked == True:
        #ask for integer between 0,9
        player1_number = simpledialog.askinteger("Tic Tac Toe [PLAYER 1]","Please enter a ODD number between [0,9]",minvalue=0,maxvalue=9)
        #make sure that the integer is odd and not repeated !
        if (player1_number % 2 != 0) and player1_number not in arr:
                arr.append(player1_number)
                b["text"] = player1_number
                clicked = False
                count += 1
                checkifwin()
                L1 = Label(screen, text="PLAYER 2 TURN [Even]" , font=("COMIC SANS MS",7,"bold")).grid(row=0,column=0)
        else :
            messagebox.showerror("Tic Tac Toe[P1] ","ERROR !!, Player 1 can choose only ODD numbers\n be sure that you don't repeat the number ")
            b_click(b)
    elif b["text"]== "" and clicked == False:      
        player2_number = simpledialog.askinteger("Tic Tac Toe [PLAYER 2]","Please enter a EVEN number between [0,9]",minvalue=0,maxvalue=9)
        #make sure that the integer is even and not repeated !
        if (player2_number % 2 == 0)and player2_number not in arr:
            arr.append(player2_number)
            b["text"] = player2_number
            clicked = True
            count += 1
            checkifwin()
            l1 = Label(screen, text="PLAYER 1 TURN [ODD]" , font=("COMIC SANS MS",7,"bold")).grid(row=0,column=0)
        else :
            messagebox.showerror("Tic Tac Toe[P2] ","ERROR !!, Player 2 can choose only EVEN numbers\n be sure that you don't repeat the number ")
  
# Button build :
b1 = Button(screen, text ="" , font=("Helvetica",20),height =3 , width=6, bg="SystemButtonFace",command=lambda: b_click(b1) )
b2 = Button(screen, text= "" , font=("Helvetica",20),height =3 , width=6, bg="SystemButtonFace",command=lambda: b_click(b2) )
b3 = Button(screen, text= "" , font=("Helvetica",20),height =3 , width=6, bg="SystemButtonFace",command=lambda: b_click(b3) )

b4 = Button(screen, text= "" , font=("Helvetica",20),height =3 , width=6, bg="SystemButtonFace",command=lambda: b_click(b4) )
b5 = Button(screen, text= "" , font=("Helvetica",20),height =3 , width=6, bg="SystemButtonFace",command=lambda: b_click(b5) )
b6 = Button(screen, text= "" , font=("Helvetica",20),height =3 , width=6, bg="SystemButtonFace",command=lambda: b_click(b6) )

b7 = Button(screen, text= "" , font=("Helvetica",20),height =3 , width=6, bg="SystemButtonFace",command=lambda: b_click(b7) )
b8 = Button(screen, text= "" , font=("Helvetica",20),height =3 , width=6, bg="SystemButtonFace",command=lambda: b_click(b8) )
b9 = Button(screen, text= "" , font=("Helvetica",20),height =3 , width=6, bg="SystemButtonFace",command=lambda: b_click(b9) )
L1=Label(screen, text="PLAYER 1 TURN [ODD]" , font=("COMIC SANS MS",7,"bold"))
L1.grid(row=0, column=0)

#Put the button on the screen :

b1.grid(row=1, column=0)
b2.grid(row=1, column=1)
b3.grid(row=1, column=2)

b4.grid(row=2, column=0)
b5.grid(row=2, column=1)
b6.grid(row=2, column=2)

b7.grid(row=3, column=0)
b8.grid(row=3, column=1)
b9.grid(row=3, column=2)

#OFF THE BUTTON IF SOME ONE WIN !
def disabled_all_buttons():
    b1.configure(state=DISABLED)
    b2.configure(state=DISABLED)
    b3.configure(state=DISABLED)
    b4.configure(state=DISABLED)
    b5.configure(state=DISABLED)
    b6.configure(state=DISABLED)
    b7.configure(state=DISABLED)
    b8.configure(state=DISABLED)
    b9.configure(state=DISABLED)
#WIN Condition
def checkifwin():
    global count,winner
    winner = False
    #here we check the turn !
    if count % 2 != 0:
        #check if the button has a integer text
        if  isinstance(b1["text"], int) and isinstance(b7["text"], int)  and isinstance(b4["text"], int):
            #check if the sum of the buttons is equal to 15
            if b1["text"] + b4["text"] + b7["text"] == 15:
                b1.config(bg = "red"),b4.config(bg = "red"),b7.config(bg = "red")
                winner = True
                messagebox.showinfo("Tic Tac Toe ","Player 1 Win")
                disabled_all_buttons()
            
        if isinstance(b1["text"], int) and isinstance(b2["text"], int)  and isinstance(b3["text"], int):
            if b1["text"] + b2["text"] + b3["text"] == 15:
                b1.config(bg = "red"),b2.config(bg = "red"),b3.config(bg = "red")
                winner = True
                messagebox.showinfo("Tic Tac Toe ","Player 1 Win")
                disabled_all_buttons()
            
        if isinstance(b4["text"], int) and isinstance(b5["text"], int)  and isinstance(b7["text"], int):
            if b4["text"] + b5["text"] + b6["text"]==15:
                b4.config(bg = "red"),b5.config(bg = "red"),b6.config(bg = "red")
                winner = True
                messagebox.showinfo("Tic Tac Toe ","Player 1 Win")
                disabled_all_buttons()

        if isinstance(b7["text"], int) and isinstance(b8["text"], int)  and isinstance(b9["text"], int):
            if b7["text"] + b8["text"] + b9["text"]==15:
                b7.config(bg = "red"),b8.config(bg = "red"),b9.config(bg = "red")
                winner = True
                messagebox.showinfo("Tic Tac Toe ","Player 1 Win")
                disabled_all_buttons()

        if isinstance(b2["text"], int) and isinstance(b5["text"], int)  and isinstance(b8["text"], int):
            if b2["text"] + b5["text"] + b8["text"]==15:
                b2.config(bg = "red"),b5.config(bg = "red"),b8.config(bg = "red")
                winner = True
                messagebox.showinfo("Tic Tac Toe ","Player 1 Win")
                disabled_all_buttons()
        
        if isinstance(b3["text"], int) and isinstance(b6["text"], int)  and isinstance(b9["text"], int):
            if b3["text"] + b6["text"] + b9["text"]==15:
                b7.config(bg = "red"),b8.config(bg = "red"),b9.config(bg = "red")
                winner = True
                messagebox.showinfo("Tic Tac Toe ","Player 1 Win")
                disabled_all_buttons()

        if isinstance(b1["text"], int) and isinstance(b5["text"], int)  and isinstance(b9["text"], int):
            if b1["text"] + b5["text"] + b9["text"]==15:
                b1.config(bg = "red"),b5.config(bg = "red"),b9.config(bg = "red")
                winner = True
                messagebox.showinfo("Tic Tac Toe ","Player 1 Win")
                disabled_all_buttons()

        if isinstance(b3["text"], int) and isinstance(b5["text"], int)  and isinstance(b7["text"], int):
            if b3["text"] + b5["text"] + b7["text"]==15:
                b1.config(bg = "red"),b5.config(bg = "red"),b7.config(bg = "red")
                winner = True
                messagebox.showinfo("Tic Tac Toe ","Player 1 Win")
                disabled_all_buttons()

    else:
        
        if isinstance(b1["text"], int) and isinstance(b7["text"], int)  and isinstance(b4["text"], int):
            if b1["text"] + b4["text"] + b7["text"]==15:
                b1.config(bg = "red"),b4.config(bg = "red"),b7.config(bg = "red")
                winner = True
                messagebox.showinfo("Tic Tac Toe ","Player 2 Win")
                disabled_all_buttons()
            
        if isinstance(b1["text"], int) and isinstance(b2["text"], int)  and isinstance(b3["text"], int):
            if b1["text"] + b2["text"] + b3["text"]==15:
                b1.config(bg = "red"),b2.config(bg = "red"),b3.config(bg = "red")
                winner = True
                messagebox.showinfo("Tic Tac Toe ","Player 2 Win")
                disabled_all_buttons()
            
        if isinstance(b4["text"], int) and isinstance(b5["text"], int)  and isinstance(b6["text"], int):
            if b4["text"] + b5["text"] + b6["text"]==15:
                b4.config(bg = "red"),b5.config(bg = "red"),b6.config(bg = "red")
                winner = True
                messagebox.showinfo("Tic Tac Toe ","Player 2 Win")
                disabled_all_buttons()

        if isinstance(b7["text"], int) and isinstance(b8["text"], int)  and isinstance(b9["text"], int):
            if b7["text"] + b8["text"] + b9["text"]==15:
                b7.config(bg = "red"),b8.config(bg = "red"),b9.config(bg = "red")
                winner = True
                messagebox.showinfo("Tic Tac Toe ","Player 2 Win")
                disabled_all_buttons()

        if isinstance(b2["text"], int) and isinstance(b5["text"], int)  and isinstance(b8["text"], int):
            if b2["text"] + b5["text"] + b8["text"]==15:
                b2.config(bg = "red"),b5.config(bg = "red"),b8.config(bg = "red")
                winner = True
                messagebox.showinfo("Tic Tac Toe ","Player 2 Win")
                disabled_all_buttons()
        
        if isinstance(b3["text"], int) and isinstance(b6["text"], int)  and isinstance(b9["text"], int):
            if b3["text"] + b6["text"] + b9["text"]==15:
                b7.config(bg = "red"),b8.config(bg = "red"),b9.config(bg = "red")
                winner = True
                messagebox.showinfo("Tic Tac Toe ","Player 2 Win")
                disabled_all_buttons()

        if isinstance(b1["text"], int) and isinstance(b5["text"], int)  and isinstance(b9["text"], int):
            if b1["text"] + b5["text"] + b9["text"]==15:
                b1.config(bg = "red"),b5.config(bg = "red"),b9.config(bg = "red")
                winner = True
                messagebox.showinfo("Tic Tac Toe ","Player 2 Win")
                disabled_all_buttons()

        if isinstance(b3["text"], int) and isinstance(b5["text"], int)  and isinstance(b7["text"], int):
            if b3["text"] + b5["text"] + b7["text"]==15:
                b1.config(bg = "red"),b5.config(bg = "red"),b7.config(bg = "red")
                winner = True
                messagebox.showinfo("Tic Tac Toe ","Player 2 Win")
                disabled_all_buttons()
    if count == 9 and winner == False:
        messagebox.showinfo("Tic Tac Toe ","DRAW !!!")
        disabled_all_buttons()

screen.mainloop()
