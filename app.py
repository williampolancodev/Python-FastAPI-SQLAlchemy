from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def herlloWorld():
    return "Hello World 2"
