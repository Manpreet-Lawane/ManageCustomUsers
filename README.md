
# ManageCustomUsers

Authentication API's

## Description

Authenticate users with register, login, homepage, logout and rest password API's. Allows super users to access DB

### Dependencies

* Python==3.8
* Django==4.2
* Django Rest Framework==3.14
* PyJWT==2.8
* psycopg2==2.9
* please check requirements.txt for detail about dependencies

### Executing program

* make migration to save changes in models+
* run the server
```
* python manage.py makemigrations
* python manage.py migrate
* python manage.py runserver
```
* Register url json body:
```
{"email":"abc@gmail.com",
"username": "abc",
"password": "abc",
"user_type":"superuser"}
```
* login url json body:
```
{"email":"abc@gmail.com",
"username": "abc",
"password": "abc"}
```
* Home url:
  * copy token from login and paste after home url
    * i.e localhost/auth/home/?token=<copied token>

* Reset password json body:
```
{"email":"abc@gmail.com",
"password": "abcd"}
```
## Version History

* 0.1
    * Initial Release

