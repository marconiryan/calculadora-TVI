from tkinter import *
from tkinter import messagebox


class Calculadora:
    def __init__(self, root):
        self.expressao = ""

        self.display = Label(root, font=("Arial", 15))
        Label(root).grid(column=0,row=0,pady=50)
        Button(text="1", command=self.BtN1).grid(row=4, column=0, ipadx=15, ipady=15, pady=2, padx=2)
        Button(text="2", command=self.BtN2).grid(row=4, column=1, ipadx=5, ipady=5, pady=2, padx=2)
        Button(text="3", command=self.BtN3).grid(row=4, column=2, ipadx=5, ipady=5, pady=2, padx=2)
        Button(text="4", command=self.BtN4).grid(row=3, column=0, ipadx=5, ipady=5, pady=2, padx=2)
        Button(text="5", command=self.BtN5).grid(row=3, column=1, ipadx=5, ipady=5, pady=2, padx=2)
        Button(text="6", command=self.BtN6).grid(row=3, column=2, ipadx=5, ipady=5, pady=2, padx=2)
        Button(text="7", command=self.BtN7).grid(row=2, column=0, ipadx=5, ipady=5, pady=2, padx=2)
        Button(text="8", command=self.BtN8).grid(row=2, column=1, ipadx=5, ipady=5, pady=2, padx=2)
        Button(text="9", command=self.BtN9).grid(row=2, column=2, ipadx=5, ipady=5, pady=2, padx=2)
        Button(text="0", command=self.BtN0).grid(row=5, column=0, ipadx=5, ipady=5, pady=2, padx=2)
        Button(text=",", command=self.BtN0).grid(row=5, column=1, ipadx=5, ipady=5, pady=2, padx=2)
        Button(text="=", command=self.BtEqual).grid(row=5, column=3, ipadx=5, ipady=5, pady=2, padx=2)
        Button(text="+", command=self.BtSum).grid(row=5, column=2, ipadx=5, ipady=5, pady=2, padx=2)
        Button(text="-", command=self.BtSub).grid(row=4, column=3, ipadx=5, ipady=5, pady=2, padx=2)
        Button(text="*", command=self.BtMult).grid(row=3, column=3, ipadx=5, ipady=5, pady=2, padx=2)
        Button(text="/", command=self.BtDiv).grid(row=2, column=3, ipadx=5, ipady=5, pady=2, padx=2)
        Button(text="^", command=self.BtDiv).grid(row=1, column=3, ipadx=5, ipady=5, pady=2, padx=2)
        Button(text="⌫", command=self.BtBackSpace).grid(row=1, column=0, ipadx=5, ipady=5)
        self.display.place(height=50,width=50,x=0,y=0)

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
