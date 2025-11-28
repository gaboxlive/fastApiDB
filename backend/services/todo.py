from typing import List

from fastapi import HTTPException
from sqlalchemy import select
from starlette import status

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

    def todo_by_id(self, todo_id: int) -> TodoSchema | None:
        return TodoDataManager(self.session).todo_by_id(todo_id)

    def update_todo(self, todo_request):
        return TodoDataManager(self.session).update_todo(todo_request)

    def delete_todo(self, todo_id: int):
        return TodoDataManager(self.session).delete_todo(todo_id)

class TodoDataManager(BaseDataManager):
    def get_all_todos(self) -> List[TodoSchema]:
        schemas: List[TodoSchema] = list()

        stmt = select(TodosModel)
        for model in self.get_all(stmt):
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
            title=todo_request.todoTitle,
            description=todo_request.todoDescription,
            priority=todo_request.todoPriority,
            completed=todo_request.todoCompleted
        )
        self.add_one(new_todo)
        return todo_request

    def todo_by_id(self, todo_id: int) -> TodoSchema | None:
        stmt = select(TodosModel).where(TodosModel.id == todo_id)
        returned_todo = self.get_one(stmt)
        if returned_todo is not None:
            todo_json = TodoSchema(
                todoId=returned_todo.id,
                todoTitle=returned_todo.title,
                todoDescription=returned_todo.description,
                todoPriority=returned_todo.priority,
                todoCompleted=returned_todo.completed
            )
            return todo_json
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Item not found')

    def update_todo(self, todo_request):
        stmt = select(TodosModel).where(TodosModel.id == todo_request.todoId)
        todo_model = self.get_one(stmt)
        if todo_model is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Item with the specified ID not found')
        todo_model.title = todo_request.todoTitle
        todo_model.description = todo_request.todoDescription
        todo_model.priority = todo_request.todoPriority
        todo_model.completed = todo_request.todoCompleted
        self.add_one(todo_model)

    def delete_todo(self, todo_id: int):
        stmt = select(TodosModel).where(TodosModel.id == todo_id)
        todo_model = self.get_one(stmt)
        if todo_model is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Item with the specified ID not found')
        self.delete_one(todo_model)
