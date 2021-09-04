import json
import config
from typing import Optional
from fastapi import FastAPI
from src.db.Executer import SQLExecuter

app = FastAPI()
ex = SQLExecuter(config.DB_NAME)


# @app.get("/")
# def read_root():
#     return {"Hello": "World"}
#
#
# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Optional[str] = None):
#     return {"item_id": item_id, "q": q}

@app.get("/analysis/{company_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.get("/companys/")
def get_companys():
    companys = ex.get_companys()

    json_string = json.dumps(companys)

    return {"item_id": json_string}