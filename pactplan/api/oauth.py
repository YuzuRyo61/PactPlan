from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm

from ..depends import db_session
from ..library import check_password
from ..models import User

PP_AR_OA = APIRouter()


@PP_AR_OA.post(
    "/token"
)
async def oauth_pb_login(
        form_data: OAuth2PasswordRequestForm = Depends(),
        db=Depends(db_session)
):
    data = db.query(User). \
        filter(
        User.username == form_data.username,
        User.is_remote_user == False  # noqa: E712
    ).one()
    if data is None:
        raise HTTPException(
            status_code=400,
            detail="Incorrect username or password"
        )
    if data.is_suspend:
        raise HTTPException(
            status_code=403,
            detail="This user is suspended"
        )

    if not check_password(form_data.password, data.password):
        raise HTTPException(
            status_code=400,
            detail="Incorrect username or password"
        )

    # TODO: ここにアクセストークンの発行とかを書くのかも。とりあえず仮でTrue返してる
    return True
