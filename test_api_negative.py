import requests
import pytest
 
BASE_URL = "https://qa-internship.avito.com/api/1"
SELLER_ID_INVALID = 1
SELLER_ID = 111112

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


PAYLOAD = { 
        "name": "Телефон", 
        "price": 85566, 
        "sellerId": SELLER_ID, 
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


@pytest.fixture 
def create_post(): 
    url = f"{BASE_URL}/item" 
    payload = PAYLOAD
    headers = { 
        'Content-Type': 'application/json' 
    } 
     
    response = requests.post(url, json=payload, headers=headers) 
    assert response.status_code == 200, "Post request failed" 
     
    # Получаем статус и ID нового объявления 
    response_data = response.json() 
    status_text = response_data.get("status", "") 
     
    # Извлекаем ID из строки статуса 
    post_id = status_text.split()[-1] 
    return post_id 

def test_get_post_by_id_error_in_like_field(create_post): 
    # Используем ID созданного поста для получения его через GET запрос 
    post_id = create_post 
    url = f"{BASE_URL}/item/{post_id}" 
     
    response = requests.get(url) 
    assert response.status_code == 200, "Get request failed" 
     
    # Предположим, что ответ — это список объектов 
    post_data_list = response.json() 
    assert isinstance(post_data_list, list), "Response is not a list" 
    assert len(post_data_list) > 0, "Post list is empty" 
     
    # Проверяем данные первого объекта в списке 
    post_data = post_data_list[0] 
     
    assert post_data.get("id") == post_id, "ID does not match" 
    assert post_data.get("name") == PAYLOAD["name"], "Name does not match" 
    assert post_data.get("price") == PAYLOAD["price"], "Price does not match" 
    assert post_data.get("sellerId") == SELLER_ID, "Seller ID does not match"
    assert post_data.get("statistics").get("contacts") == PAYLOAD["statistics"]["contacts"], "Contacts does not match"
    assert post_data.get("statistics").get("like") == PAYLOAD["statistics"]["like"], "Like does not match"
    assert post_data.get("statistics").get("viewCount") == PAYLOAD["statistics"]["viewCount"], "ViewCount does not match"
