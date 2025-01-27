from fastapi import FastAPI
from backend.main import search_agent
from pydantic import BaseModel
import uvicorn


class Body(BaseModel):
    text: str

app = FastAPI()

@app.get("/")
def welcome():
    return {"message": "Welcome to the Pydantic AI-APP!"}

@app.post("/search")
async def generate_response(body: Body):
    user_prompt = body.text
    result = await search_agent.run(user_prompt)
    #result = generate(question, llm, PromptTemplate)
    return {"response": result.data}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=80)
