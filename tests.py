from models import Customer


def test_get_customer(app_client, customer):
    response = app_client.get(f'/customers/{customer.id}')
    parsed_customer = response.json()

    assert response.status_code == 200
    assert parsed_customer['name'] == 'John Doe'


def test_get_customers(app_client, customer, customer2):
    response = app_client.get('/customers')
    parsed_customers = response.json()

    assert response.status_code == 200
    assert parsed_customers[0]['id'] == customer.id
    assert parsed_customers[1]['id'] == customer2.id


def test_create_customer(app_client, customer_body, db):
    response = app_client.post('/customers/', json=customer_body)
    parsed_customer = response.json()

    db_customer = db.query(Customer).filter(Customer.id == parsed_customer['id']).first()

    assert response.status_code == 201
    assert parsed_customer['name'] == customer_body['name']
    assert db_customer.name == customer_body['name']


def test_update_customer(app_client, customer, customer_body):
    response = app_client.put(f'/customers/{customer.id}', json=customer_body)
    parsed_customer = response.json()

    assert response.status_code == 200
    assert parsed_customer['name'] == customer_body['name']


def test_patch_customer(app_client, customer):
    customer_body = {'name': 'Ivan Ivanov'}
    response = app_client.patch(f'/customers/{customer.id}', json=customer_body)
    parsed_customer = response.json()
    assert response.status_code == 200
    assert parsed_customer['name'] == customer_body['name']


def test_delete_customer(app_client, customer, db):
    response = app_client.delete(f'/customers/{customer.id}')
    db_customer = db.query(Customer).filter(Customer.id == customer.id).first()

    assert response.status_code == 204
    assert not db_customer
