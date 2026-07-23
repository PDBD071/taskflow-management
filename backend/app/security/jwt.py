from datetime import datetime, timedelta

from jose import jwt


SECRET_KEY = "taskflow-secret-key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60


def criar_token(data: dict):

    dados = data.copy()

    expiracao = datetime.utcnow() + timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )

    dados.update(
        {
            "exp": expiracao
        }
    )

    token = jwt.encode(
        dados,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    return token