from src.db.Executer import SQLExecuter

ex = SQLExecuter("./data/fluger.db")

print(ex.get_companys())
