from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer

from ..depends import db_session
from ..models import User

oauth2_pb_scheme = OAuth2PasswordBearer(
    tokenUrl="/oauth/token"
)


async def get_user(
        token: str = Depends(oauth2_pb_scheme),
        db=Depends(db_session)
):
    user = db.query(User).get(token)
    if not user:
        raise HTTPException(
            status_code=401,
            detail="Invalid authentication credentials",
            headers={
                "WWW-Authenticate": "Bearer"
            }
        )
    if user.is_suspend:
        raise HTTPException(
            status_code=403,
            detail="This user is suspended"
        )
    return user
