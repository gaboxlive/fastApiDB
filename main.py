from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from uvicorn.middleware.proxy_headers import ProxyHeadersMiddleware

from routes import todos

app = FastAPI(
    title='FASTAPI',
    description='FASTAPI BASE PROJECT',
    version='1.0',
    swagger_ui_parameters={'defaultModelsExpandDepth': 1}
)

origins = [
    "*",  # Example: your frontend running on localhost:3000
    #"https://your-frontend-domain.com", # Example: your deployed frontend
    # Add other allowed origins as needed
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,  # Allow cookies, authorization headers, etc.
    allow_methods=["*"],     # Allow all HTTP methods (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],     # Allow all request headers
)
app.add_middleware(
    ProxyHeadersMiddleware,
    trusted_hosts=["172.17.0.1"],
    # Or use trusted_hosts=["*"] to trust all incoming IPs (use with caution in production)
)

app.include_router(todos.route)

#uvicorn main:app --reload --port 8080 --forwarded-allow-ips="*"