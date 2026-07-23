from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
import app.schemas as schemas
from app.controllers import user_controller


router = APIRouter(
    prefix="/usuarios",
    tags=["Usuários"]
)


@router.post(
    "/registrar",
    response_model=schemas.UserResponse,
    summary="Registrar Usuário"
)
def registrar(
    usuario: schemas.UserCreate,
    db: Session = Depends(get_db)
):

    novo_usuario = user_controller.criar_usuario(
        db,
        usuario
    )

    if novo_usuario is None:
        raise HTTPException(
            status_code=400,
            detail="E-mail já cadastrado"
        )

    return novo_usuario


@router.post(
    "/login",
    summary="Login de Usuário"
)
def login(
    dados: schemas.LoginSchema,
    db: Session = Depends(get_db)
):

    resultado = user_controller.login(
        db,
        dados.email,
        dados.password
    )

    if resultado is None:
        raise HTTPException(
            status_code=401,
            detail="E-mail ou senha inválidos"
        )

    return resultado