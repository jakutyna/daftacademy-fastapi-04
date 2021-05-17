from sqlalchemy.orm import Session

from . import models


def get_suppliers(db: Session):
    return db.query(models.Supplier).all()


def get_supplier_by_id(db: Session, supplier_id: int):
    return db.query(models.Supplier).filter(models.Supplier.SupplierID == supplier_id).first()


def get_products_by_supplier(db: Session, supplier_id: int):
    return db.query(models.Product).filter(models.Product.SupplierID == supplier_id).\
        order_by(models.Product.ProductID.desc()).all()


def get_category_by_id(db: Session, category_id: int):
    return db.query(models.Category).filter(models.Category.CategoryID == category_id).first()
