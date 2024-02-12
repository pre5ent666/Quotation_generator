"""
Ref.:
- https://www.pythontutorial.net/tkinter/tkinter-treeview/
- 
"""
import tkinter as tk
from tkinter import ttk
from src.tk_items import Page
from database_tools import Database_Cli

LARGEFONT = ("Arial", 20)
USERS_DATA = "./db/users_data.db"
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
        columns = ("name", "tax_id", "phone", "fax", "address")

        clients_tree = ttk.Treeview(self, columns=columns, show='headings')
        clients_tree.column("# 1",anchor=tk.W, stretch=tk.NO, width=200)
        clients_tree.heading("name",text="客戶名稱")
        clients_tree.column("# 2",anchor=tk.W, stretch=tk.NO, width=100)
        clients_tree.heading("tax_id",text="統一編號")
        clients_tree.column("# 3",anchor=tk.W, stretch=tk.NO, width=100)
        clients_tree.heading("phone",text="電話")
        clients_tree.column("# 4",anchor=tk.W, stretch=tk.NO, width=100)
        clients_tree.heading("fax",text="傳真")
        clients_tree.column("# 5",anchor=tk.W, stretch=tk.NO, width=250)
        clients_tree.heading("address",text="地址")
        
        with Database_Cli(USERS_DATA) as db:
            tb_clinets = db.read_all_from_table("clients")
            for row in tb_clinets:
                print(row)
                clients_tree.insert("", tk.END, values=row)

        clients_tree.pack()

        scrollbar = ttk.Scrollbar(root, orient=tk.VERTICAL, command=clients_tree.yview)
        clients_tree.configure(yscroll=scrollbar.set)
        scrollbar.pack()


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

        # p1.show()
        p3.show()

if __name__ == "__main__":
    root = tk.Tk()
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry("400x400")
    root.mainloop()
