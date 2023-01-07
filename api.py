from fastapi import FastAPI
from app.signup_route import router as signuprouter
from app.login_route import router as loginrouter


app = FastAPI()

app.get("/")
def homepage():
    return {"data" : "you are at the homepage"}

app.include_router(signuprouter, tags=["user-signup"])
app.include_router(loginrouter, tags=["user-login"])
