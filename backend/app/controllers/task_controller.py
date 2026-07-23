from sqlalchemy.orm import Session

import app.schemas as schemas
from app.services import task_service


def criar_task(
    db: Session,
    task: schemas.TaskCreate,
    usuario_id: int
):

    return task_service.criar_task(
        db,
        task,
        usuario_id
    )


def listar_tasks(
    db: Session,
    usuario_id: int
):

    return task_service.listar_tasks(
        db,
        usuario_id
    )


def buscar_task(
    db: Session,
    task_id: int,
    usuario_id: int
):

    return task_service.buscar_task(
        db,
        task_id,
        usuario_id
    )


def atualizar_task(
    db: Session,
    task_id: int,
    task: schemas.TaskCreate,
    usuario_id: int
):

    return task_service.atualizar_task(
        db,
        task_id,
        task,
        usuario_id
    )


def excluir_task(
    db: Session,
    task_id: int,
    usuario_id: int
):

    return task_service.excluir_task(
        db,
        task_id,
        usuario_id
    )