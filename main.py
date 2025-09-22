# Main file : 
from fastapi import FastAPI
from fastapi.params import Body

#initialize the FastAPI app
app = FastAPI()

# Define a root endpoint
@app.get("/")
async def root():
    return {"message": "Welcome to my fast api"}

# Define a POST endpoint to create a new post
@app.post("/posts")
async def create_post(
  payload: dict = Body(...)
):
  print(payload)
  return {"message": "Post created successfully"}