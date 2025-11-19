import app

def test_get_tasks():
    with app.app.test_client() as client:
        response = client.get('/tasks')
        assert response.status_code == 200
        assert isinstance(response.get_json(), list)

def test_create_task():
    app.tasks.clear()
    with app.app.test_client() as client:
        response = client.post('/tasks', json={'title': 'Test'})
        assert response.status_code == 201
        assert response.get_json()['title'] == 'Test'