# Vom importa aceasta biblioteca pentru interfata grafica si o vom redenumi tk pentru a scrie mai rapid
import tkinter as tk
import board as b
import random

board = [[1, 2, 3, 4,1],
         [2, 3, 4, 5,1],
         [3, 4, 5, 6,1],
         [4, 5, 6, 7,1],
         [1,1,1,1,1]]
#Vom avea nevoie de aceasta matrice ca sa vedem deja ce elemente au participat la o schimbare, ca in aceeasi tura sa nu participe la inca o schimbare
#De exeumplu daca am avea 8 16 8 8 si am dat la dreapta ar trebui sa fie 0 8 16 16, iar daca n am folosi asta ar da 0 0 8 32
boardViz = [[1, 2, 3, 4,1],
         [2, 3, 4, 5,1],
         [3, 4, 5, 6,1],
         [4, 5, 6, 7,1],
         [1,1,1,1,1]]

b.initializare(board)
finalScore=0

m=tk.Tk()
#Voi imparti jocul in 2 frame-uri. Partea de jos unde e jocul, si partea de sus unde sunt butoanele, scorul etc
#Dam titlu jocului
m.title('2048')
#Setam marimea tablei
m.geometry("700x800")

topFrame=tk.Frame(master=m, height=100, width=650)
topFrame.pack()
#Am folosit propagate deoarece am vrut ca topFrame-ul sa aiba un size fixat si sa nu se modifice singur
topFrame.propagate(0)

bottomFrame=tk.Frame(m)
bottomFrame.pack()

#button1=tk.Button(topFrame, text="Play", justify="center", fg="red", width=15, bg="yellow")
#button1.pack()

values=[0,2,4,8,16,32,64,128,256,512,1024,2048]
colors=["snow","gainsboro","papaya whip","peach puff","light salmon","dark orange","red","yellow","yellow2","yellow3","yellow4","gold"]

def returnColor(x):
    for i in range(0,12):
        if(x==values[i]):
            return colors[i]

def returnScor():
    s=0
    for i in range (0,4):
        for j in range(0,4):
            s=s+board[i][j]
    return s

def InterfataScor(thisFrame, board):
    tk.Label(thisFrame,text="Score",font = "Helvetica 30 bold").grid(row=0)
    tk.Label(thisFrame, text=str(finalScore),font = "Helvetica 30 bold").grid(row=1)

def InterfataMatrice(thisFrame,board):
    cells=[]
    for i in range(0, 4):
        row=[]
        for j in range(0,4):
            cell_frame = tk.Frame(thisFrame, width=150, height=150,bg="grey64")
            cell_frame.grid(row=i, column=j, padx=0.5, pady=0.5)
            culoare=returnColor(board[i][j])
            valoareText=str(board[i][j])
            if board[i][j]==0:
                valoareText=""
            cell_number=tk.Label(thisFrame,bg=culoare,text=valoareText,font = "Helvetica 50 bold", height=2, width=4, borderwidth=1, relief="solid")
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

def NotEndGame():
    #Daca gasim cel putin un 0 putem face clar o miscare
    for i in range(0,4):
        for j in range(0,4):
            if board[i][j]==0:
                print(1)
                return True
    #Vom verifica acum pt toate elementele cu 4 vecini, ele avand toate 4 miscari libere
    for i in range (1,3):
        for j in range(1,3):
            if board[i][j]==board[i][j+1]: #Daca se poate duce in dreapta(right key) pt a combina elementele
                print(2)
                return True
            else:
                if board[i][j]==board[i][j-1]:#Daca se poate duce in stanga(left key) pt a combina elementele
                    print(3)
                    return True
                else:
                    if board[i][j]==board[i+1][j]:#Daca se poate duce in jos(down key) pt a combina elementele
                        print(4)
                        return True
                    else:
                        if board[i][j]==board[i-1][j]:#Dace se poate duce in sus(up key) pt a combina elementele
                            print(5)
                            return True
    #Va trebui sa vedem acum si rama matricei(ei nu avand aceleasi vecini si avand un numar mai mic
    for j in range(1,4):#Vom verifica pt prima si ultima linie daca avem vreo sansa sa facem stanga(left key). Primul element clar nu trebuie luat in considerare caci el nu poate face stanga
        if board[0][j]==board[0][j-1]: #Pentru prima linie
            print(6)
            return True
        if board[3][j]==board[3][j-1]: #Pentru ultima linie
            print(7)
            return True
    for j in range(0,3):#Vom verifica pentru prima si ultima linie daca putem face dreapta(right key). Tot asa cel mai din dreapta element n are ce verificare sa aiba.
        if board[0][j]==board[0][j+1]:
            print(8)
            return True
        if board[3][j]==board[3][j+1]:
            print(9)
            return True
    for i in range(1,4):#Vom ferifica acum daca pe prima sau ultima coloana putem merge in sus(up key)
        if board[i][0]==board[i-1][0]:
            print(10)
            return True
        if board[i][3]==board[i-1][3]:
            print(11)
            return True
    for i in range(0,3):#Vom verifica daca putem merge in jos(down key) pe prima si ultima coloana
        if board[i][0]==board[i+1][0]:
            print(12)
            return True
        if board[i][3]==board[i+1][3]:
            print(13)
            return True
    #Daca am ajuns pana aici clar nu mai aveam nicio miscare disponibila asa ca vom returna Flase
    print(14)
    return False

