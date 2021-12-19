from tkinter import *
from tkinter import messagebox


class Calculadora:

    def __init__(self, root):
        self.expressao = ""
        self.display = Label(root, font=("Arial", 15),relief="solid")
        CheckOperation = IntVar()
        var_rely, var_relx = 0.5,0.55

        Checkbutton(text="Calcul",offvalue=0,onvalue=1,variable=CheckOperation,).place(relx=0.1,rely=0.2)
        Checkbutton(text="Graph",offvalue=1,onvalue=2,variable=CheckOperation).place(relx=0.4,rely=0.2)
        Checkbutton(text="TVI",offvalue=1,onvalue=3,variable=CheckOperation).place(relx=0.7,rely=0.2)

        Button(text="CE", command=self.BtBackSpace,relief="solid").place(rely=var_rely, relx=var_relx, width=30, height=30, x=60, y=-30,anchor="center")
        Button(text="%", command=self.BtBackSpace,relief="solid").place(rely=var_rely, relx=var_relx, width=30, height=30, x=30, y=-30,anchor="center")
        Button(text=")", command=self.BtBackSpace,relief="solid").place(rely=var_rely, relx=var_relx, width=30, height=30, x=0, y=-30,anchor="center")
        Button(text="(", command=self.BtBackSpace,relief="solid").place(rely=var_rely, relx=var_relx, width=30, height=30, x=-30, y=-30,anchor="center")
        Button(text="√", command=self.BtBackSpace,relief="solid").place(rely=var_rely, relx=var_relx, width=30, height=30, x=-60, y=-30,anchor="center")
        Button(text="x", command=self.BtBackSpace,relief="solid").place(rely=var_rely, relx=var_relx, width=30, height=30, x=-90, y=-30,anchor="center")

        Button(text="sin", command=self.BtN7,relief="solid").place(rely=var_rely, relx=var_relx, width=30, height=30, x=-90, y=0,anchor="center")
        Button(text="cos", command=self.BtN7,relief="solid").place(rely=var_rely, relx=var_relx, width=30, height=30, x=-60, y=0,anchor="center")
        Button(text="7", command=self.BtN7,relief="solid").place(rely=var_rely, relx=var_relx, width=30, height=30, x=-30, y=0,anchor="center")
        Button(text="8", command=self.BtN8,relief="solid").place(rely=var_rely, relx=var_relx, width=30, height=30, x=0, y=0,anchor="center")
        Button(text="9", command=self.BtN9,relief="solid").place(rely=var_rely, relx=var_relx, width=30, height=30, x=30, y=0,anchor="center")
        Button(text="/", command=self.BtDiv,relief="solid").place(rely=var_rely, relx=var_relx, width=30, height=30, x=60, y=0,anchor="center")

        Button(text="tan", command=self.BtN4,relief="solid").place(rely=var_rely, relx=var_relx, width=30, height=30, x=-90, y=30,anchor="center")
        Button(text="x^y", command=self.BtN4,relief="solid").place(rely=var_rely, relx=var_relx, width=30, height=30, x=-60, y=30,anchor="center")
        Button(text="4", command=self.BtN4,relief="solid").place(rely=var_rely, relx=var_relx, width=30, height=30, x=-30, y=30,anchor="center")
        Button(text="5", command=self.BtN5,relief="solid").place(rely=var_rely, relx=var_relx, width=30, height=30, x=0, y=30,anchor="center")
        Button(text="6", command=self.BtN6,relief="solid").place(rely=var_rely, relx=var_relx, width=30, height=30, x=30, y=30,anchor="center")
        Button(text="*", command=self.BtMult,relief="solid").place(rely=var_rely, relx=var_relx, width=30, height=30, x=60, y=30,anchor="center")

        Button(text="log", command=self.BtN1,relief="solid").place(rely=var_rely, relx=var_relx, width=30, height=30, x=-90, y=60,anchor="center")
        Button(text="ln", command=self.BtN1,relief="solid").place(rely=var_rely, relx=var_relx, width=30, height=30, x=-60, y=60,anchor="center")
        Button(text="1", command=self.BtN1,relief="solid").place(rely=var_rely, relx=var_relx, width=30, height=30, x=-30, y=60,anchor="center")
        Button(text="2", command=self.BtN2,relief="solid").place(rely=var_rely, relx=var_relx, width=30, height=30, x=0, y=60,anchor="center")
        Button(text="3", command=self.BtN3,relief="solid").place(rely=var_rely, relx=var_relx, width=30, height=30, x=30, y=60,anchor="center")
        Button(text="-", command=self.BtSub,relief="solid").place(rely=var_rely, relx=var_relx, width=30, height=30, x=60, y=60,anchor="center")

        Button(text="0", command=self.BtN0,relief="solid").place(rely=var_rely, relx=var_relx, width=30, height=30, x=-30, y=90,anchor="center")
        Button(text=".", command=self.BtPoint, relief="solid").place(rely=var_rely, relx=var_relx, width=30, height=30, x=0, y=90, anchor="center")
        Button(text="=", command=self.BtEqual, relief="solid").place(rely=var_rely, relx=var_relx, width=30, height=30, x=30,y=90, anchor="center")
        Button(text="+", command=self.BtSum,relief="solid").place(rely=var_rely, relx=var_relx, width=30, height=30, x=60, y=90,anchor="center")
        Button(text="e", command=self.BtSum,relief="solid").place(rely=var_rely, relx=var_relx, width=30, height=30, x=-60, y=90,anchor="center")
        Button(text="π", command=self.BtSum,relief="solid").place(rely=var_rely, relx=var_relx, width=30, height=30, x=-90, y=90,anchor="center")

        self.display.pack(side="top", fill=X, pady=5, padx=5)

    def calculator(self):
        if self.expressao.count("x"):
            self.display.config(text="Impossivel fazer essa conta com o 'X'!")

    @staticmethod
    def graph(expressao:str,P1=-50,P2=50) -> dict:
        if expressao.count("x"):
            import numpy as np
            expressao = lambda x: eval(expressao)
            eixo_x = np.linspace(P1,P2,(abs(P1) + abs(P2))*2)
            eixo_y = list(map(expressao,eixo_x))
            return {"X":eixo_x, "Y": eixo_y}
        else:
            messagebox.showinfo("X","Preciso de um 'X' para calcular")

    @staticmethod
    def TVI(equacao:str,P1: float, P2: float) -> float:
        if equacao.count("x"):
            equacao = lambda x: eval(equacao)
            if equacao(P1) * equacao(P2) < 0:
                menor, maior = P1, P2
                if equacao(P1) > 0:
                    menor, maior = P2, P1
                while round(equacao(maior), 5) != 0.0:
                    media = (maior + menor) / 2
                    if equacao(media) < 0:
                        menor = media
                    else:
                        maior = media
                return maior
        else:
            messagebox.showinfo("X","Preciso de um 'X' para calcular")

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

    def BtPoint(self):
        self.expressao += "."
        self.update_display()

    def BtBackSpace(self):
        new_string = ""
        for i in range(len(self.expressao)):
            if i != len(self.expressao) - 1:
                new_string += self.expressao[i]
        self.expressao = new_string
        self.update_display()

    def BtPower(self):
        self.expressao += "^"
        self.update_display()

    def BtEqual(self):
        try:
            new_string = self.expressao.replace("^","**")
            self.display.config(text=eval(new_string))
            self.expressao = ""
        except SyntaxError:
            messagebox.showerror("Erro", "IMPOSSIVEL FAZER ESSA CONTA")
            self.expressao = ""
            self.update_display()


if __name__ == "__main__":
    app = Tk()
    app.geometry("300x350")
    app.title("Calculadora")
    app.configure(background="#1C1C1C")
    Calculadora(app)
    app.mainloop()
