from fastapi.security import OAuth2PasswordBearer

oauth2_pb_scheme = OAuth2PasswordBearer(
    tokenUrl="/oauth/token"
)
