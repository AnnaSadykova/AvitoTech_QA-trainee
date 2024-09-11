| ID: | 1 |
|----------|----------|
| Summary:  | При отправке POST-запроса на создание объявления создается объявление, где в теле запроса указано sellerId < 111111 или sellerId > 999999   |
| Expected result:   | Объявление не создается. Происходит ошибка 4xx   |
| Actual result:    |  Происходит создание объявления: в теле ответа приходит объект "status" с id объявления.  |
| Severity:    | Major    |
| Priority:    | High    |
| Status:    | New   |
| Author:    | Анна Садыкова   |
| Preconditions:    | Скачать файл "Postman-API.postman_collection" с https://gitverse.ru/avito.tech/tech-internship/content/main/Tech%20Internships%20/QA/%D0%A2%D0%B5%D1%81%D1%82%D0%BE%D0%B2%D0%BE%D0%B5%20%D0%B7%D0%B0%D0%B4%D0%B0%D0%BD%D0%B8%D0%B5_%D0%BE%D1%81%D0%B5%D0%BD%D1%8C%202024/Postman-API.postman_collection.json и загрузить в Postman.  |
| Steps to reproduce:    | 1. Перейти в POST-запрос "Сохраним объявление".<br/>  2. В теле запроса указать:  <br/>{ <br/>"name": "Tel", <br/>    "price": 1, <br/>    "sellerId": 1,<br/>     "statistics": {                "contacts": 1,               "like": 1,               "viewCount": 1}<br/>} <br/> 3. Отправить POST-запрос. <br/> 4. Обратить внимание на ответ, полученный от сервера.  |


<br/>

| ID: | 2 |
|----------|----------|
| Summary:  | При отправке POST-запроса на создание объявления создается объявление, где меняется ключ и значение пары "like": number  |
| Expected result:   | При проверке создания объявления пара ключ: значение не меняется. Они такие же, как при создании POST-запроса.   |
| Actual result:    |  Меняется ключ и значение пары "like": number.  |
| Severity:    | Critical    |
| Priority:    | High    |
| Status:    | New   |
| Author:    | Анна Садыкова   |
| Preconditions:    | Скачать файл "Postman-API.postman_collection" с https://gitverse.ru/avito.tech/tech-internship/content/main/Tech%20Internships%20/QA/%D0%A2%D0%B5%D1%81%D1%82%D0%BE%D0%B2%D0%BE%D0%B5%20%D0%B7%D0%B0%D0%B4%D0%B0%D0%BD%D0%B8%D0%B5_%D0%BE%D1%81%D0%B5%D0%BD%D1%8C%202024/Postman-API.postman_collection.json и загрузить в Postman. |
| Steps to reproduce:    | 1. Перейти в POST-запрос "Сохраним объявление".<br/>  2. В теле запроса указать:  <br/>{ <br/>"name": "Tel", <br/>    "price": 1, <br/>    "sellerId": 111112,<br/>     "statistics": {                "contacts": 1,               "like": 1,               "viewCount": 1} <br/>} <br/> 3. Отправить POST-запрос.  <br/> 4. Из ответа из "status" Скопировать id полученного объявления.<br/> 5. Перейти в GET-запрос "Получить объявление".<br/> 5. В Params в Path Variables в "Key" указать "id", а в "Values" вставить скопированный ранее id объявления.<br/> 6. Отправить созданный GET-запрос.<br/>7. В полученном ответе обратить внимание на ключ "likes" и его значение.  |


<br/>

