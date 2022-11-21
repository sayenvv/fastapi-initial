from fastapi import APIRouter,Depends
from fastapi_sqlalchemy import DBSessionMiddleware, db
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi.encoders import jsonable_encoder
from users.models import *
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from authentication import *
from users.serializers import *

router_user = APIRouter()

@router_user.get('/users',tags=['users'])
def users():
    return 'users are welcome'

@router_user.post('/users/create-users')
def create_users(user_:User):
    hash_password = get_password_hash(user_.password)
    userdb = UserModel(username=user_.username,email=user_.email,full_name=user_.full_name,password=hash_password)
    db.session.add(userdb)
    db.session.commit()
    data = db.session.query(UserModel).filter(UserModel.id==userdb.id)
    
    return  [i for i in data]

@router_user.post('/token',response_model=Token,)
async def login_for_accesstoken(form_data: OAuth2PasswordRequestForm = Depends()):
    db_ = db.session.query(UserModel)
    user = authenticate_user(db_, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@router_user.get("/users/me/", response_model=UserResponseSchema)
async def read_users_me(current_user: UserResponseSchema = Depends(get_current_active_user)):
    return current_user


@router_user.get("/users/me/items/")
async def read_own_items(current_user: UserResponseSchema = Depends(get_current_active_user)):
    return [{"item_id": "Foo", "owner": current_user.username}]

@router_user.post('/users/add-profile',tags=['users'])
def add_profile():

    return {'data' : 'added successfully'}