from app import app

def test_health_check():
    with app.test_client() as client:
        res = client.get('/health')
        assert res.status_code == 200
        assert res.json == {"status": "UP"}

def test_greet_default():
    with app.test_client() as client:
        res = client.get('/')
        assert res.status_code == 200
        assert res.json == {"message": "Hello, World!"}

def test_greet_custom():
    with app.test_client() as client:
        res = client.get('/?name=Prasad')
        assert res.status_code == 200
        assert res.json == {"message": "Hello, Prasad!"}
