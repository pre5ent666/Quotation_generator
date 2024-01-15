import sqlite3

class Database_Cli():
    __DB_LOCATION = "./db/users_data.db"

    def __init__(self, db_file=None):
        if db_file is None:
            db_file = self.__DB_LOCATION
        self.conn = sqlite3.connect(db_file)
        self.cur = self.conn.cursor()
    
    def __enter__(self):
        return self

    def __exit__(self, ext_type, exc_value, traceback):
        self.cur.close()
        if isinstance(exc_value, Exception):
            self.conn.rollback()
        else:
            self.conn.commit()
        self.conn.close()

    def create_table(self, table, fields):
        self.cur.execute(f"CREATE TABLE IF NOT EXISTS {table} {fields}")
    
    def insert_data(self, table, data=None):
        """ data: should be a list of tuples
        """
        n = len(data[0])
        self.cur.executemany(f"INSERT INTO {table} VALUES({'?,'*(n-1)+'?'})", data)
    
    def read_all_from_table(self, table):
        return self.cur.execute(f"SELECT * FROM {table}")
    
    def control_with_SQL_cmd(self, cmd):
        return self.cur.execute(cmd)
    
    def read_target_from_table_with_constraints(self, target, table, constraints):
        return self.cur.execute(f"SELECT {target} FROM {table} {constraints}")
    

if __name__ == "__main__":
    db_file = "./db/users_data.db"
    with Database_Cli(db_file) as db:
        i = 1
        
        # for info in db.read_all_from_table("clients"):
        #     print(f"{i} {info}")
        #     i = i + 1

        # cmd = "SELECT name FROM clients ORDER BY tax_d"
        # for info in db.control_with_SQL_cmd(cmd):
        #     print(f"{i} {info[0]}")
        #     i = i + 1

        # target = "name"
        # table = "clients"
        # const = f"ORDER BY {target}"

        target = "address"
        table = "clients"
        const = ""
        for info in db.read_target_from_table_with_constraints(target, table, const):
            print(f"{i} {info[0]}")
            i = i + 1

