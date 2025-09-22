# Important notes for my python backend revision : 

# 1.) fastApi is a modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints. It is built on top of Starlette for the web parts and Pydantic for the data parts.

# 2.) Create a virtual environment:
#    python -m venv env
#    source env/bin/activate  (Linux/Mac)
#    .\env\Scripts\activate   (Windows)
   
# 3.) Install FastAPI and Uvicorn:
#    pip install fastapi uvicorn  

# 4.) Create a simple FastAPI app (main.py):
#    from fastapi import FastAPI
#    app = FastAPI()
#    @app.get("/")
#    async def read_root():
#        return {"Hello": "World"}

# 5.) Run the app with Uvicorn:
#    uvicorn <name_of_your_file>:<Identifier_of_your_FastAPI_instance> 
#    Example: uvicorn main:app --reload (here)



### Creating a POST endpoint in FastAPI ###
# 1.) Import Body from fastapi.params
# 2.) Define a POST endpoint using @app.post decorator
# 3.) Use Body to extract the request body as a dictionary or a Pydantic model
# 4.) Return a response indicating success or failure