| ID: | 3 |
|----------|----------|
| Summary:  | При отправке POST-запроса на создание объявления без "statistics" или со "statistics", не содержащий объекта (в том числе пустого), происходит ошибка на стороне сервера. |
| Expected result:   | Происходит ошибка 4xx на стороне клиента.    |
| Actual result:    |  Status: 500 Internal Server Error <br/> В теле ответа {"message":"internal error","code":500}  |
| Severity:    | Major    |
| Priority:    | High    |
| Status:    | New   |
| Author:    | Анна Садыкова   |
| Preconditions:    | Скачать файл "Postman-API.postman_collection" с https://gitverse.ru/avito.tech/tech-internship/content/main/Tech%20Internships%20/QA/%D0%A2%D0%B5%D1%81%D1%82%D0%BE%D0%B2%D0%BE%D0%B5%20%D0%B7%D0%B0%D0%B4%D0%B0%D0%BD%D0%B8%D0%B5_%D0%BE%D1%81%D0%B5%D0%BD%D1%8C%202024/Postman-API.postman_collection.json и загрузить в Postman. |
| Steps to reproduce:    | 1. Перейти в POST-запрос "Сохраним объявление". <br/>  2. В теле запроса указать:  <br/>{ <br/>"name": "Tel", <br/>    "price": 1, <br/>    "sellerId": 111112,<br/>     "statistics": 1<br/>} <br/> <br/>или <br/><br/> { <br/>"name": "Tel", <br/>    "price": 1, <br/>    "sellerId": 111112 <br/>} <br/> <br/>3. Отправить POST-запрос. <br/> 4. Обратить внимание на ответ, полученный от сервера.  |


<br/>

| ID: | 4 |
|----------|----------|
| Summary:  | При отправке POST-запроса на создание объявления без "name" происходит создание объявления. |
| Expected result:   | Поскольку нет требований, где описано, какие поля являются обязательными, то я опираюсь на свою логику: поле "name" должно быть обязательным для заполнения, так как объявление не может не иметь названия. Соответственно, ожидаемым результатом должна быть ошибка 4xx (ошибка на стороне клиента).    |
| Actual result:    |  В теле ответа "status" с id созданного объявления.  |
| Severity:    | Major    |
| Priority:    | High    |
| Status:    | New   |
| Author:    | Анна Садыкова   |
| Preconditions:    | Скачать файл "Postman-API.postman_collection" с https://gitverse.ru/avito.tech/tech-internship/content/main/Tech%20Internships%20/QA/%D0%A2%D0%B5%D1%81%D1%82%D0%BE%D0%B2%D0%BE%D0%B5%20%D0%B7%D0%B0%D0%B4%D0%B0%D0%BD%D0%B8%D0%B5_%D0%BE%D1%81%D0%B5%D0%BD%D1%8C%202024/Postman-API.postman_collection.json и загрузить в Postman.  |
| Steps to reproduce:    | 1. Перейти в POST-запрос "Сохраним объявление". <br/>  2. В теле запроса указать:  <br/>{ <br/>    "price": 1, <br/>    "sellerId": 111112,<br/>     "statistics": {                "contacts": 1,               "like": 1,               "viewCount": 1} <br/>} <br/>3. Отправить POST-запрос. <br/> 4. Обратить внимание на ответ, полученный от сервера.  |


<br/>

| ID: | 5 |
|----------|----------|
| Summary:  | При отправке POST-запроса на создание объявления без "price" происходит создание объявления. |
| Expected result:   | Поскольку нет требований, где описано, какие поля являются обязательными, то я опираюсь на свою логику: поле "price" должно быть обязательным для заполнения, так как объявление не может не иметь цены. Соответственно, ожидаемым результатом должна быть ошибка 4xx (ошибка на стороне клиента).    |
| Actual result:    |  В теле ответа "status" с id созданного объявления.  |
| Severity:    | Major    |
| Priority:    | High    |
| Status:    | New   |
| Author:    | Анна Садыкова   |
| Preconditions:    | Скачать файл "Postman-API.postman_collection" с https://gitverse.ru/avito.tech/tech-internship/content/main/Tech%20Internships%20/QA/%D0%A2%D0%B5%D1%81%D1%82%D0%BE%D0%B2%D0%BE%D0%B5%20%D0%B7%D0%B0%D0%B4%D0%B0%D0%BD%D0%B8%D0%B5_%D0%BE%D1%81%D0%B5%D0%BD%D1%8C%202024/Postman-API.postman_collection.json и загрузить в Postman.  |
| Steps to reproduce:    | 1. Перейти в POST-запрос "Сохраним объявление". <br/>  2. В теле запроса указать:  <br/>{ <br/>    "name": "Tel", <br/>    "sellerId": 111112,<br/>     "statistics": {                "contacts": 1,               "like": 1,               "viewCount": 1} <br/>} <br/>3. Отправить POST-запрос. <br/> 4. Обратить внимание на ответ, полученный от сервера.  |


