# Main file : 
from typing import Optional
from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel

#initialize the FastAPI app
app = FastAPI()

class Post(BaseModel):
  title: str
  content: str
  rate: Optional[int] = None

# Define a root endpoint
@app.get("/")
async def root():
    return {"message": "Welcome to my fast api"}

# Define a POST endpoint to create a new post
@app.post("/posts")
async def create_post(
  posts: Post
):
  print(posts)
  return {"message": "Post created successfully", "post": posts}