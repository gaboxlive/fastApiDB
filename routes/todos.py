from typing import List

from fastapi import (
    APIRouter,
    Depends,
)
from sqlalchemy.orm import Session

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
    '''Insert a todo into a database and return the complete object'''
    print(todo_request)
    return TodoService(session).save_todo(todo_request)