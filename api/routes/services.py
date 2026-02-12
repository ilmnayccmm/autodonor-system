from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from api.database import get_db
from api import models, schemas
from api.routes.auth import get_current_user

router = APIRouter(prefix="/services", tags=["Services"])


@router.post("/", response_model=schemas.ServiceOut)
def create_service(
    data: schemas.ServiceCreate,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    if not user.is_admin:
        raise Exception("Not allowed")

    service = models.Service(**data.dict())
    db.add(service)
    db.commit()
    db.refresh(service)
    return service


@router.get("/", response_model=list[schemas.ServiceOut])
def get_services(db: Session = Depends(get_db)):
    return db.query(models.Service).all()


@router.get("/{service_id}")
def get_service(service_id: int, db: Session = Depends(get_db)):
    service = db.query(models.Service).filter(models.Service.id == service_id).first()
    if not service:
        raise HTTPException(status_code=404, detail="Service not found")
    return service


@router.delete("/{service_id}")
def delete_service(service_id: int, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    service = db.query(models.Service).filter(models.Service.id == service_id).first()
    if not service:
        raise HTTPException(status_code=404, detail="Service not found")

    db.delete(service)
    db.commit()
    return {"status": "deleted"}
