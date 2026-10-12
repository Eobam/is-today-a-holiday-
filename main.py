from fastapi import FastAPI

app = FastAPI()


usal = [11, 619, 74, 1111, 1225]

indl = [126, 815, 102]

canl = 

def detect_holiday(country):


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}

@app.get("istodayfed")
def read_item(country: str, date: int  | None = None):
    return {}