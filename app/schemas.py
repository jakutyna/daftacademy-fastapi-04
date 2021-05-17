from pydantic import BaseModel, PositiveInt, constr
from typing import Union


class SupplierBase(BaseModel):
    SupplierID: PositiveInt
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


"""
    SupplierID = Column(SmallInteger, primary_key=True, server_default=text("nextval('suppliers_supplierid_seq'::regclass)"))
    CompanyName = Column(String(40), nullable=False)
    ContactName = Column(String(30))
    ContactTitle = Column(String(30))
    Address = Column(String(60))
    City = Column(String(15))
    Region = Column(String(15))
    PostalCode = Column(String(10))
    Country = Column(String(15))
    Phone = Column(String(24))
    Fax = Column(String(24))
    HomePage = Column(Text)
"""