<br/>

| ID: | 6 |
|----------|----------|
| Summary:  | При отправке POST-запроса на создание объявления без "sellerId" происходит создание объявления. |
| Expected result:   | Поскольку нет требований, где описано, какие поля являются обязательными, то я опираюсь на свою логику: поле "sellerId" должно быть обязательным для заполнения, так как объявление не может не иметь id продавца. Соответственно, ожидаемым результатом должна быть ошибка 4xx (ошибка на стороне клиента).    |
| Actual result:    |  В теле ответа "status" с id созданного объявления.  |
| Severity:    | Major    |
| Priority:    | High    |
| Status:    | New   |
| Author:    | Анна Садыкова   |
| Preconditions:    | Скачать файл "Postman-API.postman_collection" с https://gitverse.ru/avito.tech/tech-internship/content/main/Tech%20Internships%20/QA/%D0%A2%D0%B5%D1%81%D1%82%D0%BE%D0%B2%D0%BE%D0%B5%20%D0%B7%D0%B0%D0%B4%D0%B0%D0%BD%D0%B8%D0%B5_%D0%BE%D1%81%D0%B5%D0%BD%D1%8C%202024/Postman-API.postman_collection.json и загрузить в Postman.  |
| Steps to reproduce:    | 1. Перейти в POST-запрос "Сохраним объявление". <br/>  2. В теле запроса указать:  <br/>{ <br/>    "name": "Tel", <br/>    "price": 1,<br/>     "statistics": {                "contacts": 1,               "like": 1,               "viewCount": 1} <br/>} <br/>3. Отправить POST-запрос. <br/> 4. Обратить внимание на ответ, полученный от сервера.  |


<br/>

| ID: | 7 |
|----------|----------|
| Summary:  | При отправке POST-запроса на создание объявления со значением "sellerId" меньше 0 происходит создание объявления. |
| Expected result:   | Поскольку нет требований, где описано, какие значения принимают поля, то я опираюсь на свою логику: поле "sellerId" должно принимать только положительные числа (нигде не встречала отрицательные id, также в интернете не нашла ответ на свой вопрос "могут ли id быть отрицательными"). Соответственно, ожидаемым результатом должна быть ошибка 4xx (ошибка на стороне клиента).    |
| Actual result:    |  В теле ответа "status" с id созданного объявления.  |
| Severity:    | Minor    |
| Priority:    | Trivial    |
| Status:    | New   |
| Author:    | Анна Садыкова   |
| Preconditions:    | Скачать файл "Postman-API.postman_collection" с https://gitverse.ru/avito.tech/tech-internship/content/main/Tech%20Internships%20/QA/%D0%A2%D0%B5%D1%81%D1%82%D0%BE%D0%B2%D0%BE%D0%B5%20%D0%B7%D0%B0%D0%B4%D0%B0%D0%BD%D0%B8%D0%B5_%D0%BE%D1%81%D0%B5%D0%BD%D1%8C%202024/Postman-API.postman_collection.json и загрузить в Postman.  |
| Steps to reproduce:    | 1. Перейти в POST-запрос "Сохраним объявление". <br/>  2. В теле запроса указать:  <br/>{ <br/>    "name": "Tel", <br/>    "price": 1, <br/> "sellerId": -1, <br/>     "statistics": {                "contacts": 1,               "like": 1,               "viewCount": 1} <br/>} <br/>3. Отправить POST-запрос. <br/> 4. Обратить внимание на ответ, полученный от сервера.  |


<br/>

