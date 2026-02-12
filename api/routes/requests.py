from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from api.database import get_db
from api import models, schemas
from api.routes.auth import get_current_user

router = APIRouter(prefix="/requests", tags=["Requests"])


@router.post("/", response_model=schemas.RequestOut)
def create_request(
    data: schemas.RequestCreate,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    req = models.Request(
        user_id=user.id,
        service_id=data.service_id,
        phone=data.phone,
        comment=data.comment
    )
    db.add(req)
    db.commit()
    db.refresh(req)
    return req


@router.get("/", response_model=list[schemas.RequestOut])
def get_my_requests(
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    if user.is_admin:
        return db.query(models.Request).all()
    return db.query(models.Request).filter(models.Request.user_id == user.id).all()
