from tkinter import *
from fractions import Fraction
win = Tk()
win.title("conway")
x = win.winfo_screenwidth()
y = win.winfo_screenheight()
win.resizable(0, 0)
win.geometry(f'1200x650+{(x - 1200) // 2}+{(y - 650) // 2}')
def calculate():
    text_result.delete(1.0, END)
    n_r_str = ent_n_r.get()
    if not n_r_str.isdigit():
        btn_calculate.config(text="Please enter a valid number")
        return
    else:
        btn_calculate.config(text="Calculate")
    n_r = int(n_r_str)
    factor = Fraction(10, 1)
    L_F = [Fraction(7, 3), Fraction(99, 98), Fraction(13, 49), Fraction(39, 35),
           Fraction(36, 91), Fraction(10, 143), Fraction(49, 13), Fraction(7, 11),
           Fraction(1, 2), Fraction(91, 1)]
    for j in range(n_r):
        for i in L_F:
            number = i * factor
            if number.denominator == 1:
                factor = number
                break
        temp = factor
        while temp > 1 and temp % 10 == 0:
            temp //= 10
        if temp == 1:
            text_result.insert(END, f"{int(factor)}, ", "red")
        else:
            text_result.insert(END, f"{int(factor)}, ")
lbl_n_r = Label(win, text="Number of repetitions:", font='arial 16')
lbl_n_r.place(x=20, y=20)
ent_n_r = Entry(win, font='arial 16')
ent_n_r.place(x=240, y=20)
btn_calculate = Button(win, text="Calculate", font='arial 14', command=calculate)
btn_calculate.pack(side=BOTTOM, pady=10)
frame_text = Frame(win)
frame_text.pack(pady=50)

scrollbar = Scrollbar(frame_text)
scrollbar.pack(side=RIGHT, fill=Y)

text_result = Text(
    frame_text,
    font='arial 16',
    height=20,
    width=80,
    yscrollcommand=scrollbar.set
)
text_result.pack(side=LEFT)

scrollbar.config(command=text_result.yview)

text_result.tag_config("red", foreground="red")
win.mainloop()