# Vom importa aceasta biblioteca pentru interfata grafica si o vom redenumi tk pentru a scrie mai rapid
import tkinter as tk
import board as b

def InterfataMatrice(thisFrame,board):
    cells=[]
    for i in range(0, 4):
        row=[]
        for j in range(0,4):
            cell_frame = tk.Frame(thisFrame, width=150, height=125,bg="red")
            cell_frame.grid(row=i, column=j, padx=0.5, pady=0.5)
            cell_number=tk.Label(thisFrame,bg="yellow",text=str(board[i][j]))
            cell_number.grid(row=i,column=j)
m=tk.Tk()
#Voi imparti jocul in 2 frame-uri. Partea de jos unde e jocul, si partea de sus unde sunt butoanele, scorul etc
#Dam titlu jocului
m.title('2048')
#Setam marimea tablei
m.geometry("650x650")

topFrame=tk.Frame(master=m, height=100, width=650)
topFrame.pack()
#Am folosit propagate deoarece am vrut ca topFrame-ul sa aiba un size fixat si sa nu se modifice singur
topFrame.propagate(0)

bottomFrame=tk.Frame(m)
bottomFrame.pack()

button1=tk.Button(topFrame, text="Play", justify="center", fg="red", width=15, bg="yellow")
button1.pack()

board = [[1, 2, 3, 4],
         [2, 3, 4, 5],
         [3, 4, 5, 6],
         [4, 5, 6, 7]]

b.initializare(board)

InterfataMatrice(bottomFrame,board)

m.mainloop()