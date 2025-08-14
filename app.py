from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class InputText(BaseModel):
    input: str

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/predict")
def predict(data: InputText):
    # Dummy response for now
    return {"output": f"You said: {data.input}"}
