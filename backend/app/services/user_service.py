from passlib.context import CryptContext
from sqlalchemy.orm import Session

from app import models


pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)


def criar_hash_senha(senha: str):
    return pwd_context.hash(
        senha[:72]
    )


def verificar_senha(
    senha: str,
    senha_hash: str
):
    return pwd_context.verify(
        senha[:72],
        senha_hash
    )


def buscar_usuario_email(
    db: Session,
    email: str
):
    return db.query(models.User).filter(
        models.User.email == email
    ).first()


def criar_usuario(
    db: Session,
    usuario
):

    senha_hash = criar_hash_senha(
        usuario.password
    )

    novo_usuario = models.User(
        name=usuario.name,
        email=usuario.email,
        password_hash=senha_hash
    )

    db.add(novo_usuario)
    db.commit()
    db.refresh(novo_usuario)

    return novo_usuario


def autenticar_usuario(
    db: Session,
    email: str,
    senha: str
):

    usuario = buscar_usuario_email(
        db,
        email
    )

    if usuario is None:
        return None

    senha_valida = verificar_senha(
        senha,
        usuario.password_hash
    )

    if senha_valida is False:
        return None

    return usuario