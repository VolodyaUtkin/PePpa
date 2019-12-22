from tkinter import *


class Menu(Frame):
    def __init__(self, master):
        super(Menu, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        Label(self,
              text="Калькулятор"
              ).grid(row=0, column=1, sticky=W)

        self.job1 = BooleanVar()
        Label(self,
              text="Работа 1"
              ).grid(row=2, column=0, sticky=W)
        Label(self,
              text="Amount:"
              ).grid(row=2, column=3, sticky=W)
        self.job11_amount = Entry(self)
        assert isinstance(W, object)
        self.job11_amount.grid(row=2, column=1, sticky=W)

        Checkbutton(self,
                    variable=self.job1
                    ).grid(row=2, column=2, sticky=W)
        Label(self,
              text="Amount:"
              ).grid(row=2, column=3, sticky=W)
        self.job12_amount = Entry(self)
        self.job12_amount.grid(row=2, column=4, sticky=W)

        self.job2 = BooleanVar()
        Label(self,
              text="Работа 2"
              ).grid(row=3, column=0, sticky=W)
        Label(self,
              text="Amount:"
              ).grid(row=3, column=3, sticky=W)
        self.job21_amount = Entry(self)
        assert isinstance(W, object)
        self.job21_amount.grid(row=3, column=1, sticky=W)

        Checkbutton(self,
                    variable=self.job2
                    ).grid(row=3, column=2, sticky=W)
        Label(self,
              text="Amount:"
              ).grid(row=3, column=3, sticky=W)
        self.job22_amount = Entry(self)
        self.job22_amount.grid(row=3, column=4, sticky=W)

        self.job3 = BooleanVar()
        Label(self,
              text="Работа 3 "
              ).grid(row=4, column=0, sticky=W)
        Label(self,
              text="Amount:"
              ).grid(row=4, column=3, sticky=W)
        self.job31_amount = Entry(self)
        assert isinstance(W, object)
        self.job31_amount.grid(row=4, column=1, sticky=W)

        Checkbutton(self,
                    variable=self.job3
                    ).grid(row=4, column=2, sticky=W)
        Label(self,
              text="Amount:"
              ).grid(row=4, column=3, sticky=W)
        self.job32_amount = Entry(self)
        self.job32_amount.grid(row=4, column=4, sticky=W)

        Button(self,
               text="Order!",
               command=self.order,
               ).grid(row=5, column=0, sticky=W)

        self.yours = Text(self, width=50, height=10, wrap=WORD)
        self.yours.grid(row=6, column=0, columnspan=5)

    def order(self):
        price = 0
        order = ""
        job21 = self.job21_amount.get()
        job22 = self.job22_amount.get()
        job11 = self.job11_amount.get()
        job12 = self.job12_amount.get()
        job31 = self.job31_amount.get()
        job32 = self.job32_amount.get()
        if self.job1.get():
            price += float(job11) * float(job12)
            order += "job1 "
        if self.job2.get():
            price += float(job21) * float(job22)
            order += "job2  "
        if self.job3.get():
            price += float(job31) * float(job32)
            order += "job3 "

        yours = "Твой накоп: "
        yours += order
        yours += "\nВ сумме: "
        yours += str(price)

        self.yours.delete(0.0, END)
        self.yours.insert(0.0, yours)


root = Tk()
root.title("Калькулятор")
app = Menu(root)
root.mainloop()
