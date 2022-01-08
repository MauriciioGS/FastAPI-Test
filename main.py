from os import link, name
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

class Material(BaseModel):
    id:int
    name:str
    url_image:str

    class Config:
        orm_mode=True

class Course(BaseModel):
    id:int
    name:str
    description:str
    date:str
    url_course:str

    class Config:
        orm_mode=True

class Workshop(BaseModel):
    id:int
    name:str
    description:str
    date:str
    url_workshop:str

    class Config:
        orm_mode=True

class Topic(BaseModel):
    id:int
    id_material:int
    title:str
    url_notes:str

    class Config:
        orm_mode=True

db = SessionLocal()

# Herramientas CRUD -------------------------------------------------------------------------------------

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
    db.delete(tool_to_delete)
    db.commit()

    if tool_to_delete is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, details = "Resource Not Found")

    return tool_to_delete

# Material CRUD -----------------------------------------------------------------------------------------

#db = SessionLocal()

@app.get('/material',response_model=List[Material],
        status_code=status.HTTP_200_OK)
def get_all_materials():
    materials = db.query(models.Material).all()
    return materials

@app.get('/material/{material_id}', response_model=Material,
        status_code=status.HTTP_200_OK)
def get_an_material(material_id:int):
    material = db.query(models.Material).filter(models.Material.id == material_id).first()
    return material

@app.post('/materials',response_model=Material,
        status_code=status.HTTP_201_CREATED)
def create_an_material(material:Material):

    db_item = db.query(models.Material).filter(models.Material.name == material.name).first()
    if db_item is not None:
        raise HTTPException(status_code=400, details="Material already exists")

    new_material = models.Material(
            name=material.name,
            url_image = material.url_image
            )

    db.add(new_material)
    db.commit()

    return new_material

@app.put('/material/{material_id}', response_model=Material,
        status_code=status.HTTP_200_OK)
def update_an_material(material_id:int,material:Material):
    material_to_update = db.query(models.Material).filter(models.Material.id == material_id).first()
    material_to_update.name = material.name
    material_to_update.url_image = material.url_image

    db.commit()

    return material_to_update

@app.delete('/material/{material_id}', response_model=Material,
        status_code=status.HTTP_200_OK)
def delete_material(material_id:int):
    material_to_delete = db.query(models.Material).filter(models.Material.id == material_id).first()
    db.delete(material_to_delete)
    db.commit()

    if material_to_delete is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, details = "Resource Not Found")

    return material_to_delete

# Cursos CRUD ------------------------------------------------------------------------------------------

#db = SessionLocal()

@app.get('/courses',response_model=List[Course],
        status_code=status.HTTP_200_OK)
def get_all_courses():
    courses = db.query(models.Course).all()
    return courses

@app.get('/course/{course_id}', response_model=Course,
        status_code=status.HTTP_200_OK)
def get_an_course(course_id:int):
    course = db.query(models.Course).filter(models.Course.id == course_id).first()
    return course

@app.post('/course',response_model=Course,
        status_code=status.HTTP_201_CREATED)
def create_a_course(course:Course):

    db_item = db.query(models.Course).filter(models.Course.name == course.name).first()

    if db_item is not None:
        raise HTTPException(status_code=400, details="Course already exists")

    new_course = models.Course(
            name = course.name,
            description = course.description,
            date = course.date,
            link = course.url_course
            )

    db.add(new_course)
    db.commit()

    return new_course

@app.put('/course/{course_id}', response_model=Course,
        status_code=status.HTTP_200_OK)
def update_an_course(course_id:int,course:Course):
    course_to_update = db.query(models.Course).filter(models.Course.id == course_id).first()
    course_to_update.name = course.name
    course_to_update.description = course.description
    course_to_update.date = course.date
    course_to_update.url_course = course.url_course

    db.commit()

    return course_to_update

@app.delete('/course/{course_id}', response_model=Tool,
        status_code=status.HTTP_200_OK)