| ID: | 8 |
|----------|----------|
| Summary:  | При отправке POST-запроса на создание объявления со значением "price" меньше 0 происходит создание объявления. |
| Expected result:   | Поскольку нет требований, где описано, какие значения принимают поля, то я опираюсь на свою логику: поле "price" должно принимать только положительные числа. Соответственно, ожидаемым результатом должна быть ошибка 4xx (ошибка на стороне клиента).    |
| Actual result:    |  В теле ответа "status" с id созданного объявления.  |
| Severity:    | Major    |
| Priority:    | High    |
| Status:    | New   |
| Author:    | Анна Садыкова   |
| Preconditions:    | Скачать файл "Postman-API.postman_collection" с https://gitverse.ru/avito.tech/tech-internship/content/main/Tech%20Internships%20/QA/%D0%A2%D0%B5%D1%81%D1%82%D0%BE%D0%B2%D0%BE%D0%B5%20%D0%B7%D0%B0%D0%B4%D0%B0%D0%BD%D0%B8%D0%B5_%D0%BE%D1%81%D0%B5%D0%BD%D1%8C%202024/Postman-API.postman_collection.json и загрузить в Postman.  |
| Steps to reproduce:    | 1. Перейти в POST-запрос "Сохраним объявление". <br/>  2. В теле запроса указать:  <br/>{ <br/>    "name": "Tel", <br/>    "price": -1, <br/> "sellerId": 111112, <br/>     "statistics": {                "contacts": 1,               "like": 1,               "viewCount": 1} <br/>} <br/>3. Отправить POST-запрос. <br/> 4. Обратить внимание на ответ, полученный от сервера.  |


<br/>

| ID: | 9 |
|----------|----------|
| Summary:  | При отправке POST-запроса на создание объявления с числовым значением "name" происходит ошибка на стороне сервера. |
| Expected result:   | Ошибка 4xx (ошибка на стороне клиента).    |
| Actual result:    |  Status: 500Internal Server Error <br/> В теле ответа {"message":"internal error","code":500}.  |
| Severity:    | Major    |
| Priority:    | High    |
| Status:    | New   |
| Author:    | Анна Садыкова   |
| Preconditions:    | Скачать файл "Postman-API.postman_collection" с https://gitverse.ru/avito.tech/tech-internship/content/main/Tech%20Internships%20/QA/%D0%A2%D0%B5%D1%81%D1%82%D0%BE%D0%B2%D0%BE%D0%B5%20%D0%B7%D0%B0%D0%B4%D0%B0%D0%BD%D0%B8%D0%B5_%D0%BE%D1%81%D0%B5%D0%BD%D1%8C%202024/Postman-API.postman_collection.json и загрузить в Postman.  |
| Steps to reproduce:    | 1. Перейти в POST-запрос "Сохраним объявление". <br/>  2. В теле запроса указать:  <br/>{ <br/>    "name": 1, <br/>    "price": 1, <br/> "sellerId": 111112, <br/>     "statistics": {                "contacts": 1,               "like": 1,               "viewCount": 1} <br/>} <br/>3. Отправить POST-запрос. <br/> 4. Обратить внимание на ответ, полученный от сервера.  |


<br/>

| ID: | 10 |
|----------|----------|
| Summary:  | При отправке POST-запроса на создание объявления с текстом - SQL-инъекцией (или любым другим вредоносным кодом) в поле "name" происходит создание объявления. |
| Expected result:   | Ошибка 4xx (ошибка на стороне клиента).    |
| Actual result:    |  Создание объявления: в теле ответа id объявления.  |
| Severity:    | Critical    |
| Priority:    | High    |
| Status:    | New   |
| Author:    | Анна Садыкова   |
| Preconditions:    | Скачать файл "Postman-API.postman_collection" с https://gitverse.ru/avito.tech/tech-internship/content/main/Tech%20Internships%20/QA/%D0%A2%D0%B5%D1%81%D1%82%D0%BE%D0%B2%D0%BE%D0%B5%20%D0%B7%D0%B0%D0%B4%D0%B0%D0%BD%D0%B8%D0%B5_%D0%BE%D1%81%D0%B5%D0%BD%D1%8C%202024/Postman-API.postman_collection.json и загрузить в Postman.  |
| Steps to reproduce:    | 1. Перейти в POST-запрос "Сохраним объявление". <br/>  2. В теле запроса указать:  <br/>{ <br/>    "name": "DROP TABLE Seller", <br/>    "price": 1, <br/> "sellerId": 111112, <br/>     "statistics": {                "contacts": 1,               "like": 1,               "viewCount": 1} <br/>} <br/>3. Отправить POST-запрос. <br/> 4. Обратить внимание на ответ, полученный от сервера.  |


