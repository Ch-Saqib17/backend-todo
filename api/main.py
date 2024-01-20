from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column,String,Integer, create_engine
from sqlalchemy.ext.declarative import declarative_base
from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session
from pydantic import BaseModel
from fastapi import HTTPException
from fastapi.middleware.cors import CORSMiddleware

conn_str : str = "postgresql://Ch-Saqib:4H0iLkyNBpqu@ep-weathered-credit-48841962.us-east-2.aws.neon.tech/piaic?sslmode=require"

engine = create_engine(conn_str)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class Todo(Base):
    __tablename__ = "todo"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=True)


class TodoCreate(BaseModel):
    name: str

class TodoResponse(BaseModel):
    id : int 
    name : str



def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app : FastAPI = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
def get_all(db : Session = Depends(get_db)):
    todo_all = db.query(Todo).all()
    return todo_all

@app.post("/api/",response_model=TodoResponse)
def create_todo(todo : TodoCreate, db : Session = Depends(get_db)):
    new_todo = Todo(name=todo.name)
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
    return new_todo

@app.delete("/api/{todo_id}")
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    todo_delete = db.query(Todo).filter(Todo.id == todo_id).first()

    if not todo_delete:
        raise HTTPException(status_code=404, detail="Todo not found")

    db.delete(todo_delete)
    db.commit()
    return todo_delete

@app.put("/api/{todo_id}")
def update_todo(todo_id: int, todo : TodoCreate , db : Session = Depends(get_db)):
    todo_update = db.query(Todo).filter(Todo.id == todo_id).first()

    if not todo_update:
        raise HTTPException(status_code=404, detail="Todo not Update")

    todo_update.name = todo.name

    db.commit()
    db.refresh(todo_update)

    return todo_update
