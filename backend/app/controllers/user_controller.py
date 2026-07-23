from sqlalchemy.orm import Session

import app.schemas as schemas
from app.services import user_service
from app.security.jwt import criar_token


def criar_usuario(
    db: Session,
    usuario: schemas.UserCreate
):

    usuario_existente = user_service.buscar_usuario_email(
        db,
        usuario.email
    )

    if usuario_existente:
        return None

    return user_service.criar_usuario(
        db,
        usuario
    )


def login(
    db: Session,
    email: str,
    senha: str
):

    usuario = user_service.autenticar_usuario(
        db,
        email,
        senha
    )

    if usuario is None:
        return None

    token = criar_token(
        {
            "sub": str(usuario.id)
        }
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }