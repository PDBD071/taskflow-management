from sqlalchemy.orm import Session

import app.models as models
import app.schemas as schemas


def criar_task(
    db: Session,
    task: schemas.TaskCreate,
    usuario_id: int
):

    nova_task = models.Task(
        titulo=task.titulo,
        descricao=task.descricao,
        concluida=task.concluida,
        user_id=usuario_id
    )

    db.add(nova_task)
    db.commit()
    db.refresh(nova_task)

    return nova_task


def listar_tasks(
    db: Session,
    usuario_id: int
):

    return db.query(models.Task).filter(
        models.Task.user_id == usuario_id
    ).all()


def buscar_task(
    db: Session,
    task_id: int,
    usuario_id: int
):

    return db.query(models.Task).filter(
        models.Task.id == task_id,
        models.Task.user_id == usuario_id
    ).first()


def atualizar_task(
    db: Session,
    task_id: int,
    task: schemas.TaskCreate,
    usuario_id: int
):

    tarefa = buscar_task(
        db,
        task_id,
        usuario_id
    )

    if tarefa is None:
        return None

    tarefa.titulo = task.titulo
    tarefa.descricao = task.descricao
    tarefa.concluida = task.concluida

    db.commit()
    db.refresh(tarefa)

    return tarefa


def excluir_task(
    db: Session,
    task_id: int,
    usuario_id: int
):

    task = buscar_task(
        db,
        task_id,
        usuario_id
    )

    if task:
        db.delete(task)
        db.commit()

    return task