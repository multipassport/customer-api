import uvicorn
from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

import schemas
import services
from database import get_db

app = FastAPI()


@app.post('/customers/', response_model=schemas.CustomerGet, status_code=201)
def create_customer(customer: schemas.CustomerBase, db: Session = Depends(get_db)):
    return services.create_customer(db, customer)


@app.get('/customers/', response_model=list[schemas.CustomerGet])
def get_customers(db: Session = Depends(get_db)):
    return services.get_customers(db)


@app.get('/customers/{customer_id}', response_model=schemas.CustomerGet)
def get_customer(customer_id: int, db: Session = Depends(get_db)):
    return services.get_customer(db, customer_id)


@app.put('/customers/{customer_id}', response_model=schemas.CustomerBase)
def update_customer(customer_id:int, customer: schemas.CustomerBase, db: Session = Depends(get_db)):
    return services.update_customer(db, customer, customer_id)


@app.patch('/customers/{customer_id}', response_model=schemas.CustomerBase)
def patch_customer(customer_id:int, customer: schemas.CustomerPatch, db: Session = Depends(get_db)):
    return services.update_customer(db, customer, customer_id)


@app.delete('/customers/{customer_id}', status_code=204)
def delete_customer(customer_id:int, db: Session = Depends(get_db)):
    return services.delete_customer(db, customer_id)


if __name__ == '__main__':
    uvicorn.run(app='app:app', host='0.0.0.0', port=8080, reload=True)
