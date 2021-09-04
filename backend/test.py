import config
from src.db.Executer import SQLExecuter
import json

ex = SQLExecuter(config.DB_NAME)

companys = ex.get_companys()
# print(str(companys))

a = str(companys)


# json_string = json.dumps(companys)
#
# print(json_string)
