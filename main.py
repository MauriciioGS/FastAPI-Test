from fastapi import FastAPI,status,HTTPException
from pydantic import BaseModel
from typing import List
from database import SessionLocal
import models

app = FastAPI()

class Tool(BaseModel):
    id:int
    title:str
    description:str
    image:str
    link:str

    class Config:
        orm_mode=True

db = SessionLocal()

@app.get('/tools',response_model=List[Tool],
        status_code=status.HTTP_200_OK)
def get_all_tools():
    tools = db.query(models.Tool).all()
    return tools

@app.get('/tool/{tool_id}', response_model=Tool,
        status_code=status.HTTP_200_OK)
def get_an_tool(tool_id:int):
    tool = db.query(models.Tool).filter(models.Tool.id == tool_id).first()
    return tool

@app.post('/tools',response_model=Tool,
        status_code=status.HTTP_201_CREATED)
def create_an_tool(tool:Tool):

    db_item = db.query(models.Tool).filter(models.Tool.title == tool.title).first()

    if db_item is not None:
        raise HTTPException(status_code=400, details="Tool already exists")

    new_tool = models.Tool(
            title=tool.title,
            description = tool.description,
            image = tool.image,
            link = tool.link
            )

    db.add(new_tool)
    db.commit()

    return new_tool

@app.put('/tool/{tool_id}', response_model=Tool,
        status_code=status.HTTP_200_OK)
def update_an_tool(tool_id:int,tool:Tool):
    tool_to_update = db.query(models.Tool).filter(models.Tool.id == tool_id).first()
    tool_to_update.title = tool.title
    tool_to_update.description = tool.description
    tool_to_update.image = tool.image
    tool_to_update.link = tool.link

    db.commit()

    return tool_to_update

@app.delete('/tool/{tool_id}', response_model=Tool,
        status_code=status.HTTP_200_OK)
def delete_tool(tool_id:int):
    tool_to_delete = db.query(models.Tool).filter(models.Tool.id == tool_id).first()

    if tool_to_delete is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, details = "Resource Not Found")

    db.delete(tool_to_delete)
    db.commit

    return tool_to_delete

