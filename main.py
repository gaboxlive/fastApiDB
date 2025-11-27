from fastapi import FastAPI
from routes import todos

app = FastAPI(
    title='FASTAPI',
    description='FASTAPI BASE PROJECT',
    version='1.0',
    swagger_ui_parameters={'defaultModelsExpandDepth': 1}
)

app.include_router(todos.route)