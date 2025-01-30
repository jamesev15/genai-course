from fastapi import FastAPI

app = FastAPI()

@app.get("/summarizer")
def summarizer(link: str) -> dict:
    return {"link": link}