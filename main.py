from fastapi import FastAPI
from api.routes import router


app = FastAPI(title="AI Text Detector")


app.include_router(router)


@app.get("/")
def read_root():
    return {"message": "Welcome to AI Text Detector API"}
