from schemas.base import BaseSchema
from typing import Optional
from pydantic import Field

class TodoSchema(BaseSchema):
    todoId: Optional[int] = Field(description="todo Id is not needed on create", default = None)
    todoTitle: str
    todoDescription: str
    todoPriority: int
    todoCompleted: bool
