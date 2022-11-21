from fastapi import FastAPI
from admins.admin_views import router_admin
from users.users_view import router_user
from fastapi_sqlalchemy import DBSessionMiddleware, db
import os
from dotenv import load_dotenv

load_dotenv('.env')

app = FastAPI()
app.add_middleware(DBSessionMiddleware, db_url=os.environ['DATABASE_URI'])
app.include_router(router_admin)
app.include_router(router_user)
@app.get("/get-data")
def get_data():
    return "you are welcome"