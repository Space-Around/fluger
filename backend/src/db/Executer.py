import sqlite3
import config


class SQLExecuter:
    def __init__(self, path_to_db):
        self.conn = sqlite3.connect(path_to_db)
        self.cur = self.conn.cursor()

    def get_companys(self):
        self.cur.execute("""
                SELECT *
                FROM companys;
            """)

        companys_raw = self.cur.fetchall()
        companys = []

        for company_raw in companys_raw:
            companys.append({
                "id": int(company_raw[0]),
                "name": str(company_raw[1])
            })

        return companys




