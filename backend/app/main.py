from fastapi import FastAPI

from app.database import Base, engine
from app.routes import user_routes
from app.routes import task_routes


Base.metadata.create_all(
    bind=engine
)


tags_metadata = [
    {
        "name": "Inicio",
        "description": "Rota inicial da API"
    },
    {
        "name": "Usuários",
        "description": "Operações relacionadas aos usuários"
    },
    {
        "name": "Tarefas",
        "description": "Operações relacionadas às tarefas"
    }
]


app = FastAPI(
    title="TaskFlow - Gerenciamento de Tarefas API",
    version="1.0.0",
    description="API para gerenciamento de tarefas",
    openapi_tags=tags_metadata
)


@app.get(
    "/",
    tags=["Inicio"],
    summary="Inicio"
)
def inicio():
    return {
        "mensagem": "API de gerenciamento de tarefas funcionando"
    }


app.include_router(
    user_routes.router
)

app.include_router(
    task_routes.router
)