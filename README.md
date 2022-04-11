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

 GET [/api/v1/profile/me/]()  - User Profile
 PATCH [/api/v1/profile/update/username/]() - Update Profile
```
{
    "about_me":"I am passionate about Real Estate",
    "phone_number":"+77777777777"
}
```
 GET [/api/v1/profile/agents/all/]()  - Get All Agents \
 GET [/api/v1/profile/top-agents/all/]()  - Get Top Agents

### Property

 POST [api/v1/properties/create/]() - Create Property
```
{
    "title":"My very big property",
    "country":"Japan",
    "city":"Tokyo",
    "price":100000
}
```
GET [/api/v1/properties/all/]() - Get Propery List \
GET [/api/v1/properties/agents/]() - Get Agent Property List \
GET [/api/v1/properties/details/PROPERTYNAME/]() - Property Detail\
PUT [/api/v1/properties/update/PROPERTYNAME/]() - Update Property
```
{
    "title":"Property in Russsia",
    "description":"The best property ever",
    "country":"Russia"
}
```
DELETE [/api/v1/properties/delete/PROPERTYNAME/]() - Delete Property

### Ratings & Enquiries

POST [/api/v1/ratings/UUID/]() - Rate an Agent (1 - 5)

```
{
    "rating":4,
    "comment":"He did good"
}
```
POST [/api/v1/enquiries/]() - Send Enquire
```
{
    "name":"Test",
    "email":"test@gmail.com",
    "subject":"the test enquiry email",
    "message":"The message than was tested with this email"
}
```

### Users

POST [/api/v1/auth/users/]() - Registration
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
POST [/api/v1/auth/users/activation/]()- Activate Account
```
#Даннные были отправлены на email
{
    "uid":"Mg",
    "token":"b391cc-fbdca5a8fc1cfae3e40495e05c779ce7"
}
```
POST [/api/v1/auth/jwt/create/]() - Authtorization
```
{
    "email":"",
    "password":""
}
```
POST [/api/v1/auth/users/reset_password/]() - Reset Password Request
```
{
    "email":""
}
```
POST [/api/v1/auth/users/reset_password_confirm/]() - Confirm Reset Password
```
{
    "new_password":"",
    "re_new_password":"",
    "uid":"Nw",
    "token":"b35hhr-fd5f7a584b4788a2fdea289ae3aa941c"
}
```

