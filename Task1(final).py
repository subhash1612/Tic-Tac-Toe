import random
import os


board = [' ' for x in range(10)]
inp = 'Y'

class Person:

    def __init__(self,name,ctype):
        self.name = name
        self.ctype = ctype  #To keep a track of the character(X/O)
        self.score = 0  #To keep track of the wins of the player
    
    def playerMove(self):
        
        check = True
        while check:
            pos = int(input("Enter the pos: "))
            try:
                if(pos>0 and pos<10):

                    if(isFree(pos)):   #Only if the entered position is free the player is allowed to place his character
                        check = False
                        insertAtPos(pos,self.ctype)
                       
                    else:
                        print("Position already occupied")
                else:
                      print("Enter a pos in the given range!")
            except:
                print("Enter an integer!")

class Computer:

    def __init__(self,ctype="X"):
        self.ctype = ctype
        self.name = "Computer"
        self.score = 0
    
    def compMove(self):
        move = 0
        possiblemoves = [i for i,let in enumerate(board) if(let==' ') and i!=0] #To get the list of all the possible moves with indices
        for let in['X','O']:
            for x in possiblemoves:
                copy = board[:] #creating a copy of the board and checking possible move to win
                copy[x] = let
                res = checkWinner(copy,let)
                if (res==1):
                    move = x
                    return move
        
        odd = []    #getting the corner points (1,3,7,9)
        for i in possiblemoves:
            if i in [1,3,7,9]:
                odd.append(i)
        
        if(len(odd)>0):
            move  = selectRand(odd) #To select a random position from the corner points for the computer
            return move
        
        even = [] #getting the edges
        for i in possiblemoves:
            if i in [2,4,6,8]: #To select a random position from the edge points(2,4,6,8) for the computer
                even.append(i)
        
        if(len(even)>0):
            move = selectRand(even)
            return move

        if(5 in possiblemoves): #checking if the center postition is free(i.e 5)
            move = 5
            return move
        return move


def selectRand(lst):
    i =  random.randint(0,len(lst)-1)
    return lst[i]           


def checkfull(board): #Function to check if board is full
    if(board.count(' ') >1):
        return False
    else:
        return True

def isFree(pos):
    return board[pos] == ' '

def insertAtPos(pos,let): #Insert respective character at desired position
    board[pos] = let


def checkWinner(board,p): #Function to decide the winner

    if((board[1]==p and board[2]==p) and (board[3]==p)):
        return 1
    elif((board[4]==p and board[5]==p) and (board[6]==p)):
        return 1
    elif((board[7]==p and board[8]==p) and (board[9]==p)):
        return 1
    elif((board[1]==p and board[4]==p) and (board[7]==p)):
        return 1
    elif((board[2]==p and board[5]==p) and (board[8]==p)):
        return 1
    elif((board[3]==p and board[6]==p) and (board[9]==p)):
        return 1
    elif((board[1]==p and board[5]==p) and (board[9]==p)):
        return 1
    elif((board[3]==p and board[5]==p) and (board[7]==p)):
        return 1
    else:
        return 0

def printBoard(board): # Function to print the tic tac toe board

    print(board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('- + - + -')
    print(board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('- + - + -')
    print(board[7] + ' | ' + board[8] + ' | ' + board[9])

def deideCompChar(ptype): #Function to decide the character type of the player based on the users choice
    if(ptype=='X'):
        ctype = 'O'
    else:
        ctype = 'X'
    return ctype
    


os.system("cls")
print("Welcome to the tic tac toe game")
name = input('Enter your name: ')
ptype = input("Enter your character type(X/O): ")[0]
player = Person(name,ptype)
comp = Computer()
ctype = deideCompChar(ptype)
comp.ctype = ctype
while(inp == 'Y'):
    os.system("cls")
    board = [' ' for x in range(10)] #Statement to clear the board if the user wants to play again
    os.system("cls")
    printBoard(board)
    while(not(checkfull(board))): #Iterate until the board is full
        cres = checkWinner(board,comp.ctype)
        if(cres==0): #The computer has not won yet(1 is returned if it has won)
            player.playerMove() #Player makes his move
            os.system("cls")
            printBoard(board)
        else:
            print("\n"+comp.name + " has won")
            comp.score += 1
            break
            
        pres = checkWinner(board,player.ctype) #Checking if the player has won
        if(pres == 0):
            move = comp.compMove()
            if(move == 0): #No possible moves available(Board is full)
                break
    
            insertAtPos(move,comp.ctype)
            os.system("cls")
            printBoard(board)

        else:
            print("\nCongratulations!! you had won")
            player.score += 1
            break
                
    if(checkfull(board) and cres!=1 and pres!=1):
        print("\nGame is a tie")
    print("\n\nScore\n")
    print(comp.name + ': '+str(comp.score) +"\t"+player.name+": "+str(player.score))
    inps = input('\nDo you want to play again(Y/N): ')
    inp = inps.upper()
        

        
