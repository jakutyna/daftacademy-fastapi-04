from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import PositiveInt
from sqlalchemy.orm import Session

from app import crud, schemas
from app.database import get_db

router = APIRouter(tags=['northwind'])


# Ex1
@router.get("/suppliers", response_model=List[schemas.Supplier])
async def suppliers_view(db: Session = Depends(get_db)):
    return crud.get_suppliers(db)


@router.get("/suppliers/{supplier_id}", response_model=schemas.SupplierById)
async def suppliers_id_view(supplier_id: PositiveInt, db: Session = Depends(get_db)):
    supplier = crud.get_supplier_by_id(db, supplier_id)
    if supplier is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Supplier not found")
    return supplier


# Ex2
@router.get("/suppliers/{supplier_id}/products", response_model=List[schemas.ProductBySupplier])
async def products_id_view(supplier_id: PositiveInt, db: Session = Depends(get_db)):
    products = crud.get_products_by_supplier(db, supplier_id)
    if len(products) == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Supplier not found")
    for product in products:
        category = crud.get_category_by_id(db, product.CategoryID)
        product.Category = category
    return products


# Ex3
@router.post("/suppliers", response_model=schemas.SupplierCreate, status_code=201)
async def create_supplier_view(supplier: schemas.SupplierCreate, db: Session = Depends(get_db)):
    db_supplier = crud.create_supplier(db, supplier)
    return db_supplier


# Ex4
@router.put("/suppliers/{supplier_id}", response_model=schemas.SupplierCreate, status_code=200)
async def update_supplier_view(supplier_id: PositiveInt, supplier: schemas.SupplierUpdate,
                               db: Session = Depends(get_db)):
    db_supplier = crud.update_supplier(db, supplier_id, supplier)
    if db_supplier is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    return db_supplier