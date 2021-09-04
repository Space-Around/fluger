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


@app.get("/analysis/{company_id}")
def read_item(company_id: int, q: Optional[str] = None):
    return {}

@app.get("/companys/")
def get_companys():
    companys = ex.get_companys()

    json_string = json.dumps(companys)

    return {"companys": json_string}