from fastapi import Depends, HTTPException, status
import token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def get_current_user(token: str= Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Coul not validat credentials",
        headers={"WWW-Authenticate": "Bearer"}
    )

    try:
        payload = jwt.decode 