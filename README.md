# Real Estate App
Application for rent/buying a home.

Stack : Django Rest Framework + PostgreSql
## Installation

Rename ".env.example"  - > ".env" and write your dependencies:
```bash
SECRET_KEY=#Secret key from django settings
DEBUG=#True or False
ALLOWED_HOSTS=#"localhost 127.0.0.1 [::1]"
POSTGRES_ENGINE=#django.db.backends.postgresql
POSTGRES_USER=#db credentials
POSTGRES_PASSWORD=#db credentials
POSTGRES_DB=#db credentials
PG_HOST=#db credentials
PG_PORT=#db credentials
SIGNING_KEY=#generate code
EMAIL_HOST=#smtp credentials
EMAIL_PORT=#smtp credentials
EMAIL_HOST_USER=#smtp credentials
EMAIL_HOST_PASSWORD=#smtp credentials
DOMAIN=#127.0.0.1:8000
```
Create database and fill credentials into file.\
Make smtp server account and fill credentials. #example https://www.mailnest.io/ \
Run commands bellow:

```bash
py -m venv env

./env/scripts/activate

pip install -r requirements.py

py manage.py makemigrations
py manage.py migrate
py manage.py runserver
```
## API endpoints
These endpoints allow you to handle Stripe subscriptions for Publish and Analyze.
### Profiles

 GET [/api/v1/profile/me/]()  - Профиль пользователя\
 PATCH [/api/v1/profile/update/username/]() - Обновить профиль
```
{
    "about_me":"I am passionate about Real Estate",
    "phone_number":"+77777777777"
}
```
 GET [/api/v1/profile/agents/all/]()  - Список всех агентов \
 GET [/api/v1/profile/top-agents/all/]()  - Список всех топ агентов

### Property

 POST [api/v1/properties/create/]() - Создать недвижимость
```
{
    "title":"My very big property",
    "country":"Japan",
    "city":"Tokyo",
    "price":100000
}
```
GET [/api/v1/properties/all/]() - Список всех недвижимостей \
GET [/api/v1/properties/agents/]() - Список недвижимости определенного агента\
GET [/api/v1/properties/details/PROPERTYNAME/]() - Информация о недвижимости\
PUT [/api/v1/properties/update/PROPERTYNAME/]() - Обновить информацию о недвижимости
```
{
    "title":"Property in Russsia",
    "description":"The best property ever",
    "country":"Russia"
}
```
DELETE [/api/v1/properties/delete/PROPERTYNAME/]() - Удалить недвижимость

### Ratings & Enquiries

POST [/api/v1/ratings/UUID/]() - Оценить агента (1 - 5)

```
{
    "rating":4,
    "comment":"He did good"
}
```
POST [/api/v1/enquiries/]() - Отправить запрос
```
{
    "name":"Test",
    "email":"test@gmail.com",
    "subject":"the test enquiry email",
    "message":"The message than was tested with this email"
}
```

### Users

POST [/api/v1/auth/users/]() - Регистрация
```
{
    "username": "",
    "first_name": "",
    "last_name": "",
    "email": "",
    "password": "",
    "re_password": ""
}
```
POST [/api/v1/auth/users/activation/]()- Активация аккаунта
```
#Даннные были отправлены на email
{
    "uid":"Mg",
    "token":"b391cc-fbdca5a8fc1cfae3e40495e05c779ce7"
}
```
POST [/api/v1/auth/jwt/create/]() - Авторизация
```
{
    "email":"",
    "password":""
}
```
POST [/api/v1/auth/users/reset_password/]() - Запрос на смену пароля
```
{
    "email":""
}
```
POST [/api/v1/auth/users/reset_password_confirm/]() - Подтверждение смены пароля 
```
{
    "new_password":"",
    "re_new_password":"",
    "uid":"Nw",
    "token":"b35hhr-fd5f7a584b4788a2fdea289ae3aa941c"
}
```

