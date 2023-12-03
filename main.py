from fastapi import FastAPI
from app.router import excel, tools


app = FastAPI()

app.include_router(excel.router)
app.include_router(tools.router)
