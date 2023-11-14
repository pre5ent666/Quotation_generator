import tkinter as tk
from tkinter import ttk

LARGEFONT = ("Arial", 20)

class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
    def show(self):
        self.lift()

class New_record(Page):
    pg_name = "單日記帳"

    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        label = tk.Label(self, text=self.pg_name, font=LARGEFONT)
        label.pack(side="top", fill="both", expand=True)

class Monthly_report(Page):
    pg_name = "月統計"

    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        label = tk.Label(self, text=self.pg_name, font=LARGEFONT)
        label.pack(side="top", fill="both", expand=True)

class Customs_list(Page):
    pg_name = "客戶名單"

    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        label = tk.Label(self, text=self.pg_name, font=LARGEFONT)
        label.pack(side="top", fill="both", expand=True)

class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        p1 = New_record(self)
        p2 = Monthly_report(self)
        p3 = Customs_list(self)

        buttonframe = tk.Frame(self)
        container = tk.Frame(self)
        buttonframe.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)

        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        b1 = tk.Button(buttonframe, text=p1.pg_name, command=p1.show)
        b2 = tk.Button(buttonframe, text=p2.pg_name, command=p2.show)
        b3 = tk.Button(buttonframe, text=p3.pg_name, command=p3.show)

        b1.pack(side="left")
        b2.pack(side="left")
        b3.pack(side="left")

        p1.show()

if __name__ == "__main__":
    root = tk.Tk()
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry("400x400")
    root.mainloop()
