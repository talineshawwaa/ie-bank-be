from iebank_api import app
import pytest

def test_get_accounts(testing_client):
    """
    GIVEN a Flask application
    WHEN the '/accounts' page is requested (GET)
    THEN check the response is valid
    """
    response = testing_client.get('/accounts')
    assert response.status_code == 200

def test_dummy_wrong_path():
    """
    GIVEN a Flask application
    WHEN the '/wrong_path' page is requested (GET)
    THEN check the response is valid
    """
    with app.test_client() as client:
        response = client.get('/wrong_path')
        assert response.status_code == 404

def test_create_account(testing_client):
    """
    GIVEN a Flask application
    WHEN the '/accounts' page is posted to (POST)
    THEN check the response is valid and the account is created correctly
    """
    response = testing_client.post('/accounts', json={'name': 'John Doe', 'currency': '€', 'country': 'Spain'})
    assert response.status_code == 200
    data = response.get_json()
    assert data['name'] == 'John Doe'
    assert data['currency'] == '€'
    assert data['country'] == 'Spain'
    assert data['status'] == 'Active'

def test_update_account(testing_client):
    """
    GIVEN a Flask application
    WHEN an account is updated (PUT) on '/accounts/<id>'
    THEN check the response is valid and contains the updated data
    """
    # Create an account first
    response = testing_client.post('/accounts', json={'name': 'John Doe', 'currency': '€', 'country': 'Spain'})
    data = response.get_json()
    account_id = data['id']

    # Update the account
    response = testing_client.put(f'/accounts/{account_id}', json={'name': 'John Smith'})
    assert response.status_code == 200
    updated_data = response.get_json()
    assert updated_data['name'] == 'John Smith'

def test_delete_account(testing_client):
    """
    GIVEN a Flask application
    WHEN an account is deleted (DELETE) on '/accounts/<id>'
    THEN check the account is successfully deleted
    """
    # Create an account first
    response = testing_client.post('/accounts', json={'name': 'John Doe', 'currency': '€', 'country': 'Spain'})
    data = response.get_json()
    account_id = data['id']

    # Delete the account
    response = testing_client.delete(f'/accounts/{account_id}')
    assert response.status_code == 200
    deleted_data = response.get_json()
    assert deleted_data['id'] == account_id

def test_get_single_account(testing_client):
    """
    GIVEN a Flask application
    WHEN an account is retrieved (GET) on '/accounts/<id>'
    THEN check the response is valid and contains the correct data
    """
    # Create an account first
    response = testing_client.post('/accounts', json={'name': 'John Doe', 'currency': '€', 'country': 'Spain'})
    data = response.get_json()
    account_id = data['id']

    # Retrieve the account
    response = testing_client.get(f'/accounts/{account_id}')
    assert response.status_code == 200
    retrieved_data = response.get_json()
    assert retrieved_data['id'] == account_id
    assert retrieved_data['name'] == 'John Doe'
    assert retrieved_data['country'] == 'Spain'
