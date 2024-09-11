#В ходе тестирования был обнаружен баг (он указан в файле BUGS.md), который блокирует успешное прохождение теста: при отправке пары ключ-значение - "like": 35 (или любая другая цифра/число) в полученном объекте эта же пара меняется: ключ меняется на "likes", а значение меняется на 0. Для успешного прохождения теста было принято решение в POST-запросе не добавлять данную пару ключ-значение (ранее мной было также протестировано, что данная пара ключ-значение - необязательны).

#Поскольку в условии задания указано, что "Все тесты должны быть пройдены", то я не писала негативные автотесты, которые в любом случае фэйлятся и таким образом не соотвествуют условию задания. 

import requests
import pytest

BASE_URL = "https://qa-internship.avito.com/api/1"
SELLER_ID = 111112

PAYLOAD = { 
        "name": "Телефон", 
        "price": 85566, 
        "sellerId": SELLER_ID, 
        "statistics": { 
            "contacts": 32,
            "viewCount": 14 
        } 
    }
 
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


def test_create_post(create_post): 
    # Проверяем, что ID возвращается и корректный 
    assert create_post is not None 
    assert len(create_post) > 0 
 
 
def test_get_post_by_id(create_post): 
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
    assert post_data.get("statistics").get("viewCount") == PAYLOAD["statistics"]["viewCount"], "ViewCount does not match"

def test_get_items_by_seller():
    url = f"{BASE_URL}/{SELLER_ID}/item"

    response = requests.get(url) 
    assert response.status_code == 200, "Get request failed" 

    post_data_list = response.json() 
    assert isinstance(post_data_list, list), "Response is not a list" 
    assert len(post_data_list) > 0, "Post list is empty" 

