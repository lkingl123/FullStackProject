from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
#App object
app = FastAPI()


origins = ['htpps://localhost:300']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"Ping":"Pong"}


@app.get("/api/todo")
async def get_todo():
    return 1

@app.get("/api/todo{id}")
async def get_todo():
    return 1