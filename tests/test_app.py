"""Pruebas automaticas para los endpoints de Flask."""

import pytest

from app import app


@pytest.fixture
def client():
    app.config.update(TESTING=True)
    with app.test_client() as test_client:
        yield test_client


def test_saludo_con_nombre(client):
    response = client.get('/hello?name=Gabriela')
    assert response.status_code == 200
    assert response.get_data(as_text=True) == 'Hello, Gabriela!'


def test_saludo_sin_nombre(client):
    response = client.get('/hello')
    assert response.status_code == 200
    assert response.get_data(as_text=True) == 'Hello, mundo!'


def test_estado_salud(client):
    response = client.get('/health')
    assert response.status_code == 200
    assert response.json == {'status': 'ok'}
