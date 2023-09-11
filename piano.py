from tkinter import *
from playsound import playsound

root = Tk()
root.title("Piano")
root.geometry('1530x755+0+0')
root.configure(background='#80461B')
root.resizable(False, False)


# ------------UPPER FUNCTIONS-----------


def playCS():
    playsound('Audios/CS.wav', False)


def playDS():
    playsound('Audios/DS.wav', False)

def playFS():
    playsound('Audios/FS.wav', False)


def playGS():
    playsound('Audios/GS.wav', False)


def playBB():
    playsound('Audios/BB.wav', False)


def playCS1():
    playsound('Audios/CS1.wav', False)


def playDS1():
    playsound('Audios/DS1.wav', False)


# ----------------LOWER FUNCTIONS-------------

def playC():
    playsound('Audios/C.wav', False)


def playD():
    playsound('Audios/D.wav', False)


def playE():
    playsound('Audios/E.wav', False)


def playF():
    playsound('Audios/F.wav', False)


def playG():
    playsound('Audios/G.wav', False)


def playA():
    playsound('Audios/A.wav', False)


def playB():
    playsound('Audios/B.wav', False)


def playC1():
    playsound('Audios/C1.wav', False)


def playD1():
    playsound('Audios/D1.wav', False)


def playE1():
    playsound('Audios/E1.wav', False)


def playF1():
    playsound('Audios/F1.wav', False)


# ------------FRAME------------

ABC = Frame(root, bg="#B87333", bd=20, relief=RIDGE)
ABC.grid()
ABC1 = Frame(ABC, bg="#B87333", bd=20, relief=RIDGE)
ABC1.grid()
ABC2 = Frame(ABC, bg="#B87333", relief=RIDGE)
ABC2.grid()
ABC3 = Frame(ABC, bg="#B87333", relief=RIDGE)
ABC3.grid()

# ----------LABEL-----------
Label(ABC1, text="-- Piano Player -- \n (11 Keyed Piano)", font=('Comic Sans MS', 25, 'bold'), padx=565, pady=8,
      bd=4, bg="#80461B", fg='white', justify=CENTER).grid(row=0, column=0, columnspan=11)

# ---------------BUTTONS----------
btnCs = Button(ABC2, height=7, width=6, bd=4, text="\n\nC#\n\n\n (w)", font=(
    'arial', 18, 'bold'), bg="black", fg='white', command=playC)
btnCs.grid(row=0, column=0, padx=5, pady=5)

btnDs = Button(ABC2, height=7, width=6, bd=4, text="\n\nD#\n\n\n (e)", font=(
    'arial', 18, 'bold'), bg="black", fg='white', command=playDS)
btnDs.grid(row=0, column=1, padx=5, pady=5)

btnSpace2 = Button(ABC2, state=DISABLED, height=6,
                   width=2, bg="#B87333", relief=FLAT)
btnSpace2.grid(row=0, column=3, padx=0, pady=0)

btnFs = Button(ABC2, height=7, width=6, bd=4, text="\n\nF#\n\n\n (r)", font=(
    'arial', 18, 'bold'), bg="black", fg='white', command=playFS)
btnFs.grid(row=0, column=4, padx=5, pady=5)

btnGs = Button(ABC2, height=7, width=6, bd=4, text="\n\nG#\n\n\n (t)", font=(
    'arial', 18, 'bold'), bg="black", fg='white', command=playGS)
btnGs.grid(row=0, column=6, padx=5, pady=5)

btnBb = Button(ABC2, height=7, width=6, bd=4, text="\n\nBb\n\n\n (y)", font=(
    'arial', 18, 'bold'), bg="black", fg='white', command=playBB)
btnBb.grid(row=0, column=8, padx=5, pady=5)

btnSpace5 = Button(ABC2, state=DISABLED, height=6,
                   width=2, bg="#B87333", relief=FLAT)
btnSpace5.grid(row=0, column=7, padx=0, pady=0)

btnCs1 = Button(ABC2, height=7, width=6, bd=4, text="\n\nC#1\n\n\n (u)", font=(
    'arial', 18, 'bold'), bg="black", fg='white', command=playCS1)
btnCs1.grid(row=0, column=10, padx=5, pady=5)

