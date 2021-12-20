from tkinter import *
from tkinter import messagebox


class Calculadora:

    def __init__(self, root):
        self.expressao = ""
        self.display = Label(root, font=("Arial", 15),relief="solid")
        var_rely, var_relx = 0.5,0.55
        self.calculator_on = True
        self.graph_on = False
        self.Tvi_on = False
        self.modo = Label(text="C",bg="#1C1C1C",fg="#00BFFF")
        self.Ponto1 = Entry(width=3,state="disabled",bg="#90EE90")
        self.Ponto2 = Entry(width=3,state="disabled",bg="#90EE90")

        Label(text="Ponto A",bg="#1C1C1C",fg="#F8F8FF").place(rely=0.2,relx=var_relx,x=-100)
        Label(text="Ponto B",bg="#1C1C1C",fg="#F8F8FF").place(rely=0.2,relx=var_relx,x=-5)

        Button(text="Calculadora",relief="solid",command=self.calculator,bg="#00BFFF").place(relx=0.2,rely=0.3,width=90)
        Button(text="Grafico",relief="solid",command=self.graph, bg="#00BFFF").place(relx=0.5,rely=0.3,width=60)
        Button(text="TVI",relief="solid",command=self.TVI_Points, bg="#00BFFF").place(relx=0.7,rely=0.3,width=30,height=30)

        Button(text="CE", command=self.BtBackSpace,relief="solid").place(rely=var_rely, relx=var_relx, width=30, height=30, x=60, y=-30,anchor="center")
        Button(text="%", command=self.BtPercentage,relief="solid").place(rely=var_rely, relx=var_relx, width=30, height=30, x=30, y=-30,anchor="center")
        Button(text=")", command=self.BtParR,relief="solid").place(rely=var_rely, relx=var_relx, width=30, height=30, x=0, y=-30,anchor="center")
        Button(text="(", command=self.BtParL,relief="solid").place(rely=var_rely, relx=var_relx, width=30, height=30, x=-30, y=-30,anchor="center")
        Button(text="√", command=self.BtSqrt,relief="solid").place(rely=var_rely, relx=var_relx, width=30, height=30, x=-60, y=-30,anchor="center")
        Button(text="x", command=self.BtX,relief="solid").place(rely=var_rely, relx=var_relx, width=30, height=30, x=-90, y=-30,anchor="center")

        Button(text="sin", command=self.BtSin,relief="solid").place(rely=var_rely, relx=var_relx, width=30, height=30, x=-90, y=0,anchor="center")
        Button(text="cos", command=self.BtCos,relief="solid").place(rely=var_rely, relx=var_relx, width=30, height=30, x=-60, y=0,anchor="center")
        Button(text="7", command=self.BtN7,relief="solid").place(rely=var_rely, relx=var_relx, width=30, height=30, x=-30, y=0,anchor="center")
        Button(text="8", command=self.BtN8,relief="solid").place(rely=var_rely, relx=var_relx, width=30, height=30, x=0, y=0,anchor="center")
        Button(text="9", command=self.BtN9,relief="solid").place(rely=var_rely, relx=var_relx, width=30, height=30, x=30, y=0,anchor="center")
        Button(text="/", command=self.BtDiv,relief="solid").place(rely=var_rely, relx=var_relx, width=30, height=30, x=60, y=0,anchor="center")

        Button(text="tan", command=self.BtTan,relief="solid").place(rely=var_rely, relx=var_relx, width=30, height=30, x=-90, y=30,anchor="center")
        Button(text="x^y", command=self.BtPower,relief="solid").place(rely=var_rely, relx=var_relx, width=30, height=30, x=-60, y=30,anchor="center")
        Button(text="4", command=self.BtN4,relief="solid").place(rely=var_rely, relx=var_relx, width=30, height=30, x=-30, y=30,anchor="center")
        Button(text="5", command=self.BtN5,relief="solid").place(rely=var_rely, relx=var_relx, width=30, height=30, x=0, y=30,anchor="center")
        Button(text="6", command=self.BtN6,relief="solid").place(rely=var_rely, relx=var_relx, width=30, height=30, x=30, y=30,anchor="center")
        Button(text="*", command=self.BtMult,relief="solid").place(rely=var_rely, relx=var_relx, width=30, height=30, x=60, y=30,anchor="center")

        Button(text="log", command=self.BtLog,relief="solid").place(rely=var_rely, relx=var_relx, width=30, height=30, x=-90, y=60,anchor="center")
        Button(text="ln", command=self.BtLn,relief="solid").place(rely=var_rely, relx=var_relx, width=30, height=30, x=-60, y=60,anchor="center")
        Button(text="1", command=self.BtN1,relief="solid").place(rely=var_rely, relx=var_relx, width=30, height=30, x=-30, y=60,anchor="center")
        Button(text="2", command=self.BtN2,relief="solid").place(rely=var_rely, relx=var_relx, width=30, height=30, x=0, y=60,anchor="center")
        Button(text="3", command=self.BtN3,relief="solid").place(rely=var_rely, relx=var_relx, width=30, height=30, x=30, y=60,anchor="center")
        Button(text="-", command=self.BtSub,relief="solid").place(rely=var_rely, relx=var_relx, width=30, height=30, x=60, y=60,anchor="center")

        Button(text="0", command=self.BtN0,relief="solid").place(rely=var_rely, relx=var_relx, width=30, height=30, x=-30, y=90,anchor="center")
        Button(text=".", command=self.BtPoint, relief="solid").place(rely=var_rely, relx=var_relx, width=30, height=30, x=0, y=90, anchor="center")
        Button(text="=", command=self.BtEqual, relief="solid").place(rely=var_rely, relx=var_relx, width=30, height=30, x=30,y=90, anchor="center")
        Button(text="+", command=self.BtSum,relief="solid").place(rely=var_rely, relx=var_relx, width=30, height=30, x=60, y=90,anchor="center")
        Button(text="e", command=self.BtEuler,relief="solid").place(rely=var_rely, relx=var_relx, width=30, height=30, x=-60, y=90,anchor="center")
        Button(text="π", command=self.BtPi,relief="solid").place(rely=var_rely, relx=var_relx, width=30, height=30, x=-90, y=90,anchor="center")

        self.display.pack(side="top", fill=X, pady=5, padx=5)
        self.Ponto1.place(rely=0.2,relx=var_relx,x=50,width=23,height=23)
        self.Ponto2.place(rely=0.2,relx=var_relx,x=-40,width=23,height=23)
        self.modo.place(relx=0.92,rely=0.09)

    def calculator(self):
        self.Ponto1.configure(state="disabled")
        self.Ponto2.configure(state="disabled")
        self.modo.config(text="C")
        self.update_display()
        self.calculator_on = True
        self.Tvi_on = self.graph_on = False

    def graph(self):
        self.graph_on = True
        self.calculator_on = self.Tvi_on = False
        self.modo.config(text="G")
        self.Ponto1.configure(state="disabled")
        self.Ponto2.configure(state="disabled")

    def TVI_Points(self) -> list:
        self.modo.config(text="T")
        self.Tvi_on = True
        self.calculator_on = self.graph_on = False
        self.Ponto1.configure(state="normal")
        self.Ponto2.configure(state="normal")
        return [self.Ponto1.get(),self.Ponto2.get()]

    def TVI(self,P1,P2) -> float:
        if self.expressao.count("x"):
            equacao = lambda x: eval(self.expressao)
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

    def BtX(self):
        self.expressao += "x"
        self.update_display()

    def BtParR(self):
        self.expressao += ")"
        self.update_display()

    def BtParL(self):
        self.expressao += "("
        self.update_display()

    def BtPercentage(self):
        self.expressao += "%"
        self.update_display()

    def BtSqrt(self):
        self.expressao += "sqrt("
        self.update_display()

    def BtSin(self):
        self.expressao += "sin("
        self.update_display()

    def BtCos(self):
        self.expressao += "cos("
        self.update_display()

    def BtTan(self):
        self.expressao += "tan("
        self.update_display()

    def BtLog(self):
        self.expressao += "log("
        self.update_display()

    def BtLn(self):
        self.expressao += "ln("
        self.update_display()

    def BtPi(self):
        self.expressao += "π"
        self.update_display()

    def BtEuler(self):
        self.expressao += "e"
        self.update_display()

    def BtEqual(self):
        try:
            if self.calculator_on:
                if self.expressao.count("x"):
                    messagebox.showinfo("X", "Não consigo fazer essa conta com esse X")
                else:
                    new_string = self.expressao.replace("^","**")
                    self.display.config(text=eval(new_string))
                    self.expressao = ""
            elif self.graph_on:
                if self.expressao.count("x"):
                    import matplotlib.pyplot as graph
                    import numpy as np
                    self.calculator_on = self.Tvi_on = False
                    expressao = lambda x: eval(self.expressao)
                    eixo_x = np.linspace(-50, 50, (abs(-50) + abs(50)) * 2)
                    eixo_y = list(map(expressao, eixo_x))
                    graph.plot(eixo_x,eixo_y)
                    graph.show()
                else:
                    messagebox.showinfo("X", "Preciso de pelo menos um 'X'")
            elif self.Tvi_on:
                if self.expressao.count("x"):
                    import matplotlib.pyplot as graph
                    import numpy as np
                    try:
                        P1,P2 = list(map(float,self.TVI_Points()))
                        equacao = lambda x: eval(self.expressao)
                        eixo_x = np.linspace(P1, P2, int(abs(P1) + abs(P2)) * 2)
                        eixo_y = list(map(equacao, eixo_x))
                        conta = self.TVI(P1,P2)
                        print(conta)
                        if conta:
                            graph.scatter(conta,0)
                            graph.annotate(f"X = {conta:.3f}",xy=(conta, 0),xytext=(conta / 2,(P1+P2)/2),
                                           arrowprops=dict(arrowstyle="->", connectionstyle="arc3"))
                        graph.plot(eixo_x,eixo_y,color="g")
                        graph.stem(eixo_x,eixo_y,linefmt='cyan')
                        graph.title("Teorema do Valor Intermediario")
                        graph.xlabel("Eixo X")
                        graph.ylabel("Eixo Y")
                        graph.show()
                    except ValueError:
                        messagebox.showinfo("Pontos","Informe os Pontos A e B")

                else:
                    messagebox.showinfo("X", "Preciso de pelo menos um 'X'")
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
