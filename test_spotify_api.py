import pytest
import requests

# Використовуємо офіційний Base URL Spotify API для документації
BASE_URL = "https://api.spotify.com/v1"


def test_spotify_unauthorized_search():
    """Сценарій 1: Перевірка захисту API (Unauthorized)"""
    # Спроба пошуку без Bearer токена
    endpoint = f"{BASE_URL}/search"
    params = {'q': 'Imagine Dragons', 'type': 'track'}

    response = requests.get(endpoint, params=params)

    # 1. Перевірка HTTP-статусу (має бути 401)
    assert response.status_code == 401

    # 2. Перевірка структури відповіді (JSON)
    data = response.json()
    assert "error" in data
    assert data["error"]["status"] == 401
    assert data["error"]["message"] == "No token provided"


def test_spotify_get_track_invalid_id():
    """Сценарій 2: Перевірка обробки некоректного ID треку (Not Found / Bad Request)"""
    invalid_track_id = "this_is_not_a_valid_id"
    endpoint = f"{BASE_URL}/tracks/{invalid_track_id}"

    response = requests.get(endpoint)

    # Очікуємо статус помилки (зазвичай 400 або 401, якщо немає токена)
    assert response.status_code in [400, 401]


def test_api_endpoint_existence():
    """Сценарій 3: Перевірка пріоритету безпеки (Security Priority)"""
    response = requests.get(f"{BASE_URL}/non_existent_endpoint")
    # Spotify повертає 401 навіть для неіснуючих сторінок, якщо запит неавторизований
    assert response.status_code == 401