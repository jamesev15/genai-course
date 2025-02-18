from fastapi import FastAPI
from langserve import add_routes
from chains import chain, llm
from pydantic import BaseModel



class UserRequest(BaseModel):
    user_request: str


app = FastAPI()

add_routes(
    app,
    llm,
    path="/openai"
)

add_routes(
    app,
    chain.with_types(input_type=UserRequest),
    path="/rephrasor"
)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8080)