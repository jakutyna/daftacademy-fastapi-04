from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from . import models, schemas


def get_suppliers(db: Session):
    return db.query(models.Supplier).all()


def get_supplier_by_id(db: Session, supplier_id: int):
    return db.query(models.Supplier).filter(models.Supplier.SupplierID == supplier_id).first()


def get_products_by_supplier(db: Session, supplier_id: int):
    return db.query(models.Product).filter(models.Product.SupplierID == supplier_id). \
        order_by(models.Product.ProductID.desc()).all()


def get_category_by_id(db: Session, category_id: int):
    return db.query(models.Category).filter(models.Category.CategoryID == category_id).first()


def create_supplier(db: Session, supplier: schemas.SupplierCreate):
    db_supplier = models.Supplier(**supplier.dict())
    db.add(db_supplier)
    db.commit()
    db.refresh(db_supplier)
    return db_supplier


def update_supplier(db: Session, supplier_id: int, supplier: schemas.SupplierUpdate):
    db_supplier = db.query(models.Supplier).filter(models.Supplier.SupplierID == supplier_id).first()
    if db_supplier is None:
        return None

    # updates 'db_supplier' object attributes with values from corresponding 'supplier' object attributes
    for field, value in vars(supplier).items():
        setattr(db_supplier, field, value) if value else None

    # commit will update modified model instance fields in db
    db.commit()
    # refresh will get latest model instance from db (verification that fields wher updated in db)
    db.refresh(db_supplier)
    return db_supplier


def delete_supplier(db: Session, supplier_id: int):
    db_supplier = db.query(models.Supplier).filter(models.Supplier.SupplierID == supplier_id).first()
    if db_supplier is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Supplier not found")
    db.delete(db_supplier)
    db.commit()
    return db_supplier
