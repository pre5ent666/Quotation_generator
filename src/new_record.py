import flet as ft
from database_tools import Database_Cli

class New_Record(ft.UserControl):
    """
    This UserControl can add/delete a new record to/from database (records_data.db).
    Records should include: 
    client(select by dropdown), date(default is today), product(select by dropdown), price per pcs, pcs, cost.
    
    User can also modify the records showing on the screen.
    Here will be a history screen to display last 5 records of the seleted client.
    """
    def __init__(self):
        super().__init__()
    
    def build(self):
        usr_db = Database_Cli("./db/users_data.db")
        client_list = usr_db.read_target_from_table_with_constraints("name", "clients")

        def dropdown_updated(e):
            clients_info = usr_db.read_client_info_by_name(dd.value)
            t.value = f"Clients Info: {clients_info}"
            self.update()
        
        t = ft.Text("Hi")
        dd = ft.Dropdown(
            on_change=dropdown_updated,
            options=[],
            width=200,
        )
        
        for cname in client_list:
            dd.options.append(ft.dropdown.Option(cname[0]))

        return ft.Column(controls=[dd, t])

def main(page):
    page.add(New_Record())

if __name__ == "__main__":
    ft.app(target=main)