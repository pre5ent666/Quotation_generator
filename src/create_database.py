from database_tools import Database_Cli

db_file = "./db/users_data.db"
with Database_Cli(db_file) as ud:
    table = "clients"
    # ub.create_table(table="clients", fields=["name", "tax_id", "phone", "fax", "address"])
    # ub.insert_data(table, data=[("範例企業有限公司", "12345678", "02-123456789", "02-123456788", "台北市範例區沒有路1號"), ("記帳有限公司", "01234567", "0912345678", "", "桃園市記帳區小幫手路2號")])
    i = 1
    for info in ud.read_all_from_table(table):
        print(f"{i} {info}")
        i = i + 1

record_db = "./db/records_data.db"
with Database_Cli(record_db) as rd:
    rd.create_table("sales_report", ["client", "date", "product", "price", "pcs", "cost"])
    
    # i = 1
    # for info in rd.read_all_from_table(table):
    #     print(f"{i} {info}")
    #     i = i + 1
