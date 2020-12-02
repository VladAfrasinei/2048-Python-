# Vom importa aceasta biblioteca pentru interfata grafica si o vom redenumi tk pentru a scrie mai rapid
import tkinter as tk
import board as b
import random

board = [[1, 2, 3, 4,1],
         [2, 3, 4, 5,1],
         [3, 4, 5, 6,1],
         [4, 5, 6, 7,1],
         [1,1,1,1,1]]

b.initializare(board)

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

def InterfataMatrice(thisFrame,board):
    cells=[]
    for i in range(0, 4):
        row=[]
        for j in range(0,4):
            cell_frame = tk.Frame(thisFrame, width=150, height=125,bg="red")
            cell_frame.grid(row=i, column=j, padx=0.5, pady=0.5)
            cell_number=tk.Label(thisFrame,bg="yellow",text=str(board[i][j]),font = "Helvetica 50 bold")
            cell_number.grid(row=i,column=j)

def PunereElementRandomInMatrice():
    ok=0
    for i in range(0,4):
        for j in range(0,4):
            if board[i][j]==0:
                ok=1
    if ok==1:
        linie = random.randint(0, 3)
        coloana = random.randint(0, 3)
        while (board[linie][coloana]!=0):
            linie = random.randint(0, 3)
            coloana = random.randint(0, 3)
        board[linie][coloana] = 2

def leftKey(event):
    for i in range (0,4):
        for j in range(1,4):
            if(board[i][j]!=0):
                k=j-1
                while board[i][k]==0 and k>=0:
                    k=k-1
                if k==-1:
                    board[i][0] = board[i][j]
                    board[i][j] = 0
                else:
                    if board[i][k]==board[i][j]:
                        board[i][k]=board[i][k]*2
                        board[i][j]=0
                    else:
                        if board[i][k]!=0 and j!=(k+1):
                            board[i][k+1]=board[i][j]
                            board[i][j]=0
    PunereElementRandomInMatrice()
    b.afisareMatrice(board)
    InterfataMatrice(bottomFrame,board)


def rightKey(event):
    for i in range(0, 4):
        for j in range(2, -1, -1):
            if (board[i][j] != 0):
                k = j + 1
                while board[i][k] == 0 and k <= 3:
                    k = k + 1
                if k == 4:
                    board[i][3] = board[i][j]
                    board[i][j] = 0
                else:
                    if board[i][k] == board[i][j]:
                        board[i][k] = board[i][k] * 2
                        board[i][j] = 0
                    else:
                        if board[i][k] != 0 and j != (k-1):
                            board[i][k-1] = board[i][j]
                            board[i][j] = 0
    PunereElementRandomInMatrice()
    b.afisareMatrice(board)
    InterfataMatrice(bottomFrame, board)

def upKey(event):
    for i in range(1, 4):
        for j in range(0, 4):
            if (board[i][j] != 0):
                k = i - 1
                while board[k][j] == 0 and k >= 0:
                    k = k - 1
                if k == -1:
                    board[0][j] = board[i][j]
                    board[i][j] = 0
                else:
                    if board[k][j] == board[i][j]:
                        board[k][j] = board[k][j] * 2
                        board[i][j] = 0
                    else:
                        if board[k][j] != 0 and i != (k + 1):
                            board[k + 1][j] = board[i][j]
                            board[i][j] = 0
    PunereElementRandomInMatrice()
    b.afisareMatrice(board)
    InterfataMatrice(bottomFrame, board)

def downKey(event):
    for i in range(2, -1, -1):
        for j in range(0,4):
            if (board[i][j] != 0):
                k = i + 1
                while board[k][j] == 0 and k <= 3:
                    k = k + 1
                if k == 4:
                    board[3][j] = board[i][j]
                    board[i][j] = 0
                else:
                    if board[k][j] == board[i][j]:
                        board[k][j] = board[k][j] * 2
                        board[i][j] = 0
                    else:
                        if board[k][j] != 0 and i != (k - 1):
                            board[k-1][j] = board[i][j]
                            board[i][j] = 0
    PunereElementRandomInMatrice()
    b.afisareMatrice(board)
    InterfataMatrice(bottomFrame, board)


InterfataMatrice(bottomFrame,board)
m.bind('<Left>', leftKey)
m.bind('<Right>', rightKey)
m.bind('<Up>', upKey)
m.bind('<Down>', downKey)

m.mainloop()