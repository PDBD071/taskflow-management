from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt
from sqlalchemy.orm import Session

from app.database import get_db
from app import models
from app.security.jwt import SECRET_KEY, ALGORITHM


security = HTTPBearer()


def usuario_atual(
    credenciais: HTTPAuthorizationCredentials = Depends(security),
    db: Session = Depends(get_db)
):

    token = credenciais.credentials

    try:
        dados = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        usuario_id = dados.get("sub")

        if usuario_id is None:
            raise HTTPException(
                status_code=401,
                detail="Token inválido"
            )

    except Exception:
        raise HTTPException(
            status_code=401,
            detail="Token inválido"
        )


    usuario = db.query(models.User).filter(
        models.User.id == int(usuario_id)
    ).first()


    if usuario is None:
        raise HTTPException(
            status_code=404,
            detail="Usuário não encontrado"
        )


    return usuario