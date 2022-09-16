from fastapi import FastAPI
import psycopg2
import configparser
import sqlalchemy

CONFIG_PATH = "config.ini"

app = FastAPI()

@app.get("/")
async def root():
    return {"Hello":"World"}
