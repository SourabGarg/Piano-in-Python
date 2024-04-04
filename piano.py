import sys
import os

from tkinter import *
from playsound import playsound

root = Tk()
root.title("Flowing Notes")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"{screen_width}x{screen_height}+0+0")
root.configure(background='#171716')
root.resizable(False, False)


# While running as .py

# def play_note(n):
#     playsound(f"Audios/{n}.wav", False)
#


# While running as .exe
def get_sound_file_path(filename):
    if getattr(sys, 'frozen', False):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, "Audios", filename)


def play_note(n):
    sound_file_path = get_sound_file_path(f"{n}.wav")
    playsound(sound_file_path, False)


# ------------FRAME------------

ABC = Frame(root, bg="#171716", bd=20, relief=RIDGE)
ABC.grid()
ABC1 = Frame(ABC, bg="#171716", bd=20, relief=RIDGE)
ABC1.grid()
ABC2 = Frame(ABC, bg="#171716", relief=RIDGE)
ABC2.grid()
ABC3 = Frame(ABC, bg="#171716", relief=RIDGE)
ABC3.grid()

# ----------LABEL-----------
Label(ABC1, text="--FLowing Notes-- \n (11 Keyed Piano)", font=('Comic Sans MS', 25, 'bold'), padx=555, pady=43,
      bd=4, bg="#000000", fg='white', justify=CENTER).grid(row=0, column=0, columnspan=11)

# ---------------BUTTONS----------
btnCs = Button(ABC2, height=7, width=6, bd=4, text="\n\nC#\n\n\n w ", font=(
    'arial', 18, 'bold'), bg="black", fg='white', command=lambda: play_note("CS"))
btnCs.grid(row=0, column=0, padx=5, pady=5)

btnDs = Button(ABC2, height=7, width=6, bd=4, text="\n\nD#\n\n\n e ", font=(
    'arial', 18, 'bold'), bg="black", fg='white', command=lambda: play_note("DS"))
btnDs.grid(row=0, column=1, padx=5, pady=5)

btnSpace2 = Button(ABC2, state=DISABLED, height=6,
                   width=2, bg="#171716", relief=FLAT)
btnSpace2.grid(row=0, column=3, padx=0, pady=0)

btnFs = Button(ABC2, height=7, width=6, bd=4, text="\n\nF#\n\n\n r ", font=(
    'arial', 18, 'bold'), bg="black", fg='white', command=lambda: play_note("FS"))
btnFs.grid(row=0, column=4, padx=5, pady=5)

btnGs = Button(ABC2, height=7, width=6, bd=4, text="\n\nG#\n\n\n t ", font=(
    'arial', 18, 'bold'), bg="black", fg='white', command=lambda: play_note("GS"))
btnGs.grid(row=0, column=6, padx=5, pady=5)

btnBb = Button(ABC2, height=7, width=6, bd=4, text="\n\nBb\n\n\n y ", font=(
    'arial', 18, 'bold'), bg="black", fg='white', command=lambda: play_note("BB"))
btnBb.grid(row=0, column=8, padx=5, pady=5)

btnSpace5 = Button(ABC2, state=DISABLED, height=6,
                   width=2, bg="#171716", relief=FLAT)
btnSpace5.grid(row=0, column=7, padx=0, pady=0)

btnCs1 = Button(ABC2, height=7, width=6, bd=4, text="\n\nC#1\n\n\n u ", font=(
    'arial', 18, 'bold'), bg="black", fg='white', command=lambda: play_note("CS1"))
btnCs1.grid(row=0, column=10, padx=5, pady=5)

btnDs1 = Button(ABC2, height=7, width=6, bd=4, text="\n\nD#1\n\n\n i ", font=(
    'arial', 18, 'bold'), bg="black", fg='white', command=lambda: play_note("DS1"))
btnDs1.grid(row=0, column=12, padx=5, pady=5)

# --------------LOWER BUTTONS--------------------

