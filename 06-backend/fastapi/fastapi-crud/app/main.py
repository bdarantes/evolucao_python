from fastapi import FastAPI

app = FastAPI(
    title="API CRUD com FastAPI",
    version="1.0.0"
)


@app.get("/")
def root():
    return {"message": "API funcionando!"}