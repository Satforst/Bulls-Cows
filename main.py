from tkinter import *
import random


class Window:
    def __init__(self, master):
        self.master = master

        self.guess_number = None
        self.cows = 0
        self.bulls = 0
        master.title("Bulls and Cows")

        self.label = Label(master, text="Let`s play Bulls and Cows game!")
        self.label.grid(row=0, column=0, columnspan=2, sticky=W + E)

        self.startBut = Button(master, text="Start game", command=self.start, state=NORMAL)
        self.startBut.grid(row=1, column=0)

        self.closeBut = Button(master, text="Close", command=master.quit)
        self.closeBut.grid(row=1, column=2)

        self.helpBut = Button(master, text='help', command=self.help)
        self.helpBut.grid(row=1, column=1)

        vcmd = master.register(self.str_checking)  # we have to wrap the command
        self.entry = Entry(master, validate="key", validatecommand=(vcmd, '%P'))


    def start(self):
        g_numb = []
        while len(g_numb) <= 3:
            rand_numb = random.randint(0, 9)
            if rand_numb not in g_numb: g_numb.append(rand_numb)
        self.g_numb = g_numb

        vcmd = self.master.register(self.str_checking)  # we have to wrap the command
        self.entry = Entry(self.master, validate="key", validatecommand=(vcmd, '%P'))
        self.entry.grid(row=2, column=0, columnspan=2, sticky=W + E)
        print(g_numb)

        self.comBut = Button(self.master, text='Try It', command=self.bulls_cows)
        self.comBut.grid(row=3, column=0, columnspan=2, sticky=W + E)

        self.startBut.configure(state=DISABLED)
        return g_numb

    def str_checking(self, input_numbers):
        if not input_numbers:
            self.guess_number = None
            return True
        try:
            guess_number = int(input_numbers)
            if 0 <= guess_number < 9876:
                self.guess_number = guess_number
                return True
            else:
                return False
        except ValueError:
            return False


    def bulls_cows(self):
        print(self.guess_number)
        if not type(self.guess_number) is list:
            self.guess_number = [int(number) for number in str(self.guess_number)]
        self.cows = 0
        for tip_i in self.guess_number:
            for guess_i in self.g_numb:
                if tip_i == guess_i:
                    self.cows += 1

        self.bulls = 0
        for index, _ in enumerate(self.g_numb):
            if self.guess_number[index] == self.g_numb[index]:
                self.bulls += 1
                self.cows -= 1

        if self.bulls == 4:
            self.message = "Congratulations, You guessed all 4 bulls!\n" \
                           "Do you want play another game?"
            self.resBut = Button(self.master, text='Play again', command=self.reset)
            self.resBut.grid(row=5, column=0, columnspan=2, sticky=W + E)
        else:
            self.message = f"You guessed {self.bulls} bulls and {self.cows} cows."
        self.label_text = StringVar()
        self.label_text.set(self.message)
        self.label = Label(self.master, textvariable=self.label_text)
        self.label.grid(row=4, column=0, columnspan=2, sticky=W + E)

    def reset(self):
        self.message = ""
        self.label_text.set(self.message)
        self.start()

    def help(self):
        help_win = Toplevel(root)
        help_win.title('Manual')
        help_win.geometry("640x400")
        display = Label(help_win, text="""The numerical version of the game is usually played with 4 digits, but can 
        also be played with 3 or any other number of digits.\n
On a sheet of paper, the players each write a 4-digit secret number. The digits must be all different. Then, in turn, 
the players try to guess their opponent's number who gives the number of matches. If the matching digits are in their
 right positions, they are "bulls", if in different positions, they are "cows". Example:\n
Secret number: 4271\n
Opponent's try: 1234\n
Answer: 1 bull and 2 cows. (The bull is "2", the cows are "4" and "1".)\n
The first one to reveal the other's secret number in the least number of guesses wins the game.\n
The game may also be played by two teams of players, with the team members discussing their strategy\n
 before selecting a move.
A computer program moo, written in 1970 by J. M. Grochow at MIT in the PL/I computer language for the Multics \n
operating system, was amongst the first Bulls and Cows computer implementations, inspired by a similar program written \n
by Frank King in 1968 and running on the Cambridge University mainframe. Because the game has simple rules, \n
while it is difficult and entertaining, there are many computer variants; it is often included in telephones and PDAs.
It is proven that any number could be solved within seven turns. \n
Minimal average game length is 26274/5040=5.2131 turns
https://en.wikipedia.org/wiki/Bulls_and_Cows""")
        display.pack()




root = Tk()
app = Window(root)
root.mainloop()
