from email.policy import default
from typing import List

from fastapi import (
    APIRouter,
    Depends,
    Request
)
from sqlalchemy.orm import Session
from starlette import status

from config.session import create_session

#from TodoApp.schemas.auth import UserSchema
from schemas.todo import TodoSchema
#from app.services.auth import get_current_user
from services.todo import TodoService


route = APIRouter(prefix="/api/v1/todos")


@route.get("/")
async def get_all_todos(
    session: Session = Depends(create_session),
) -> List[TodoSchema]:
    """Get all todos."""
    return TodoService(session).get_all_todos()

@route.post("/")
async def create_todo(
        todo_request: TodoSchema,
        session: Session = Depends(create_session),
) -> TodoSchema:
    """Insert a todo into a database and return the complete object"""
    return TodoService(session).save_todo(todo_request)

@route.get("/todo/{todo_id}")
async def get_todo_by_id(
        todo_id: int,
        session: Session = Depends(create_session)
) -> TodoSchema:
    todo_found = TodoService(session).todo_by_id(todo_id)
    return todo_found

@route.put("/", status_code=status.HTTP_204_NO_CONTENT)
async def update_todo(
        todo_request: TodoSchema,
        session: Session = Depends(create_session)
):
    TodoService(session).update_todo(todo_request)

@route.delete("/todo/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo(
        todo_id: int,
        session: Session = Depends(create_session)
):
    TodoService(session).delete_todo(todo_id)

#@route.get("/clientIp", status_code=status.HTTP_200_OK)
#async def get_client_ip(data: Request):
#    return {
#        'client_data': data.client.host
#    }

@route.get("/clientIp", status_code=status.HTTP_200_OK)
async def get_client_ip(data: Request):
    print(data.headers)
    return {
        'client_data': data.headers.get('host')
    }