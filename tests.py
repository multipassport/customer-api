def test_get_user(app_client, customer):
    response = app_client.get(f'/customers/{customer.id}')
    parsed_customer = response.json()

    assert response.status_code == 200
    assert parsed_customer['name'] == 'John Doe'