<br/>

| ID: | 11 |
|----------|----------|
| Summary:  | При отправке POST-запроса на создание объявления с текстом - SQL-инъекцией (или любым другим вредоносным кодом) (или любым невредоносным текстом) в поле "price" происходит ошибка на стороне сервера. |
| Expected result:   | Ошибка 4xx (ошибка на стороне клиента).    |
| Actual result:    |  Status: 500Internal Server Error <br/> В теле ответа {"message":"internal error","code":500}.  |
| Severity:    | Critical    |
| Priority:    | High    |
| Status:    | New   |
| Author:    | Анна Садыкова   |
| Preconditions:    | Скачать файл "Postman-API.postman_collection" с https://gitverse.ru/avito.tech/tech-internship/content/main/Tech%20Internships%20/QA/%D0%A2%D0%B5%D1%81%D1%82%D0%BE%D0%B2%D0%BE%D0%B5%20%D0%B7%D0%B0%D0%B4%D0%B0%D0%BD%D0%B8%D0%B5_%D0%BE%D1%81%D0%B5%D0%BD%D1%8C%202024/Postman-API.postman_collection.json и загрузить в Postman.  |
| Steps to reproduce:    | 1. Перейти в POST-запрос "Сохраним объявление". <br/>  2. В теле запроса указать:  <br/>{ <br/>    "name": "Tel", <br/>    "price": "DROP TABLE Seller", <br/> "sellerId": 111112, <br/>     "statistics": {                "contacts": 1,               "like": 1,               "viewCount": 1} <br/>} <br/>3. Отправить POST-запрос. <br/> 4. Обратить внимание на ответ, полученный от сервера.  |


<br/>

| ID: | 12 |
|----------|----------|
| Summary:  | При отправке POST-запроса на создание объявления с текстом - SQL-инъекцией (или любым другим вредоносным кодом) (или любым невредоносным текстом) в поле "sellerId" происходит ошибка на стороне сервера. |
| Expected result:   | Ошибка 4xx (ошибка на стороне клиента).    |
| Actual result:    |  Status: 500Internal Server Error <br/> В теле ответа {"message":"internal error","code":500}.  |
| Severity:    | Critical    |
| Priority:    | High    |
| Status:    | New   |
| Author:    | Анна Садыкова   |
| Preconditions:    | Скачать файл "Postman-API.postman_collection" с https://gitverse.ru/avito.tech/tech-internship/content/main/Tech%20Internships%20/QA/%D0%A2%D0%B5%D1%81%D1%82%D0%BE%D0%B2%D0%BE%D0%B5%20%D0%B7%D0%B0%D0%B4%D0%B0%D0%BD%D0%B8%D0%B5_%D0%BE%D1%81%D0%B5%D0%BD%D1%8C%202024/Postman-API.postman_collection.json и загрузить в Postman.  |
| Steps to reproduce:    | 1. Перейти в POST-запрос "Сохраним объявление". <br/>  2. В теле запроса указать:  <br/>{ <br/>    "name": "Tel", <br/>    "price": 1, <br/> "sellerId": "DROP TABLE Seller", <br/>     "statistics": {                "contacts": 1,               "like": 1,               "viewCount": 1} <br/>} <br/>3. Отправить POST-запрос. <br/> 4. Обратить внимание на ответ, полученный от сервера.  |


