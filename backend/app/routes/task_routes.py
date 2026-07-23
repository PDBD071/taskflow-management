from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

import app.schemas as schemas
from app.database import get_db
from app.controllers import task_controller
from app.security.auth import usuario_atual
from app import models


router = APIRouter(
    prefix="/tarefas",
    tags=["Tarefas"]
)


@router.post(
    "/",
    response_model=schemas.TaskResponse,
    summary="Criar Tarefa"
)
def criar_tarefa(
    tarefa: schemas.TaskCreate,
    db: Session = Depends(get_db),
    usuario: models.User = Depends(usuario_atual)
):

    return task_controller.criar_task(
        db,
        tarefa,
        usuario.id
    )


@router.get(
    "/",
    response_model=list[schemas.TaskResponse],
    summary="Listar Tarefas"
)
def listar_tarefas(
    db: Session = Depends(get_db),
    usuario: models.User = Depends(usuario_atual)
):

    return task_controller.listar_tasks(
        db,
        usuario.id
    )


@router.get(
    "/{task_id}",
    response_model=schemas.TaskResponse,
    summary="Buscar Tarefa"
)
def buscar_tarefa(
    task_id: int,
    db: Session = Depends(get_db),
    usuario: models.User = Depends(usuario_atual)
):

    tarefa = task_controller.buscar_task(
        db,
        task_id,
        usuario.id
    )

    if tarefa is None:
        raise HTTPException(
            status_code=404,
            detail="Tarefa não encontrada"
        )

    return tarefa


@router.put(
    "/{task_id}",
    response_model=schemas.TaskResponse,
    summary="Atualizar Tarefa"
)
def atualizar_tarefa(
    task_id: int,
    tarefa: schemas.TaskCreate,
    db: Session = Depends(get_db),
    usuario: models.User = Depends(usuario_atual)
):

    tarefa_atualizada = task_controller.atualizar_task(
        db,
        task_id,
        tarefa,
        usuario.id
    )

    if tarefa_atualizada is None:
        raise HTTPException(
            status_code=404,
            detail="Tarefa não encontrada"
        )

    return tarefa_atualizada


@router.delete(
    "/{task_id}",
    summary="Excluir Tarefa"
)
def excluir_tarefa(
    task_id: int,
    db: Session = Depends(get_db),
    usuario: models.User = Depends(usuario_atual)
):

    tarefa = task_controller.excluir_task(
        db,
        task_id,
        usuario.id
    )

    if tarefa is None:
        raise HTTPException(
            status_code=404,
            detail="Tarefa não encontrada"
        )

    return {
        "mensagem": "Tarefa excluída com sucesso"
    }