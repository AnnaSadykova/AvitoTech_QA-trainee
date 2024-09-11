import requests
import pytest
 
BASE_URL = "https://qa-internship.avito.com/api/1"
SELLER_ID_INVALID = 1

PAYLOAD_INVALID_ID = { 
        "name": "Телефон", 
        "price": 85566, 
        "sellerId": SELLER_ID_INVALID, 
        "statistics": { 
            "contacts": 32, 
            "like": 35, 
            "viewCount": 14 
        } 
    }

@pytest.fixture 
def create_post_invalid_id(): 
    url = f"{BASE_URL}/item" 
    payload = PAYLOAD_INVALID_ID
    headers = { 
        'Content-Type': 'application/json' 
    } 
     
    response = requests.post(url, json=payload, headers=headers) 
    assert response.status_code == 200, "Post request failed" 
     
    # Получаем статус и ID нового объявления 
    response_data = response.json() 
    status_text = response_data.get("status", "") 
     
    # Извлекаем ID из строки статуса 
    post_id = status_text.split()[-1]  # Предположим, что ID в конце строки 
    return post_id 


def test_create_post_invalid_id(create_post_invalid_id): 
    # Проверяем, что если SELLER_ID > 999999 или SELLER_ID < 111111, то объявление не должно создаваться 
    assert create_post_invalid_id is None, "Post request must not be created" 