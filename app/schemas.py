from pydantic import BaseModel, PositiveInt, constr
from typing import Optional, Union


# ========= Category schemas
class CategoryBase(BaseModel):
    CategoryID: PositiveInt
    CategoryName: constr(max_length=15)


class Category(CategoryBase):
    class Config:
        orm_mode = True


# ========= Product schemas
class ProductBase(BaseModel):
    ProductID: PositiveInt
    ProductName: constr(max_length=40)


class ProductBySupplier(ProductBase):
    Category: Category
    Discontinued: int

    class Config:
        orm_mode = True


# ========= Suppliers schemas
class SupplierBase(BaseModel):
    SupplierID: Optional[PositiveInt]
    CompanyName: constr(max_length=40)


class Supplier(SupplierBase):
    class Config:
        orm_mode = True


class SupplierById(SupplierBase):
    ContactName: Union[constr(max_length=30), None]
    ContactTitle: Union[constr(max_length=30), None]
    Address: Union[constr(max_length=60), None]
    City: Union[constr(max_length=15), None]
    Region: Union[constr(max_length=15), None]
    PostalCode: Union[constr(max_length=10), None]
    Country: Union[constr(max_length=15), None]
    Phone: Union[constr(max_length=24), None]
    Fax: Union[constr(max_length=24), None]
    HomePage: Union[str, None]

    class Config:
        orm_mode = True


class SupplierCreate(SupplierBase):
    ContactName: Union[constr(max_length=30), None]
    ContactTitle: Union[constr(max_length=30), None]
    Address: Union[constr(max_length=60), None]
    City: Union[constr(max_length=15), None]
    PostalCode: Union[constr(max_length=10), None]
    Country: Union[constr(max_length=15), None]
    Phone: Union[constr(max_length=24), None]

    class Config:
        orm_mode = True


class SupplierCreateResponse(SupplierBase):
    ContactName: Union[constr(max_length=30), None]
    ContactTitle: Union[constr(max_length=30), None]
    Address: Union[constr(max_length=60), None]
    City: Union[constr(max_length=15), None]
    PostalCode: Union[constr(max_length=10), None]
    Country: Union[constr(max_length=15), None]
    Phone: Union[constr(max_length=24), None]
    Fax: Union[constr(max_length=24), None]
    HomePage: Union[str, None]

    class Config:
        orm_mode = True


class SupplierUpdate(SupplierBase):
    ContactName: Union[constr(max_length=30), None]
