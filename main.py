from math import e, pi, sqrt, tan, cos, sin, log as ln, log10 as log
from tkinter import Frame, Tk, Entry, Label, Button, messagebox
from tkinter.constants import BOTH, BOTTOM, LEFT, TOP, X
import matplotlib.pyplot as graph
from numpy import linspace


class Function:
    def __init__(self, root):
        self.__expressao = ""
        self.display = Label(root, font=("Arial", 15), relief="solid")
        self.__calculator_on = True
        self.__graph_on = False
        self.__tvi_on = False
        self.ponto_1 = Entry()
        self.ponto_2 = Entry()
        self.modo = Label()
        self.botoes = [["x", lambda: self.func_button("x")], ["√", lambda: self.func_button("sqrt(")],
                       ["(", lambda: self.func_button("(")], [")", lambda: self.func_button(")")],
                       ["%", lambda: self.func_button("%")], ["CE", self.BtBackSpace],
                       ["sin", lambda: self.func_button("sin(")], ["cos", lambda: self.func_button("cos(")],
                       ["7", lambda: self.func_button("7")], ["8", lambda: self.func_button("8")],
                       ["9", lambda: self.func_button("9")], ["/", lambda: self.func_button("/")],
                       ["tan", lambda: self.func_button("tan(")], ["x^y", lambda: self.func_button("^")],
                       ["4", lambda: self.func_button("4")], ["5", lambda: self.func_button("5")],
                       ["6", lambda: self.func_button("6")], ["*", lambda: self.func_button("*")],
                       ["log", lambda: self.func_button("log(")], ["ln", lambda: self.func_button("ln(")],
                       ["1", lambda: self.func_button("1")], ["2", lambda: self.func_button("2")],
                       ["3", lambda: self.func_button("3")], ["-", lambda: self.func_button("-")],
                       ["π", lambda: self.func_button("π")], ["e", lambda: self.func_button("e")],
                       ["0", lambda: self.func_button("0")], [".", lambda: self.func_button(".")], ["=", self.BtEqual],
                       ["+", lambda: self.func_button("+")]]

    def func_button(self, texto: str):
        self.__expressao += texto
        self.update_display()

    def calculator(self) -> None:
        self.ponto_1.configure(state="disabled")
        self.ponto_2.configure(state="disabled")
        self.modo.config(text="C")
        self.update_display()
        self.__calculator_on = True
        self.__tvi_on = self.__graph_on = False

    def graph(self) -> None:
        self.__graph_on = True
        self.__calculator_on = self.__tvi_on = False
        self.modo.config(text="G")
        self.ponto_1.configure(state="disabled")
        self.ponto_2.configure(state="disabled")

    def TVI_Points(self) -> list:
        self.modo.config(text="T")
        self.__tvi_on = True
        self.__calculator_on = self.__graph_on = False
        self.ponto_1.configure(state="normal")
        self.ponto_2.configure(state="normal")
        return [self.ponto_1.get(), self.ponto_2.get()]

    def TVI(self, P1, P2) -> float:
        if self.__expressao.count("x"):
            equacao = lambda x: eval(self.__expressao)
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
            messagebox.showinfo("X", "Preciso de um 'X' para calcular")

    def update_display(self) -> None:
        self.display.config(text=self.__expressao)

    def BtBackSpace(self) -> None:
        new_string = ""
        for i in range(len(self.__expressao)):
            if i != len(self.__expressao) - 1:
                new_string += self.__expressao[i]
        self.__expressao = new_string
        self.update_display()

    def BtCalculator(self) -> None:
        if self.__expressao.count("x"):
            messagebox.showinfo("X", "Não consigo fazer essa conta com esse X")
        else:
            new_string = self.__expressao.replace("^", "**")
            self.display.config(text=eval(new_string))
            self.__expressao = ""

    def BtGraph(self) -> None:
        if self.__expressao.count("x"):
            self.__calculator_on = self.__tvi_on = False
            eixo_x = linspace(-20, 20, 40)
            eixo_y = list(map(lambda x: eval(self.__expressao), eixo_x))
            graph.plot(eixo_x, eixo_y)
            graph.show()
        else:
            messagebox.showinfo("X", "Preciso de pelo menos um 'X'")

    def BtTVI(self) -> None:
        if self.__expressao.count("x"):
            try:
                P1, P2 = list(map(float, self.TVI_Points()))
                eixo_x = linspace(P1, P2, int(abs(P1) + abs(P2)) * 2)
                eixo_y = list(map(lambda x: eval(self.__expressao), eixo_x))
                conta = self.TVI(P1, P2)
                if conta:
                    messagebox.showinfo(
                        "Tem", f"a equação tem pelo menos uma solução neste intervalo com valor de {conta:.4f}")
                    graph.scatter(conta, 0)
                    graph.title(
                        "A equação tem pelo menos uma solução neste intervalo", fontsize=10)
                    graph.plot(eixo_x, eixo_y, color="g",
                               label="Há uma solução neste intervalo")
                    graph.annotate(f"X = {conta:.3f}", xy=(conta, 0),
                                   xytext=(conta / 2, (max(eixo_y) + min(eixo_y)) / 2),
                                   arrowprops=dict(arrowstyle="->", connectionstyle="arc3"))
                else:
                    messagebox.showinfo(
                        "Não tem",
                        "não é possível afirmar que existe solução neste intervalo, tente outros dois números")
                    graph.title(
                        "Não é possível afirmar que existe solução neste intervalo", fontsize=10)
                    graph.plot(eixo_x, eixo_y, color="g", label="Não há solução neste intervalo")
                graph.stem(eixo_x, eixo_y, linefmt='cyan')
                graph.suptitle("Teorema do Valor Intermediario", fontsize=14)
                graph.xlabel("Eixo X")
                graph.ylabel("Eixo Y")
                graph.show()
            except ValueError:
                messagebox.showinfo("Pontos", "Informe os Pontos A e B")

        else:
            messagebox.showinfo("X", "Preciso de pelo menos um 'X'")

    def format_expression(self) -> str:
        return self.__expressao.replace("^", "**").replace("π", "pi").replace("%", "/100 *")

    def BtEqual(self) -> None:
        try:
            self.__expressao = self.format_expression()
            if self.__calculator_on:
                self.BtCalculator()
            elif self.__graph_on:
                self.BtGraph()
            elif self.__tvi_on:
                self.BtTVI()
        except (SyntaxError,NameError):
            messagebox.showerror("Erro", "IMPOSSIVEL FAZER ESSA CONTA")
            self.__expressao = ""
            self.update_display()

    @staticmethod
    def set_buttons(root: Frame, list_button: list, flag: str = "=") -> None:
        for linha in range(5):
            frame_linha = Frame(root)
            frame_linha.pack()
            for coluna in range(6):
                texto, funcao = list_button[coluna + linha * 6]
                background = "#FFFFFF"
                if flag == texto:
                    background = "#00BFFF"
                Button(frame_linha, text=texto, command=funcao, relief="solid", bg=background, width=2, height=1).pack(
                    side=LEFT, ipadx=4, ipady=2, fill=BOTH)


