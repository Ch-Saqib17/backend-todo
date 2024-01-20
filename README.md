First Creat te a Next Project

In next project you can create a folder outside the src or app directory 

After the creation of  folder you can create a python file

After the creation of file you can install package

I already write all packages name in requirements.txt

Then Make a variable in python file

app : FastAPI = FastAPI()

After this you can make a crud opreation like this

@app.get("/")
def get_all():
    return {"text":"Hello World"}

In Post method you see a pydantic issue

You can with BaseModel who import pydantic

from pydantic import BaseModel

Then make a class

class TodoResponse(BaseModel):
    id : int 
    name : str

After making of class then add this class in post method 

@app.get("/api/",response_model=TodoResponse)
def get_all():
    return {"text":"Hello World"}

In Update or Delete Method make without response model

After this check all your crud opreation 

If it's perform then make a ui 

First install the package i write in below

npm i axios

After this you can fetch data from database with the help of 
axios like 

const data = await axios.get("localhost:8000")

const data = await axios.post("localhost:8000/api/")

const data = await axios.delete("localhost:8000/api/{id}")

const data = await axios.update("localhost:8000/api/{id}")

After this if data is fetching properly 

Then style todo app with your own mind set