<br/>

| ID: | 13 |
|----------|----------|
| Summary:  | При отправке POST-запроса на создание объявления с текстом - SQL-инъекцией (или любым другим вредоносным кодом) (или любым невредоносным текстом) в поле "contacts" происходит ошибка на стороне сервера. |
| Expected result:   | Ошибка 4xx (ошибка на стороне клиента).    |
| Actual result:    |  Status: 500Internal Server Error <br/> В теле ответа {"message":"internal error","code":500}.  |
| Severity:    | Critical    |
| Priority:    | High    |
| Status:    | New   |
| Author:    | Анна Садыкова   |
| Preconditions:    | Скачать файл "Postman-API.postman_collection" с https://gitverse.ru/avito.tech/tech-internship/content/main/Tech%20Internships%20/QA/%D0%A2%D0%B5%D1%81%D1%82%D0%BE%D0%B2%D0%BE%D0%B5%20%D0%B7%D0%B0%D0%B4%D0%B0%D0%BD%D0%B8%D0%B5_%D0%BE%D1%81%D0%B5%D0%BD%D1%8C%202024/Postman-API.postman_collection.json и загрузить в Postman.  |
| Steps to reproduce:    | 1. Перейти в POST-запрос "Сохраним объявление". <br/>  2. В теле запроса указать:  <br/>{ <br/>    "name": "Tel", <br/>    "price": 1, <br/> "sellerId": 111112, <br/>     "statistics": {                "contacts": "DROP TABLE Seller",               "like": 1,               "viewCount": 1} <br/>} <br/>3. Отправить POST-запрос. <br/> 4. Обратить внимание на ответ, полученный от сервера.  |


<br/>

| ID: | 14 |
|----------|----------|
| Summary:  | При отправке POST-запроса на создание объявления с текстом - SQL-инъекцией (или любым другим вредоносным кодом) (или любым невредоносным текстом) в поле "viewCount" происходит ошибка на стороне сервера. |
| Expected result:   | Ошибка 4xx (ошибка на стороне клиента).    |
| Actual result:    |  Status: 500Internal Server Error <br/> В теле ответа {"message":"internal error","code":500}.  |
| Severity:    | Critical    |
| Priority:    | High    |
| Status:    | New   |
| Author:    | Анна Садыкова   |
| Preconditions:    | Скачать файл "Postman-API.postman_collection" с https://gitverse.ru/avito.tech/tech-internship/content/main/Tech%20Internships%20/QA/%D0%A2%D0%B5%D1%81%D1%82%D0%BE%D0%B2%D0%BE%D0%B5%20%D0%B7%D0%B0%D0%B4%D0%B0%D0%BD%D0%B8%D0%B5_%D0%BE%D1%81%D0%B5%D0%BD%D1%8C%202024/Postman-API.postman_collection.json и загрузить в Postman.  |
| Steps to reproduce:    | 1. Перейти в POST-запрос "Сохраним объявление". <br/>  2. В теле запроса указать:  <br/>{ <br/>    "name": "Tel", <br/>    "price": 1, <br/> "sellerId": 111112, <br/>     "statistics": {                "contacts": 1,               "like": 1,               "viewCount": "DROP TABLE Seller"} <br/>} <br/>3. Отправить POST-запрос. <br/> 4. Обратить внимание на ответ, полученный от сервера.  |


<br/>

