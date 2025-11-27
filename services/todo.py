from typing import List

from sqlalchemy import select

from models.todo import TodosModel
from schemas.todo import TodoSchema
from services.base import (
    BaseDataManager,
    BaseService,
)


class TodoService(BaseService):
    def get_all_todos(self) -> List[TodoSchema]:
        """Get all todos."""

        return TodoDataManager(self.session).get_all_todos()

    def save_todo(self, todo_request) -> TodoSchema:
        return TodoDataManager(self.session).save_todo(todo_request)


class TodoDataManager(BaseDataManager):
    def get_all_todos(self) -> List[TodoSchema]:
        schemas: List[TodoSchema] = list()

        stmt = select(TodosModel)
        for model in self.get_all(stmt):
            print("ssssssss:  ", model.to_dict())
            schemas.append(TodoSchema(
                todoId=model.id,
                todoTitle=model.title,
                todoDescription=model.description,
                todoPriority=model.priority,
                todoCompleted=model.completed)
            )
        return schemas

    def save_todo(self, todo_request) -> TodoSchema:
        new_todo = TodosModel(
            id=todo_request.todoId,
            title=todo_request.todoTitle,
            description=todo_request.todoDescription,
            priority=todo_request.todoPriority,
            completed=todo_request.todoCompleted
        )
        self.add_one(new_todo)
        return todo_request