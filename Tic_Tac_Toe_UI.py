from tkinter import *
from tkinter import messagebox
from winsound import PlaySound
from tic import *


buttonarray=None
win_or_draw=None
count=1
def destruct():
    global t,winnerWindow
    t.destroy()
    winnerWindow.destroy()
def Quit():
    global t 
    msg=messagebox.askquestion("Confirm","Are you want to Quit? You still have chances!")
    if msg=='yes':
        t.destroy()
def displayWinner(winner):
    global t,winnerWindow,ID    
    winnerWindow=Tk()
    winnerWindow.title("Winner Window")
    winnerWindow.configure(bg="Black")
    l1=Label(winnerWindow,text="THE WINNER IS: ",font=("COMIC SANS MS",15),bg="Black",fg="White")
    l1.pack()
    l2=Label(winnerWindow,text=winner,font=("COMIC SANS S",15),bg="Black",fg="White")
    l2.pack()
    bproceed=Button(winnerWindow,text="Proceed",font=("COMIC SANS  MS",10,"bold"),command=destruct)
    bproceed.pack()
def TicTacToeGUI():
    global t,buttonarray
    t=Tk()
    t.title("TIC TAC TOE")
    t.configure(bg="white")  
    #Making the background of the window as white#Displaying the player
    l1=Label(t,text="PLAYER: 1(X)",height=3,font=("COMIC SANS MS",10,"bold"),bg="white")
    l1.grid(row=0,column=0)#Quit button
    exitButton=Button(t,text="Quit",command=Quit,font=("COMIC SANS MS",10,"bold"))
    exitButton.grid(row=0,column=2)#Grid buttons
    b1=Button(t,text="",height=4,width=8,bg="black",activebackground="white",fg="white",font="Times 15 bold",command=lambda: changeVal(b1,0,user))
    b2=Button(t,text="",height=4,width=8,bg="black",activebackground="white",fg="white",font="Times 15 bold",command=lambda: changeVal(b2,1,user))
    b3=Button(t,text="",height=4,width=8,bg="black",activebackground="white",fg="white",font="Times 15 bold",command=lambda: changeVal(b3,2,user))
    b4=Button(t,text="",height=4,width=8,bg="black",activebackground="white",fg="white",font="Times 15 bold",command=lambda: changeVal(b4,3,user))
    b5=Button(t,text="",height=4,width=8,bg="black",activebackground="white",fg="white",font="Times 15 bold",command=lambda: changeVal(b5,4,user))
    b6=Button(t,text="",height=4,width=8,bg="black",activebackground="white",fg="white",font="Times 15 bold",command=lambda: changeVal(b6,5,user))
    b7=Button(t,text="",height=4,width=8,bg="black",activebackground="white",fg="white",font="Times 15 bold",command=lambda: changeVal(b7,6,user))
    b8=Button(t,text="",height=4,width=8,bg="black",activebackground="white",fg="white",font="Times 15 bold",command=lambda: changeVal(b8,7,user))
    b9=Button(t,text="",height=4,width=8,bg="black",activebackground="white",fg="white",font="Times 15 bold",command=lambda: changeVal(b9,8,user))
    buttonarray=[b1,b2,b3,b4,b5,b6,b7,b8,b9]
    b1.grid(row=2,column=0)
    b2.grid(row=2,column=1)
    b3.grid(row=2,column=2)
    b4.grid(row=3,column=0)
    b5.grid(row=3,column=1)
    b6.grid(row=3,column=2)
    b7.grid(row=4,column=0)
    b8.grid(row=4,column=1)
    b9.grid(row=4,column=2)
    if is_AI_first:
        best_move_positon=get_best_move(player_bord)
        print(best_move_positon)
        changeVal( buttonarray[best_move_positon],best_move_positon,"x")
    t.mainloop()
def changeVal(button,position,player):
    global count,win_or_draw#Checking if button is available
    if button["text"]=="" and win_or_draw==None: 
        button["text"]=player
        player_bord[position]=player
        win_or_draw=get_winner(player_bord)
        if win_or_draw!=None:
            print(win_or_draw,player_bord)
            displayWinner(win_or_draw)
        if player==user:
            best_move_positon=get_best_move(player_bord)
            print(best_move_positon)
            changeVal( buttonarray[best_move_positon],best_move_positon,AI)

    else:
        if win_or_draw==None:
            messagebox.showerror("Error","This box already has a value!")
is_AI_first=False
TicTacToeGUI() 