| ID: | 15 |
|----------|----------|
| Summary:  | При отправке POST-запроса на создание объявления со значением "sellerId" равным очень большому числу, например, 100000000000000000000000000000000000000000 (или очень большому числу со знаком "-", например, -100000000000000000000000000000000000000000) происходит ошибка на стороне сервера. |
| Expected result:   | Ошибка 4xx (ошибка на стороне клиента).    |
| Actual result:    |  Status: 500Internal Server Error <br/> В теле ответа {"message":"internal error","code":500}  |
| Severity:    | Minor    |
| Priority:    | Low    |
| Status:    | New   |
| Author:    | Анна Садыкова   |
| Preconditions:    | Скачать файл "Postman-API.postman_collection" с https://gitverse.ru/avito.tech/tech-internship/content/main/Tech%20Internships%20/QA/%D0%A2%D0%B5%D1%81%D1%82%D0%BE%D0%B2%D0%BE%D0%B5%20%D0%B7%D0%B0%D0%B4%D0%B0%D0%BD%D0%B8%D0%B5_%D0%BE%D1%81%D0%B5%D0%BD%D1%8C%202024/Postman-API.postman_collection.json и загрузить в Postman.  |
| Steps to reproduce:    | 1. Перейти в POST-запрос "Сохраним объявление". <br/>  2. В теле запроса указать:  <br/>{ <br/>    "name": "Tel", <br/>    "price": 1, <br/> "sellerId": 100000000000000000000000000000000000000000, <br/>     "statistics": {                "contacts": 1,               "like": 1,               "viewCount": 1} <br/>} <br/>3. Отправить POST-запрос. <br/> 4. Обратить внимание на ответ, полученный от сервера.  |


<br/>

| ID: | 16 |
|----------|----------|
| Summary:  | При отправке GET-запроса "Получить все объявления по продавцам" с указанием в Params "sellerID значения "DROP TABLE Seller" в ответе выдается список объектов. |
| Expected result:   | Ошибка 4xx (ошибка на стороне клиента).    |
| Actual result:    |  В теле ответа список объектов.  |
| Severity:    | Critical    |
| Priority:    | High    |
| Status:    | New   |
| Author:    | Анна Садыкова   |
| Preconditions:    | Скачать файл "Postman-API.postman_collection" с https://gitverse.ru/avito.tech/tech-internship/content/main/Tech%20Internships%20/QA/%D0%A2%D0%B5%D1%81%D1%82%D0%BE%D0%B2%D0%BE%D0%B5%20%D0%B7%D0%B0%D0%B4%D0%B0%D0%BD%D0%B8%D0%B5_%D0%BE%D1%81%D0%B5%D0%BD%D1%8C%202024/Postman-API.postman_collection.json и загрузить в Postman.  |
| Steps to reproduce:    | 1. Перейти в GET-запрос "Получить все объявления по продавцам". <br/> 2. В Params в значении "sellerID" указать "DROP TABLE Seller". <br/> 3. Отправить POST-запрос. <br/> 4. Обратить внимание на ответ, полученный от сервера.|


<br/>

| ID: | 17 |
|----------|----------|
| Summary:  | При отправке POST-запроса на создание объявления со значением "name" равным очень большому числу, например, 100000000000000000000000000000000000000000 (или очень большому числу со знаком "-", например, -100000000000000000000000000000000000000000) происходит ошибка на стороне сервера. |
| Expected result:   | Ошибка 4xx (ошибка на стороне клиента).    |
| Actual result:    |  Status: 500Internal Server Error <br/> В теле ответа {"message":"internal error","code":500}  |
| Severity:    | Minor    |
| Priority:    | Low    |
| Status:    | New   |
| Author:    | Анна Садыкова   |
| Preconditions:    | Скачать файл "Postman-API.postman_collection" с https://gitverse.ru/avito.tech/tech-internship/content/main/Tech%20Internships%20/QA/%D0%A2%D0%B5%D1%81%D1%82%D0%BE%D0%B2%D0%BE%D0%B5%20%D0%B7%D0%B0%D0%B4%D0%B0%D0%BD%D0%B8%D0%B5_%D0%BE%D1%81%D0%B5%D0%BD%D1%8C%202024/Postman-API.postman_collection.json и загрузить в Postman.  |
| Steps to reproduce:    | 1. Перейти в POST-запрос "Сохраним объявление". <br/>  2. В теле запроса указать:  <br/>{ <br/>    "name": -100000000000000000000000000000000000000000 , <br/>    "price": 1, <br/> "sellerId": 111112, <br/>     "statistics": {                "contacts": 1,               "like": 1,               "viewCount": 1} <br/>} <br/>3. Отправить POST-запрос. <br/> 4. Обратить внимание на ответ, полученный от сервера.  |

