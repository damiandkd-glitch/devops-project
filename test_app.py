from app import app

def test_home_page():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200

def test_home_contains_text():
    client = app.test_client()
    response = client.get('/')
    assert b'TEKST_KTOREGO_NIE_MA_NA_STRONIE' in response.data