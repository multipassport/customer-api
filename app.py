import uvicorn
from fastapi import FastAPI

import schemas

app = FastAPI()


@app.post('/customers/', response_model=schemas.CustomerGet, status_code=201)
def create_customer(customer: schemas.CustomerBase):
    pass


@app.get('/customers/', response_model=list[schemas.CustomerGet])
def get_customers():
    pass


@app.get('/customers/{customer_id}', response_model=schemas.CustomerGet)
def get_customer():
    pass


@app.put('/customers/{customer_id}', response_model=schemas.CustomerGet)
def update_customer(customer: schemas.CustomerBase):
    pass


@app.patch('/customers/{customer_id}', response_model=schemas.CustomerGet)
def patch_customer(customer: schemas.CustomerPatch):
    pass


@app.delete('/customers/{customer_id}', status_code=204)
def delete_customer():
    pass


if __name__ == '__main__':
    uvicorn.run(app='app:app', host='0.0.0.0', port=8080, reload=True)
