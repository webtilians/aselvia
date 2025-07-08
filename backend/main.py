from fastapi import FastAPI
import os

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hola Mundo desde FastAPI!"}

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))  # lee el puerto que Railway le pasa
    uvicorn.run("main:app", host="0.0.0.0", port=port)
