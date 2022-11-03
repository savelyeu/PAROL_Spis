from tkinter import *
from tkinter import messagebox
import pyperclip
from random import randint, shuffle, choice

DARK = "#222831"
MIDDLE = "#393E46"
YELLOW = "#FFD369"
GRAY = "#EEEEEE"

def gen_pass():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
               'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
               'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
               'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
               'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    pass_letters = [choice(letters) for _ in range(randint(8, 11))]
    pass_numbers = [choice(numbers) for _ in range(randint(3, 5))]
    pass_symbols = [choice(symbols) for _ in range(randint(2, 6))]

    pass_list = pass_letters + pass_numbers + pass_symbols
    shuffle(pass_list)

    password = "".join(pass_list)
    entry3.insert(0, password)
    pyperclip.copy(password)

def save():
    web = entry1.get()
    email = entry2.get()
    password = entry3.get()

    if len(web) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oj nie", message="Zapoŭni ŭsie pali, \nkali laska")
    else:
        ok = messagebox.askokcancel(title="Daviedka", message=f"Web staronka:{web} \nEmail/Imia: {email}"
                                                       f"\nParoĺ: {password}\n"f"Zhoda? ")
        if ok:
            with open("data.txt", "a") as data:
                data.write(f"{web}, {email}, {password}\n")
                entry1.delete(0, END)
                entry3.delete(0, END)


win = Tk()
win.title("PAROĹ")
win.minsize(width=200, height=200)
win.config(padx=30, pady=30, bg=DARK)

can = Canvas(height=200, width=200)
image = PhotoImage(file="pass.png")
can.create_image(130, 100, image=image)
can.config(bg=DARK, highlightthickness=0)
can.grid(row=0, column=1)

lab1 = Label(text="Web staronka:", highlightthickness=0, bg=DARK).grid(row=1, column=0)
lab2 = Label(text="Email abo Imia:", highlightthickness=0, bg=DARK).grid(row=2, column=0)
lab3 = Label(text="Paroĺ:", highlightthickness=0, bg=DARK).grid(row=3, column=0)

entry1 = Entry(width=38, highlightthickness=0, border=0)
entry1.grid(row=1, column=1, columnspan=2)
entry1.focus()
entry2 = Entry(width=38, highlightthickness=0, border=0)
entry2.grid(row=2, column=1, columnspan=2)
entry3 = Entry(width=22, highlightthickness=0, border=0)
entry3.grid(row=3, column=1)


gen_button = Button(text="Hienieravać paroĺ", width=12, command=gen_pass, highlightthickness=0, highlightbackground=DARK, bg=MIDDLE).grid(row=3, column=2)
add_button = Button(text="Dadać", width=36, command=save, highlightthickness=0, highlightbackground=DARK, bg=MIDDLE).grid(row=4, column=1, columnspan=2)


win.mainloop()