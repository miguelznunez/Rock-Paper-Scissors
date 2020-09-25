from tkinter import *
import random 

root = Tk()

root.title('Rock Paper Scissors')

root.iconbitmap('roc.ico')

root.resizable(width=False,height=False)

click = True

rHandPhoto = PhotoImage(file = 'rHand.png')
pHandPhoto = PhotoImage(file = 'pHand.png')
sHandPhoto = PhotoImage(file = 'sHand.png')

rockPhoto = PhotoImage(file = 'rock.png')
paperPhoto = PhotoImage(file = 'paper.png')
scissorsPhoto = PhotoImage(file = 'scissors.png')

winPhoto = PhotoImage(file = 'win.png')
loosePhoto = PhotoImage(file = 'loose.png')
tiePhoto = PhotoImage(file = 'tie.png')

rHandButton = ''
pHandButton = ''
sHandButton = ''

def play():
    global rHandButton,pHandButton,sHandButton

    rHandButton = Button(root,image = rHandPhoto, command = lambda:youPick('rock'))
    pHandButton = Button(root,image = pHandPhoto,
                                          command = lambda:youPick('paper'))
    sHandButton = Button(root,image = sHandPhoto,
                                          command = lambda:youPick('scissors'))

    rHandButton.grid(row = 0,column = 0)
    pHandButton.grid(row = 0,column = 1)
    sHandButton.grid(row = 0,column = 2)

def computerPick():
    choice = random.choice(['rock','paper','scissors'])
    return choice

def youPick(yourChoice):
    global click

    compPick = computerPick()

    if click == True:
        if yourChoice == 'rock':
            rHandButton.configure(image = rockPhoto)
            if compPick == 'rock':
                pHandButton.configure(image = rockPhoto)
                sHandButton.configure(image = tiePhoto)
                click = False
            elif compPick == 'paper':
                pHandButton.configure(image = paperPhoto)
                sHandButton.configure(image = loosePhoto)
                click = False
            else:
                pHandButton.configure(image = scissorsPhoto)
                sHandButton.configure(image = winPhoto)
                click = False

        elif yourChoice == 'paper':
            pHandButton.configure(image = paperPhoto)
            if compPick == 'rock':
                rHandButton.configure(image = rockPhoto)
                sHandButton.configure(image = winPhoto)
                click = False
            elif compPick == 'paper':
                rHandButton.configure(image = paperPhoto)
                sHandButton.configure(image = tiePhoto)
                click = False
            else:
                rHandButton.configure(image = scissorsPhoto)
                sHandButton.configure(image = loosePhoto)
                click = False
                
        elif yourChoice == 'scissors':
            sHandButton.configure(image = scissorsPhoto)
            if compPick == 'rock':
                pHandButton.configure(image = rockPhoto)
                rHandButton.configure(image = loosePhoto)
                click = False
            elif compPick == 'paper':
                pHandButton.configure(image = paperPhoto)
                rHandButton.configure(image = winPhoto)
                click = False
            else:
                pHandButton.configure(image = scissorsPhoto)
                rHandButton.configure(image = tiePhoto)
                click = False
    else:
        if yourChoice == 'rock' or yourChoice == 'paper' or yourChoice == 'scissors':
            rHandButton.configure(image = rHandPhoto)
            pHandButton.configure(image = pHandPhoto)
            sHandButton.configure(image = sHandPhoto)
            click = True

play()

root.mainloop()

