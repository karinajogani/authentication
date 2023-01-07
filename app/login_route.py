from fastapi import APIRouter, Depends, status, HTTPException
from app.schemas import Userinfo
from app.models import User
from Database.db_base import get_db
from app.utils import verify_password, create_access_token, refresh_access_token
from sqlalchemy.orm import Session

router= APIRouter()

@router.post("/login")
def login_user(user: Userinfo, db: Session = Depends(get_db)):
    """user login api using post method
    """    
    if not db.query(User).filter(User.name == user.name).count():
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="user not found")

    else:
        user_obj = db.query(User).filter(User.name == user.name).first()
        user_password = user_obj.password

        if verify_password(user.password, user_password):
            access_token = create_access_token(user_obj.name)
            refresh_token = refresh_access_token(user_obj.name)

            return {"access_token": access_token, "refresh_token": refresh_token}

        else: raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Incorrect name or password")
