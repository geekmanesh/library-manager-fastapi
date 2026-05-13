from passlib.context import CryptContext

from models.user import User


def authenticate_user(username: str, password: str, db):
    user = db.query(User).filter(User.username == username).first()
    if not user:
        return False
    if not bcrypt_context.verify(password, user.hashed_password):
        return False
    return True


bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
