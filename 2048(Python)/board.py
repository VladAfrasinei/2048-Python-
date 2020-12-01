import random

def initializare(board):
    for i in range(0,4):
        for j in range(0,4):
            board[i][j]=0
    linie=random.randint(0, 3)
    coloana=random.randint(0, 3)
    board[linie][coloana]=2
    linie1=random.randint(0, 3)
    coloana1=random.randint(0, 3)
    while(linie==linie1 and coloana==coloana1):
        linie1 = random.randint(0, 3)
        coloana1 = random.randint(0, 3)
    board[linie1][coloana1]=2

def afisareMatrice(board):
    for i in range(0, 4):
        for j in range(0, 4):
            print(board[i][j], end="")
        print("")
    print("")

def returnareMatrice(board):
    return board

def returnMatrice():
    matrice = []
    for i in range(0,4):
        matrice.append([])
        for j in range(0,4):
            matrice[i].append(text_var[i][j].get())





board = [[1, 2, 3, 4],
         [2, 3, 4, 5],
         [3, 4, 5, 6],
         [4, 5, 6, 7]]
initializare(board)
afisareMatrice(board)