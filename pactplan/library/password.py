import bcrypt


def gen_password(raw_password: str) -> bytes:
    return bcrypt.hashpw(
        raw_password.encode(),
        bcrypt.gensalt()
    )


def check_password(
        raw_password: str,
        hashed_password: bytes
) -> bool:
    return bcrypt.checkpw(
        raw_password.encode(),
        hashed_password
    )
