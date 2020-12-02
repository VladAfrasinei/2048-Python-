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


board = [[1, 2, 3, 4,1],
         [2, 3, 4, 5,1],
         [3, 4, 5, 6,1],
         [4, 5, 6, 7,1],
         [1,1,1,1,1]]
initializare(board)
afisareMatrice(board)