<br/>

| ID: | 18 |
|----------|----------|
| Summary:  | При отправке POST-запроса на создание объявления со значением "contacts" равным очень большому числу, например, 100000000000000000000000000000000000000000 (или очень большому числу со знаком "-", например, -100000000000000000000000000000000000000000) происходит ошибка на стороне сервера. |
| Expected result:   | Ошибка 4xx (ошибка на стороне клиента).    |
| Actual result:    |  Status: 500Internal Server Error <br/> В теле ответа {"message":"internal error","code":500}  |
| Severity:    | Minor    |
| Priority:    | Low    |
| Status:    | New   |
| Author:    | Анна Садыкова   |
| Preconditions:    | Скачать файл "Postman-API.postman_collection" с https://gitverse.ru/avito.tech/tech-internship/content/main/Tech%20Internships%20/QA/%D0%A2%D0%B5%D1%81%D1%82%D0%BE%D0%B2%D0%BE%D0%B5%20%D0%B7%D0%B0%D0%B4%D0%B0%D0%BD%D0%B8%D0%B5_%D0%BE%D1%81%D0%B5%D0%BD%D1%8C%202024/Postman-API.postman_collection.json и загрузить в Postman.  |
| Steps to reproduce:    | 1. Перейти в POST-запрос "Сохраним объявление". <br/>  2. В теле запроса указать:  <br/>{ <br/>    "name": "Tel" , <br/>    "price": 1, <br/> "sellerId": 111112, <br/>     "statistics": {                "contacts": -100000000000000000000000000000000000000000,               "like": 1,               "viewCount": 1} <br/>} <br/>3. Отправить POST-запрос. <br/> 4. Обратить внимание на ответ, полученный от сервера.  |

<br/>

| ID: | 19 |
|----------|----------|
| Summary:  | При отправке POST-запроса на создание объявления со значением "viewCount" равным очень большому числу, например, 100000000000000000000000000000000000000000 (или очень большому числу со знаком "-", например, -100000000000000000000000000000000000000000) происходит ошибка на стороне сервера. |
| Expected result:   | Ошибка 4xx (ошибка на стороне клиента).    |
| Actual result:    |  Status: 500Internal Server Error <br/> В теле ответа {"message":"internal error","code":500}  |
| Severity:    | Minor    |
| Priority:    | Low    |
| Status:    | New   |
| Author:    | Анна Садыкова   |
| Preconditions:    | Скачать файл "Postman-API.postman_collection" с https://gitverse.ru/avito.tech/tech-internship/content/main/Tech%20Internships%20/QA/%D0%A2%D0%B5%D1%81%D1%82%D0%BE%D0%B2%D0%BE%D0%B5%20%D0%B7%D0%B0%D0%B4%D0%B0%D0%BD%D0%B8%D0%B5_%D0%BE%D1%81%D0%B5%D0%BD%D1%8C%202024/Postman-API.postman_collection.json и загрузить в Postman.  |
| Steps to reproduce:    | 1. Перейти в POST-запрос "Сохраним объявление". <br/>  2. В теле запроса указать:  <br/>{ <br/>    "name": "Tel" , <br/>    "price": 1, <br/> "sellerId": 111112, <br/>     "statistics": {                "contacts": 1,               "like": 1,               "viewCount": -100000000000000000000000000000000000000000} <br/>} <br/>3. Отправить POST-запрос. <br/> 4. Обратить внимание на ответ, полученный от сервера.  |


<br/>

| ID: | 20 |
|----------|----------|
| Summary:  | Улучшение: в ответе на POST-запрос в "status" плохо сделано, что id объявления вписан в сообщение со строкой. <br/> Вместо { "status": "Сохранили объявление - 979bf9b7-e06e-44fa-a576-c9e75c43f262"} лучше сразу указать id: { "status": "979bf9b7-e06e-44fa-a576-c9e75c43f262"}|