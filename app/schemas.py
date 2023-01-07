from pydantic import BaseModel

class Userdata(BaseModel):
    """create schema for userdata
    """
    name: str
    password: str

# class Displayuser(BaseModel):
#     """create schema for display user
#     """
#     name: str

#     class Config:
#         orm_mode = True

class Userinfo(BaseModel):
    """create schema for user information
    """
    name: str
    password: str

    class Config:
        orm_mode = True
