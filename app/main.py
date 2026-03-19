from fastapi import FastAPI

app = FastAPI(title="Vetly", version="0.0.1")


@app.get("/")
def health():
    return {"Hello": "World"}