class Calculadora(Function):
    def __init__(self, root):
        super().__init__(root=root)
        self.display.pack(side="top", fill=BOTH, pady=5, padx=5)
        frame_geral = Frame(root, bg="#1C1C1C")
        frame_mode_txt = Frame(root, bg="#1C1C1C")
        frame_points = Frame(frame_geral, bg="#1C1C1C")
        frame_point_1 = Frame(frame_points, bg="#1C1C1C")
        frame_point_2 = Frame(frame_points, bg="#1C1C1C")
        frame_mode = Frame(frame_geral)
        frame_botao = Frame(frame_geral, bg="#1C1C1C")

        frame_mode_txt.pack(side=TOP, anchor="e")
        frame_geral.pack()
        frame_points.pack(pady=10)
        frame_point_1.pack(side=LEFT, padx=10)
        frame_point_2.pack(side=LEFT, padx=18)
        frame_mode.pack(side=TOP)
        frame_botao.pack(side=BOTTOM)
        self.modo = Label(frame_mode_txt, text="C", bg="#1C1C1C", fg="#00BFFF")
        self.modo.pack(fill=X, padx=10)
        Label(frame_point_1, text="Ponto A", bg="#1C1C1C", fg="#F8F8FF").pack(side=LEFT, padx=5)
        Label(frame_point_2, text="Ponto B", bg="#1C1C1C", fg="#F8F8FF").pack(side=LEFT, padx=5)
        self.ponto_1 = Entry(frame_point_1, width=3, state="disabled", bg="#90EE90")
        self.ponto_2 = Entry(frame_point_2, width=3, state="disabled", bg="#90EE90")
        self.ponto_1.pack(side=LEFT)
        self.ponto_2.pack(side=LEFT)
        Button(frame_mode, text="Calculadora", relief="solid", command=self.calculator, bg="#00BFFF").pack(side=LEFT,
                                                                                                           ipadx=10)
        Button(frame_mode, text="Grafico", relief="solid", command=self.graph, bg="#00BFFF").pack(side=LEFT, ipadx=8)
        Button(frame_mode, text="TVI", relief="solid", command=self.TVI_Points, bg="#00BFFF").pack(side=LEFT, ipadx=2)

        self.set_buttons(frame_botao, list_button=self.botoes)


if __name__ == "__main__":
    app = Tk()
    app.geometry("350x350")
    app.title("Calculadora")
    app.configure(background="#1C1C1C")
    Calculadora(app)
    app.resizable(False,False)
    app.mainloop()
