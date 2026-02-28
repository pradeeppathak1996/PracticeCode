from fastapi import FastAPI, Depends

app = FastAPI()

def get_db():
    return "DB Connection"

@app.get("/")
def read_data(db = Depends(get_db)):
    return {"db": db}