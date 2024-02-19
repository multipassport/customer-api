from fastapi import HTTPException
from sqlalchemy.orm import Session

from models import Customer
from schemas import CustomerBase, CustomerPatch


def get_customer(db: Session, customer_id: int):
    db_customer = db.query(Customer).filter(Customer.id == customer_id).first()
    if not db_customer:
        raise HTTPException(status_code=404, detail='Customer is not found')
    return db_customer


def get_customers(db: Session):
    return db.query(Customer).order_by(Customer.id.asc())


def create_customer(db: Session, customer: CustomerBase):
    customer_data = Customer(**customer.model_dump())
    db.add(customer_data)
    db.commit()
    return customer_data


def update_customer(db: Session, customer: CustomerPatch, customer_id: int):
    customer_query = db.query(Customer).filter(Customer.id == customer_id)
    if not customer_query:
        raise HTTPException(status_code=404, detail='Customer is not found')
    customer_data = customer.model_dump(exclude_unset=True)
    customer_query.update(customer_data)
    db.commit()
    db_customer = customer_query.first()
    return {
        'name': db_customer.name,
        'address': db_customer.address,
        'age': db_customer.age,
        'description': db_customer.description,
    }


def delete_customer(db: Session, customer_id: int):
    db_customer = db.query(Customer).filter(Customer.id == customer_id).first()
    if not db_customer:
        raise HTTPException(status_code=404, detail='Customer is not found')
    db.delete(db_customer)
    db.commit()
