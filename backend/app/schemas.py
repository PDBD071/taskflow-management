from pydantic import BaseModel, EmailStr, Field


# ==========================
# SCHEMAS DE USUÁRIO
# ==========================

class UserCreate(BaseModel):
    name: str = Field(
        ...,
        title="Nome do Usuário"
    )

    email: EmailStr = Field(
        ...,
        title="E-mail"
    )

    password: str = Field(
        ...,
        title="Senha"
    )


class UserResponse(BaseModel):
    id: int = Field(
        ...,
        title="Identificador"
    )

    name: str = Field(
        ...,
        title="Nome do Usuário"
    )

    email: EmailStr = Field(
        ...,
        title="E-mail"
    )

    class Config:
        from_attributes = True


class LoginSchema(BaseModel):
    email: EmailStr = Field(
        ...,
        title="E-mail"
    )

    password: str = Field(
        ...,
        title="Senha"
    )


# ==========================
# SCHEMAS DE TAREFA
# ==========================

class TaskCreate(BaseModel):
    titulo: str = Field(
        ...,
        title="Título da Tarefa"
    )

    descricao: str | None = Field(
        None,
        title="Descrição da Tarefa"
    )

    concluida: bool = Field(
        False,
        title="Tarefa Concluída"
    )


class TaskResponse(BaseModel):
    id: int = Field(
        ...,
        title="Identificador"
    )

    titulo: str = Field(
        ...,
        title="Título da Tarefa"
    )

    descricao: str | None = Field(
        None,
        title="Descrição da Tarefa"
    )

    concluida: bool = Field(
        ...,
        title="Tarefa Concluída"
    )

    user_id: int = Field(
        ...,
        title="Usuário Responsável"
    )


    class Config:
        from_attributes = True