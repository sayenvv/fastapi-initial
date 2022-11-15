from fastapi import APIRouter

router_admin = APIRouter()

@router_admin.get('/admins',tags=['admins'])
def admins():
    return 'admins are welcome'