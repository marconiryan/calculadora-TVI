from tkinter import *
from tkinter import messagebox


class Calculadora:
    def __init__(self, root):
        self.expressao = ""

        self.display = Label(root, font=("Arial", 15), bg="#696969")
        Button(text="⌫", command=self.BtBackSpace).place(rely=0.45, relx=0.45, width=120, height=30, x=15, y=-30,anchor="center")

        Button(text="7", command=self.BtN7).place(rely=0.45, relx=0.45, width=30, height=30, x=-30, y=0,anchor="center")
        Button(text="8", command=self.BtN8).place(rely=0.45, relx=0.45, width=30, height=30, x=0, y=0,anchor="center")
        Button(text="9", command=self.BtN9).place(rely=0.45, relx=0.45, width=30, height=30, x=30, y=0,anchor="center")
        Button(text="/", command=self.BtDiv).place(rely=0.45, relx=0.45, width=30, height=30, x=60, y=0,anchor="center")

        Button(text="4", command=self.BtN4).place(rely=0.45, relx=0.45, width=30, height=30, x=-30, y=30,anchor="center")
        Button(text="5", command=self.BtN5).place(rely=0.45, relx=0.45, width=30, height=30, x=0, y=30,anchor="center")
        Button(text="6", command=self.BtN6).place(rely=0.45, relx=0.45, width=30, height=30, x=30, y=30,anchor="center")
        Button(text="*", command=self.BtMult).place(rely=0.45, relx=0.45, width=30, height=30, x=60, y=30,anchor="center")

        Button(text="1", command=self.BtN1).place(rely=0.45, relx=0.45, width=30, height=30, x=-30, y=60,anchor="center")
        Button(text="2", command=self.BtN2).place(rely=0.45, relx=0.45, width=30, height=30, x=0, y=60,anchor="center")
        Button(text="3", command=self.BtN3).place(rely=0.45, relx=0.45, width=30, height=30, x=30, y=60,anchor="center")
        Button(text="-", command=self.BtSub).place(rely=0.45, relx=0.45, width=30, height=30, x=60, y=60,anchor="center")

        Button(text="0", command=self.BtN0).place(rely=0.45, relx=0.45, width=30, height=30, x=-30, y=90,anchor="center")
        Button(text=",", command=self.BtComma).place(rely=0.45, relx=0.45, width=30, height=30, x=0, y=90,anchor="center")
        Button(text="=", command=self.BtEqual).place(rely=0.45, relx=0.45, width=30, height=30, x=30, y=90,anchor="center")
        Button(text="+", command=self.BtSum).place(rely=0.45, relx=0.45, width=30, height=30, x=60, y=90,anchor="center")

        Button(text="^", command=self.BtDiv)

        self.display.pack(side="top", fill=X, pady=5, padx=5)

    def update_display(self):
        self.display.config(text=self.expressao)

    def BtN0(self):
        self.expressao += "0"
        self.update_display()

    def BtN1(self):
        self.expressao += "1"
        self.update_display()

    def BtN2(self):
        self.expressao += "2"
        self.update_display()

    def BtN3(self):
        self.expressao += "3"
        self.update_display()

    def BtN4(self):
        self.expressao += "4"
        self.update_display()

    def BtN5(self):
        self.expressao += "5"
        self.update_display()

    def BtN6(self):
        self.expressao += "6"
        self.update_display()

    def BtN7(self):
        self.expressao += "7"
        self.update_display()

    def BtN8(self):
        self.expressao += "8"
        self.update_display()

    def BtN9(self):
        self.expressao += "9"
        self.update_display()

    def BtSum(self):
        self.expressao += "+"
        self.update_display()

    def BtSub(self):
        self.expressao += "-"
        self.update_display()

    def BtMult(self):
        self.expressao += "*"
        self.update_display()

    def BtDiv(self):
        self.expressao += "/"
        self.update_display()

    def BtComma(self):
        self.expressao += "."
        self.update_display()

    def BtBackSpace(self):
        new_string = ""
        for i in range(len(self.expressao)):
            if i != len(self.expressao) - 1:
                new_string += self.expressao[i]
        self.expressao = new_string
        self.update_display()

    def BtEqual(self):
        try:
            self.display.config(text=eval(self.expressao))
            self.expressao = ""
        except SyntaxError:
            messagebox.showerror("Erro", "IMPOSSIVEL FAZER ESSA CONTA")


if __name__ == "__main__":
    app = Tk()
    app.geometry("500x300")
    app.title("Calculadora")
    app.configure(background="#1C1C1C")
    Calculadora(app)
    app.mainloop()
