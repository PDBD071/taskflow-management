from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from app.database import Base


# ==========================
# MODELO DE USUÁRIO
# ==========================
# Representa os usuários cadastrados no sistema.
# Um usuário pode possuir várias tarefas.


class User(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password_hash = Column(String, nullable=False)

    # Relacionamento 1:N
    # Um usuário possui várias tarefas.
    tasks = relationship(
        "Task",
        back_populates="owner"
    )


# ==========================
# MODELO DE TAREFA
# ==========================
# Representa uma tarefa pertencente a um usuário.


class Task(Base):

    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, nullable=False)
    descricao = Column(String, nullable=True)
    concluida = Column(Boolean, default=False)

    # Chave estrangeira que identifica
    # o proprietário da tarefa.
    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )

    # Relacionamento com o usuário
    # responsável pela tarefa.
    owner = relationship(
        "User",
        back_populates="tasks"
    )