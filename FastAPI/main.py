import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return {'message' : "Hello, Stranger"}

@app.get('/welcome')
def get_name(name : str):
    print(f"Hello this is {name}")
    return {"Welcometo The Shivam Goel's FastAPI learning" : f'{name}'}

if __name__ == "__main__":
    uvicorn.run(app,host="127.0.0.1",port=8000)

##To start the application run the cmd
# uvicorn main:app --reload