btnDs1 = Button(ABC2, height=7, width=6, bd=4, text="\n\nD#1\n\n\n (i)", font=(
    'arial', 18, 'bold'), bg="black", fg='white', command=playDS1)
btnDs1.grid(row=0, column=12, padx=5, pady=5)

# --------------LOWER BUTTONS--------------------

btnC = Button(ABC3, height=10, width=6, bd=4, text="\n\n\n\nC\n\n\n\n\n (a)", bg="white", fg='black', font=(
    'arial', 18, 'bold'), command=playC)
btnC.grid(row=0, column=0, padx=5, pady=5)

btnD = Button(ABC3, height=10, width=6, bd=4, text="\n\n\n\nD\n\n\n\n\n (s)", bg="white", fg='black', font=(
    'arial', 18, 'bold'), command=playD)
btnD.grid(row=0, column=1, padx=5, pady=5)

btnE = Button(ABC3, height=10, width=6, bd=4, text="\n\n\n\nE\n\n\n\n\n (d)", bg="white", fg='black',
              font=('''By Sourab Garg'''
                    'arial', 18, 'bold'), command=playE)
btnE.grid(row=0, column=2, padx=5, pady=5)

btnF = Button(ABC3, height=10, width=6, bd=4, text="\n\n\n\nF\n\n\n\n\n (f)", bg="white", fg='black', font=(
    'arial', 18, 'bold'), command=playF)
btnF.grid(row=0, column=3, padx=5, pady=5)

btnG = Button(ABC3, height=10, width=6, bd=4, text="\n\n\n\nG\n\n\n\n\n (g)", bg="white", fg='black', font=(
    'arial', 18, 'bold'), command=playG)
btnG.grid(row=0, column=4, padx=5, pady=5)

btnA = Button(ABC3, height=10, width=6, bd=4, text="\n\n\n\nA\n\n\n\n\n (h)", bg="white", fg='black', font=(
    'arial', 18, 'bold'), command=playA)
btnA.grid(row=0, column=5, padx=5, pady=5)

btnB = Button(ABC3, height=10, width=6, bd=4, text="\n\n\n\nB\n\n\n\n\n (j)", bg="white", fg='black', font=(
    'arial', 18, 'bold'), command=playB)
btnB.grid(row=0, column=6, padx=5, pady=5)

btnC1 = Button(ABC3, height=10, width=6, bd=4, text="\n\n\n\nC1\n\n\n\n\n (k)", bg="white", fg='black', font=(
    'arial', 18, 'bold'), command=playC1)
btnC1.grid(row=0, column=7, padx=5, pady=5)

btnD1 = Button(ABC3, height=10, width=6, bd=4, text="\n\n\n\nD1\n\n\n\n\n (l)", bg="white", fg='black', font=(
    'arial', 18, 'bold'), command=playD1)
btnD1.grid(row=0, column=8, padx=5, pady=5)

btnE1 = Button(ABC3, height=10, width=6, bd=4, text="\n\n\n\nE1\n\n\n\n\n (n)", bg="white", fg='black', font=(
    'arial', 18, 'bold'), command=playE1)
btnE1.grid(row=0, column=9, padx=5, pady=5)

btnF1 = Button(ABC3, height=10, width=6, bd=4, text="\n\n\n\nF1\n\n\n\n\n (m)", bg="white", fg='black', font=(
    'arial', 18, 'bold'), command=playF1)
btnF1.grid(row=0, column=10, padx=5, pady=5)

# ---------------LOWER KEYBINDS----------
root.bind('a', lambda event: playC())
root.bind('s', lambda event: playD())
root.bind('d', lambda event: playE())
root.bind('f', lambda event: playF())
root.bind('g', lambda event: playG())
root.bind('h', lambda event: playA())
root.bind('j', lambda event: playB())
root.bind('k', lambda event: playC1())
root.bind('l', lambda event: playD1())
root.bind('n', lambda event: playE1())
root.bind('m', lambda event: playF1())

# --------------UPPER KEYBINDS-------

root.bind('w', lambda event: playCS())
root.bind('e', lambda event: playDS())
root.bind('r', lambda event: playFS())
root.bind('t', lambda event: playGS())
root.bind('y', lambda event: playBB())
root.bind('u', lambda event: playCS1())
root.bind('i', lambda event: playDS1())

root.mainloop()