btnC = Button(ABC3, height=10, width=6, bd=4, text="\n\n\n\nC\n\n\n\n\n a ", bg="white", fg='black', font=(
    'arial', 18, 'bold'), command=lambda: play_note("C"))
btnC.grid(row=0, column=0, padx=5, pady=5)

btnD = Button(ABC3, height=10, width=6, bd=4, text="\n\n\n\nD\n\n\n\n\n s ", bg="white", fg='black', font=(
    'arial', 18, 'bold'), command=lambda: play_note("D"))
btnD.grid(row=0, column=1, padx=5, pady=5)

btnE = Button(ABC3, height=10, width=6, bd=4, text="\n\n\n\nE\n\n\n\n\n d ", bg="white", fg='black',
              font=('''By Sourab Garg'''
                    'arial', 18, 'bold'), command=lambda: play_note("E"))
btnE.grid(row=0, column=2, padx=5, pady=5)

btnF = Button(ABC3, height=10, width=6, bd=4, text="\n\n\n\nF\n\n\n\n\n f ", bg="white", fg='black', font=(
    'arial', 18, 'bold'), command=lambda: play_note("F"))
btnF.grid(row=0, column=3, padx=5, pady=5)

btnG = Button(ABC3, height=10, width=6, bd=4, text="\n\n\n\nG\n\n\n\n\n g ", bg="white", fg='black', font=(
    'arial', 18, 'bold'), command=lambda: play_note("G"))
btnG.grid(row=0, column=4, padx=5, pady=5)

btnA = Button(ABC3, height=10, width=6, bd=4, text="\n\n\n\nA\n\n\n\n\n h ", bg="white", fg='black', font=(
    'arial', 18, 'bold'), command=lambda: play_note("A"))
btnA.grid(row=0, column=5, padx=5, pady=5)

btnB = Button(ABC3, height=10, width=6, bd=4, text="\n\n\n\nB\n\n\n\n\n j ", bg="white", fg='black', font=(
    'arial', 18, 'bold'), command=lambda: play_note("B"))
btnB.grid(row=0, column=6, padx=5, pady=5)

btnC1 = Button(ABC3, height=10, width=6, bd=4, text="\n\n\n\nC1\n\n\n\n\n k ", bg="white", fg='black', font=(
    'arial', 18, 'bold'), command=lambda: play_note("C1"))
btnC1.grid(row=0, column=7, padx=5, pady=5)

btnD1 = Button(ABC3, height=10, width=6, bd=4, text="\n\n\n\nD1\n\n\n\n\n l ", bg="white", fg='black', font=(
    'arial', 18, 'bold'), command=lambda: play_note("D1"))
btnD1.grid(row=0, column=8, padx=5, pady=5)

btnE1 = Button(ABC3, height=10, width=6, bd=4, text="\n\n\n\nE1\n\n\n\n\n ; ", bg="white", fg='black', font=(
    'arial', 18, 'bold'), command=lambda: play_note("E1"))
btnE1.grid(row=0, column=9, padx=5, pady=5)

btnF1 = Button(ABC3, height=10, width=6, bd=4, text="\n\n\n\nF1\n\n\n\n\n ' ", bg="white", fg='black', font=(
    'arial', 18, 'bold'), command=lambda: play_note("F1"))
btnF1.grid(row=0, column=10, padx=5, pady=5)

key_bindings = {
    'a': 'C',
    's': 'D',
    'd': 'E',
    'f': 'F',
    'g': 'G',
    'h': 'A',
    'j': 'B',
    'k': 'C1',
    'l': 'D1',
    ';': 'E1',
    "'": 'F1',
    'w': 'CS',
    'e': 'DS',
    'r': 'FS',
    't': 'GS',
    'y': 'BB',
    'u': 'CS1',
    'i': 'DS1',
}

for key, note in key_bindings.items():
    root.bind(key, lambda event, n=note: play_note(n))

root.mainloop()
