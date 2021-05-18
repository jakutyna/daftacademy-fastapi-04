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
    supplier = crud.create_supplier(db, supplier)
    return supplier
