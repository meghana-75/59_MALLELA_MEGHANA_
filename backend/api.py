from fastapi import FastAPI
from pydantic import BaseModel
from rag_chain import ask_question
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()


app.add_middleware(
CORSMiddleware,
allow_origins=["*"],
allow_credentials=True,
allow_methods=["*"],
allow_headers=["*"],
)


class Question(BaseModel):
question: str


@app.post("/chat")
def chat(q: Question):
answer = ask_question(q.question)
return {"answer": answer}

cd backend
python -m venv .venv
.\.venv\Scripts\Activate.ps1