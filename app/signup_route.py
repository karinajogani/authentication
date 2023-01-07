from fastapi import APIRouter, Depends, Request
from app.schemas import Userdata
from Database.db_base import get_db
from sqlalchemy.orm import Session
from app.models import User
from app.utils import password_hash, JWTBearer, decodeJWT

router = APIRouter()

@router.get("/alluser",dependencies=[Depends(JWTBearer())])
def alluser(request: Request, db:Session = Depends(get_db)):
    """create api for get all user using get method
    """    
    access_token = request.headers["Authorization"][7:]
    decoded = decodeJWT(access_token)
    print(decoded)
    db_users = db.query(User).all()

    return db_users

@router.post("/user_signup")
def signupp(user: Userdata, db: Session = Depends(get_db)):
    """create api for user signup using post method
    """    
    newuser = User(name=user.name, password=password_hash(user.password))
    db.add(newuser)
    db.commit()

    return "user signed in"
