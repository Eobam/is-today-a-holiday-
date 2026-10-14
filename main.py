from fastapi import FastAPI

app = FastAPI()


usal = [11, 619, 74, 1111, 1225]

indl = [126, 815, 102]

canl = [11, 518, 71, 97, 930, 112, 1011, 1225, 1226]

rusl = [11, 17, 223, 38, 51, 59, 612, 114]

def detect_holiday(coun, dat):
    if coun == "russia":
        if dat in rusl:
            return "yes"
        elif dat not in rusl:
            return "no"
    if coun in ("usa", "united states", "united states of america"):
        if dat in usal:
            return "yes"
        elif dat not in usal:
            return "no"
    if coun == "canada":
        if dat in canl:
            return "yes"
        elif dat not in canl:
            return "no"
            

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}

@app.get("/istodayfed")
def check_fed(country: str, date: int):
    yenof = detect_holiday(country, date)
    return {"isit": yenof}