def delete_course(course_id:int):
    course_to_delete = db.query(models.Course).filter(models.Course.id == course_id).first()
    db.delete(course_to_delete)
    db.commit()

    if course_to_delete is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, details = "Resource Not Found")

    return course_to_delete

# Talleres CRUD -----------------------------------------------------------------------------------------

#db = SessionLocal()

@app.get('/workshops',response_model=List[Workshop],
        status_code=status.HTTP_200_OK)
def get_all_workshops():
    workshops = db.query(models.Workshop).all()
    return workshops

@app.get('/workshop/{workshop_id}', response_model=Workshop,
        status_code=status.HTTP_200_OK)
def get_a_workshop(workshop_id:int):
    workshop = db.query(models.Workshop).filter(models.Workshop.id == workshop_id).first()
    return workshop

@app.post('/workshop',response_model=Workshop,
        status_code=status.HTTP_201_CREATED)
def create_a_workshop(workshop:Workshop):

    db_item = db.query(models.Workshop).filter(models.Workshop.name == workshop.name).first()

    if db_item is not None:
        raise HTTPException(status_code=400, details="Workshop already exists")

    new_workshop = models.Workshop(
            name=workshop.name,
            description = workshop.description,
            date = workshop.date,
            url_workshop = workshop.url_workshop
            )

    db.add(new_workshop)
    db.commit()

    return new_workshop

@app.put('/workshop/{workshop_id}', response_model=Workshop,
        status_code=status.HTTP_200_OK)
def update_a_workshop(workshop_id:int,workshop:Workshop):
    workshop_to_update = db.query(models.Workshop).filter(models.Workshop.id == workshop_id).first()
    workshop_to_update.name = workshop.name
    workshop_to_update.description = workshop.description
    workshop_to_update.date = workshop.date
    workshop_to_update.url_workshop = workshop.url_workshop

    db.commit()

    return workshop_to_update

@app.delete('/workshop/{workshop_id}', response_model=Workshop,
        status_code=status.HTTP_200_OK)
def delete_workshop(workshop_id:int):
    workshop_to_delete = db.query(models.Workshop).filter(models.Workshop.id == workshop_id).first()
    db.delete(workshop_to_delete)
    db.commit()

    if workshop_to_delete is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, details = "Resource Not Found")

    return workshop_to_delete

# Temas CRUD -----------------------------------------------------------------------------------------

#db = SessionLocal()

@app.get('/topics',response_model=List[Topic],
        status_code=status.HTTP_200_OK)
def get_all_topics():
    topics = db.query(models.Topic).all()
    return topics

@app.get('/topic/{topic_id}', response_model=Topic,
        status_code=status.HTTP_200_OK)
def get_a_topic(topic_id:int):
    topic = db.query(models.Topic).filter(models.Topic.id == topic_id).first()
    return topic

@app.post('/topic',response_model=Topic,
        status_code=status.HTTP_201_CREATED)
def create_a_topic(topic:Topic):

    db_item = db.query(models.Topic).filter(models.Topic.title == topic.title).first()

    if db_item is not None:
        raise HTTPException(status_code=400, details="Topic already exists")

    new_topic = models.Topic(
            id_material = topic.id_material,
            title=topic.title,
            url_notes = topic.url_notes
            )

    db.add(new_topic)
    db.commit()

    return new_topic

@app.put('/topic/{topic_id}', response_model=Topic,
        status_code=status.HTTP_200_OK)
def update_a_topic(topic_id:int,topic:Topic):
    topic_to_update = db.query(models.Topic).filter(models.Topic.id == topic_id).first()
    topic_to_update.id_material = topic.id_material
    topic_to_update.title = topic.title
    topic_to_update.url_notes = topic.url_notes

    db.commit()

    return topic_to_update

@app.delete('/topic/{topic_id}', response_model=Topic,
        status_code=status.HTTP_200_OK)
def delete_topic(topic_id:int):
    topic_to_delete = db.query(models.Topic).filter(models.Topic.id == topic_id).first()
    db.delete(topic_to_delete)
    db.commit()

    if topic_to_delete is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, details = "Resource Not Found")

    return topic_to_delete