def WinGame():
    for i in range(0,4):
        for j in range(0,4):
            if board[i][j]==2048:
                return True
    return False

def InterfataGameOver(thisFrame,board):
    if WinGame()==True:
        gameFrame = tk.Frame(thisFrame)
        gameFrame.place(relx=0.5, rely=0.5, anchor="center")
        tk.Label(gameFrame, text="You won!",bg="gold",font="Helvetica 50 bold").pack()
    else:
        gameFrame = tk.Frame(thisFrame)
        gameFrame.place(relx=0.5, rely=0.5, anchor="center")
        tk.Label(gameFrame, text="You lost!", bg="gold", font="Helvetica 50 bold").pack()

def initializareCu0(boardx):
    for i in range(0,4):
        for j in range(0,4):
            boardx[i][j]=0

def leftKey(event):
    initializareCu0(boardViz)
    global finalScore
    print(boardViz)
    ok=False
    for i in range (0,4):
        for j in range(1,4):
            if(board[i][j]!=0):
                k=j-1
                while board[i][k]==0 and k>=0:
                    k=k-1
                if k==-1:
                    board[i][0] = board[i][j]
                    board[i][j] = 0
                    ok=True
                else:
                    if board[i][k]==board[i][j] and boardViz[i][k]==0:
                        board[i][k]=board[i][k]*2
                        finalScore=finalScore+board[i][k]
                        board[i][j]=0
                        boardViz[i][k]=1
                        ok=True
                    else:
                        if board[i][k]!=0 and j!=(k+1):
                            board[i][k+1]=board[i][j]
                            board[i][j]=0
                            ok=True
    if(ok==True):
        PunereElementRandomInMatrice()
    b.afisareMatrice(board)
    InterfataMatrice(bottomFrame,board)
    InterfataScor(topFrame, board)
    if(WinGame()==True or NotEndGame()==False):
        InterfataGameOver(bottomFrame,board)


def rightKey(event):
    initializareCu0(boardViz)
    global finalScore
    ok=False
    for i in range(0, 4):
        for j in range(2, -1, -1):
            if (board[i][j] != 0):
                k = j + 1
                while board[i][k] == 0 and k <= 3:
                    k = k + 1
                if k == 4:
                    board[i][3] = board[i][j]
                    board[i][j] = 0
                    ok = True
                else:
                    if board[i][k] == board[i][j] and boardViz[i][k]==0:
                        board[i][k] = board[i][k] * 2
                        finalScore = finalScore + board[i][k]
                        board[i][j] = 0
                        boardViz[i][k]=1
                        ok = True
                    else:
                        if board[i][k] != 0 and j != (k-1):
                            board[i][k-1] = board[i][j]
                            board[i][j] = 0
                            ok = True
    if ok==True:
        PunereElementRandomInMatrice()
    b.afisareMatrice(board)
    InterfataMatrice(bottomFrame, board)
    InterfataScor(topFrame, board)
    if (WinGame() == True or NotEndGame() == False):
        InterfataGameOver(bottomFrame, board)

def upKey(event):
    initializareCu0(boardViz)
    global finalScore
    ok=False
    for i in range(1, 4):
        for j in range(0, 4):
            if (board[i][j] != 0):
                k = i - 1
                while board[k][j] == 0 and k >= 0:
                    k = k - 1
                if k == -1:
                    board[0][j] = board[i][j]
                    board[i][j] = 0
                    ok = True
                else:
                    if board[k][j] == board[i][j] and boardViz[k][j]==0:
                        board[k][j] = board[k][j] * 2
                        finalScore = finalScore + board[k][j]
                        board[i][j] = 0
                        boardViz[k][j]=1
                        ok = True
                    else:
                        if board[k][j] != 0 and i != (k + 1):
                            board[k + 1][j] = board[i][j]
                            board[i][j] = 0
                            ok = True
    if(ok==True):
        PunereElementRandomInMatrice()
    b.afisareMatrice(board)
    InterfataMatrice(bottomFrame, board)
    InterfataScor(topFrame, board)
    if (WinGame() == True or NotEndGame() == False):
        InterfataGameOver(bottomFrame, board)

def downKey(event):
    initializareCu0(boardViz)
    global finalScore
    ok=False
    for i in range(2, -1, -1):
        for j in range(0,4):
            if (board[i][j] != 0):
                k = i + 1
                while board[k][j] == 0 and k <= 3:
                    k = k + 1
                if k == 4:
                    board[3][j] = board[i][j]
                    board[i][j] = 0
                    ok = True
                else:
                    if board[k][j] == board[i][j]:
                        board[k][j] = board[k][j] * 2
                        finalScore = finalScore + board[k][j]
                        board[i][j] = 0
                        boardViz[k][j]=1
                        ok = True
                    else:
                        if board[k][j] != 0 and i != (k - 1):
                            board[k-1][j] = board[i][j]
                            board[i][j] = 0
                            ok = True
    if ok==True:
        PunereElementRandomInMatrice()
    b.afisareMatrice(board)
    InterfataMatrice(bottomFrame, board)
    InterfataScor(topFrame, board)
    if (WinGame() == True or NotEndGame() == False):
        InterfataGameOver(bottomFrame, board)


InterfataMatrice(bottomFrame,board)
InterfataScor(topFrame,board)
m.bind('<Left>', leftKey)
m.bind('<Right>', rightKey)
m.bind('<Up>', upKey)
m.bind('<Down>', downKey)

m.mainloop()
