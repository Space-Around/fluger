import sqlite3
import config

class Executer:
    def __init__(self):
        self.conn = sqlite3.connect(config.DB_NAME)
        self.cur = self.conn.cursor()

    def get_companys(self):
        self.cur.execute("""
                SELECT *
                FROM companys;
            """)

        companys_raw = self.cur.fetchone()
        companys = []

        for company_raw in companys_raw:
            companys.append({
                "id": company_raw[0],
                "name": company_raw[1]
            })

        return companys




